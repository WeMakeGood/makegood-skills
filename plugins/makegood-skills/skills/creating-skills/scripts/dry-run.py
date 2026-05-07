#!/usr/bin/env python3
"""
Simulate the full skill loading flow.

Usage:
    python dry-run.py <skill-path>
    python dry-run.py <skill-path> "test prompt"

Simulates:
1. Metadata extraction (Level 1 - always loaded)
2. Trigger matching against test prompt
3. SKILL.md content loading (Level 2)
4. File reference detection
5. Resource loading simulation (Level 3)
6. Token estimation for loaded content
7. Complete "effective context" output
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def estimate_tokens(text: str) -> int:
    """Rough token estimation (approximately 4 chars per token)."""
    return len(text) // 4


def extract_frontmatter(content: str) -> Tuple[Dict[str, str], str]:
    """Extract frontmatter and body from SKILL.md."""
    if not content.startswith("---"):
        return {}, content

    lines = content.split("\n")
    end_index = None

    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = i
            break

    if end_index is None:
        return {}, content

    frontmatter = {}
    for line in lines[1:end_index]:
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip("\"'")
            frontmatter[key] = value

    body = "\n".join(lines[end_index + 1:]).strip()
    return frontmatter, body


def find_file_references(content: str) -> List[str]:
    """Find markdown file references in content."""
    # Match [text](path) where path is not a URL
    pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(pattern, content)

    refs = []
    for text, path in matches:
        if not path.startswith(("http://", "https://", "#")):
            refs.append(path)

    return refs


def simulate_trigger_match(description: str, prompt: str) -> Tuple[bool, List[str]]:
    """Simulate trigger matching between description and prompt."""
    stop_words = {
        "a", "an", "the", "and", "or", "for", "to", "in", "on", "at", "by",
        "with", "from", "of", "is", "are", "was", "were", "be", "been",
        "being", "have", "has", "had", "do", "does", "did", "will", "would",
        "could", "should", "may", "might", "must", "shall", "can", "this",
        "that", "these", "those", "it", "its", "when", "use", "using", "i",
        "me", "my", "please", "help", "want", "need",
    }

    desc_words = set(
        word.lower()
        for word in re.findall(r"\b[a-zA-Z]+\b", description)
        if word.lower() not in stop_words and len(word) > 2
    )

    prompt_words = set(
        word.lower()
        for word in re.findall(r"\b[a-zA-Z]+\b", prompt)
        if word.lower() not in stop_words and len(word) > 2
    )

    matches = list(desc_words & prompt_words)
    triggered = len(matches) >= 2 or (
        len(matches) == 1 and len(prompt_words) <= 3
    )

    return triggered, matches


def dry_run(skill_path: Path, test_prompt: Optional[str] = None):
    """Perform a full dry run simulation."""
    skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        print(f"ERROR: SKILL.md not found in {skill_path}")
        sys.exit(1)

    content = skill_md.read_text()
    frontmatter, body = extract_frontmatter(content)

    name = frontmatter.get("name", "unknown")
    description = frontmatter.get("description", "")

    print()
    print("=" * 60)
    print("SKILL DRY RUN SIMULATION")
    print("=" * 60)

    # Level 1: Metadata
    print()
    print("-" * 60)
    print("LEVEL 1: METADATA (Always loaded at startup)")
    print("-" * 60)
    print()
    print(f"Name: {name}")
    print(f"Description: {description}")
    print()

    metadata_tokens = estimate_tokens(f"{name} {description}")
    print(f"Token estimate: ~{metadata_tokens} tokens")

    # Trigger matching
    if test_prompt:
        print()
        print("-" * 60)
        print("TRIGGER MATCHING")
        print("-" * 60)
        print()
        print(f"Test prompt: \"{test_prompt}\"")
        print()

        triggered, matches = simulate_trigger_match(description, test_prompt)

        if matches:
            print(f"Matching keywords: {', '.join(matches)}")
        else:
            print("Matching keywords: (none)")

        print()
        if triggered:
            print("RESULT: Skill WOULD be triggered")
        else:
            print("RESULT: Skill would NOT be triggered")
            print("        (Insufficient keyword overlap)")

    # Level 2: Instructions
    print()
    print("-" * 60)
    print("LEVEL 2: INSTRUCTIONS (Loaded when triggered)")
    print("-" * 60)
    print()

    body_lines = body.split("\n")
    body_tokens = estimate_tokens(body)

    print(f"SKILL.md body: {len(body_lines)} lines, ~{body_tokens} tokens")
    print()

    # Show first 20 lines as preview
    preview_lines = body_lines[:20]
    print("Content preview (first 20 lines):")
    print("-" * 40)
    for line in preview_lines:
        print(f"  {line[:70]}{'...' if len(line) > 70 else ''}")
    if len(body_lines) > 20:
        print(f"  ... ({len(body_lines) - 20} more lines)")
    print("-" * 40)

    # Level 3: Resources
    print()
    print("-" * 60)
    print("LEVEL 3: RESOURCES (Loaded as needed)")
    print("-" * 60)
    print()

    file_refs = find_file_references(body)
    total_resource_tokens = 0

    if file_refs:
        print("Referenced files found in SKILL.md:")
        print()

        for ref in file_refs:
            ref_path = skill_path / ref

            if ref_path.exists():
                ref_content = ref_path.read_text()
                ref_lines = len(ref_content.split("\n"))
                ref_tokens = estimate_tokens(ref_content)
                total_resource_tokens += ref_tokens
                status = f"{ref_lines} lines, ~{ref_tokens} tokens"
            else:
                status = "FILE NOT FOUND"

            print(f"  {ref}: {status}")
    else:
        print("No file references found in SKILL.md body")

    # Scripts
    scripts_dir = skill_path / "scripts"
    if scripts_dir.exists():
        print()
        print("Scripts available (executed, not loaded into context):")
        for script in sorted(scripts_dir.iterdir()):
            if script.is_file():
                print(f"  {script.name}")

    # Summary
    print()
    print("-" * 60)
    print("EFFECTIVE CONTEXT SUMMARY")
    print("-" * 60)
    print()

    total_tokens = metadata_tokens + body_tokens

    print(f"Level 1 (Metadata):     ~{metadata_tokens:,} tokens (always loaded)")
    print(f"Level 2 (SKILL.md):     ~{body_tokens:,} tokens (on trigger)")
    print(f"Level 3 (References):   ~{total_resource_tokens:,} tokens (on demand)")
    print()
    print(f"Minimum context cost:   ~{metadata_tokens:,} tokens")
    print(f"Typical context cost:   ~{metadata_tokens + body_tokens:,} tokens")
    print(f"Maximum context cost:   ~{metadata_tokens + body_tokens + total_resource_tokens:,} tokens")

    # Recommendations
    print()
    print("-" * 60)
    print("RECOMMENDATIONS")
    print("-" * 60)
    print()

    issues = []

    if body_tokens > 5000:
        issues.append(
            f"SKILL.md body is large (~{body_tokens} tokens). "
            "Consider moving content to referenced files."
        )

    if len(body_lines) > 500:
        issues.append(
            f"SKILL.md has {len(body_lines)} lines. "
            "Recommended: under 500 lines."
        )

    if not file_refs and body_tokens > 3000:
        issues.append(
            "No file references but large SKILL.md. "
            "Consider progressive disclosure with referenced files."
        )

    missing_refs = [
        ref for ref in file_refs if not (skill_path / ref).exists()
    ]
    if missing_refs:
        issues.append(
            f"Missing referenced files: {', '.join(missing_refs)}"
        )

    if issues:
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("  No issues detected. Skill structure looks good.")

    print()


def main():
    parser = argparse.ArgumentParser(
        description="Simulate skill loading flow"
    )
    parser.add_argument("skill_path", help="Path to skill directory")
    parser.add_argument(
        "test_prompt",
        nargs="?",
        help="Optional prompt to test trigger matching",
    )
    args = parser.parse_args()

    skill_path = Path(args.skill_path)

    if not skill_path.is_dir():
        print(f"ERROR: {skill_path} is not a directory")
        sys.exit(1)

    dry_run(skill_path, args.test_prompt)


if __name__ == "__main__":
    main()
