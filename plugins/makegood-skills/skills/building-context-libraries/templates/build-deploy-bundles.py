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
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# @ directive matcher
#
# Match a line that begins (after optional whitespace) with @ followed by a
# path. The path is everything after @ until end-of-line, stripped. Only
# lines that consist solely of an @-directive are expanded; @ embedded in
# prose is left alone.
# ---------------------------------------------------------------------------

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
# CLI
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
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
    args = parser.parse_args()

    repo_root = Path.cwd()
    agents_dir = repo_root / "agents"
    deploy_dir = repo_root / "deploy" / "agents"

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
