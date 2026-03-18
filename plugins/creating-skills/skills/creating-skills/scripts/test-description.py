#!/usr/bin/env python3
"""
Test skill description quality and discoverability.

Usage:
    python test-description.py <skill-path>
    python test-description.py <skill-path> "test phrase 1" "test phrase 2"

Tests:
- Third-person voice (no I/you/we language)
- Specificity (not vague/generic)
- Trigger conditions present
- Keyword matching against test phrases
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Optional


class TestResult:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, msg: str):
        self.errors.append(msg)
        print(f"ERROR: {msg}")

    def warning(self, msg: str):
        self.warnings.append(msg)
        print(f"WARNING: {msg}")

    def success(self, msg: str):
        print(f"OK: {msg}")

    def info(self, msg: str):
        print(f"INFO: {msg}")

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0


def extract_description(skill_path: Path) -> Optional[str]:
    """Extract description from SKILL.md frontmatter."""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return None

    content = skill_md.read_text()
    if not content.startswith("---"):
        return None

    lines = content.split("\n")
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("description:"):
            return line.split(":", 1)[1].strip().strip("\"'")

    return None


def check_voice(description: str, result: TestResult):
    """Check for first/second person voice."""
    bad_patterns = [
        (r"\bI can\b", "I can"),
        (r"\bI will\b", "I will"),
        (r"\bI am\b", "I am"),
        (r"\bI['']m\b", "I'm"),
        (r"\byou can\b", "you can"),
        (r"\byou will\b", "you will"),
        (r"\byou are\b", "you are"),
        (r"\byou['']re\b", "you're"),
        (r"\bwe can\b", "we can"),
        (r"\bwe will\b", "we will"),
        (r"\byour\b", "your"),
        (r"\bmy\b", "my"),
    ]

    found_issues = False
    for pattern, label in bad_patterns:
        if re.search(pattern, description, re.IGNORECASE):
            result.error(f"Description uses non-third-person voice: found '{label}'")
            found_issues = True

    if not found_issues:
        result.success("Third-person voice: OK")


def check_specificity(description: str, result: TestResult):
    """Check for vague/generic language."""
    vague_patterns = [
        (r"^Helps with\b", "Helps with..."),
        (r"^Does stuff\b", "Does stuff..."),
        (r"^Handles\b", "Handles..."),
        (r"^Works with\b", "Works with..."),
        (r"^A tool for\b", "A tool for..."),
        (r"^A skill for\b", "A skill for..."),
        (r"\bvarious\b", "various"),
        (r"\bmultiple things\b", "multiple things"),
        (r"\band more\b", "and more"),
        (r"\betc\.\b", "etc."),
    ]

    for pattern, label in vague_patterns:
        if re.search(pattern, description, re.IGNORECASE):
            result.warning(f"Description may be too vague: matches '{label}'")

    # Word count
    words = description.split()
    word_count = len(words)

    if word_count < 10:
        result.warning(
            f"Description is very short ({word_count} words). "
            "Consider adding more detail about WHEN to use this skill."
        )
    else:
        result.success(f"Description length: {word_count} words")

    # Trigger conditions
    trigger_patterns = [
        r"\buse when\b",
        r"\buse for\b",
        r"\buse if\b",
        r"\bwhen .+ mentions?\b",
        r"\bwhen working with\b",
        r"\bwhen .+ asks?\b",
    ]

    has_trigger = any(
        re.search(p, description, re.IGNORECASE) for p in trigger_patterns
    )

    if has_trigger:
        result.success("Description includes trigger conditions")
    else:
        result.warning(
            "Description should include trigger conditions "
            "(e.g., 'Use when...', 'Use for...')"
        )


def test_keyword_matching(
    description: str, test_phrases: List[str], result: TestResult
):
    """Test if description keywords match test phrases."""
    if not test_phrases:
        result.info("No test phrases provided. Skipping trigger matching test.")
        return

    print()
    print(f"Testing trigger matching against {len(test_phrases)} phrase(s):")

    # Common words to ignore
    stop_words = {
        "a", "an", "the", "and", "or", "for", "to", "in", "on", "at", "by",
        "with", "from", "of", "is", "are", "was", "were", "be", "been",
        "being", "have", "has", "had", "do", "does", "did", "will", "would",
        "could", "should", "may", "might", "must", "shall", "can", "this",
        "that", "these", "those", "it", "its", "when", "use", "using", "i",
        "me", "my", "please", "help", "want", "need",
    }

    # Extract keywords from description
    desc_words = set(
        word.lower()
        for word in re.findall(r"\b[a-zA-Z]+\b", description)
        if word.lower() not in stop_words and len(word) > 2
    )

    for phrase in test_phrases:
        phrase_words = set(
            word.lower()
            for word in re.findall(r"\b[a-zA-Z]+\b", phrase)
            if word.lower() not in stop_words and len(word) > 2
        )

        matches = desc_words & phrase_words
        match_count = len(matches)
        total_words = len(phrase_words) if phrase_words else 1

        if match_count > 0:
            match_pct = (match_count * 100) // total_words
            matched_str = ", ".join(sorted(matches))

            if match_pct >= 30:
                result.success(
                    f'Phrase "{phrase}" -> {match_count} keyword matches '
                    f"({match_pct}%): {matched_str}"
                )
            else:
                result.warning(
                    f'Phrase "{phrase}" -> weak match: {match_count} keywords '
                    f"({match_pct}%): {matched_str}"
                )
        else:
            result.error(
                f'Phrase "{phrase}" -> NO keyword matches. '
                "Description may not trigger for this use case."
            )


def main():
    parser = argparse.ArgumentParser(
        description="Test skill description quality and discoverability"
    )
    parser.add_argument("skill_path", help="Path to skill directory")
    parser.add_argument(
        "test_phrases",
        nargs="*",
        help="Optional phrases to test trigger matching",
    )
    args = parser.parse_args()

    skill_path = Path(args.skill_path)

    if not skill_path.is_dir():
        print(f"ERROR: {skill_path} is not a directory")
        sys.exit(1)

    print()
    print("=" * 50)
    print(f"Testing Description: {skill_path.name}")
    print("=" * 50)

    description = extract_description(skill_path)

    if not description:
        print("ERROR: Could not extract description from frontmatter")
        sys.exit(1)

    print()
    print("Description:")
    print(f'  "{description}"')
    print()

    result = TestResult()

    check_voice(description, result)
    check_specificity(description, result)
    test_keyword_matching(description, args.test_phrases, result)

    print()
    print("=" * 50)
    if result.errors:
        print(f"FAILED: {len(result.errors)} error(s), {len(result.warnings)} warning(s)")
        sys.exit(1)
    elif result.warnings:
        print(f"PASSED with warnings: {len(result.warnings)} warning(s)")
        sys.exit(0)
    else:
        print("PASSED: All description tests passed")
        sys.exit(0)


if __name__ == "__main__":
    main()
