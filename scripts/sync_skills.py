#!/usr/bin/env python3
"""Sync vendored skill content from per-skill GitHub releases.

Reads skills.yaml at the repo root, fetches each skill's pinned release ZIP from
GitHub via gh, unzips it, and places the skill folder at:

    plugins/makegood-skills/skills/<skill-name>/

This produces an aggregator plugin containing all Make Good skills as a single
installable unit (`/plugin install makegood-skills@makegood-skills`).

Run from the makegood-skills repo root:

    python3 scripts/sync_skills.py

Requirements: gh CLI authenticated, yaml package (or skills.yaml in JSON).
"""
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGIN_SKILLS_DIR = REPO_ROOT / "plugins" / "makegood-skills" / "skills"
MANIFEST = REPO_ROOT / "skills.yaml"


def load_manifest() -> list:
    """Parse the skills manifest. Supports YAML or JSON-as-YAML."""
    text = MANIFEST.read_text()
    try:
        import yaml
        data = yaml.safe_load(text)
    except ImportError:
        data = json.loads(text)
    return data["skills"]


def fetch_release_zip(repo: str, tag: str, dest_dir: Path) -> Path:
    """Download the release ZIP for a given repo+tag using gh."""
    subprocess.run(
        ["gh", "release", "download", tag, "--repo", repo, "--dir", str(dest_dir), "--pattern", "*.zip"],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    zips = list(dest_dir.glob("*.zip"))
    if not zips:
        raise RuntimeError(f"No ZIP found in release for {repo}@{tag}")
    return zips[0]


def sync_one(skill_entry: dict):
    skill_name = skill_entry["name"]
    repo = skill_entry["repo"]
    tag = skill_entry["tag"]

    print(f"  {skill_name} <- {repo}@{tag}")

    target = PLUGIN_SKILLS_DIR / skill_name
    if target.exists():
        shutil.rmtree(target)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        zip_path = fetch_release_zip(repo, tag, tmp_path)

        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(tmp_path)

        # The ZIP contains a top-level <skill-name>/ folder
        extracted = tmp_path / skill_name
        if not extracted.exists():
            raise RuntimeError(f"Expected {extracted} in ZIP for {skill_name}")

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(extracted, target)


def main():
    if not MANIFEST.exists():
        print(f"ERROR: {MANIFEST} not found", file=sys.stderr)
        sys.exit(1)

    skills = load_manifest()
    print(f"Syncing {len(skills)} skills into {PLUGIN_SKILLS_DIR}")

    PLUGIN_SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    for skill_entry in skills:
        sync_one(skill_entry)

    print("\nSync complete.")


if __name__ == "__main__":
    main()
