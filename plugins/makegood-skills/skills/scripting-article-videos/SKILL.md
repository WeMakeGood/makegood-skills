---
name: scripting-article-videos
description: Creates short video scripts (primarily 1-minute shorts/reels) from article drafting artifacts. Mines comprehension findings, process logs, and article plans for research that was interesting but fell outside the article's structural argument — connections found, surprises, gaps flagged. Use when user says script a video, create video script, make a video from the article, write a short, or references video content for an article. Activates when article drafting artifacts exist (article plan, process log, draft) from the drafting-articles skill.
---

# Scripting Article Videos

<purpose>
Claude's default when asked to create a video from an article is to summarize the article —
compressing the argument into a shorter format. This skill exists because the videos are
supplemental, not derivative. They highlight research the article couldn't elaborate on:
connections found during comprehension, surprises in the evidence, gaps flagged in the process
log. The article already tells its story. The video tells an adjacent one.
</purpose>

## Critical Rules

**ARCHIVE EXCLUSION:** Never read, load, or reference any file from an `Archive/` directory.

**SOURCING:** Every claim in the script must trace to a specific research document from the article's research base. Before writing any claim, locate its source. If a claim can't be sourced, cut it.

**EPISTEMIC CALIBRATION:** The script's language must make clear whether the speaker is reporting a finding, extending it, or offering their own analysis. This is a spoken-language discipline — "the research found" vs. "what this suggests" vs. "here's what I think."

**PROFESSIONAL CHALLENGE:** If the proposed video topic doesn't have enough sourced material for a compelling script, or if the user's direction would produce a summary rather than supplemental content — name the problem and propose an alternative.

**SUPPLEMENTAL, NOT SUMMARY:** The video highlights material the article excluded or couldn't elaborate on. It does not summarize, recap, or condense the article. It can reference the article ("check out the full treatment at the link in the description") but must stand on its own as a distinct piece of content.

**WORD BUDGET:** ~150-180 words for a 1-minute target. Every word earns its place. Can go longer with user approval, but default to tight.

**VOICE PROFILE, NOT WRITING STANDARDS:** Load the voice profile for role adoption. Do NOT load the writing standards module — video has different conventions than longform prose. Use [references/VIDEO-CONVENTIONS.md](references/VIDEO-CONVENTIONS.md) instead.

---

## Project Setup

This skill reads the same **project manifest** (`project-manifest.md`) as the drafting-articles skill. It requires that an article has been drafted (or is in progress past Phase 2).

**What the skill reads from the manifest:**

| Component | What it provides |
|-----------|-----------------|
| **Voice profile** | Role adoption for on-camera delivery |
| **Audience document** | Who the viewer is, register |
| **Research directory** | Source documents for sourcing claims |
| **Series map** | Series context, article positioning (if series) |
| **Drafts directory** | Where to find article plan, process log, draft |

**What the skill reads from drafting artifacts:**

| Artifact | What to mine |
|----------|-------------|
| **Article plan** | Comprehension findings — connections, surprises, gaps, narrative elements |
| **Process log** | What didn't make the cut and why, self-corrections, editorial notes |
| **Article draft** | What the article DID cover (to avoid retreading) |
| **Role block** | Identity assignment from Design phase |

---

## Quick Start

Tell the agent which article's video to script — by number, title, or description. The agent reads the project manifest and article artifacts, mines for excluded material, and proposes video topic(s).

Example triggers:
- "Script a video for Article 3"
- "Create a short from the healthcare article"
- "What video could we make from the article we just drafted?"

---

## Interaction Model

**GATE** — a self-check. The agent writes a commitment statement before proceeding.

**STOP** — a user interaction point. The agent presents work and waits for the user to respond.

---

<phase_setup>
## Phase 1: Setup + Comprehend

### Step 1: Load Materials

1. Read the project manifest
2. Read the article plan (comprehension findings + structural plan)
3. Read the process log
4. Skim the article draft (for scope — what was covered)
5. Read the audience document
6. Read the series map (if series) for article positioning
7. Read [references/VIDEO-CONVENTIONS.md](references/VIDEO-CONVENTIONS.md)

### Step 2: Mine for Excluded Material

Work through the article plan's comprehension findings and the process log. Identify material that meets ALL three criteria:

1. **Interesting** — a genuine finding, connection, or surprise, not filler
2. **Excluded** — not covered in the article draft, or covered only in passing
3. **Sourceable** — traces to specific research documents

**Where to look:**

| Source | What to mine |
|--------|-------------|
| **Connections Found** (article plan) | Cross-document connections the article didn't develop |
| **Surprises** (article plan) | Findings that challenged assumptions but weren't central to the argument |
| **Gaps to Flag** (article plan) | Missing evidence that's interesting in its own right |
| **Process log** | Material cut during Design or Editorial — look for "cut because" or "outside scope" notes |
| **What the Evidence Doesn't Earn** (article plan) | Claims the outline proposed that research didn't fully support — the gap itself may be the story |

### Step 3: Propose Video Topic(s)

From the mined material, propose 1-3 video topics. For each:

- **The hook** — one sentence that would stop a scroll
- **The payoff** — what the viewer learns or reconsiders
- **Source material** — which research documents support it
- **Connection to the article** — how it relates without retreading

### GATE

Write:
- "Article artifacts loaded: [list]"
- "Excluded material identified: [count] candidates"
- "Topics proposed: [count]"

### STOP 1

Present the proposed topics to the user. For each topic, show the hook, the payoff, and the source material. Ask: "Which topic should we script? Or should we combine elements?"

Do not proceed until the user selects a topic.
</phase_setup>

---

<phase_script>
## Phase 2: Script

### Step 1: Load Voice Profile

1. Read the voice profile (full document) from the manifest path
2. Read the role block from the article plan
3. Adopt the role for on-camera delivery — same person as the article, more conversational register

**Voice calibration for video:** The person on camera is the same person who wrote the article, but they're talking to someone directly. Sentences are shorter. The register shifts toward how this person explains things in conversation — not how they write. Re-read the voice profile for conversational patterns, teaching mode, or direct address mode.

### Step 2: Evidence Inventory

Before writing, list the specific findings and details available from research documents for this topic. This inventory is exhaustive — it is the only material available for the script. No fabrication of examples, statistics, or anecdotes not in the research.

### Step 3: Write the Script

**Read [references/VIDEO-CONVENTIONS.md](references/VIDEO-CONVENTIONS.md) now** if not already fresh.

Write a teleprompter-ready script following these conventions:

**Format:**

```
# Video Script: [Title]
# Article: [Number] — [Article Title]
# Target: ~[N] words / ~[N] seconds
# Date: YYYY-MM-DD

---

[HOOK]

Script text here. Written exactly as the speaker will read it.
Each paragraph is a beat — a natural pause point.

                                        [B-ROLL: description of visual]

More script text. The speaker continues after the visual.

                                        [B-ROLL: description]

[CTA]

Check out the full article at the link in the description for
[what they'll find there — specific, not generic].

---

# Sources
- [Finding]: [research document name + URL]
```

**Script rules:**
- Write for the ear, not the eye — read it aloud mentally
- One idea per beat (paragraph)
- B-roll suggestions are margin notes for the editor, right-aligned
- The hook is the first 5-10 words the viewer hears — it must create a question or tension
- The CTA connects to the article without summarizing it — point to what's there, not what it says
- No section headers in the script body — this is continuous spoken delivery
- No timestamps or timing marks — actual read time determines pacing

### Step 4: Word Count Check

Count the words in the script body (excluding b-roll notes, metadata, and sources). If over 180 words for a 1-minute target, cut. If the material genuinely needs more time, note the overage and the user can approve a longer format.

### GATE

Write:
- "Voice profile loaded: [name]"
- "Evidence inventory: [count] items"
- "Script word count: [N] words"
- "Target length: [N] seconds"
- "All claims sourced: [yes/no — if no, list unsourced claims]"
</phase_script>

---

<phase_review>
## Phase 3: Review + Present

### Step 1: Self-Review

Check the script against these criteria:

| Check | Question |
|-------|----------|
| **Supplemental** | Does this tell a different story than the article, or summarize it? |
| **Sourced** | Can every empirical claim trace to a research document? |
| **Hooked** | Would the first line stop a scroll? |
| **Voiced** | Does this sound like the person talking, or like an essay read aloud? |
| **Tight** | Is every word earning its place? Could any sentence be cut without losing meaning? |
| **CTA** | Does the call-to-action point to what's in the article without summarizing? |

If any check fails, revise before presenting.

### Step 2: Present to User

Present the complete script with:
- The script itself (teleprompter-ready)
- Word count and estimated duration
- Source list
- Any weaknesses you see in the script
- B-roll suggestions context (what the editor would need to know)

**Ask:** "Ready to shoot, or should we adjust the script?"

### STOP 2

Wait for user feedback. Iterate as needed. The script is final when the user confirms.

### Output

Save the final script to the drafts directory: `Drafts/article-[N]-video-script-[date].md`
</phase_review>

---

<failed_attempts>
## What DOESN'T Work

- **Summarizing the article instead of highlighting excluded material.** The default impulse is to compress the article's argument into video format. The video must tell an adjacent story — something the article couldn't cover. If the script reads like a shorter version of the article, the mining step failed.

- **Writing in longform prose style instead of spoken/conversational.** Article prose reads differently than spoken delivery. Subordinate clauses, complex sentence structures, and evidence-dense paragraphs don't work on camera. The voice profile's conversational mode — not its analytical writing mode — leads the script.

- **Including too much.** One minute is ~150 words. A single finding, well-delivered, is stronger than three findings crammed together. The temptation is to pack in everything interesting from the mining step. The discipline is choosing ONE thread and serving it completely.

- **Loading writing standards.** The writing standards module governs longform prose conventions. Video has different rules — pacing, hook structure, spoken rhythm. Loading writing standards anchors the agent on prose conventions that don't serve video.

- **Fabricating research details not in the source documents.** The same guardrail from article drafting applies here: the evidence inventory step lists available material, and the script writes from that inventory only. The temptation is stronger in video because conversational delivery invites anecdotal detail — but the research is the research.

- **Generic CTAs.** "Check out the full article for more." (more what?) The CTA must point to something concrete the viewer will find in the article — a specific finding, framework, or analysis — without summarizing the article's argument.

- **Writing for the eye instead of the ear.** If you wouldn't say it in conversation, don't put it in the script. Semicolons, em dashes, and parentheticals don't exist in spoken delivery.
</failed_attempts>

---

## Reference Files

| File | Purpose |
|------|---------|
| [references/VIDEO-CONVENTIONS.md](references/VIDEO-CONVENTIONS.md) | Hook structure, pacing, CTA patterns for short-form video |
