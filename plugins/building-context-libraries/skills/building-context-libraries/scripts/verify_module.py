#!/usr/bin/env python3
"""
Verify module facts against source documents.
Flags content that doesn't appear in any source file.

Usage:
    python verify_module.py <module_path> <source_dir>

Example:
    python verify_module.py ./context-library/modules/foundation/F1_identity.md ./sources
"""

import sys
import re
from pathlib import Path


def extract_facts(module_path: Path) -> list[tuple[str, str]]:
    """
    Extract potential facts (names, numbers, emails, etc.) from module.
    Returns list of (fact, category) tuples.
    """
    content = module_path.read_text()

    facts = []

    # EINs
    for match in re.findall(r'\d{2}-\d{7}', content):
        facts.append((match, 'EIN'))

    # Emails
    for match in re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', content):
        facts.append((match, 'email'))

    # Phone numbers
    for match in re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', content):
        facts.append((match, 'phone'))

    # Years (standalone, likely founding dates or milestones)
    for match in re.findall(r'\b(19|20)\d{2}\b', content):
        facts.append((match, 'year'))

    # Dollar amounts
    for match in re.findall(r'\$[\d,]+(?:\.\d{2})?', content):
        facts.append((match, 'amount'))

    # Quoted strings (likely titles, names, specific terms)
    for match in re.findall(r'"([^"]+)"', content):
        if len(match) > 3:  # Skip very short quotes
            facts.append((match, 'quoted'))

    # URLs
    for match in re.findall(r'https?://[^\s\)]+', content):
        facts.append((match, 'URL'))

    return facts


def search_sources(fact: str, source_dir: Path) -> str | None:
    """Search for fact in source files. Returns filename if found, None otherwise."""
    for source_file in source_dir.rglob('*.md'):
        try:
            content = source_file.read_text()
            if fact in content:
                return source_file.name
        except Exception:
            continue

    # Also check .txt files
    for source_file in source_dir.rglob('*.txt'):
        try:
            content = source_file.read_text()
            if fact in content:
                return source_file.name
        except Exception:
            continue

    return None


def main():
    if len(sys.argv) < 3:
        print("Usage: verify_module.py <module_path> <source_dir>")
        print("Example: verify_module.py ./modules/F1_identity.md ./sources")
        sys.exit(1)

    module_path = Path(sys.argv[1])
    source_dir = Path(sys.argv[2])

    if not module_path.exists():
        print(f"Error: Module file '{module_path}' not found")
        sys.exit(1)

    if not source_dir.exists():
        print(f"Error: Source directory '{source_dir}' not found")
        sys.exit(1)

    facts = extract_facts(module_path)

    if not facts:
        print("No extractable facts found (EINs, emails, phones, years, amounts, quotes, URLs)")
        print("Manual verification recommended for names and other content.")
        sys.exit(0)

    print(f"Verifying {len(facts)} extracted facts from {module_path.name}...")
    print(f"Source directory: {source_dir}")
    print()

    verified = []
    unverified = []

    for fact, category in facts:
        source = search_sources(fact, source_dir)
        if source:
            verified.append((fact, category, source))
            print(f"✓ [{category}] '{fact}' found in {source}")
        else:
            unverified.append((fact, category))
            print(f"✗ [{category}] '{fact}' NOT FOUND in sources")

    print()
    print("=" * 60)
    print(f"RESULTS: {len(verified)} verified, {len(unverified)} unverified")
    print("=" * 60)

    if unverified:
        print()
        print("⚠️  UNVERIFIED FACTS - Review these carefully:")
        for fact, category in unverified:
            print(f"  - [{category}] {fact}")
        print()
        print("Actions needed:")
        print("1. Search source files manually for these facts")
        print("2. If found: the pattern may need adjustment (contact maintainer)")
        print("3. If NOT found: remove from module or flag for user review")
        sys.exit(1)
    else:
        print()
        print("✓ All extracted facts verified against sources")
        print()
        print("Note: This script checks patterns (EINs, emails, dates, etc.)")
        print("Manual review still recommended for names and descriptive content.")


if __name__ == "__main__":
    main()
