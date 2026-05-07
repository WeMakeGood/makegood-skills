# Phase 1: Setup

> **CRITICAL RULES — Read these first:**
> - Read the project manifest (`project-manifest.md`) before anything else. It contains file paths for all project components. If no manifest exists, ask the user for: research files, voice profile path, writing standards preference, audience description, and output directory.
> - Do not load any file from an `Archive/` directory. Archived files are deprecated.
> - This phase scaffolds and loads. It does not analyze, orient, or plan.

---

## What This Phase Does

Read the project manifest, load all materials, confirm everything is present. The output is a confirmed loading record and a started process log. No analytical work happens here — that belongs in Comprehend.

---

<phase_setup>
## Read Manifest and Load Materials

**REQUIRED:** Read the project manifest first. If no manifest exists, gather the minimum from the user and note it in the article plan.

**Start the process log** — create `Drafts/article-[N]-process-log.md` with the article number, title, and date.

From the manifest, load in this order:

**1. Article context:**
- Series map (if series article) — locate the specific article section for thesis, argument arc, misconception to reframe, keyword targets, and series build position
- Article brief (if single article) — thesis, argument arc, research-to-load
- Audience document — who the reader is
- Core thesis/framework document (if provided) — the structural argument the article serves
- Context modules (if listed in manifest) — organizational identity, ethical framework, content methodology, or other modules that inform how the article represents the organization. These are not research — they are organizational knowledge for accuracy and alignment.

**2. Research:**
- Research index (if provided in the manifest) — read the evidence map to identify which research documents serve this article
- Load documents marked as **primary evidence** for this article's thesis elements
- Load **supporting evidence** documents relevant to the argument arc
- **Background context** documents: note their existence but do not load unless Comprehend identifies a specific need

**3. Writing standards:**
- Load the writing standards module from the manifest. The writing standards inform structural decisions throughout — how sections open, how evidence enters prose, how passages land. Load them now so they're available from the start.

**4. Voice profile — thinking patterns and mode selection:**
- Read the voice profile. The voice profile describes how the author *thinks*, not just how they write — entry point patterns, reasoning sequences, cross-domain movement, how disagreement arrives. Note which generative mode leads. **Full role adoption and first-person commitment happen in the Draft phase** — but the thinking patterns are active from here onward.

**LOG:** Record what was loaded in compressed form — file names, primary/supporting designation, and any gaps. One line per document, or a grouped list. Keep tight — everything logged here is loaded again at Draft time.

**GATE:** Write to the process log:
- "Article: [number and title]"
- "Manifest: [filepath, or 'none — setup gathered from user']"
- "Research documents loaded: [list by short name, noting primary vs. supporting]"
- "Article brief/series map reviewed: [yes/no]"
- "Keyword targets: [list primary and gap terms, or 'none provided']"
- "Context modules loaded: [list by name, or 'none']"
- "Writing standards loaded: [filename]"
- "Voice profile scanned for mode selection: [leading mode]"
- "Loading gaps: [list, or 'none']"

**STOP.** Present to the user:
- Which article is being drafted
- What was loaded (listed by name)
- Any loading gaps — documents referenced but not found
- Any ambiguities — if the article maps to more than one possibility

Do not proceed until the user confirms.
</phase_setup>

---

## After This Phase

Update the article plan's phase status and set:
- **Current phase:** Phase 2 (Comprehend)
- **Next phase file:** `references/phases/PHASE_2_COMPREHEND.md`

Proceed directly to Comprehend in the same session — Setup and Comprehend always run together in Session A.
