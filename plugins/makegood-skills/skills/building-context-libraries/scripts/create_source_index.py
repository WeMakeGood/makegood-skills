#!/usr/bin/env python3
"""
Create initial source index for context library building.

This script generates the source-index.md file that the LLM MUST use.
It ensures ALL files are inventoried — the LLM cannot skip documents.

The script:
1. Finds all markdown/text files in the source directory
2. Classifies each by likely type (transcript, strategy, etc.)
3. Assesses signal clarity (clear vs buried)
4. Generates source-index.md with every file listed
5. The LLM must read and process every file in this index

Usage:
    python create_source_index.py <SOURCE_PATH> <OUTPUT_PATH>

Example:
    python create_source_index.py ./source ./context-library
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def estimate_tokens(text: str) -> int:
    """Estimate tokens (roughly 0.75 words per token for English)."""
    words = count_words(text)
    return int(words / 0.75)


def classify_document(filepath: Path, content: str) -> tuple[str, str]:
    """
    Classify document type and signal clarity.

    Returns: (type, signal)
    - type: strategy, operational, transcript, interview, notes, reference, financial, legal
    - signal: clear (knowledge stated directly), buried (meaning embedded in noise)
    """
    name_lower = filepath.name.lower()
    content_lower = content.lower()[:2000]  # Check first 2000 chars

    # Check for transcript indicators
    transcript_indicators = [
        'transcript', 'recording', 'meeting notes',
        '[speaker', 'speaker:', 'q:', 'a:',
        'um,', 'uh,', 'you know,', 'i mean,',
        '>> ', '>>> ',
    ]
    if any(ind in name_lower or ind in content_lower for ind in transcript_indicators):
        return ('transcript', 'buried')

    # Check for interview indicators
    interview_indicators = ['interview', 'q&a', 'conversation with', 'discussion with']
    if any(ind in name_lower or ind in content_lower for ind in interview_indicators):
        return ('interview', 'buried')

    # Check for financial documents
    financial_indicators = ['financ', 'budget', 'revenue', 'pricing', 'invoice', 'billing']
    if any(ind in name_lower for ind in financial_indicators):
        return ('financial', 'clear')

    # Check for legal documents
    legal_indicators = ['legal', 'contract', 'agreement', 'terms', 'compliance', 'bylaws']
    if any(ind in name_lower for ind in legal_indicators):
        return ('legal', 'clear')

    # Check for strategy documents
    strategy_indicators = [
        'strategy', 'strategic', 'vision', 'mission', 'positioning',
        'roadmap', 'plan', 'goals', 'objectives', 'reorganization'
    ]
    if any(ind in name_lower for ind in strategy_indicators):
        return ('strategy', 'clear')

    # Check for operational documents
    operational_indicators = [
        'process', 'procedure', 'workflow', 'handbook', 'guide',
        'policy', 'standard', 'protocol', 'sop'
    ]
    if any(ind in name_lower for ind in operational_indicators):
        return ('operational', 'clear')

    # Check for notes (signal depends on content)
    notes_indicators = ['notes', 'memo', 'minutes']
    if any(ind in name_lower for ind in notes_indicators):
        # Check if it looks conversational
        if 'said' in content_lower or 'mentioned' in content_lower:
            return ('notes', 'buried')
        return ('notes', 'clear')

    # Default to reference (clear signal)
    return ('reference', 'clear')


def extract_brief_description(content: str) -> str:
    """Extract a brief description from the document."""
    # Try to get first heading
    for line in content.split('\n')[:20]:
        if line.startswith('# '):
            return line[2:].strip()[:60]

    # Otherwise first non-empty line
    for line in content.split('\n')[:10]:
        stripped = line.strip()
        if stripped and not stripped.startswith('#') and not stripped.startswith('---'):
            return stripped[:60]

    return ""


def find_documents(source_dir: Path) -> list[Path]:
    """Find all markdown and text documents."""
    extensions = {'.md', '.txt', '.markdown'}
    documents = []

    for ext in extensions:
        documents.extend(source_dir.rglob(f'*{ext}'))

    # Filter out hidden files
    documents = [d for d in documents if not any(
        part.startswith('.') for part in d.parts
    )]

    return sorted(documents)


def generate_source_index(source_dir: Path, output_dir: Path) -> str:
    """Generate the source-index.md content."""
    documents = find_documents(source_dir)

    if not documents:
        return f"# Source Index\n\nNo documents found in {source_dir}\n"

    # Analyze each document
    file_entries = []
    total_tokens = 0
    buried_count = 0

    for doc in documents:
        try:
            with open(doc, 'r', encoding='utf-8') as f:
                content = f.read()

            rel_path = doc.relative_to(source_dir)
            doc_type, signal = classify_document(doc, content)
            tokens = estimate_tokens(content)
            description = extract_brief_description(content)

            total_tokens += tokens
            if signal == 'buried':
                buried_count += 1

            file_entries.append({
                'path': str(rel_path),
                'type': doc_type,
                'signal': signal,
                'tokens': tokens,
                'description': description
            })
        except Exception as e:
            file_entries.append({
                'path': str(doc.relative_to(source_dir)),
                'type': 'error',
                'signal': 'error',
                'tokens': 0,
                'description': f'Error: {e}'
            })

    # Generate markdown
    lines = [
        "# Source Index",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}",
        f"**Source path:** {source_dir}",
        f"**Output path:** {output_dir}",
        "**Status:** indexing",
        "",
        f"**Total files:** {len(file_entries)}",
        f"**Total tokens:** ~{total_tokens:,}",
        f"**Buried-signal sources:** {buried_count} (Comprehend extracts meaning directly)",
        "",
        "---",
        "",
        "## CRITICAL INSTRUCTIONS",
        "",
        "**These rules are embedded here so they survive context compaction.**",
        "",
        "### Rules for This Index",
        "- You MUST read and process EVERY file listed below. Do not skip files.",
        "- Update this index after reading EACH file. Do not batch updates.",
        "- NEVER invent details. Every fact must come from a source file you actually read.",
        "- NEVER fill gaps with plausible information. Gaps are gaps — report them.",
        "",
        "### Rules for Comprehension (Phase 2)",
        "- Buried-signal sources are handled in Comprehend — extract behavioral meaning directly.",
        "- Do NOT rewrite or clean up buried-signal sources. Understand what they reveal about how the organization operates.",
        "- Do NOT propose any module structure during Comprehend. Structure comes in Design (Phase 3).",
        "- If starting Phase 2, read `references/phases/PHASE_2_COMPREHEND.md` first.",
        "",
        "### Rules for Module Building (Phase 4)",
        "- Modules are METAPROMPTS that shape agent behavior — not fact sheets copied from sources.",
        "- Re-read working sources IN THE SAME TURN you write each module. NEVER write from memory.",
        "- Token budget is room for useful content, not a ceiling. Under-budget agents need more depth.",
        "- If starting Phase 4, read `references/phases/PHASE_4_BUILD.md` first.",
        "",
        "### Resuming a Build",
        "- If `build-state.md` exists in this directory, read it first — it tracks progress and points to the current phase instruction file.",
        "- If resuming without `build-state.md`, check the Status field above and the Reading Checklist below to determine where you left off.",
        "",
        "---",
        "",
        "## Source Files",
        "",
        "| # | File | Type | Signal | Tokens | Description |",
        "|---|------|------|--------|--------|-------------|",
    ]

    for i, entry in enumerate(file_entries, 1):
        lines.append(
            f"| {i} | {entry['path']} | {entry['type']} | {entry['signal']} | "
            f"~{entry['tokens']:,} | {entry['description']} |"
        )

    lines.extend([
        "",
        "### Type Values",
        "- `strategy` — Positioning, decisions, strategic direction",
        "- `operational` — Processes, structures, procedures",
        "- `transcript` — Conversational speech",
        "- `interview` — Q&A format",
        "- `notes` — Meeting notes, informal",
        "- `reference` — Supporting material",
        "- `financial` — Financial data, pricing",
        "- `legal` — Legal documents, agreements",
        "",
        "### Signal Values",
        "- `clear` — Organizational knowledge stated directly; use as reference during module writing",
        "- `buried` — Meaning embedded in conversational artifacts, filler, or unstructured notes; Comprehend extracts the patterns directly",
        "",
        "---",
        "",
        "## HOW TO USE THIS INDEX",
        "",
        "This index is your working checklist. Follow these steps:",
        "",
        "1. **Read files in order** — process each file listed in the checklist below",
        "2. **Update the checklist** — after reading each file, mark it [x] and add notes",
        "3. **Add conflicts/gaps** — record issues in the sections below as you find them",
        "4. **Do not skip files** — every file must be read and marked",
        "5. **Do not proceed** to Comprehend until all files are read and user approves",
        "",
        "---",
        "",
        "## Reading Checklist",
        "",
        "**Mark each file [x] as you read it. Add notes about what you found.**",
        "",
    ])

    for i, entry in enumerate(file_entries, 1):
        lines.append(f"- [ ] {i}. `{entry['path']}` — *notes: [add after reading]*")

    lines.extend([
        "",
        "---",
        "",
        "## Conflicts Identified",
        "",
        "**Add conflicts here as you discover them:**",
        "",
        "*Example: Document A says X, but Document B says Y — need to resolve*",
        "",
        "- *(none yet)*",
        "",
        "---",
        "",
        "## Gaps Identified",
        "",
        "**Add missing information here as you discover it:**",
        "",
        "*Example: No information found about pricing structure*",
        "",
        "- *(none yet)*",
        "",
        "---",
        "",
        "## Initial Agent Needs Assessment",
        "",
        "[Populated during Setup — what agents need to do, initial role identification]",
        "",
        "---",
        "",
        "## Next Steps",
        "",
        "When ALL files above are marked [x]:",
        "",
        "1. Review the Conflicts and Gaps sections you filled in",
        "2. Update the Status field at the top to `comprehending`",
        "3. Present this completed index to the user for approval",
        "4. **Do NOT proceed to Comprehend until user approves this index**",
        ""
    ])

    return '\n'.join(lines)


def main():
    if len(sys.argv) < 3:
        print("Usage: python create_source_index.py <SOURCE_PATH> <OUTPUT_PATH>")
        print("Example: python create_source_index.py ./source ./context-library")
        sys.exit(1)

    source_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    if not source_dir.exists():
        print(f"Error: Source directory '{source_dir}' not found")
        sys.exit(1)

    # Create output directory if needed
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate and write index
    index_content = generate_source_index(source_dir, output_dir)
    index_path = output_dir / 'source-index.md'

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"Source index created: {index_path}")
    print(f"")
    print(f"Next steps:")
    print(f"1. Review the source index")
    print(f"2. Run the context library skill")
    print(f"3. The LLM will read ALL files listed in the index")


if __name__ == '__main__':
    main()
