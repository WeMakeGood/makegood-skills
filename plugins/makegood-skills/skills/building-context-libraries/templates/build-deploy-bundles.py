#!/usr/bin/env python3
"""
Build deployable agent bundles by resolving @include directives in agent
source files. Each agent's bundle inlines the content of every file it
@-includes, recursively, producing a single self-contained file suitable
for runtimes that don't process @include natively (Claude.ai project
upload, Cowork, generic API integrations).

Source agent files in agents/ stay modular — they reference required
context via @path directives. This script reads each agent file, expands
every @path it encounters, and writes the expanded result to deploy/agents/.

Two bundle variants:
- Standard (default): inline only the @-include directives in the agent file
  (Required Reading content). Conditional addenda stay separate; the runtime
  loads them on demand when their triggers fire.
- All-inclusive (--all-inclusive): standard inlining plus every conditional
  addendum from the `## Conditional Loads` table appended as an additional
  `## Conditional Context` section. Use for runtimes where work-time fetch
  of conditional addenda is unreliable.

Usage:
    scripts/build-deploy-bundles.py                    # build all agents (standard)
    scripts/build-deploy-bundles.py --all-inclusive    # also build all-inclusive variants
    scripts/build-deploy-bundles.py --check            # report drift without writing
    scripts/build-deploy-bundles.py --agent <basename> # build a single agent

Run from the repo root (the directory containing agents/, modules/, addenda/).
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# PyYAML is required only for the guardrail subcommands (--resolve-guardrails,
# --update-guardrails, and guardrail drift in --check). The default bundle
# build does not need it, so the import is deferred: a missing PyYAML must not
# break the offline bundle build.
try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


def _require_yaml() -> None:
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required for guardrail commands but is not installed. "
            "Install it with: pip install pyyaml"
        )

# ---------------------------------------------------------------------------
# @ directive matcher
#
# Match a line that begins (after optional whitespace) with @ followed by a
# path. The path is everything after @ until end-of-line, stripped. Only
# lines that consist solely of an @-directive are expanded; @ embedded in
# prose is left alone.
# ---------------------------------------------------------------------------

# Script version. This script is a skill-versioned artifact: it is vendored
# into each library, and the library's build-state records this version. A
# migration that ships a newer script re-vendors it and updates that record.
# Bump this in lockstep with the skill version whenever the script changes.
SCRIPT_VERSION = "1.8.0"

INCLUDE_PATTERN = re.compile(r"^\s*@(\S+)\s*$")

# Maximum depth of recursive @-expansion. Guards against accidental cycles.
MAX_DEPTH = 16

# Header for the appended section in all-inclusive bundles.
CONDITIONAL_CONTEXT_HEADER = "## Conditional Context"


# ---------------------------------------------------------------------------
# Expansion
# ---------------------------------------------------------------------------


def expand_includes(
    source_path: Path,
    repo_root: Path,
    visited: set[Path] | None = None,
    depth: int = 0,
    bundle_seen: set[Path] | None = None,
) -> str:
    """Read source_path and return its content with all @path directives
    recursively expanded. Paths in @ directives are resolved relative to
    repo_root.

    `visited` tracks paths in the current include chain (for cycle detection).
    `bundle_seen`, when supplied, tracks paths inlined anywhere in the current
    bundle build — when an @-target's resolved path is already in `bundle_seen`,
    the target is replaced by a one-line cross-reference instead of being
    re-inlined. Used by the all-inclusive variant to prevent the same shared
    file from appearing twice when it's reachable from multiple roots
    (e.g., two conditional addenda that both @-include a shared module).
    Pass None to get the standard recursive expansion with no de-duplication."""

    if visited is None:
        visited = set()

    resolved = source_path.resolve()

    if resolved in visited:
        raise RuntimeError(
            f"Cycle detected: {source_path} is already in the include chain"
        )

    if depth > MAX_DEPTH:
        raise RuntimeError(
            f"@include nesting exceeded {MAX_DEPTH} levels at {source_path}"
        )

    visited = visited | {resolved}

    try:
        text = source_path.read_text()
    except FileNotFoundError:
        raise RuntimeError(f"@include target not found: {source_path}")

    if bundle_seen is not None:
        bundle_seen.add(resolved)

    output_lines: list[str] = []
    for line in text.splitlines():
        match = INCLUDE_PATTERN.match(line)
        if match:
            include_path = repo_root / match.group(1)
            include_resolved = include_path.resolve()
            if bundle_seen is not None and include_resolved in bundle_seen:
                # Already inlined elsewhere in this bundle — leave a pointer.
                rel = match.group(1)
                output_lines.append(
                    f"<!-- @include {rel} omitted: already inlined earlier in this bundle -->"
                )
            else:
                included = expand_includes(
                    include_path, repo_root, visited, depth + 1, bundle_seen
                )
                output_lines.append(included.rstrip("\n"))
        else:
            output_lines.append(line)

    return "\n".join(output_lines) + "\n"


# ---------------------------------------------------------------------------
# Conditional Loads table parsing
#
# Find the `## Conditional Loads` section in an agent file, then parse the
# markdown table. Return a list of (file_path, trigger) pairs for each row.
# Returns [] if the section is missing or contains no table rows.
# ---------------------------------------------------------------------------


CONDITIONAL_HEADER = re.compile(r"^##\s+Conditional Loads\s*$")
NEXT_HEADER = re.compile(r"^##\s+\S")
TABLE_ROW = re.compile(r"^\|\s*`?([^`|]+?)`?\s*\|\s*(.+?)\s*\|\s*$")


def parse_conditional_table(agent_text: str) -> list[tuple[str, str]]:
    """Extract (file_path, trigger) pairs from the agent file's
    `## Conditional Loads` table. File paths in the first column may
    optionally be wrapped in backticks; both forms are accepted."""
    rows: list[tuple[str, str]] = []
    in_section = False
    in_table = False
    saw_separator = False

    for line in agent_text.splitlines():
        if CONDITIONAL_HEADER.match(line):
            in_section = True
            continue
        if in_section and NEXT_HEADER.match(line):
            break
        if not in_section:
            continue

        # Once in section, look for the table.
        stripped = line.strip()
        if stripped.startswith("|"):
            if not in_table:
                in_table = True
                continue  # header row
            if not saw_separator:
                saw_separator = True
                continue  # separator row (|---|---|)
            match = TABLE_ROW.match(stripped)
            if match:
                file_path = match.group(1).strip()
                trigger = match.group(2).strip()
                if file_path and trigger and not file_path.startswith("--"):
                    rows.append((file_path, trigger))
        elif in_table and not stripped:
            # Blank line after table content ends the table
            break

    return rows


# ---------------------------------------------------------------------------
# Build (standard variant)
# ---------------------------------------------------------------------------


def build_agent(agent_path: Path, repo_root: Path, deploy_dir: Path) -> Path:
    """Build the standard bundle for one agent. Returns the path written."""
    expanded = expand_includes(agent_path, repo_root)
    output_path = deploy_dir / agent_path.name
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(expanded)
    return output_path


def check_agent(agent_path: Path, repo_root: Path, deploy_dir: Path) -> bool:
    """Compare the standard expansion against the existing deploy file.
    Returns True if in sync, False if drift detected. Missing deploy file
    counts as drift."""
    expanded = expand_includes(agent_path, repo_root)
    output_path = deploy_dir / agent_path.name
    if not output_path.exists():
        return False
    return output_path.read_text() == expanded


# ---------------------------------------------------------------------------
# Build (all-inclusive variant)
# ---------------------------------------------------------------------------


def render_all_inclusive(agent_path: Path, repo_root: Path) -> str:
    """Produce the all-inclusive bundle text for one agent without writing.
    Inlines required-reading content (via @-include expansion) and appends
    every conditional addendum's content under a `## Conditional Context`
    section. Tracks paths seen anywhere in the bundle so a shared file
    reachable from multiple roots is inlined once and cross-referenced
    elsewhere — preventing duplication."""
    bundle_seen: set[Path] = set()
    expanded = expand_includes(
        agent_path, repo_root, bundle_seen=bundle_seen
    )
    conditional_rows = parse_conditional_table(agent_path.read_text())

    if not conditional_rows:
        return expanded

    appended_sections: list[str] = [CONDITIONAL_CONTEXT_HEADER, ""]
    appended_sections.append(
        "The following sections inline every conditional addendum's content. "
        "The Conditional Loads table above still applies — it tells the agent "
        "which inlined section to attend to for the work in front of it."
    )
    appended_sections.append("")
    for file_path, trigger in conditional_rows:
        target = repo_root / file_path
        try:
            content = expand_includes(
                target, repo_root, bundle_seen=bundle_seen
            )
        except RuntimeError as exc:
            raise RuntimeError(
                f"Conditional addendum {file_path} (referenced in "
                f"{agent_path.name}'s Conditional Loads table) failed to "
                f"expand: {exc}"
            )
        appended_sections.append(f"### {file_path}")
        appended_sections.append(f"*Load when:* {trigger}")
        appended_sections.append("")
        appended_sections.append(content.rstrip("\n"))
        appended_sections.append("")

    return expanded.rstrip("\n") + "\n\n" + "\n".join(appended_sections) + "\n"


def build_agent_all_inclusive(
    agent_path: Path, repo_root: Path, deploy_dir: Path
) -> Path:
    """Build and write the all-inclusive bundle for one agent. Returns the
    path written. The Conditional Loads table is preserved in the bundle so
    the agent retains per-work selectivity over the already-loaded content."""
    expanded = render_all_inclusive(agent_path, repo_root)
    output_name = agent_path.stem + ".all-inclusive.md"
    output_path = deploy_dir / output_name
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(expanded)
    return output_path


def check_agent_all_inclusive(
    agent_path: Path, repo_root: Path, deploy_dir: Path
) -> bool:
    """Compare the all-inclusive expansion against the existing deploy file.
    Same drift semantics as the standard check."""
    expanded = render_all_inclusive(agent_path, repo_root)
    output_name = agent_path.stem + ".all-inclusive.md"
    output_path = deploy_dir / output_name
    if not output_path.exists():
        return False
    return output_path.read_text() == expanded


# ---------------------------------------------------------------------------
# Guardrails versioning
#
# F0/S0 behavioral guardrail modules are owned by the makegood-guardrails repo
# and consumed here as a pinned, vendored dependency. guardrails.lock records
# the declared version (intent) and the resolved version (what was fetched and
# written into modules/). The vendored files carry a generated-file banner and
# are what the bundle build expands — so the default build stays fully local
# and offline. Resolution (network) is a separate, deliberate step.
# ---------------------------------------------------------------------------

LOCK_NAME = "guardrails.lock"

# Banner prepended to a vendored guardrail module. The body below it is the
# verbatim upstream module; --check re-fetches and compares the body (banner
# stripped) to detect hand-edits.
BANNER_PREFIX = "<!-- GENERATED — vendored from makegood-guardrails"
BANNER_RE = re.compile(r"^<!-- GENERATED — vendored from makegood-guardrails[^\n]*-->\n", re.M)


def load_lock(repo_root: Path) -> dict:
    _require_yaml()
    lock_path = repo_root / LOCK_NAME
    if not lock_path.exists():
        raise RuntimeError(
            f"{LOCK_NAME} not found in {repo_root}. This library has not been "
            "converted to consume versioned guardrails."
        )
    return yaml.safe_load(lock_path.read_text())


def write_lock(repo_root: Path, lock: dict) -> None:
    """Write the lock back, preserving the leading comment block verbatim and
    re-serializing the data below it."""
    lock_path = repo_root / LOCK_NAME
    existing = lock_path.read_text()
    comment_lines = []
    for line in existing.splitlines(keepends=True):
        if line.lstrip().startswith("#") or not line.strip():
            comment_lines.append(line)
        else:
            break
    body = yaml.safe_dump(lock, sort_keys=False, default_flow_style=False)
    lock_path.write_text("".join(comment_lines) + body)


def banner_for(tag: str, sha: str) -> str:
    return (
        f"{BANNER_PREFIX}@{tag} (sha {sha}). "
        "Do not edit here; edit upstream in makegood-guardrails and re-lock. -->\n"
    )


def strip_banner(text: str) -> str:
    return BANNER_RE.sub("", text, count=1)


# ---------------------------------------------------------------------------
# S0 backstop splice
#
# S0 2.0.0+ splits into a durable core (gates) and a volatile backstop (the
# current-generation prose-signature list), versioned independently upstream
# as the s0-backstop artifact. The core carries BACKSTOP:BEGIN/END markers;
# at resolve time the backstop is fetched at its own tag and its body
# (frontmatter stripped — the frontmatter is build metadata) is spliced
# between the markers, producing a single vendored S0 file. Consumers see one
# S0; only this script knows it's composed. Lock key: S0_BACKSTOP.
#
# S0 1.x has no markers and no backstop — the legacy single-fetch path still
# applies, so libraries pinned to s0-v1.0.0 resolve unchanged.
# ---------------------------------------------------------------------------

SPLICE_KEY = "S0_BACKSTOP"
SPLICE_HOST_KEY = "S0"
BACKSTOP_MODULE_FILENAME = "S0_backstop.md"
BACKSTOP_BEGIN = "<!-- BACKSTOP:BEGIN -->"
BACKSTOP_END = "<!-- BACKSTOP:END -->"
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def tag_for(key: str, version: str) -> str:
    """Lock key -> upstream tag: F0 -> f0-vX.Y.Z, S0_BACKSTOP -> s0-backstop-vX.Y.Z."""
    return f"{key.lower().replace('_', '-')}-v{version}"


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def splice_backstop(host_text: str, backstop_body: str, tag: str, sha: str) -> str:
    """Replace everything between the BACKSTOP markers in the S0 core with the
    backstop body plus a provenance comment. The markers themselves are kept,
    so a later re-resolve splices into a fresh upstream core, never into an
    already-spliced file."""
    begin = host_text.find(BACKSTOP_BEGIN)
    end = host_text.find(BACKSTOP_END)
    if begin == -1 or end == -1 or end < begin:
        raise RuntimeError(
            "S0 core is missing its BACKSTOP:BEGIN/END markers — cannot splice "
            f"the {SPLICE_KEY} artifact. S0 2.0.0+ is required."
        )
    head = host_text[: begin + len(BACKSTOP_BEGIN)]
    tail = host_text[end:]
    provenance = (
        f"<!-- Spliced from s0-backstop@{tag} (sha {sha}). Do not hand-edit "
        "between these markers; edit upstream in makegood-guardrails and re-lock. -->"
    )
    return (
        head + "\n" + provenance + "\n\n"
        + backstop_body.strip("\n") + "\n\n" + tail
    )


def compose_s0_body(
    source: str, s0_tag: str, backstop_tag: str, module_filename: str
) -> tuple[str, str, str]:
    """Fetch the S0 core and the backstop at their respective tags and return
    (spliced_body, s0_sha, backstop_sha). Network step."""
    core_body, s0_sha = fetch_module(source, s0_tag, module_filename)
    if BACKSTOP_BEGIN not in core_body:
        raise RuntimeError(
            f"S0 at {s0_tag} has no BACKSTOP markers but {SPLICE_KEY} is "
            "declared in the lock. Pin S0 to 2.0.0 or later, or remove the "
            f"{SPLICE_KEY} declaration."
        )
    raw_backstop, b_sha = fetch_module(source, backstop_tag, BACKSTOP_MODULE_FILENAME)
    body = splice_backstop(
        core_body, strip_frontmatter(raw_backstop), backstop_tag, b_sha
    )
    return body, s0_sha, b_sha


def latest_upstream_versions(source: str, keys) -> dict[str, str]:
    """Query upstream tags (git ls-remote — no clone) and return the highest
    semver per lock key. Used by --check's report-only upstream-newer notice."""
    result = subprocess.run(
        ["git", "ls-remote", "--tags", source], capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"git ls-remote {source} failed: {result.stderr.strip()}"
        )
    prefixes = {key: f"{key.lower().replace('_', '-')}-v" for key in keys}
    latest: dict[str, tuple[int, int, int]] = {}
    for line in result.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) != 2 or not parts[1].startswith("refs/tags/"):
            continue
        name = parts[1][len("refs/tags/"):]
        if name.endswith("^{}"):
            name = name[: -len("^{}")]
        for key, prefix in prefixes.items():
            if name.startswith(prefix):
                match = SEMVER_RE.match(name[len(prefix):])
                if match:
                    version = tuple(int(x) for x in match.groups())
                    if key not in latest or version > latest[key]:
                        latest[key] = version
    return {k: ".".join(str(x) for x in v) for k, v in latest.items()}


def fetch_module(source: str, tag: str, module_filename: str) -> tuple[str, str]:
    """Shallow-clone the makegood-guardrails repo at `tag`, read
    modules/<module_filename>, return (body_text, resolved_sha). Network step.
    Raises RuntimeError on any git failure so the caller can report cleanly."""
    tmp = tempfile.mkdtemp(prefix="guardrails-")
    try:
        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", tag, source, tmp],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"git clone of {source}@{tag} failed: {result.stderr.strip()}"
            )
        sha_result = subprocess.run(
            ["git", "-C", tmp, "rev-parse", "HEAD"],
            capture_output=True, text=True,
        )
        sha = sha_result.stdout.strip() if sha_result.returncode == 0 else "unknown"
        module_path = Path(tmp) / "modules" / module_filename
        if not module_path.exists():
            raise RuntimeError(
                f"module modules/{module_filename} not found in "
                f"{source}@{tag}"
            )
        return module_path.read_text(), sha
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def resolve_guardrails(repo_root: Path) -> int:
    """Fetch each declared guardrail version, vendor it into the path named in
    the lock's resolved block (with banner), and write the resolved block back
    (version, tag, sha). Network step. Idempotent for pinned versions."""
    lock = load_lock(repo_root)
    source = lock["source"]
    declared = lock["declared"]
    resolved = lock.setdefault("resolved", {})

    for key, version in declared.items():
        if key == SPLICE_KEY:
            continue  # resolved together with its host module below
        tag = tag_for(key, version)
        entry = resolved.get(key)
        if not entry or "vendored" not in entry:
            raise RuntimeError(
                f"lock resolved.{key}.vendored missing — cannot determine "
                f"where to vendor {key}. Set it in {LOCK_NAME}."
            )
        vendored_rel = entry["vendored"]
        module_filename = Path(vendored_rel).name

        print(f"  resolving {key} {version} (tag {tag})...")
        if key == SPLICE_HOST_KEY and SPLICE_KEY in declared:
            backstop_version = declared[SPLICE_KEY]
            backstop_tag = tag_for(SPLICE_KEY, backstop_version)
            print(f"    splicing {SPLICE_KEY} {backstop_version} (tag {backstop_tag})...")
            body, sha, backstop_sha = compose_s0_body(
                source, tag, backstop_tag, module_filename
            )
            resolved[SPLICE_KEY] = {
                "version": backstop_version,
                "tag": backstop_tag,
                "sha": backstop_sha,
                "spliced_into": vendored_rel,
            }
        else:
            body, sha = fetch_module(source, tag, module_filename)
            if key == SPLICE_HOST_KEY and BACKSTOP_BEGIN in body:
                raise RuntimeError(
                    f"S0 {version} carries BACKSTOP splice markers but "
                    f"{SPLICE_KEY} is not declared in {LOCK_NAME}. Add it "
                    f"(e.g. --update-guardrails {SPLICE_KEY}=1.0.0) and re-resolve."
                )

        dest = repo_root / vendored_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(banner_for(tag, sha) + body)

        resolved[key] = {
            "version": version,
            "tag": tag,
            "sha": sha,
            "vendored": vendored_rel,
        }
        print(f"    vendored -> {vendored_rel}")

    write_lock(repo_root, lock)
    print(f"  {LOCK_NAME} updated.")
    return 0


def update_guardrails(repo_root: Path, bumps: list[str]) -> int:
    """Bump declared versions (e.g. F0=1.3.0), then re-resolve. The deliberate
    upgrade action; produces a reviewable diff to the lock and vendored files."""
    lock = load_lock(repo_root)
    declared = lock["declared"]
    for bump in bumps:
        if "=" not in bump:
            raise RuntimeError(f"bad --update-guardrails arg '{bump}', expected KEY=VERSION")
        key, version = bump.split("=", 1)
        key = key.strip()
        version = version.strip()
        if key not in declared:
            if key == SPLICE_KEY:
                # The backstop is the one guardrail a library legitimately
                # adds after the fact (adopting the S0 2.0.0 split).
                print(f"  adding new declared guardrail {key} = {version}")
            else:
                raise RuntimeError(
                    f"'{key}' is not a declared guardrail in {LOCK_NAME} "
                    f"(have: {', '.join(declared)})"
                )
        else:
            print(f"  declaring {key} -> {version} (was {declared[key]})")
        declared[key] = version
    write_lock(repo_root, lock)
    return resolve_guardrails(repo_root)


def check_guardrails(repo_root: Path) -> list[tuple[str, str]]:
    """Report-only. Two checks, neither of which modifies anything or fails
    the run:

    1. Drift — compare each vendored guardrail file's body (banner stripped)
       against the version recorded in the lock's resolved block, by
       re-fetching from upstream. For S0 with a spliced backstop, the expected
       body is re-composed (core + backstop at their locked tags).
    2. Upstream-newer — report when upstream has a newer tagged version than
       the library declares, so stale libraries surface themselves. Adoption
       stays deliberate (--update-guardrails); this is a notice, not an action.

    Returns (level, message) tuples; level is DRIFT, NEWER, or WARN.
    Empty list means in sync and current."""
    messages: list[tuple[str, str]] = []
    try:
        lock = load_lock(repo_root)
    except RuntimeError as exc:
        return [("WARN", str(exc))]
    source = lock["source"]
    declared = lock.get("declared", {})
    resolved = lock.get("resolved", {})

    for key, entry in resolved.items():
        if key == SPLICE_KEY:
            continue  # verified as part of its host module's composed body
        vendored_rel = entry.get("vendored")
        tag = entry.get("tag")
        if not vendored_rel or not tag:
            messages.append(("DRIFT", f"{key}: lock resolved block incomplete"))
            continue
        dest = repo_root / vendored_rel
        if not dest.exists():
            messages.append(
                ("DRIFT", f"{key}: vendored file missing at {vendored_rel}")
            )
            continue
        try:
            if key == SPLICE_HOST_KEY and SPLICE_KEY in resolved:
                backstop_tag = resolved[SPLICE_KEY].get("tag")
                if not backstop_tag:
                    messages.append(
                        ("DRIFT", f"{SPLICE_KEY}: lock resolved block incomplete")
                    )
                    continue
                upstream_body, _, _ = compose_s0_body(
                    source, tag, backstop_tag, Path(vendored_rel).name
                )
            else:
                upstream_body, _ = fetch_module(
                    source, tag, Path(vendored_rel).name
                )
        except RuntimeError as exc:
            messages.append(
                ("WARN", f"{key}: could not verify against upstream ({exc})")
            )
            continue
        local_body = strip_banner(dest.read_text())
        if local_body != upstream_body:
            messages.append((
                "DRIFT",
                f"{key}: vendored {vendored_rel} differs from {tag} upstream "
                "— it was hand-edited, or the lock points at the wrong tag. "
                "Re-run --resolve-guardrails to restore.",
            ))

    # Upstream-newer notice (one ls-remote for all keys; no clone).
    try:
        latest = latest_upstream_versions(source, declared.keys())
        for key, declared_version in declared.items():
            match = SEMVER_RE.match(str(declared_version))
            if not match or key not in latest:
                continue
            declared_tuple = tuple(int(x) for x in match.groups())
            latest_tuple = tuple(int(x) for x in latest[key].split("."))
            if latest_tuple > declared_tuple:
                messages.append((
                    "NEWER",
                    f"{key}: {latest[key]} available upstream (declared: "
                    f"{declared_version}) — adopt with --update-guardrails "
                    f"{key}={latest[key]}",
                ))
    except RuntimeError as exc:
        messages.append(("WARN", f"could not query upstream tags ({exc})"))

    return messages


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--version",
        action="version",
        version=f"build-deploy-bundles.py {SCRIPT_VERSION}",
        help="Print the script version (a skill-versioned artifact) and exit.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report which agent bundles are out of sync without writing",
    )
    parser.add_argument(
        "--agent",
        help="Build a single agent by basename (without .md), e.g. "
        "'donor_research_and_enrichment'",
    )
    parser.add_argument(
        "--all-inclusive",
        action="store_true",
        help="Build (or check) the all-inclusive variant: inlines every "
        "conditional addendum alongside required-reading content. Use for "
        "runtimes where work-time fetch of conditional addenda is unreliable.",
    )
    parser.add_argument(
        "--resolve-guardrails",
        action="store_true",
        help="Fetch the guardrail versions declared in guardrails.lock from "
        "makegood-guardrails and vendor them into modules/ (with a generated "
        "banner), then write the resolved block. Network step; separate from "
        "the offline bundle build.",
    )
    parser.add_argument(
        "--update-guardrails",
        nargs="+",
        metavar="KEY=VERSION",
        help="Bump declared guardrail version(s) (e.g. F0=1.3.0) then "
        "re-resolve. The deliberate upgrade action — produces a reviewable "
        "diff to guardrails.lock and the vendored module.",
    )
    args = parser.parse_args()

    repo_root = Path.cwd()
    agents_dir = repo_root / "agents"
    deploy_dir = repo_root / "deploy" / "agents"

    # Guardrail subcommands run independently of the bundle build (they touch
    # the network; the bundle build does not).
    if args.update_guardrails:
        try:
            return update_guardrails(repo_root, args.update_guardrails)
        except RuntimeError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2

    if args.resolve_guardrails:
        try:
            return resolve_guardrails(repo_root)
        except RuntimeError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2

    if not agents_dir.is_dir():
        print(
            f"error: agents/ directory not found in {repo_root}. "
            "Run from the repo root.",
            file=sys.stderr,
        )
        return 2

    if args.agent:
        agent_path = agents_dir / f"{args.agent}.md"
        if not agent_path.exists():
            print(f"error: agent not found: {agent_path}", file=sys.stderr)
            return 2
        agent_paths = [agent_path]
    else:
        agent_paths = sorted(agents_dir.glob("*.md"))

    if not agent_paths:
        print(f"warning: no agent files found in {agents_dir}", file=sys.stderr)
        return 0

    if args.check:
        # Report guardrail drift first (report-only — never fails the run, so
        # libraries in repos we no longer own can be checked without implying
        # an action we can't take). Skipped silently if no lock is present.
        if (repo_root / LOCK_NAME).exists():
            g_messages = check_guardrails(repo_root)
            if g_messages:
                print("  guardrails:")
                for level, msg in g_messages:
                    print(f"    [{level}] {msg}")
            if not any(level == "DRIFT" for level, _ in g_messages):
                print("  [ok] guardrails match locked versions")

        drift = []
        for agent_path in agent_paths:
            if args.all_inclusive:
                in_sync = check_agent_all_inclusive(agent_path, repo_root, deploy_dir)
                label = f"{agent_path.stem}.all-inclusive.md"
            else:
                in_sync = check_agent(agent_path, repo_root, deploy_dir)
                label = agent_path.name
            status = "ok" if in_sync else "DRIFT"
            print(f"  [{status}] {label}")
            if not in_sync:
                drift.append(label)
        if drift:
            print(
                f"\n{len(drift)} bundle(s) out of sync. "
                "Run without --check to rebuild.",
                file=sys.stderr,
            )
            return 1
        return 0

    for agent_path in agent_paths:
        try:
            if args.all_inclusive:
                output_path = build_agent_all_inclusive(
                    agent_path, repo_root, deploy_dir
                )
            else:
                output_path = build_agent(agent_path, repo_root, deploy_dir)
            print(f"  built {output_path.relative_to(repo_root)}")
        except RuntimeError as exc:
            print(f"  error building {agent_path.name}: {exc}", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
