#!/usr/bin/env python3
"""
Initialize a new skill directory with the standard structure.

Usage:
    python init_skill.py <skill-name> [--path <skills-directory>]

Creates:
    skills/<skill-name>/
    ├── SKILL.md          # Template with frontmatter
    ├── references/       # For additional documentation
    └── scripts/          # For utility scripts
"""

import argparse
import re
import sys
from pathlib import Path


SKILL_TEMPLATE = '''---
name: {name}
description: [Describe what this skill does and when Claude should use it. Include keywords for discovery. Write in third person.]
---

# {title}

## Overview

[Brief explanation of the skill's purpose and capabilities.]

## Quick Start

[Provide a simple example or the most common use case.]

## Instructions

[Step-by-step guidance for Claude to follow when using this skill.]

## Examples

[Concrete examples showing input/output or usage patterns.]

## Additional Resources

[If needed, link to files in references/ folder:]

- See [references/REFERENCE.md](references/REFERENCE.md) for detailed documentation
'''


def validate_name(name: str) -> tuple:
    """Validate skill name and return (is_valid, error_message)."""
    if not name:
        return False, "Name cannot be empty"

    if len(name) > 64:
        return False, f"Name exceeds 64 characters ({len(name)} chars)"

    if not re.match(r'^[a-z0-9-]+$', name):
        return False, "Name must contain only lowercase letters, numbers, and hyphens"

    if name.startswith('-') or name.endswith('-'):
        return False, "Name cannot start or end with a hyphen"

    if '--' in name:
        return False, "Name cannot contain consecutive hyphens"

    if re.search(r'(anthropic|claude)', name, re.IGNORECASE):
        return False, "Name cannot contain reserved words: 'anthropic', 'claude'"

    return True, None


def to_title(name: str) -> str:
    """Convert hyphenated name to title case."""
    return ' '.join(word.capitalize() for word in name.split('-'))


def init_skill(name: str, base_path: Path) -> Path:
    """Initialize a new skill directory."""
    skill_path = base_path / name

    if skill_path.exists():
        print(f"ERROR: Directory already exists: {skill_path}")
        sys.exit(1)

    # Create directory structure
    skill_path.mkdir(parents=True)
    (skill_path / "references").mkdir()
    (skill_path / "scripts").mkdir()

    # Create SKILL.md from template
    title = to_title(name)
    content = SKILL_TEMPLATE.format(name=name, title=title)
    (skill_path / "SKILL.md").write_text(content)

    # Create placeholder reference file
    ref_content = f"# {title} Reference\n\n[Detailed documentation goes here]\n"
    (skill_path / "references" / "REFERENCE.md").write_text(ref_content)

    return skill_path


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new skill directory"
    )
    parser.add_argument(
        "name",
        help="Skill name (lowercase, hyphens allowed)"
    )
    parser.add_argument(
        "--path",
        default="skills",
        help="Base directory for skills (default: skills/)"
    )
    args = parser.parse_args()

    # Validate name
    is_valid, error = validate_name(args.name)
    if not is_valid:
        print(f"ERROR: Invalid skill name: {error}")
        sys.exit(1)

    base_path = Path(args.path)
    if not base_path.exists():
        print(f"ERROR: Base path does not exist: {base_path}")
        sys.exit(1)

    # Create skill
    skill_path = init_skill(args.name, base_path)

    print(f"Created skill: {skill_path}")
    print()
    print("Next steps:")
    print(f"  1. Edit {skill_path}/SKILL.md")
    print("  2. Update the description with trigger conditions")
    print("  3. Add instructions and examples")
    print("  4. Validate: python scripts/validate.py " + str(skill_path))
    print("  5. Test: python scripts/dry-run.py " + str(skill_path))


if __name__ == "__main__":
    main()
