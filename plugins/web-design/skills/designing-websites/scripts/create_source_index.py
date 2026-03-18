#!/usr/bin/env python3
"""
Create or update the source index for website design projects.

Scans one or more source directories (including context libraries) and
generates or updates source-index.md. Safe to re-run — new files are
appended with the next available ID. Existing entries are preserved.

The script:
1. Finds all markdown/text files across all provided paths
2. Discovers context library structure (agent definitions, modules, addenda)
   by parsing YAML frontmatter
3. Classifies each file by type and signal clarity
4. Creates source-index.md on first run, or merges new files on subsequent runs

Usage:
    python create_source_index.py <OUTPUT_PATH> <PATH> [PATH] [PATH] ...

Examples:
    python create_source_index.py ./tmp/project ./source
    python create_source_index.py ./tmp/project ./source ./context-library
    python create_source_index.py ./tmp/project ./planning ./context-lib ./extra-docs
"""

import os
import sys
import re
import yaml
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Tuple, Set


def count_words(text: str) -> int:
    return len(text.split())


def estimate_tokens(text: str) -> int:
    return int(count_words(text) / 0.75)


def extract_frontmatter(content: str) -> Optional[Dict]:
    """Extract YAML frontmatter from a markdown file."""
    if not content.startswith('---'):
        return None
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1])
    except (yaml.YAMLError, Exception):
        return None


def is_context_library(directory: Path) -> bool:
    """Check if a directory looks like a context library (has agents/ or modules/)."""
    return (directory / 'agents').exists() or (directory / 'modules').exists()


def classify_context_library_file(filepath: Path, content: str, frontmatter: Optional[Dict]) -> Tuple[str, str]:
    """Classify a file from a context library."""
    name_lower = filepath.name.lower()
    rel_parts = filepath.parts

    if 'agents' in rel_parts:
        return ('agent-definition', 'clear')
    if 'addenda' in rel_parts:
        return ('addendum', 'clear')
    if frontmatter and 'module_id' in frontmatter:
        module_id = str(frontmatter['module_id']).lower()
        if module_id.startswith('s0') or 'prose' in name_lower or 'voice' in name_lower:
            return ('voice-profile', 'clear')
        return ('context-module', 'clear')
    if 'modules' in rel_parts:
        if 's0' in name_lower or 'prose_standards' in name_lower or 'natural_prose' in name_lower:
            return ('voice-profile', 'clear')
        return ('context-module', 'clear')
    if 'voice' in name_lower or 'prose' in name_lower:
        return ('voice-profile', 'clear')
    if 'writing' in name_lower and 'standard' in name_lower:
        return ('writing-standards', 'clear')
    return ('context-module', 'clear')


def classify_source_file(filepath: Path, content: str) -> Tuple[str, str]:
    """Classify a source document."""
    name_lower = filepath.name.lower()
    content_lower = content.lower()[:2000]

    synthesis_indicators = ['synthesis', 'interview-synthesis', 'key quotes', 'speaker information']
    if any(ind in name_lower for ind in synthesis_indicators):
        return ('interview-synthesis', 'clear')

    transcript_indicators = [
        'transcript', 'recording', '[speaker', 'speaker:', 'q:', 'a:',
        'um,', 'uh,', 'you know,', '>> ',
    ]
    if any(ind in name_lower or ind in content_lower for ind in transcript_indicators):
        return ('transcript', 'buried')

    brand_indicators = ['brand', 'style guide', 'visual identity', 'logo', 'color']
    if any(ind in name_lower for ind in brand_indicators):
        return ('brand-guide', 'clear')

    copy_indicators = ['website', 'copy', 'page content', 'existing-site', 'current-site']
    if any(ind in name_lower for ind in copy_indicators):
        return ('existing-copy', 'clear')

    org_indicators = [
        'strategy', 'mission', 'vision', 'annual report', 'program',
        'about', 'overview', 'plan', 'goals', 'dossier'
    ]
    if any(ind in name_lower for ind in org_indicators):
        return ('org-doc', 'clear')

    return ('reference', 'clear')


def extract_brief_description(content: str) -> str:
    """Extract a brief description from the document."""
    for line in content.split('\n')[:20]:
        if line.startswith('# '):
            return line[2:].strip()[:80]
    for line in content.split('\n')[:10]:
        stripped = line.strip()
        if stripped and not stripped.startswith('#') and not stripped.startswith('---'):
            return stripped[:80]
    return ""


def find_documents(directory: Path) -> List[Path]:
    """Find all markdown and text documents, excluding hidden files."""
    extensions = {'.md', '.txt', '.markdown'}
    documents = []
    for ext in extensions:
        documents.extend(directory.rglob(f'*{ext}'))
    documents = [d for d in documents if not any(
        part.startswith('.') for part in d.parts
    )]
    return sorted(documents)


def discover_context_library(lib_path: Path) -> Dict:
    """Discover context library structure by reading agent definition frontmatter."""
    result = {
        'agent_definitions': [],
        'modules': [],
        'addenda': [],
        'voice_profile': None,
        'writing_standards': None,
    }

    agents_dir = lib_path / 'agents'
    if agents_dir.exists():
        for f in sorted(agents_dir.glob('*.md')):
            try:
                content = f.read_text(encoding='utf-8')
                fm = extract_frontmatter(content)
                if fm:
                    result['agent_definitions'].append({
                        'path': str(f),
                        'name': fm.get('agent_name', f.stem),
                        'domain': fm.get('agent_domain', 'unknown'),
                        'modules': fm.get('modules', {}),
                        'addenda': fm.get('addenda', []),
                    })
            except Exception:
                pass

    modules_dir = lib_path / 'modules'
    if modules_dir.exists():
        for tier_dir in ['foundation', 'shared', 'specialized']:
            tier_path = modules_dir / tier_dir
            if tier_path.exists():
                for f in sorted(tier_path.glob('*.md')):
                    try:
                        content = f.read_text(encoding='utf-8')
                        fm = extract_frontmatter(content)
                        result['modules'].append({
                            'path': str(f),
                            'id': fm.get('module_id', f.stem) if fm else f.stem,
                            'tier': tier_dir,
                            'purpose': fm.get('purpose', '') if fm else '',
                        })
                        name_lower = f.name.lower()
                        if 's0' in name_lower or 'natural_prose' in name_lower or 'prose_standards' in name_lower:
                            result['voice_profile'] = str(f)
                        if 'writing_standards' in name_lower and result['writing_standards'] is None:
                            result['writing_standards'] = str(f)
                    except Exception:
                        pass

    addenda_dir = lib_path / 'addenda'
    if addenda_dir.exists():
        for f in sorted(addenda_dir.glob('*.md')):
            try:
                content = f.read_text(encoding='utf-8')
                fm = extract_frontmatter(content)
                result['addenda'].append({
                    'path': str(f),
                    'id': fm.get('addendum_id', f.stem) if fm else f.stem,
                    'name': fm.get('addendum_name', f.stem) if fm else f.stem,
                })
            except Exception:
                pass

    return result


def parse_existing_index(index_path: Path) -> Tuple[Set[str], int]:
    """
    Parse an existing source-index.md to find already-indexed file paths
    and the highest ID used.

    Returns: (set of file paths already indexed, highest ID number)
    """
    existing_paths = set()
    max_id = 0

    try:
        content = index_path.read_text(encoding='utf-8')
    except Exception:
        return existing_paths, max_id

    # Parse the Source Files table for existing paths
    in_table = False
    for line in content.split('\n'):
        if '| # | File |' in line:
            in_table = True
            continue
        if in_table and line.startswith('|'):
            if '---|' in line:
                continue
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 3:
                try:
                    file_id = int(parts[1])
                    file_path = parts[2]
                    existing_paths.add(file_path)
                    max_id = max(max_id, file_id)
                except (ValueError, IndexError):
                    pass
        elif in_table and not line.startswith('|'):
            in_table = False

    # Also parse reading checklist for paths
    for line in content.split('\n'):
        match = re.match(r'- \[[ x]\] (\d+)\. `([^`]+)`', line)
        if match:
            existing_paths.add(match.group(2))
            max_id = max(max_id, int(match.group(1)))

    return existing_paths, max_id


def generate_new_entries(source_dirs: List[Path], existing_paths: Set[str], start_id: int) -> List[Dict]:
    """
    Scan directories and return entries for files not already in the index.

    Returns: list of file entry dicts for Source Files table and Reading Checklist.
    """
    file_entries = []
    current_id = start_id

    for directory in source_dirs:
        if not directory.exists():
            continue

        is_ctx_lib = is_context_library(directory)
        docs = find_documents(directory)

        for doc in docs:
            path_str = str(doc)
            if path_str in existing_paths:
                continue

            try:
                content = doc.read_text(encoding='utf-8')
                fm = extract_frontmatter(content)

                if is_ctx_lib:
                    doc_type, signal = classify_context_library_file(doc, content, fm)
                else:
                    doc_type, signal = classify_source_file(doc, content)

                tokens = estimate_tokens(content)
                current_id += 1

                file_entries.append({
                    'id': current_id,
                    'path': path_str,
                    'type': doc_type,
                    'signal': signal,
                    'tokens': tokens,
                    'description': extract_brief_description(content),
                })
            except Exception as e:
                current_id += 1
                file_entries.append({
                    'id': current_id,
                    'path': path_str,
                    'type': 'error',
                    'signal': 'error',
                    'tokens': 0,
                    'description': f'Error: {e}',
                })

    return file_entries


def generate_full_index(source_dirs: List[Path], output_dir: Path) -> str:
    """Generate a complete source-index.md from scratch."""

    # Discover context libraries
    lib_infos = []
    for d in source_dirs:
        if is_context_library(d):
            lib_infos.append((d, discover_context_library(d)))

    # Collect all files
    all_entries = []
    current_id = 0

    for directory in source_dirs:
        if not directory.exists():
            continue
        is_ctx_lib = is_context_library(directory)
        docs = find_documents(directory)
        for doc in docs:
            try:
                content = doc.read_text(encoding='utf-8')
                fm = extract_frontmatter(content)
                if is_ctx_lib:
                    doc_type, signal = classify_context_library_file(doc, content, fm)
                else:
                    doc_type, signal = classify_source_file(doc, content)
                tokens = estimate_tokens(content)
                current_id += 1
                all_entries.append({
                    'id': current_id,
                    'path': str(doc),
                    'type': doc_type,
                    'signal': signal,
                    'tokens': tokens,
                    'description': extract_brief_description(content),
                })
            except Exception as e:
                current_id += 1
                all_entries.append({
                    'id': current_id,
                    'path': str(doc),
                    'type': 'error',
                    'signal': 'error',
                    'tokens': 0,
                    'description': f'Error: {e}',
                })

    total_tokens = sum(e['tokens'] for e in all_entries)

    # Build markdown
    lines = [
        "# Source Index",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}",
        f"**Source paths:** {', '.join(str(d) for d in source_dirs)}",
        f"**Output path:** {output_dir}",
        "**Status:** indexing",
        "",
        f"**Total files:** {len(all_entries)}",
        f"**Total tokens:** ~{total_tokens:,}",
        "",
    ]

    # Context library summaries
    for lib_path, lib_info in lib_infos:
        lines.extend([
            "---",
            "",
            f"## Context Library: {lib_path}",
            "",
        ])
        if lib_info['agent_definitions']:
            for ad in lib_info['agent_definitions']:
                lines.append(f"**Agent definition:** `{ad['path']}`")
                lines.append(f"**Agent name:** {ad['name']}")
                lines.append(f"**Agent domain:** {ad['domain']}")
                lines.append("")
                if ad['modules']:
                    lines.append("**Modules (from frontmatter):**")
                    lines.append("")
                    lines.append("| Tier | Module IDs |")
                    lines.append("|------|-----------|")
                    for tier, module_list in ad['modules'].items():
                        if module_list:
                            lines.append(f"| {tier} | {', '.join(module_list)} |")
                    lines.append("")
                if ad['addenda']:
                    lines.append("**Addenda (from frontmatter):**")
                    for addendum in ad['addenda']:
                        if isinstance(addendum, dict):
                            lines.append(f"- {addendum.get('addendum_name', addendum)}")
                        else:
                            lines.append(f"- {addendum}")
                    lines.append("")
        else:
            lines.append("No agent definitions found.")
            lines.append("")

        if lib_info['voice_profile']:
            lines.append(f"**Voice profile:** `{lib_info['voice_profile']}`")
        if lib_info['writing_standards']:
            lines.append(f"**Writing standards:** `{lib_info['writing_standards']}`")
        if lib_info['voice_profile'] or lib_info['writing_standards']:
            lines.append("")

        lines.append(f"**Modules found:** {len(lib_info['modules'])}")
        lines.append(f"**Addenda found:** {len(lib_info['addenda'])}")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## PROCESS GATES FOR THIS INDEX",
        "",
        "**These rules are embedded here so they survive context compaction.**",
        "",
        "### Reading Rules",
        "- Read EVERY file listed below. Follow the Read-Then-Index gate: read one file, update the checklist, read the next.",
        "- After reading all files, identify what the sources DO and DON'T answer about website requirements.",
        "- Only ask the user about gaps the sources don't cover — typically CTAs (project-specific decisions) and technical stack.",
        "",
        "### Comprehension Rules (Phase 2)",
        "- Extract organizational REASONING, not facts. How the org thinks, not what it contains.",
        "- After comprehension, update this index with Website Content Mappings — what each source contributes to the website, by ID.",
        "- Buried-signal sources are handled in Comprehend — extract meaning directly.",
        "- Do NOT propose strategy, CTAs, or sitemap structure during Comprehend.",
        "",
        "### Sitemap Rules (Phase 4)",
        "- Every page in the sitemap must reference source IDs from this index.",
        "- The sitemap is the construction plan — it tells Phase 5/6 which files to re-read for each page.",
        "",
        "### Content Rules (Phase 6)",
        "- Before writing each page, re-read the source files listed in that page's sitemap entry.",
        "- Voice profile and writing standards must be the LAST documents loaded before content generation.",
        "- Re-read context modules every 3-4 pages during generation — they compact silently.",
        "",
        "---",
        "",
        "## Source Files",
        "",
        "| # | File | Type | Signal | Tokens | Description |",
        "|---|------|------|--------|--------|-------------|",
    ])

    for entry in all_entries:
        lines.append(
            f"| {entry['id']} | {entry['path']} | {entry['type']} | {entry['signal']} | "
            f"~{entry['tokens']:,} | {entry['description']} |"
        )

    lines.extend([
        "",
        "### Type Values",
        "- `agent-definition` — System prompt preamble defining an agent's role and modules",
        "- `context-module` — Metaprompt module containing organizational reasoning",
        "- `voice-profile` — Voice/prose standards (may be S0_natural_prose_standards)",
        "- `writing-standards` — Writing standards (if separate from voice profile)",
        "- `addendum` — Volatile reference data (prices, bios, catalogs)",
        "- `brand-guide` — Brand identity, visual standards, tone guidance",
        "- `existing-copy` — Current website content",
        "- `org-doc` — Organizational strategy, programs, reports",
        "- `interview-synthesis` — Synthesized interview findings",
        "- `transcript` — Raw conversational content",
        "- `reference` — Other supporting material",
        "",
        "### Signal Values",
        "- `clear` — Knowledge stated directly; read and index as-is",
        "- `buried` — Meaning embedded in conversational artifacts; Comprehend extracts reasoning directly",
        "",
        "---",
        "",
        "## Reading Checklist",
        "",
        "**Read each file, mark [x], add notes about what you found.**",
        "",
    ])

    for entry in all_entries:
        lines.append(f"- [ ] {entry['id']}. `{entry['path']}` ({entry['type']}) — *notes: [add after reading]*")

    lines.extend([
        "",
        "---",
        "",
        "## Website Content Mappings (Phase 2)",
        "",
        "**After comprehension, map each source to what it contributes to the website.**",
        "",
        "| ID | Source File | Website Contribution | Key Material | Comprehension Finding |",
        "|----|-------------|---------------------|-------------|----------------------|",
        "| | *(populated during Phase 2)* | | | |",
        "",
        "---",
        "",
        "## Gaps Identified",
        "",
        "**What the sources DON'T answer about website requirements:**",
        "",
        "- *(populated after reading all files)*",
        "",
        "---",
        "",
        "## Conflicts Identified",
        "",
        "- *(none yet)*",
        "",
    ])

    return '\n'.join(lines)


def append_to_index(index_path: Path, new_entries: List[Dict]) -> None:
    """Append new file entries to an existing source-index.md."""
    content = index_path.read_text(encoding='utf-8')

    # Find the end of the Source Files table and append new rows
    table_rows = []
    checklist_rows = []
    for entry in new_entries:
        table_rows.append(
            f"| {entry['id']} | {entry['path']} | {entry['type']} | {entry['signal']} | "
            f"~{entry['tokens']:,} | {entry['description']} |"
        )
        checklist_rows.append(
            f"- [ ] {entry['id']}. `{entry['path']}` ({entry['type']}) — *notes: [add after reading]*"
        )

    # Insert table rows before "### Type Values"
    if '### Type Values' in content:
        content = content.replace(
            '### Type Values',
            '\n'.join(table_rows) + '\n\n### Type Values'
        )

    # Insert checklist rows before "## Website Content Mappings" or "## Gaps Identified"
    insert_before = '## Website Content Mappings'
    if insert_before not in content:
        insert_before = '## Gaps Identified'

    if insert_before in content:
        content = content.replace(
            insert_before,
            '\n'.join(checklist_rows) + '\n\n---\n\n' + insert_before
        )

    # Update total files and tokens counts
    total_new_tokens = sum(e['tokens'] for e in new_entries)
    # Update the "Total files" line
    content = re.sub(
        r'\*\*Total files:\*\* \d+',
        lambda m: f"**Total files:** {int(m.group().split()[-1]) + len(new_entries)}",
        content
    )

    # Update status note
    timestamp = datetime.now().strftime('%Y-%m-%d')
    update_note = f"\n**Updated:** {timestamp} — added {len(new_entries)} new files\n"
    content = content.replace('**Status:** indexing', f'**Status:** indexing{update_note}', 1)
    content = content.replace('**Status:** comprehending', f'**Status:** comprehending{update_note}', 1)
    content = content.replace('**Status:** building', f'**Status:** building{update_note}', 1)

    index_path.write_text(content, encoding='utf-8')


def main():
    if len(sys.argv) < 3:
        print("Usage: python create_source_index.py <OUTPUT_PATH> <PATH> [PATH] [PATH] ...")
        print()
        print("Scans one or more source directories and creates/updates source-index.md.")
        print("Safe to re-run — new files are appended, existing entries preserved.")
        print()
        print("Examples:")
        print("  python create_source_index.py ./tmp/project ./source")
        print("  python create_source_index.py ./tmp/project ./source ./context-library")
        print("  python create_source_index.py ./tmp/project ./planning ./context-lib ./extra-docs")
        print()
        print("Context libraries are auto-detected (directories with agents/ or modules/).")
        sys.exit(1)

    output_dir = Path(sys.argv[1])
    source_dirs = [Path(p) for p in sys.argv[2:]]

    # Validate paths
    for d in source_dirs:
        if not d.exists():
            print(f"Warning: Path '{d}' not found — skipping")
    source_dirs = [d for d in source_dirs if d.exists()]

    if not source_dirs:
        print("Error: No valid source paths provided")
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)
    index_path = output_dir / 'source-index.md'

    if index_path.exists():
        # Merge mode — find new files and append
        existing_paths, max_id = parse_existing_index(index_path)
        new_entries = generate_new_entries(source_dirs, existing_paths, max_id)

        if not new_entries:
            print(f"No new files found. Source index is up to date ({len(existing_paths)} files).")
            sys.exit(0)

        append_to_index(index_path, new_entries)

        print(f"Source index updated: {index_path}")
        print(f"  Added {len(new_entries)} new files (IDs #{new_entries[0]['id']}-#{new_entries[-1]['id']})")
        print(f"  Existing entries preserved ({len(existing_paths)} files)")
        for entry in new_entries:
            print(f"  + #{entry['id']} {entry['path']} ({entry['type']})")
    else:
        # Fresh index
        index_content = generate_full_index(source_dirs, output_dir)

        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)

        print(f"Source index created: {index_path}")

    # Report context libraries found
    for d in source_dirs:
        if is_context_library(d):
            print(f"\n  Context library detected: {d}")
            lib_info = discover_context_library(d)
            if lib_info['agent_definitions']:
                for ad in lib_info['agent_definitions']:
                    print(f"    Agent: {ad['name']} ({ad['domain']})")
            print(f"    Modules: {len(lib_info['modules'])}")
            print(f"    Addenda: {len(lib_info['addenda'])}")

    print()
    print("Next steps:")
    print("1. The agent reads every file in the index")
    print("2. After reading, the agent identifies gaps the sources don't cover")
    print("3. The agent asks the user ONLY about those gaps")


if __name__ == '__main__':
    main()
