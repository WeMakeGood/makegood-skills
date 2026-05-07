# Phase 1: Gather

> **PROCESS GATES — Read these first:**
> - **Read Before Ask:** Read every source document before asking the user any questions about their organization. The sources contain the organizational reasoning — asking the user to restate what documents already say wastes their time and produces answers that are less complete than the sources.
> - **Read-Then-Index:** Read one source file. Update the reading checklist immediately. Then read the next file. This sequence prevents memory blur across documents — the checklist entry is written while the file is fresh.
> - **Gaps, Not Questions:** After reading all sources, identify what the sources DON'T answer about website requirements. Ask the user only about those gaps. CTAs and technical stack are almost always gaps (they're project-specific decisions). Organizational identity, audience, and brand voice almost never are (they're in the sources).

---

## What This Phase Does

Collect source paths and context library location from the user. Run the indexing script to discover all files. Read and index every document. Identify what the sources answer and what they don't. Ask the user only about gaps. Create build state, process log, and source registry.

**Order of operations:** paths → script → read everything → identify gaps → ask about gaps only.

---

<phase_gather_sources>
## Step 1: Get Paths

Ask the user:

- "Where are your source documents?" — may be multiple directories
- "Do you have a context library for this organization? If so, where?"
- "Any other source directories?" (additional docs, interview syntheses, etc.)
- "Where should I create the project?" (default: `./tmp/<project-name>/`) → `OUTPUT_PATH`

These are the only questions before reading begins.

---

## Step 2: Run the Indexing Script

**REQUIRED:** Run the indexing script to generate the source index. The script accepts multiple source paths and auto-detects context libraries:

```bash
python3 scripts/create_source_index.py <OUTPUT_PATH> <PATH> [PATH] [PATH] ...
```

Examples:
```bash
python3 scripts/create_source_index.py ./tmp/project ./source
python3 scripts/create_source_index.py ./tmp/project ./planning ./context-library
python3 scripts/create_source_index.py ./tmp/project ./planning ./context-lib ./extra-docs
```

This creates `<OUTPUT_PATH>/source-index.md` with:
- Every file inventoried with **stable numeric IDs** that all subsequent phases reference
- Context library discovery (agent definitions, modules, addenda, voice profile, writing standards parsed from frontmatter)
- Type and signal classifications
- A reading checklist
- A Website Content Mappings skeleton for Phase 2
- Embedded process gates that survive context compaction

**Safe to re-run.** If the user provides additional source documents later, re-run the script with the new paths. It merges new files into the existing index without overwriting reading notes, comprehension mappings, or other agent-populated sections. New files get the next available IDs.

The source index is a first-class artifact — the sitemap will reference sources by these IDs, and Phases 5 and 6 will use the IDs to know which files to re-read for each page. Without it, downstream phases have no way to connect pages to source material.

**If the script fails:** Create `source-index.md` manually using the same format — numbered IDs, file paths, types, signals. The IDs are what matter. Every file must have a stable number that the sitemap can reference.

---

## Step 3: Read Every File

Read `<OUTPUT_PATH>/source-index.md` to get the complete file list.

Follow the Read-Then-Index gate: read one file, update the reading checklist with notes, then read the next.

**For context library files:**
- **Agent definitions:** Note the identity block, domain, which modules it loads (from `modules:` frontmatter), and what situations the agent handles. This tells you how the website's voice should work.
- **Context modules:** Note what organizational reasoning each module provides. These contain the org's identity, values, audience thinking, and methodology — the answers to questions you would otherwise have to ask.
- **Voice profile / writing standards:** Note the practitioner voice, prose gates, revision backstops. These load LAST in the content session.
- **Addenda:** Note what reference data is available on demand.

**For source documents:**
- **Brand guides:** Note visual identity, tone, messaging hierarchy.
- **Org docs:** Note mission, programs, positioning, how the org describes itself.
- **Interview syntheses:** Note organizational reasoning buried in conversational evidence.
- **Existing copy:** Note current messaging, what works, what doesn't.

For every file, update the source index reading checklist with:
- What organizational knowledge this file contains
- How it informs website content
- Any conflicts with other files

---

## Step 4: Identify Gaps

After reading ALL files, review what the sources answer and what they don't.

**Sources almost always answer:**
- What the organization does
- How it's different
- Who it serves
- How it talks about itself and its audiences
- Brand voice and tone

**Sources almost never answer (these are project-specific decisions):**
- What the PRIMARY CTA should be (what action do visitors take?)
- Secondary and tertiary CTAs
- Technical stack (page builder, forms plugin, integrations)
- What content to migrate from an existing site
- What success looks like for this specific website

Record gaps in the source index's Gaps section.

---

## Step 5: Ask About Gaps

Now — and only now — have a conversation with the user about what the sources don't cover.

**Always ask:**
- What is the PRIMARY action you want visitors to take?
- What is the secondary action?
- What does success look like for this website?
- Technical stack: page builder, forms plugin, integrations? (See [references/TECHNICAL-CONTEXT.md](../TECHNICAL-CONTEXT.md))

**Only ask if sources don't answer:**
- Audience questions (if sources are thin on who the org serves)
- Brand/voice questions (if no context library or brand guide exists)
- Organizational identity (if sources are missing or contradictory)

If the user cannot clearly articulate their primary CTA, help them define it. Challenge vague goals: "increase awareness" is not a CTA. What specific action demonstrates that awareness increased?

**LOG:** CTA hierarchy with the user's exact language. Technical stack decisions. Any gaps the user filled that sources didn't cover.
</phase_gather_sources>

---

## Step 6: Create Build State and Process Log

Create `<OUTPUT_PATH>/build-state.md` and `<OUTPUT_PATH>/process-log.md` using the templates from [references/TEMPLATES.md](../TEMPLATES.md).

Record in build state:
- Project metadata (organization name, output path, source path)
- Context library manifest (agent definition path, module paths from frontmatter, voice profile, writing standards)
- Source index location
- Technical stack
- Current phase: Gather (completing)

Log first entries to process log:
- What the sources revealed about the organization — key reasoning, not summaries
- CTA decisions and rationale
- Context library findings — what organizational reasoning is already encoded in modules
- Gaps that required user input vs. gaps that remain open
- Any conflicts between sources

---

## GATE

Write to build state:
- "Source index generated: [count] files"
- "Files read and indexed: [count] / [total]"
- "Context library: agent definition [path or 'none'], modules [count], voice profile [path or 'none'], writing standards [path or 'none']"
- "Primary CTA defined: [specific action]"
- "Secondary CTA defined: [specific action]"
- "Technical stack: [page builder, forms plugin, other]"
- "Gaps filled by user: [list]"
- "Gaps remaining: [list or 'none']"
- "BLOCKING gaps: [list or 'none']"

---

## STOP

**Present to the user:**
- Source inventory — what was found, what each file contributes
- Context library discovery — agent definition, modules, voice profile
- What the sources tell you about the organization (demonstrate that you read and understood them — not a list of files, but what they reveal)
- CTA hierarchy as confirmed
- Technical stack
- Remaining gaps — information still needed
- BLOCKING gaps — information required before comprehension can proceed

**Ask:**
- Did I understand the sources correctly?
- Is the CTA hierarchy right?
- Is the context library complete? Any modules I should also load?
- For BLOCKING gaps — can you provide the missing information?

**Do not proceed until the user confirms.**

---

## After This Phase

Update build state:
- **Current phase:** Phase 2 (Comprehend)
- **Next phase file:** `references/phases/PHASE_2_COMPREHEND.md`

Proceed directly to Phase 2 in the same session.
