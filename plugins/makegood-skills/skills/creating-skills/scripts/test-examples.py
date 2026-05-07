#!/usr/bin/env python3
"""
Test that skill examples are concrete, not abstract.

Usage:
    python test-examples.py <skill-path>

Tests:
- Examples section exists
- Examples contain concrete input/output pairs
- No placeholder patterns like [your data here]
- No abstract patterns like "input: ..." without actual values
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple


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


def find_example_sections(content: str) -> List[Tuple[str, str]]:
    """Find all example sections in the content."""
    sections = []

    # Pattern for markdown headers containing "example"
    header_pattern = re.compile(
        r"^(#{1,4})\s+.*example.*$", re.IGNORECASE | re.MULTILINE
    )

    matches = list(header_pattern.finditer(content))

    for i, match in enumerate(matches):
        header_level = len(match.group(1))
        start = match.end()

        # Find next header of same or higher level
        end = len(content)
        for next_match in matches[i + 1 :]:
            next_level = len(next_match.group(1))
            if next_level <= header_level:
                end = next_match.start()
                break

        # Also check for any header of same or higher level
        remaining = content[start:]
        next_header = re.search(
            rf"^#{{{1},{header_level}}}\s+", remaining, re.MULTILINE
        )
        if next_header:
            end = min(end, start + next_header.start())

        section_content = content[start:end].strip()
        sections.append((match.group(0).strip(), section_content))

    return sections


def check_placeholder_patterns(content: str, result: TestResult) -> int:
    """Check for placeholder patterns that indicate abstract examples."""
    placeholder_patterns = [
        (r"\[your [^\]]+\]", "[your ... ]"),
        (r"\[insert [^\]]+\]", "[insert ... ]"),
        (r"\[add [^\]]+\]", "[add ... ]"),
        (r"\[replace [^\]]+\]", "[replace ... ]"),
        (r"\[fill in [^\]]+\]", "[fill in ... ]"),
        (r"\[example [^\]]+\]", "[example ... ]"),
        (r"\[placeholder[^\]]*\]", "[placeholder]"),
        (r"\[TODO[^\]]*\]", "[TODO]"),
        (r"\[TBD[^\]]*\]", "[TBD]"),
        (r"<your[^>]+>", "<your ... >"),
        (r"<insert[^>]+>", "<insert ... >"),
        (r"\.\.\.your\.\.\.", "...your..."),
        (r"input:\s*\.\.\.", "input: ..."),
        (r"output:\s*\.\.\.", "output: ..."),
    ]

    found_count = 0
    for pattern, label in placeholder_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            found_count += len(matches)
            result.error(
                f"Found placeholder pattern '{label}' ({len(matches)} occurrence(s)). "
                "Examples should use concrete values."
            )

    return found_count


def check_code_blocks(content: str, result: TestResult) -> tuple[int, int]:
    """Check code blocks for concrete vs abstract examples."""
    code_block_pattern = re.compile(r"```[\w]*\n(.*?)```", re.DOTALL)
    blocks = code_block_pattern.findall(content)

    concrete_count = 0
    abstract_count = 0

    for block in blocks:
        # Check for actual values (strings, numbers, etc.)
        has_string_literal = bool(re.search(r'["\'][^"\']+["\']', block))
        has_number = bool(re.search(r"\b\d+\b", block))
        has_variable_assignment = bool(re.search(r"\w+\s*=\s*\S", block))

        # Check for placeholder indicators
        has_placeholder = bool(
            re.search(r"(\[.*\]|<.*>|\.\.\.|\#\s*TODO)", block, re.IGNORECASE)
        )

        if has_placeholder and not (has_string_literal or has_number):
            abstract_count += 1
        elif has_string_literal or has_number or has_variable_assignment:
            concrete_count += 1

    return concrete_count, abstract_count


def check_input_output_pairs(content: str, result: TestResult):
    """Check for input/output example patterns."""
    # Look for input/output patterns
    io_patterns = [
        r"input:.*\noutput:",
        r"Input:.*\nOutput:",
        r"Before:.*\nAfter:",
        r"Given:.*\nResult:",
        r"Example \d+:",
    ]

    has_io_pattern = any(
        re.search(p, content, re.IGNORECASE | re.DOTALL) for p in io_patterns
    )

    # Also check for code blocks with comments showing output
    has_output_comment = bool(
        re.search(r"#\s*(output|result|returns):", content, re.IGNORECASE)
    )

    if has_io_pattern or has_output_comment:
        result.success("Examples include input/output patterns")
    else:
        result.warning(
            "Examples should show input/output pairs or before/after comparisons"
        )


def test_examples(skill_path: Path) -> TestResult:
    """Test examples in a skill."""
    result = TestResult()
    skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        result.error(f"SKILL.md not found in {skill_path}")
        return result

    content = skill_md.read_text()

    # Also check EXAMPLES.md if it exists
    examples_md = skill_path / "EXAMPLES.md"
    if examples_md.exists():
        content += "\n\n" + examples_md.read_text()
        result.info("Also checking EXAMPLES.md")

    # Find example sections
    sections = find_example_sections(content)

    if not sections:
        # Check if there are code blocks even without explicit "Examples" header
        if "```" in content:
            result.warning(
                "No explicit 'Examples' section found, but code blocks exist. "
                "Consider adding an Examples section for clarity."
            )
        else:
            result.error(
                "No examples found. Skills should include concrete examples."
            )
        return result

    result.success(f"Found {len(sections)} example section(s)")

    # Check all example content
    all_example_content = "\n".join(section[1] for section in sections)

    # Check for placeholders
    placeholder_count = check_placeholder_patterns(all_example_content, result)

    # Check code blocks
    concrete, abstract = check_code_blocks(all_example_content, result)

    if concrete > 0:
        result.success(f"Found {concrete} code block(s) with concrete values")

    if abstract > 0:
        result.warning(
            f"Found {abstract} code block(s) that may be abstract. "
            "Ensure examples use real values, not placeholders."
        )

    # Check input/output patterns
    check_input_output_pairs(all_example_content, result)

    # Overall assessment
    if placeholder_count == 0 and concrete > abstract:
        result.success("Examples appear to be concrete")
    elif placeholder_count > 0:
        pass  # Already logged as error
    elif abstract > concrete:
        result.warning("Examples may be too abstract. Add concrete input/output pairs.")

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Test that skill examples are concrete"
    )
    parser.add_argument("skill_path", help="Path to skill directory")
    args = parser.parse_args()

    skill_path = Path(args.skill_path)

    if not skill_path.is_dir():
        print(f"ERROR: {skill_path} is not a directory")
        sys.exit(1)

    print()
    print("=" * 50)
    print(f"Testing Examples: {skill_path.name}")
    print("=" * 50)
    print()

    result = test_examples(skill_path)

    print()
    print("=" * 50)
    if result.errors:
        print(f"FAILED: {len(result.errors)} error(s), {len(result.warnings)} warning(s)")
        sys.exit(1)
    elif result.warnings:
        print(f"PASSED with warnings: {len(result.warnings)} warning(s)")
        sys.exit(0)
    else:
        print("PASSED: All example tests passed")
        sys.exit(0)


if __name__ == "__main__":
    main()
