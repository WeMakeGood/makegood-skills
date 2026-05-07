#!/usr/bin/env python3
"""Sync vendored skill content from per-skill GitHub releases.

Reads skills.yaml at the repo root, fetches each skill's pinned release ZIP from
GitHub via gh, unzips it, and places the skill folder under the aggregator's
plugin folder. The aggregator plugin folder is auto-detected as the single
folder under plugins/.

Run from the aggregator repo root:

    python3 scripts/sync_skills.py

Requirements: gh CLI authenticated (with access to private repos if any are
listed in skills.yaml), Python 3.10+, PyYAML or skills.yaml in JSON.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGINS_DIR = REPO_ROOT / "plugins"
MANIFEST = REPO_ROOT / "skills.yaml"


def find_plugin_skills_dir() -> Path:
    """Auto-detect the aggregator plugin folder under plugins/."""
    if not PLUGINS_DIR.is_dir():
        raise RuntimeError(f"plugins/ not found at {PLUGINS_DIR}")
    plugin_folders = [p for p in PLUGINS_DIR.iterdir() if p.is_dir()]
    if len(plugin_folders) != 1:
        raise RuntimeError(
            f"Expected exactly one plugin folder under {PLUGINS_DIR}, "
            f"found {len(plugin_folders)}: {[p.name for p in plugin_folders]}"
        )
    return plugin_folders[0] / "skills"


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


def sync_one(skill_entry: dict, plugin_skills_dir: Path):
    skill_name = skill_entry["name"]
    repo = skill_entry["repo"]
    tag = skill_entry["tag"]

    print(f"  {skill_name} <- {repo}@{tag}")

    target = plugin_skills_dir / skill_name
    if target.exists():
        shutil.rmtree(target)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        zip_path = fetch_release_zip(repo, tag, tmp_path)

        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(tmp_path)

        extracted = tmp_path / skill_name
        if not extracted.exists():
            raise RuntimeError(f"Expected {extracted} in ZIP for {skill_name}")

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(extracted, target)


def main():
    if not MANIFEST.exists():
        print(f"ERROR: {MANIFEST} not found", file=sys.stderr)
        sys.exit(1)

    plugin_skills_dir = find_plugin_skills_dir()
    skills = load_manifest()
    print(f"Syncing {len(skills)} skills into {plugin_skills_dir}")

    plugin_skills_dir.mkdir(parents=True, exist_ok=True)

    for skill_entry in skills:
        sync_one(skill_entry, plugin_skills_dir)

    print("\nSync complete.")


if __name__ == "__main__":
    main()
