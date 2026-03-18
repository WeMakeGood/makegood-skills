# Phase 1: Setup

> **CRITICAL RULES — Read these first:**
> - NEVER invent details. Use exact names, dates, locations from sources.
> - NEVER fill gaps. Missing information is a gap to report, not a blank to fill.
> - NEVER skip source documents. Read every file in the source directory.
> - Update the source index immediately after reading each file — do not batch.
> - This phase creates the manifest that every subsequent phase depends on. Errors here cascade.

---

## What This Phase Does

Inventory all source documents, classify them, identify what domain agents will need to *do* with this organizational knowledge, and create the build state tracker. The output is a complete source index and an initial understanding of what agents this library will serve.

---

<phase_setup_index>
## Step 1: Create the Source Index

Run the indexing script to generate the initial manifest:

```bash
scripts/create_source_index.py <SOURCE_PATH> <OUTPUT_PATH>
```

If the script isn't executable, run it with your system's Python: `python3 scripts/create_source_index.py <SOURCE_PATH> <OUTPUT_PATH>`

This creates a starting manifest with file names, types, and initial classifications. You will refine this as you read each file.

---

## Step 2: Read Every Source File

Read each file in the source index. For EVERY file, update the index entry with:

- **Type**: strategy, operational, transcript, interview, notes, reference, financial, legal
- **Signal**: `clear` (organizational knowledge stated directly, use as-is) or `buried` (meaning embedded in conversational artifacts, filler, or unstructured notes — Comprehend extracts the patterns directly)
- **Key topics**: What organizational knowledge this file contains
- **Relevance**: How this file might inform agent behavior (not just what facts it contains)
- **Conflicts**: Any contradictions with other files already read
- **Gaps**: Information this file references but doesn't contain

**CRITICAL:** Update the source index after reading each file. Do not read all files and then update — memory blurs across documents. Read one, update, read the next.

**For buried-signal sources (transcripts, raw notes):** Do NOT attempt to clean or rewrite them. Note their complexity and what behavioral patterns they contain. Comprehend (Phase 2) will extract the meaning directly.

---

## Step 3: Identify Agent Needs

Based on what you've read, draft an initial assessment:

- **What work do agents need to do** with this organizational knowledge? (Not "what information exists" but "what decisions would agents make?")
- **What agent roles emerge** from the work patterns? (Role-based, not taxonomy-based — defined by what the agent *does and decides*, not by what information category it covers)
- **What's missing?** Are there obvious gaps where agents would need information the sources don't provide?

This assessment is preliminary — Comprehend will deepen it. But it grounds the source reading in purpose rather than cataloging.

---

## Step 4: Create Build State and Process Log

Create `<OUTPUT_PATH>/build-state.md` using the template from [references/TEMPLATES.md](../TEMPLATES.md). Record:

- Library metadata (source path, output path, target model)
- Current phase: Setup (completing)
- Source index location
- Initial agent needs assessment
- Any BLOCKING gaps identified

Create `<OUTPUT_PATH>/process-log.md` using the template from [references/TEMPLATES.md](../TEMPLATES.md). Log your first entries:

- Source set overview — what you found, what surprised you, what's missing
- Initial agent role reasoning — why these roles, not others
- Any conflicts or gaps that shaped your assessment
- User decisions from the STOP review
</phase_setup_index>

---

## GATE

Write to the build state:
- "Source files indexed: [count]"
- "Files read: [count] / [total]"
- "Complex sources (will need direct comprehension): [list]"
- "Clean sources (ready to use): [list]"
- "Initial agent roles identified: [list]"
- "BLOCKING gaps: [list or 'none']"
- "Conflicts between sources: [list or 'none']"

---

## STOP

**Present to the user:**
- Complete source inventory with classifications
- Which sources are complex (transcripts, raw notes) vs. clean
- Initial agent roles — what work the library needs to support
- Any conflicts between source documents
- BLOCKING gaps — information needed that isn't in the sources
- Any files that seem irrelevant or redundant

**Ask:**
- Are these source classifications correct?
- Do the initial agent roles match what you need?
- Are there additional sources I should include?
- For BLOCKING gaps — can you provide the missing information?

**Do not proceed until the user confirms the source inventory and addresses any BLOCKING gaps.**

---

## After This Phase

Update build state:
- **Current phase:** Phase 2 (Comprehend)
- **Next phase file:** `references/phases/PHASE_2_COMPREHEND.md`

Proceed directly to Phase 2 in the same session.
