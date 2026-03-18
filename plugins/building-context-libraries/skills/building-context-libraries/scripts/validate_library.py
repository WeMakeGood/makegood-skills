#!/usr/bin/env python3
"""
Validate a context library for common issues.
Checks cross-references, duplications, and structure.
"""

import os
import sys
import re
import yaml
from pathlib import Path
from collections import defaultdict


def parse_frontmatter(content: str) -> tuple:
    """Extract YAML frontmatter and body from markdown."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1])
                body = parts[2]
                return frontmatter, body
            except yaml.YAMLError:
                pass
    return {}, content


def find_references(content: str) -> list:
    """Find cross-references in content."""
    # Pattern: [Module Name] or See [Module Name]
    pattern = r'\[([A-Z][^\]]+)\]'
    matches = re.findall(pattern, content)
    # Filter out likely markdown links
    refs = [m for m in matches if not m.startswith('http') and '/' not in m]
    return refs


def find_content_markers(content: str) -> dict:
    """Count content markers in content."""
    markers = {
        'PROPOSED': len(re.findall(r'\[PROPOSED\]', content)),
        'HIGH-STAKES': len(re.findall(r'\[HIGH-STAKES\]', content))
    }
    return markers


def extract_key_phrases(content: str, min_words: int = 5) -> set:
    """Extract key phrases for duplication detection."""
    # Remove code blocks
    content = re.sub(r'```[\s\S]*?```', '', content)
    # Remove frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]

    sentences = re.split(r'[.!?]\s+', content)
    phrases = set()

    for sentence in sentences:
        words = sentence.split()
        if len(words) >= min_words:
            # Normalize: lowercase, strip punctuation
            normalized = ' '.join(w.lower().strip('.,!?:;') for w in words[:10])
            if len(normalized) > 20:
                phrases.add(normalized)

    return phrases


def analyze_module(filepath: Path) -> dict:
    """Analyze a single module file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = parse_frontmatter(content)

        return {
            'path': str(filepath),
            'filename': filepath.name,
            'module_id': frontmatter.get('module_id'),
            'module_name': frontmatter.get('module_name'),
            'tier': frontmatter.get('tier'),
            'purpose': frontmatter.get('purpose'),
            'confidence': frontmatter.get('confidence'),
            'references': find_references(body),
            'markers': find_content_markers(body),
            'phrases': extract_key_phrases(body),
            'has_agent_instructions': 'agent instructions' in body.lower(),
            'content': content,
            'error': None
        }
    except Exception as e:
        return {
            'path': str(filepath),
            'filename': filepath.name,
            'error': str(e)
        }


def find_modules(library_dir: Path) -> list:
    """Find all module files in library."""
    modules = []
    for subdir in ['foundation', 'shared', 'specialized']:
        subpath = library_dir / subdir
        if subpath.exists():
            modules.extend(subpath.glob('*.md'))
    # Also check root
    modules.extend(library_dir.glob('*.md'))
    return modules


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_library.py <library_dir>")
        sys.exit(1)

    library_dir = Path(sys.argv[1])

    if not library_dir.exists():
        print(f"Error: Directory '{library_dir}' not found")
        sys.exit(1)

    module_files = find_modules(library_dir)

    if not module_files:
        print(f"No modules found in '{library_dir}'")
        sys.exit(0)

    modules = []
    module_names = set()
    all_phrases = defaultdict(list)  # phrase -> list of modules containing it
    issues = []

    print("Library Validation Report")
    print("=========================")
    print(f"Directory: {library_dir}")
    print(f"Modules found: {len(module_files)}")
    print()

    # Analyze all modules
    for mf in module_files:
        result = analyze_module(mf)
        modules.append(result)

        if result.get('error'):
            issues.append(f"ERROR reading {result['filename']}: {result['error']}")
            continue

        if result['module_name']:
            module_names.add(result['module_name'])
        if result['module_id']:
            module_names.add(result['module_id'])

        # Track phrases for duplication detection
        for phrase in result.get('phrases', set()):
            all_phrases[phrase].append(result['filename'])

    # Check for issues
    print("VALIDATION CHECKS")
    print("-" * 50)

    # 1. Frontmatter completeness
    print("\n1. Frontmatter Completeness")
    required_fields = ['module_id', 'module_name', 'tier', 'purpose']
    for m in modules:
        if m.get('error'):
            continue
        missing = [f for f in required_fields if not m.get(f)]
        if missing:
            issues.append(f"  {m['filename']}: Missing {', '.join(missing)}")
            print(f"  FAIL: {m['filename']} missing {', '.join(missing)}")
        else:
            print(f"  OK: {m['filename']}")

    # 2. Cross-reference validation
    print("\n2. Cross-Reference Validation")
    for m in modules:
        if m.get('error'):
            continue
        for ref in m.get('references', []):
            # Check if reference matches any known module
            if ref not in module_names:
                # Could be a valid reference to something else, just warn
                print(f"  WARN: {m['filename']} references '{ref}' - verify exists")

    # 3. Duplication check
    print("\n3. Duplication Check")
    duplicates_found = False
    for phrase, files in all_phrases.items():
        if len(files) > 1:
            duplicates_found = True
            issues.append(f"  Possible duplicate in {', '.join(files)}: '{phrase[:50]}...'")
            print(f"  WARN: Similar content in {', '.join(files)}")

    if not duplicates_found:
        print("  OK: No obvious duplications detected")

    # 4. Build artifact check (markers should be removed before delivery)
    print("\n4. Build Artifacts (should be 0 in finished library)")
    for m in modules:
        if m.get('error'):
            continue
        markers = m.get('markers', {})
        proposed = markers.get('PROPOSED', 0)
        high_stakes = markers.get('HIGH-STAKES', 0)
        if proposed > 0 or high_stakes > 0:
            print(f"  WARN: {m['filename']}: {proposed} [PROPOSED], {high_stakes} [HIGH-STAKES] — remove before delivery")
            issues.append(f"  {m['filename']}: Build-time markers not removed ({proposed} PROPOSED, {high_stakes} HIGH-STAKES)")
        else:
            print(f"  OK: {m['filename']}: no build-time markers")

    # 5. Agent instructions (standard guardrail modules are exempt)
    print("\n5. Agent Instructions Section")
    guardrail_prefixes = ('F0_agent_behavioral_standards', 'S0_natural_prose_standards')
    for m in modules:
        if m.get('error'):
            continue
        if m['filename'].startswith(guardrail_prefixes):
            print(f"  SKIP: {m['filename']} (standard guardrail module)")
            continue
        if not m.get('has_agent_instructions'):
            issues.append(f"  {m['filename']}: Missing Agent Instructions section")
            print(f"  WARN: {m['filename']} missing Agent Instructions")
        else:
            print(f"  OK: {m['filename']}")

    # Summary
    print()
    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Modules analyzed: {len(modules)}")
    print(f"Issues found: {len(issues)}")

    if issues:
        print()
        print("Issues to address:")
        for issue in issues:
            print(issue)
        print()
        print("Status: NEEDS FIXES")
        sys.exit(1)
    else:
        print()
        print("Status: PASS")
        sys.exit(0)


if __name__ == '__main__':
    main()
