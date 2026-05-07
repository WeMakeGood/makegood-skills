---
name: processing-docx-edits
description: Processes DOCX files containing tracked changes and comments, synthesizes all edits, and produces clean final documents. Use when processing Word documents with track changes, reviewer comments, collaborative edits, or markup. Activates when DOCX file with edits is provided via attached file, uploaded document, or file path.
---

# Processing DOCX Edits

Intelligently processes Word documents with tracked changes and comments, synthesizes all feedback, and produces a clean final document.

<purpose>
Claude's default when editing is to "improve" content—adding polish, fixing adjacent issues,
making things "better." Document review requires the opposite: strict fidelity to reviewer
intent. This skill exists to enforce traceability, where every change maps to a specific
tracked change or comment, and no unauthorized improvements slip in.
</purpose>

## Critical Rules

**GROUNDING:** Apply ONLY the edits explicitly present in the document. Never add "improvements" or changes not requested by reviewers.

**USER APPROVAL REQUIRED:** Do not apply edits until the user confirms. Present all changes and get explicit approval before modifying content.

**PROFESSIONAL OBJECTIVITY:** If reviewer comments are contradictory, unclear, or potentially problematic, flag this to the user rather than making assumptions. Your job is to surface decisions, not make them.

**TRACEABILITY:** Every change in the final document must trace to a specific tracked change or comment. Document what you did and why.

## Quick Start

1. Run the extraction script on the DOCX file
2. Analyze the extracted changes and comments
3. Present summary and questions to user
4. Apply approved edits and output clean document

## Workflow

Copy this checklist and track progress:

```
Progress:
- [ ] Phase 1: Extract document data (run script)
- [ ] Phase 2: Analyze full document
- [ ] Phase 3: Synthesize edits
- [ ] Phase 4: Human review checkpoint
- [ ] Phase 5: Apply edits
- [ ] Phase 6: Validate output
- [ ] Phase 7: Save final document
```

<phase_extraction>
### Phase 1: Document Extraction

**ALWAYS run the extraction script first.** It reliably extracts tracked changes, comments, and document structure.

```bash
python3 scripts/extract_docx.py <path-to-docx>
```

The script outputs JSON with:
- `summary`: Counts of changes, insertions, deletions, comments, authors
- `tracked_changes`: List of all insertions and deletions with author, date, text, paragraph
- `comments`: List of all comments with author, text, and paragraph location
- `document_content`: Paragraphs with inline markers showing where changes/comments appear

**Markers in document_content:**
- `[+INS:id]text[/INS]` - Inserted text
- `[-DEL:id]text[/DEL]` - Deleted text
- `[COMMENT:id>>]text[<<COMMENT:id]` - Text with comment attached

**If script fails:** Check error message and report to user. Common issues:
- File not found
- Not a valid DOCX
- Corrupted file

**GATE:** Before proceeding, write:
- "Extraction complete: [N] tracked changes, [M] comments from [authors]"
- "Document has [P] paragraphs"
</phase_extraction>

<phase_analysis>
### Phase 2: Full Document Analysis

**Read the ENTIRE extracted document content before making any changes.**

This enables:
- Detecting when a comment in one section affects content elsewhere
- Understanding document flow and internal references
- Identifying related content that may need coordinated changes

Build a mental model of the document's purpose, structure, and content relationships.
</phase_analysis>

<phase_synthesis>
### Phase 3: Edit Synthesis

Using the extracted data, build a unified edit list.

For each tracked change and comment, determine:
1. What change is being requested?
2. Where does it apply in the document?
3. Does this change require updates to other parts of the document?
4. Are there conflicts with other edits?

Group related changes (e.g., same author, same section, related content).
</phase_synthesis>

<phase_review>
### Phase 4: Human Review Checkpoint

**STOP. Do not proceed without explicit user confirmation.**

Present to the user:

**1. Summary of findings:**
```
Analyzed [filename]:
- X tracked changes (Y insertions, Z deletions)
- N comments from M reviewer(s): [names]

Proposed Edits:
1. [Para N]: [Change type] - [Description]
2. [Para N]: [Change type] - [Description]
...
```

**2. Questions requiring input** — Flag any comments that are:
- Discussions rather than directives ("Should we include this?")
- Ambiguous or unclear
- Conflicting with other comments
- Potentially problematic (e.g., removing important context, introducing errors)

**3. Conflicts between reviewers:**
```
Conflict in paragraph N:
- [Author A]: [Their suggestion]
- [Author B]: [Contradictory suggestion]
How should I proceed?
```

**4. Concerns (if any):**
If you notice issues with proposed edits — factual errors being introduced, important content being removed, inconsistencies being created — raise them here.

**REQUIRED:** Wait for user to explicitly confirm edits and answer all questions. Do not proceed on partial confirmation.

**GATE:** Before applying edits, write:
- "User approved: [list of approved changes]"
- "User rejected: [list, or 'none']"
- "Questions resolved: [summary of answers]"

Do not proceed until you have written these statements.
</phase_review>

<phase_application>
### Phase 5: Edit Application

**REQUIRED:** Apply ONLY edits the user explicitly approved.

1. Start with the extracted document content (markers removed)
2. Accept/reject each tracked change based on user confirmation
3. Address each comment's requested change as confirmed
4. Apply cascading changes where one edit affects other sections — document each cascading change
5. Maintain document coherence and flow

**Do not:**
- Add edits the user didn't approve
- "Improve" content beyond what was requested
- Silently resolve ambiguities — if unclear, ask
</phase_application>

<phase_validation>
### Phase 6: Validation

Review the final document to verify:
- All approved edits were applied
- All comments were addressed
- No unintended changes introduced
- Document logic and flow remain coherent

If issues found, flag them for the user before output.
</phase_validation>

<phase_output>
### Phase 7: Output

**Save the final document to `./tmp/`. Do not output full document content inline.**

1. Ensure `./tmp/` directory exists (create if needed)
2. Generate filename: `./tmp/[original-name]-final.md`
3. Write complete output to file
4. Confirm with brief summary:

```
Done! Saved to `./tmp/[filename]-final.md`.

Summary:
- Applied X tracked changes (Y accepted, Z rejected)
- Resolved N comments
- Made M additional updates where changes affected other sections
```
</phase_output>

<failed_attempts>
What DOESN'T work:

- **Skipping extraction script:** Manual parsing of DOCX XML is error-prone. The script handles edge cases (nested changes, overlapping comments) reliably.
- **"Improving" while editing:** Adding grammar fixes, rewording for clarity, or any edit not explicitly in the tracked changes violates traceability.
- **Resolving conflicts without asking:** When two reviewers contradict each other, always surface the conflict. Never silently pick one.
- **Partial confirmation:** "Proceed with most edits" is not explicit approval. Get specific approval for each contested item.
</failed_attempts>

## Scripts

| Script | Purpose |
|--------|---------|
| [scripts/extract_docx.py](scripts/extract_docx.py) | Extract tracked changes, comments, and content from DOCX |

## Example Interaction

**User:** "Process the edits in proposal.docx"

**Step 1 - Run extraction:**
```bash
python3 scripts/extract_docx.py proposal.docx
```

**Step 2 - Present findings:**
```
Analyzed proposal.docx:
- 12 tracked changes (8 insertions, 4 deletions)
- 7 comments from 2 reviewers: Sarah, Mike

Proposed Edits:
1. [Para 3]: Insertion - Add "Q3 2024" timeline reference
2. [Para 7]: Deletion - Remove outdated cost estimate ($50k)
3. [Para 12]: Comment - Mike asks to expand description
4. [Para 5, 9, 15]: Insertion - Update "Phase 1" → "Initial Phase"
...

Questions for you:
- Sarah's comment on paragraph 8: "Should we include the risk assessment section?"
  What would you like to do?

- Conflict in paragraph 6:
  - Mike: Suggests removing this paragraph entirely
  - Sarah: Asks to expand it with more detail
  How should I proceed?

Please confirm the edits and answer the questions above.
```

**User:** "Include the risk assessment. For the conflict, go with Mike's suggestion."

**Step 3 - Apply and output:**
```
Applying edits...

Done! Saved to `./tmp/proposal-final.md`.

Summary:
- Applied 12 tracked changes (11 accepted, 1 rejected)
- Resolved 7 comments
- Added risk assessment section per Sarah's comment
- Removed paragraph 6 per your direction
- Updated 2 additional references affected by changes
```

## Error Handling

If extraction fails:
```
Unable to process [filename]: [error from script]

This may happen if:
- The file is corrupted or password-protected
- The file is not a valid DOCX format
- Required content (document.xml) is missing

Please check the file and try again.
```
