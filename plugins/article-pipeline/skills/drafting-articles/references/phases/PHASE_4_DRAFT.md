# Phase 4: Draft

> **CRITICAL RULES — Read these first:**
> - **Read the project manifest FIRST.** Load the writing standards module and voice profile from their manifest paths. **Do not proceed without loading both.**
> - Read the article plan (`Drafts/article-[N]-plan.md`) before starting. It contains comprehension findings and the structural plan (metaprompts) from Session A.
> - Re-read the voice profile NOW. You are adopting a role — writing as this person, not about them.
> - Re-read [references/ARCHITECTURE.md](../ARCHITECTURE.md) NOW — Evidence Reasoning, Writing From a Voice Profile, and Narrative Construction sections.
> - Re-read research documents for each section before writing that section. Do not write from memory. The metaprompt tells you what to look for; the research provides what to write from.
> - Do not load any file from an `Archive/` directory.
>
> **GUARDRAILS THAT SURVIVE ROLE ADOPTION — these apply to every sentence, including calibration:**
> - **Source Before Statement:** Before writing any claim or narrative detail, locate its source in the research documents. If you cannot locate it, you cannot write it — your output for that detail is nothing. This applies to narrative details (days of the week, settings, feelings, sequences of events) exactly as it applies to empirical claims. The per-section protocol enforces this through step 5 (identify available narrative material) — that inventory is exhaustive. Do not add to it during generation.
> - **Mark the Move:** The reader must be able to tell whether they're receiving a sourced finding, an extension of sourced material, or original analysis — from the language itself.
> - **Writing standards:** Apply the loaded writing standards module throughout. The voice profile determines *whose* voice. The writing standards determine what craft-level rules govern the writing.
> - Role adoption means writing *as* the person. It does not mean relaxing the process gates. The gates are upstream sequence requirements — complete them before generating, not prohibitions to remember during generating.

---

## What This Phase Does

Write the article using the structural plan from Design — metaprompts that tell you how to think about each section, not what the prose should contain. Re-read research for each section: the metaprompt tells you what to look for, not what to write. The voice profile determines how sentences are built, how evidence lands, and how the reader is addressed.

**This is the highest-risk phase.** Voice profile fidelity and evidence curation degrade with context consumption. The mandatory session break before this phase exists to ensure these instructions are fresh.

---

## Before You Start

Load in this exact order. The order is intentional — voice profile and writing standards must be the **last documents loaded before calibration** so they are fresh in context when generation begins. Everything else loads first.

1. **Read the project manifest** — locate all file paths.
2. **Read `Drafts/article-[N]-plan.md`** — review comprehension findings (what the evidence earns, connections, narrative), the **`<role>` block** (your identity assignment for this article), and the **structural plan** (metaprompts for each section, structural question, article movement). The metaprompts are your thinking orientations — they tell you what stance to take and what to look for, not what to write.
3. **Read [references/ARCHITECTURE.md](../ARCHITECTURE.md)** — the full file.
4. **Re-read the audience document** — for this specific article's position in the series build (if series) or its reader context (if standalone).
5. **Load context modules** (if listed in the manifest and relevant to drafting) — organizational identity, ethical framework, content methodology. These are informational context. Load them here, before voice and standards.
6. **Load the writing standards module** — from the manifest's writing standards path. Read the full module. **This must be loaded after all informational documents.**
7. **Load the voice profile** — from the manifest's voice profile path. Read the full document. **This must be the last document loaded before calibration.** This is where role adoption begins.
8. **Complete the Voice Calibration** below before writing any article prose.

---

## Loading GATE

**REQUIRED before Voice Calibration.** List documents in the order you actually read them. The order matters — if voice profile or writing standards appear before the analytical documents, the loading sequence was wrong and must be redone.

Write to the process log:
- "1. Article plan read: [filename]."
- "2. ARCHITECTURE.md read: yes."
- "3. Audience document read: [filename]."
- "4. Context modules loaded: [list, or 'none']."
- "5. Writing standards loaded: [filename]."
- "6. Voice profile loaded (LAST — immediately before calibration): [filename]."

---

<phase_calibration>
## Voice Calibration

**REQUIRED before drafting begins.** The article plan contains a `<role>` block written during Design. That block is your identity assignment — not a description to analyze, but an identity to inhabit.

### Step 1: Read the role block

Read the `<role>` block in the article plan. This was written during Design when the voice profile was fresh. It establishes who you are for this article, how you think, and how you approach this specific piece.

### Step 2: Re-read the voice profile

Re-read the full voice profile from the path in the role block. The role block is the assignment; the voice profile is the depth. Do not scan for features to reproduce — read for the person. The role block tells you who you are; the voice profile tells you how that person thinks, reasons, enters problems, handles disagreement.

### Step 3: Verify the role is active

In the role established by the role block, answer this question: "How would you approach telling this story to this audience?" Write 1–2 sentences — not about the author, as the author.

This is a verification, not a construction. The role block already established the identity. If your answer contradicts the role block or reads like analysis of a person rather than a statement by that person, the role is not active — re-read the role block and voice profile before continuing.

**Point of view:** The role block and voice profile together determine POV. If you are the article's author, personal experiences from the research are your experiences — do not quote yourself or refer to yourself in third person. If the voice profile describes someone other than the article's author (e.g., ghostwriting), the role block will specify the POV. Follow it.

**GATE:** Write to the process log:
- "Role block read: [yes]"
- "Voice profile re-read: [filename]"
- "Role verification: [1–2 sentences as the author — how I would approach this story]"
- "Point of view: [from role block]"
- "Contextual adaptation: [which adaptation from the voice profile applies]"
- "Leading mode: [from role block / voice profile]"
</phase_calibration>

---

<phase_drafting>
## Drafting Process

The draft follows the story, not the outline. The metaprompts from Design determine the thinking orientation for each section — what stance to take, what to look for. The article has a movement — a direction the reader travels — and each section advances that movement.

### Per-Section Protocol

For EACH section in the structure:

**1. Re-read the relevant research.** The metaprompt names which research elements to re-read. Read them now, even if read before. The metaprompt tells you what to look for — read with that orientation.

**2. Re-read this section's metaprompt.** The metaprompt tells you the thinking stance, what the reader should arrive at, and how this section relates to the ones around it. It does NOT tell you what the prose should say. Write from research + voice + metaprompt orientation.

**3. Use the reader entry point.** The plan specifies where the reader enters each section — what they know, believe, or have just experienced. Draft the section from that entry point.

**4. Select evidence.** From the research you just re-read, select the 2–3 findings that carry this section's structural claim. Those get prose treatment. Everything else: hyperlink only.

**5. Identify available narrative material.** Before writing, locate in the research documents any first-person accounts, specific experiences, described moments, or personal details that belong in this section. List them. These are the only narrative details available. If a sentence would require inventing a detail not in the research — a day of the week, a setting, a feeling, a sequence of events — that detail does not exist and cannot be written. This is Source Before Statement applied to narrative: locate the source before stating the claim. If you cannot locate it, you cannot state it.

**6. Write from the role.** You are the person described in the voice profile. Write from inside their perspective, not about their topics. If the point of view is first person (you are the author), personal experiences from the research are YOUR experiences — do not quote yourself, do not refer to yourself in third person, do not attribute your own knowledge to "Frazier" or "[Author Name]." The narrative material from step 5 is your inventory. Do not add to it during generation. After writing each section, test: read the first and last paragraphs. Am I writing as this person, or about this person? Does this sound like a specific person, or like an AI writing about that person's field? Use the voice profile's gates as diagnostic tests — if any gate fails, the role has slipped. Do not insert missing features. Return to the role and regenerate the section.

**7. Layer, don't linearize.** Recognition → evidence → understanding. The reader sees something familiar, encounters data that reframes it, then sees the familiar thing differently.

**8. Follow dense evidence with connection.** After presenting findings, connect them to the reader's experience. Evidence then recognition.

**9. Close with the closing handoff from the structural plan.** The handoff is the implicit question that makes the next section necessary. The transition is the question, not a bridge phrase.

**10. Check the frame.** Does the article's opening frame (person, event, question) remain present in this section? If it has disappeared, the article has shifted from story to report. Bring the frame back before moving to the next section.

### Opening — the role test

The opening section is where role adoption succeeds or fails. After writing the opening, test it before continuing:
- **Point of view:** Am I writing as this person, or about this person? If the opening quotes or references the author in third person, the role is not active — regardless of how well the content reads. Regenerate from inside the role.
- **Specificity:** Could any competent writer on this topic have written these paragraphs? If yes, the role isn't active. Return to the voice profile, re-read the role (not the features), and regenerate.
- Use the voice profile's gates as diagnostics — but the primary question is "does this sound like a specific person?" not "does this match a list?"

Connect to the reader's search intent within the first two paragraphs. Start with the interesting part.

### Closing

Close with a question that applies the article's frame to the reader's own situation. The question must genuinely require thought.

### Hyperlinking

Every sourced finding gets an inline hyperlink using URLs from the research base. Describe the finding, link the source.

---

## Output

Write the draft to: `Drafts/[article-number]-[short-title]-draft-[date].md`

Include a YAML header:

```yaml
---
article: [number]
title: [title]
series_position: [position in series, or "standalone"]
keyword_targets: [list]
date: YYYY-MM-DD
---
```

---

## GATE

Write to the process log:
- "Draft written to: [filepath]"
- "Word count: [approximate]"
- "Structural question answered: [yes/no — does every section advance the structural question?]"
- "Article movement achieved: [yes/no — does the draft move the reader in the direction described in the structural plan?]"
- "Frame persistence: [yes/no — does the opening frame remain present throughout, or does it disappear?]"
- "Necessity test: [yes/no — could any section be removed without breaking comprehension of later sections?]"
- "Voice profile fidelity: [assessment — where did it hold, where did it slip?]"

**LOG:** Record drafting decisions in compressed form — one line per decision or self-correction. Focus on: where the story diverged from the plan, where evidence didn't fit, where the voice slipped and was corrected. Do not restate the structural plan or describe what each section covers — that's in the article plan. The log records what happened during drafting that the plan didn't anticipate.

---

## STOP

Present to the user:
- The draft filepath
- A brief assessment: whether the article moves as a whole (structural question, movement, frame persistence) or has slipped into section-by-section arrangement
- Any sections where evidence didn't support the intended claim
- Any places where the voice slipped and was corrected during drafting
- The closing question — does it work?

Ask the user to read the draft. The user may want to:
- **Confirm** — proceed to editorial cycle
- **Redirect** — change approach, restructure (returns to Design or Comprehend)
- **Provide specific feedback** — incorporated into editorial cycle

Do not proceed until the user responds.
</phase_drafting>

---

## After This Phase

Update the article plan:
- Mark Phase 4 checkbox complete
- **Current phase:** Phase 5 (Editorial + Quality + Present)
- **Next phase file:** `references/phases/PHASE_5_EDITORIAL.md`

**Tell the user:** "The draft is saved. To continue with editorial revision, you can continue in this session or start a new one. Say 'Resume drafting Article [N]' to continue."

Sessions B and C may combine if context permits and the draft was not exceptionally long.
