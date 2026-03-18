#!/usr/bin/env python3
"""
Analyze source documents for context library building.

Provides:
1. Complete inventory of all source documents
2. Token estimates and statistics
3. Document structure extraction (headings, metadata)
4. Categorization by folder/topic
5. JSON output for programmatic use

Usage:
    python analyze_sources.py <SOURCE_PATH> [--json] [--output FILE]

Examples:
    python analyze_sources.py ./sources
    python analyze_sources.py ./sources --json
    python analyze_sources.py ./sources --json --output inventory.json
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def estimate_tokens(text: str) -> int:
    """Estimate tokens (roughly 0.75 words per token for English)."""
    words = count_words(text)
    return int(words / 0.75)


def extract_yaml_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter if present."""
    if not content.startswith('---'):
        return {}

    # Find the closing ---
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return {}

    yaml_content = content[3:end_match.start() + 3]

    # Simple YAML parsing (key: value pairs)
    metadata = {}
    for line in yaml_content.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value:
                metadata[key] = value

    return metadata


def extract_headings(content: str) -> list:
    """Extract markdown headings from content."""
    headings = []
    for line in content.split('\n'):
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()
            headings.append({'level': level, 'text': text})
    return headings


def extract_first_paragraph(content: str) -> str:
    """Extract first non-empty paragraph after frontmatter and headings."""
    # Remove frontmatter
    if content.startswith('---'):
        end_match = re.search(r'\n---\s*\n', content[3:])
        if end_match:
            content = content[end_match.end() + 3:]

    # Find first paragraph (non-heading, non-empty lines)
    lines = []
    in_paragraph = False

    for line in content.split('\n'):
        stripped = line.strip()

        # Skip headings and empty lines at start
        if not in_paragraph:
            if stripped and not stripped.startswith('#'):
                in_paragraph = True
                lines.append(stripped)
        else:
            if stripped and not stripped.startswith('#'):
                lines.append(stripped)
            elif not stripped and lines:
                break  # End of paragraph

    result = ' '.join(lines)
    # Truncate if too long
    if len(result) > 300:
        result = result[:297] + '...'
    return result


def analyze_file(filepath: Path, base_dir: Path) -> dict:
    """Analyze a single file comprehensively."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Get relative path from base
        rel_path = filepath.relative_to(base_dir)

        # Determine category from folder structure
        parts = rel_path.parts
        category = parts[0] if len(parts) > 1 else 'root'
        subcategory = parts[1] if len(parts) > 2 else None

        return {
            'path': str(filepath),
            'relative_path': str(rel_path),
            'name': filepath.name,
            'category': category,
            'subcategory': subcategory,
            'size_bytes': filepath.stat().st_size,
            'words': count_words(content),
            'tokens_est': estimate_tokens(content),
            'lines': len(content.splitlines()),
            'metadata': extract_yaml_frontmatter(content),
            'headings': extract_headings(content),
            'summary': extract_first_paragraph(content),
            'modified': datetime.fromtimestamp(filepath.stat().st_mtime).isoformat(),
            'error': None
        }
    except Exception as e:
        return {
            'path': str(filepath),
            'name': filepath.name,
            'error': str(e)
        }


def find_documents(source_dir: Path) -> list:
    """Find all markdown and text documents."""
    extensions = {'.md', '.txt', '.markdown'}
    documents = []

    for ext in extensions:
        documents.extend(source_dir.rglob(f'*{ext}'))

    # Filter out hidden files and common non-content files
    documents = [d for d in documents if not any(
        part.startswith('.') for part in d.parts
    )]

    return sorted(documents)


def print_text_report(results: list, source_dir: Path, total_tokens: int, total_words: int):
    """Print human-readable text report."""
    print(f"Source Document Analysis")
    print(f"========================")
    print(f"Directory: {source_dir.absolute()}")
    print(f"Documents found: {len(results)}")
    print(f"Total tokens: ~{total_tokens:,}")
    print()

    # Group by category
    by_category = defaultdict(list)
    for r in results:
        cat = r.get('category', 'unknown')
        by_category[cat].append(r)

    # Print by category
    for category in sorted(by_category.keys()):
        docs = by_category[category]
        cat_tokens = sum(d.get('tokens_est', 0) for d in docs if not d.get('error'))
        print(f"\n## {category}/ ({len(docs)} files, ~{cat_tokens:,} tokens)")
        print("-" * 60)

        for r in docs:
            if r.get('error'):
                print(f"  ❌ {r['name']}: ERROR - {r['error']}")
            else:
                # Get title from metadata or first heading
                title = r.get('metadata', {}).get('title', '')
                if not title and r.get('headings'):
                    title = r['headings'][0]['text']
                if not title:
                    title = r['name']

                print(f"  📄 {r['relative_path']}")
                print(f"     Tokens: ~{r['tokens_est']:,} | Title: {title[:50]}")
                if r.get('summary'):
                    summary = r['summary'][:100] + '...' if len(r.get('summary', '')) > 100 else r.get('summary', '')
                    print(f"     {summary}")
                print()

    # Print totals and guidance
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total documents: {len(results)}")
    print(f"Total words: {total_words:,}")
    print(f"Total tokens (est): {total_tokens:,}")
    print()
    print("Guidance:")
    print(f"- Context libraries typically compress to 20-40% of source size")
    print(f"- Estimated library size: {int(total_tokens * 0.2):,} - {int(total_tokens * 0.4):,} tokens")
    print(f"- Target per agent: 10% of model context window (e.g., 20K for 200K-context models)")
    print()

    if total_tokens > 100000:
        print("⚠️  Large source base. Prioritize most relevant documents.")

    # Print reading order recommendation
    print("\n" + "=" * 60)
    print("RECOMMENDED READING ORDER")
    print("=" * 60)
    print("Claude should read documents in this priority:")
    print()

    # Prioritize: strategic docs first, then by category importance
    priority_keywords = ['strategic', 'architecture', 'principles', 'overview', 'mission', 'vision']
    priority_docs = []
    other_docs = []

    for r in results:
        if r.get('error'):
            continue
        name_lower = r['name'].lower()
        if any(kw in name_lower for kw in priority_keywords):
            priority_docs.append(r)
        else:
            other_docs.append(r)

    print("HIGH PRIORITY (read first):")
    for i, r in enumerate(priority_docs, 1):
        print(f"  {i}. {r['relative_path']}")

    print("\nSTANDARD PRIORITY (read after high priority):")
    for i, r in enumerate(other_docs, 1):
        print(f"  {i}. {r['relative_path']}")


def main():
    parser = argparse.ArgumentParser(
        description='Analyze source documents for context library building'
    )
    parser.add_argument('source_dir', nargs='?', default='.',
                       help='Directory containing source documents')
    parser.add_argument('--json', action='store_true',
                       help='Output as JSON instead of text')
    parser.add_argument('--output', '-o', type=str,
                       help='Write output to file instead of stdout')

    args = parser.parse_args()
    source_dir = Path(args.source_dir)

    if not source_dir.exists():
        print(f"Error: Directory '{source_dir}' not found", file=sys.stderr)
        sys.exit(1)

    documents = find_documents(source_dir)

    if not documents:
        print(f"No documents found in '{source_dir}'", file=sys.stderr)
        print("Looking for: .md, .txt, .markdown files", file=sys.stderr)
        sys.exit(0)

    # Analyze all documents
    results = []
    total_words = 0
    total_tokens = 0

    for doc in documents:
        result = analyze_file(doc, source_dir)
        results.append(result)
        if not result.get('error'):
            total_words += result['words']
            total_tokens += result['tokens_est']

    # Prepare output
    if args.json:
        output = {
            'analysis_date': datetime.now().isoformat(),
            'source_directory': str(source_dir.absolute()),
            'summary': {
                'total_documents': len(results),
                'total_words': total_words,
                'total_tokens_est': total_tokens,
                'estimated_library_size_min': int(total_tokens * 0.2),
                'estimated_library_size_max': int(total_tokens * 0.4),
            },
            'documents': results
        }
        output_str = json.dumps(output, indent=2)
    else:
        # Capture text output
        import io
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        print_text_report(results, source_dir, total_tokens, total_words)
        output_str = sys.stdout.getvalue()
        sys.stdout = old_stdout

    # Write output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output_str)
        print(f"Output written to {args.output}", file=sys.stderr)
    else:
        print(output_str)


if __name__ == '__main__':
    main()
