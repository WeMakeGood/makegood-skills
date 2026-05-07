#!/usr/bin/env python3
"""
Package a skill for distribution.

Usage:
    python package_skill.py <skill-path> [--output <output-dir>]

Creates a zip file containing the skill directory, ready for:
- Uploading to Claude.ai
- Distribution to other users
- Archival

The script validates the skill before packaging and refuses to
package invalid skills.
"""

import argparse
import shutil
import sys
import tempfile
from pathlib import Path
from zipfile import ZipFile

# Import validation from sibling module
from validate import validate_skill


def package_skill(skill_path: Path, output_dir: Path) -> Path:
    """
    Package a skill into a zip file.

    Returns the path to the created zip file.
    """
    skill_name = skill_path.name
    zip_filename = f"{skill_name}.zip"
    zip_path = output_dir / zip_filename

    # Remove existing zip if present
    if zip_path.exists():
        zip_path.unlink()

    # Create zip file
    with ZipFile(zip_path, "w") as zipf:
        for file_path in skill_path.rglob("*"):
            if file_path.is_file():
                # Skip hidden files and __pycache__
                if any(
                    part.startswith(".") or part == "__pycache__"
                    for part in file_path.parts
                ):
                    continue

                # Add file with relative path from skill root
                arcname = file_path.relative_to(skill_path.parent)
                zipf.write(file_path, arcname)

    return zip_path


def get_skill_info(skill_path: Path) -> dict:
    """Extract basic info about the skill for the summary."""
    skill_md = skill_path / "SKILL.md"
    info = {
        "name": skill_path.name,
        "files": [],
        "total_size": 0,
    }

    for file_path in skill_path.rglob("*"):
        if file_path.is_file():
            if any(
                part.startswith(".") or part == "__pycache__"
                for part in file_path.parts
            ):
                continue
            rel_path = file_path.relative_to(skill_path)
            size = file_path.stat().st_size
            info["files"].append((str(rel_path), size))
            info["total_size"] += size

    # Extract description from frontmatter
    if skill_md.exists():
        content = skill_md.read_text()
        for line in content.split("\n"):
            if line.startswith("description:"):
                info["description"] = line.split(":", 1)[1].strip().strip("\"'")
                break

    return info


def main():
    parser = argparse.ArgumentParser(
        description="Package a skill for distribution"
    )
    parser.add_argument(
        "skill_path",
        help="Path to skill directory"
    )
    parser.add_argument(
        "--output", "-o",
        default=".",
        help="Output directory for zip file (default: current directory)"
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Skip validation (not recommended)"
    )
    args = parser.parse_args()

    skill_path = Path(args.skill_path).resolve()
    output_dir = Path(args.output).resolve()

    if not skill_path.is_dir():
        print(f"ERROR: {skill_path} is not a directory")
        sys.exit(1)

    if not output_dir.is_dir():
        print(f"ERROR: Output directory does not exist: {output_dir}")
        sys.exit(1)

    # Validate first (unless skipped)
    if not args.skip_validation:
        print("Validating skill before packaging...")
        result = validate_skill(skill_path)

        if not result.passed:
            print()
            print("ERROR: Skill validation failed. Fix errors before packaging.")
            print("       Use --skip-validation to package anyway (not recommended).")
            sys.exit(1)

        if result.warnings:
            print()
            print(f"WARNING: Skill has {len(result.warnings)} warning(s).")
            print("         Consider fixing warnings before distribution.")
        print()

    # Get skill info
    info = get_skill_info(skill_path)

    # Package
    print(f"Packaging skill: {info['name']}")
    print("-" * 40)

    zip_path = package_skill(skill_path, output_dir)

    # Summary
    print()
    print("Package contents:")
    for file_name, size in sorted(info["files"]):
        print(f"  {file_name} ({size:,} bytes)")

    print()
    print(f"Total files: {len(info['files'])}")
    print(f"Total size: {info['total_size']:,} bytes")
    print()
    print(f"Created: {zip_path}")
    print(f"Zip size: {zip_path.stat().st_size:,} bytes")

    # Usage hints
    print()
    print("To use this skill:")
    print("  - Claude.ai: Upload via Settings > Features > Skills")
    print("  - Claude Code: Extract to ~/.claude/skills/ or .claude/skills/")
    print("  - Claude API: Upload via /v1/skills endpoint")


if __name__ == "__main__":
    main()
