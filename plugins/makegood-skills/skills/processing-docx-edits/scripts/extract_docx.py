#!/usr/bin/env python3
"""
Extract tracked changes, comments, and document structure from a DOCX file.

Usage:
    python3 scripts/extract_docx.py <docx_file> [--output <json_file>]

Output: JSON with document content, tracked changes, and comments.
"""

import argparse
import json
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

# Word XML namespaces
NAMESPACES = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'w14': 'http://schemas.microsoft.com/office/word/2010/wordml',
    'w15': 'http://schemas.microsoft.com/office/word/2012/wordml',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
}


def get_text(element):
    """Extract all text from an XML element and its children."""
    texts = []
    for node in element.iter():
        if node.tag == f"{{{NAMESPACES['w']}}}t" and node.text:
            texts.append(node.text)
    return ''.join(texts)


def extract_comments(zip_file):
    """Extract comments from comments.xml."""
    comments = {}
    try:
        if 'word/comments.xml' not in zip_file.namelist():
            return comments

        content = zip_file.read('word/comments.xml')
        root = ET.fromstring(content)

        for comment in root.findall('.//w:comment', NAMESPACES):
            comment_id = comment.get(f"{{{NAMESPACES['w']}}}id")
            author = comment.get(f"{{{NAMESPACES['w']}}}author", "Unknown")
            date = comment.get(f"{{{NAMESPACES['w']}}}date", "")
            text = get_text(comment)

            comments[comment_id] = {
                'id': comment_id,
                'author': author,
                'date': date,
                'text': text.strip()
            }
    except Exception as e:
        print(f"Warning: Could not parse comments: {e}", file=sys.stderr)

    return comments


def extract_document_content(zip_file, comments):
    """Extract document content with tracked changes and comment references."""
    content = zip_file.read('word/document.xml')
    root = ET.fromstring(content)

    paragraphs = []
    tracked_changes = []
    comment_refs = []
    change_counter = 0

    for para_idx, para in enumerate(root.findall('.//w:p', NAMESPACES)):
        para_texts = []

        for elem in para.iter():
            # Regular text
            if elem.tag == f"{{{NAMESPACES['w']}}}t" and elem.text:
                para_texts.append(elem.text)

            # Inserted text (tracked change)
            elif elem.tag == f"{{{NAMESPACES['w']}}}ins":
                change_counter += 1
                author = elem.get(f"{{{NAMESPACES['w']}}}author", "Unknown")
                date = elem.get(f"{{{NAMESPACES['w']}}}date", "")
                inserted_text = get_text(elem)

                tracked_changes.append({
                    'id': change_counter,
                    'type': 'insertion',
                    'author': author,
                    'date': date,
                    'text': inserted_text,
                    'paragraph': para_idx + 1
                })
                para_texts.append(f"[+INS:{change_counter}]{inserted_text}[/INS]")

            # Deleted text (tracked change)
            elif elem.tag == f"{{{NAMESPACES['w']}}}del":
                change_counter += 1
                author = elem.get(f"{{{NAMESPACES['w']}}}author", "Unknown")
                date = elem.get(f"{{{NAMESPACES['w']}}}date", "")
                deleted_text = get_text(elem)

                tracked_changes.append({
                    'id': change_counter,
                    'type': 'deletion',
                    'author': author,
                    'date': date,
                    'text': deleted_text,
                    'paragraph': para_idx + 1
                })
                para_texts.append(f"[-DEL:{change_counter}]{deleted_text}[/DEL]")

            # Comment range start
            elif elem.tag == f"{{{NAMESPACES['w']}}}commentRangeStart":
                comment_id = elem.get(f"{{{NAMESPACES['w']}}}id")
                if comment_id and comment_id in comments:
                    para_texts.append(f"[COMMENT:{comment_id}>>]")

            # Comment range end
            elif elem.tag == f"{{{NAMESPACES['w']}}}commentRangeEnd":
                comment_id = elem.get(f"{{{NAMESPACES['w']}}}id")
                if comment_id and comment_id in comments:
                    comment_refs.append({
                        'comment_id': comment_id,
                        'paragraph': para_idx + 1,
                        **comments[comment_id]
                    })
                    para_texts.append(f"[<<COMMENT:{comment_id}]")

        para_text = ''.join(para_texts).strip()
        if para_text:
            paragraphs.append({
                'index': para_idx + 1,
                'text': para_text
            })

    return paragraphs, tracked_changes, comment_refs


def extract_docx(docx_path):
    """Main extraction function."""
    docx_path = Path(docx_path)

    if not docx_path.exists():
        return {'error': f"File not found: {docx_path}"}

    if not docx_path.suffix.lower() == '.docx':
        return {'error': f"Not a DOCX file: {docx_path}"}

    try:
        with zipfile.ZipFile(docx_path, 'r') as zf:
            # Check for required files
            if 'word/document.xml' not in zf.namelist():
                return {'error': "Invalid DOCX: missing word/document.xml"}

            # Extract comments first (needed for reference lookup)
            comments = extract_comments(zf)

            # Extract document content with changes
            paragraphs, tracked_changes, comment_refs = extract_document_content(zf, comments)

            # Count unique authors
            authors = set()
            for change in tracked_changes:
                authors.add(change['author'])
            for ref in comment_refs:
                authors.add(ref['author'])

            return {
                'file': str(docx_path),
                'summary': {
                    'total_paragraphs': len(paragraphs),
                    'tracked_changes': len(tracked_changes),
                    'insertions': sum(1 for c in tracked_changes if c['type'] == 'insertion'),
                    'deletions': sum(1 for c in tracked_changes if c['type'] == 'deletion'),
                    'comments': len(comment_refs),
                    'authors': sorted(list(authors))
                },
                'tracked_changes': tracked_changes,
                'comments': comment_refs,
                'document_content': paragraphs
            }

    except zipfile.BadZipFile:
        return {'error': f"Invalid or corrupted DOCX file: {docx_path}"}
    except Exception as e:
        return {'error': f"Failed to process DOCX: {str(e)}"}


def main():
    parser = argparse.ArgumentParser(
        description='Extract tracked changes and comments from a DOCX file'
    )
    parser.add_argument('docx_file', help='Path to the DOCX file')
    parser.add_argument('--output', '-o', help='Output JSON file (default: stdout)')

    args = parser.parse_args()

    result = extract_docx(args.docx_file)

    output = json.dumps(result, indent=2, ensure_ascii=False)

    if args.output:
        Path(args.output).write_text(output)
        print(f"Extraction saved to: {args.output}")
    else:
        print(output)

    # Exit with error code if extraction failed
    if 'error' in result:
        sys.exit(1)


if __name__ == '__main__':
    main()
