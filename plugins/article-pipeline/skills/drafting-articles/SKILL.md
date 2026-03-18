---
name: drafting-articles
description: Drafts research-grounded long-form articles across multiple sessions. Reads a project manifest to find voice profile, writing standards, audience document, and research, then runs Setup, Comprehend, Design, Draft, and Editorial phases with process gates. Use when drafting, writing, resuming, or working on an article, or when the user says draft article, resume drafting, write article, draft standalone article, or references an article by number or title. Works for both series articles and standalone pieces.
---

# Drafting Articles

<purpose>
Claude's default when drafting long-form content is to load evidence and immediately plan
structure — producing competent prose organized by the plan rather than by the argument's
own logic. This skill counters that default through four mechanisms: a comprehension phase
(understand the evidence before finding the story), a design phase that produces metaprompts
(thinking orientations, not content descriptions), a mandatory process log (track reasoning
and self-corrections), and an iterative editorial cycle (revise structurally, not just
cosmetically).

The skill runs across multiple sessions because article drafting exceeds a single context
window. Loading research, reasoning through evidence, drafting, and revising all compete for
context. The session architecture ensures the critical instructions for each phase are fresh
when they matter — especially the voice profile and writing standards during drafting.

Voice profile and writing standards load in every phase — they inform connection-finding in
Comprehend, structural decisions in Design, and prose generation in Draft. The mandatory
session break before Draft ensures they reload fresh for generation, where context-window
position matters most. The voice profile's thinking patterns (how the author reasons) are
active from Setup onward; full first-person role adoption happens at Draft calibration.
</purpose>

## Critical Rules

**ARCHIVE EXCLUSION:** Never read, load, or reference any file from an `Archive/` directory. Archive directories contain deprecated documents. Loading archived material anchors the agent on previous output. This rule is absolute.

**SOURCING:** Every empirical claim must trace to a specific research document. Describe the finding and hyperlink to the source using URLs from the research base. Do not use academic author-name citation style.

**EPISTEMIC CALIBRATION:** The reader must always be able to tell whether they're receiving a sourced finding, an extension of sourced material, or the article's original analysis, from the language itself.

**GENRE:** The audience document defines register. Before writing each section, select the 2–3 findings that carry the structural argument — those get prose treatment. Everything else is available for hyperlinking only.

**PROFESSIONAL CHALLENGE:** If evidence doesn't support the outline's claims, if a section structure doesn't serve the story, or if the user's direction contradicts what the research supports — name the problem and propose an alternative. The outline is a plan, not a mandate.

**PROSE ADDRESS:** Do not assign the reader an identity or position. Present structural analysis; let the reader locate themselves. Do not self-reference the article or reference the project's internal process using internal vocabulary.

**ANTI-SYCOPHANCY:** Do not tell the user the draft is good. Present the draft and name its weaknesses. The user decides what works.

---

## Project Setup

This skill reads project-specific file locations from a **project manifest** (`project-manifest.md`). The manifest is produced by the designing-article-series skill, or can be created manually.

**What the manifest provides:**

| Component | What it provides |
|-----------|-----------------|
| **Voice profile** | Path to the voice profile — thinking patterns (Setup onward), role adoption (Draft) |
| **Writing standards** | Path to writing standards module — structural conventions (Design), craft rules (Draft) |
| **Audience document** | Path to audience document — who the reader is, register/genre conventions |
| **Research directory** | Path to research documents with source URLs |
| **Research index** | Path to evidence map organized by relevance (optional) |
| **Series map** | Path to series map with per-article thesis and argument arc (series articles only) |
| **Core thesis** | Path to thesis/framework document (optional) |
| **Drafts directory** | Where drafts and process logs are saved |
| **Context modules** | Organizational context (identity, ethical framework, content methodology) — loaded at Setup for accuracy (optional) |

**If no manifest exists:** The skill asks the user for the minimum: research files, voice profile path (or "none"), writing standards path (or "use default"), audience description, and output directory. The skill writes these to the article plan instead of reading from a manifest.

**Writing standards:** The manifest points to a local writing standards file (typically in `Context/`). The designing-article-series skill copies the selected baseline into the project during setup. If no manifest exists and the user wants a baseline, copy it from `references/baselines/` into the project directory.

---

## Quick Start

Tell the agent which article to work on — by number, title, or description. The agent will read the project manifest (or ask for setup details), determine the current phase, and begin or resume.

Example triggers:
- "Draft Article 3"
- "Let's work on the healthcare article"
- "Resume drafting where we left off"
- "Draft an article from this research"

---

## Interaction Model

**GATE** — a self-check. The agent writes a commitment statement to the process log before proceeding. Gates do not require user input.

**STOP** — a user interaction point. The agent presents its work and waits for the user to respond before proceeding. The agent never proceeds past a STOP without user input.

Every phase ends with a GATE followed by a STOP. Without stops, the agent runs all phases in a single pass, producing a draft built on unchecked assumptions.

---

## Session Architecture

The drafting process runs across multiple sessions. Each phase has a dedicated instruction file in `references/phases/`.

| Session | Phases | Instruction File | Description |
|---------|--------|------------------|-------------|
| A | Setup | [PHASE_1_SETUP.md](references/phases/PHASE_1_SETUP.md) | Read manifest, load materials, confirm |
| A | Comprehend | [PHASE_2_COMPREHEND.md](references/phases/PHASE_2_COMPREHEND.md) | Understand the evidence (STOP 1) |
| A | Design | [PHASE_3_DESIGN.md](references/phases/PHASE_3_DESIGN.md) | Find the story, build metaprompt plan (STOP 2) |
| B | Draft | [PHASE_4_DRAFT.md](references/phases/PHASE_4_DRAFT.md) | Load voice + standards LAST, write the article |
| C | Editorial + Quality + Present | [PHASE_5_EDITORIAL.md](references/phases/PHASE_5_EDITORIAL.md) | Revise, check, deliver |

**Before starting any phase:** Read the phase instruction file. It contains all procedures and gates for that phase.

### Session Groupings

| Session | Phases | Why Together |
|---------|--------|-------------|
| A | Setup + Comprehend + Design | Comprehend needs loaded research fresh; Design re-reads voice profile and writing standards before structural decisions. Two user STOPs: after Comprehend (validate reading), after Design (validate plan). |
| **MANDATORY BREAK** | | **Always start a new session before Session B** |
| B | Draft | Voice profile and writing standards must be fresh in context |
| C | Editorial + Quality + Present | All revision-focused, operating on the draft artifact |

**The boundary between A and B is mandatory** — the draft session needs a full context window for the voice profile's generative process gates to work.

---

## Starting a New Article

1. **Read the project manifest** (or ask the user for setup details).
2. **Read the Phase 1 instruction file:** [references/phases/PHASE_1_SETUP.md](references/phases/PHASE_1_SETUP.md)
3. **Begin Phase 1.**

## Resuming a Draft

If `Drafts/article-[N]-plan.md` exists:

1. **Read `article-[N]-plan.md`** — it tells you the current phase and what's done.
2. **Read the phase instruction file** for the current phase.
3. **If a phase checkbox is marked but the next phase hasn't started,** confirm with the user: "It looks like [phase] was completed. Ready to begin [next phase]?"
4. **Continue from where work left off.**

---

## The Process Log

A running document the agent writes throughout every phase, saved to `Drafts/article-[N]-process-log.md`. Started at the beginning of Phase 1, updated continuously.

**What goes in:** Reasoning, surprises, connections discovered, self-corrections, editorial notes, questions for the author.

**What it's for:** The log serves the agent's own process. During editorial revision, the agent rereads its log to see patterns in its own mistakes. The log is also a first-class output — presented to the author alongside the draft.

---

## Reference Files

| File | Purpose |
|------|---------|
| [references/ARCHITECTURE.md](references/ARCHITECTURE.md) | Evidence reasoning, voice generation, narrative construction |
| [references/phases/PHASE_1_SETUP.md](references/phases/PHASE_1_SETUP.md) | Setup instructions |
| [references/phases/PHASE_2_COMPREHEND.md](references/phases/PHASE_2_COMPREHEND.md) | Comprehend instructions |
| [references/phases/PHASE_3_DESIGN.md](references/phases/PHASE_3_DESIGN.md) | Design instructions |
| [references/phases/PHASE_4_DRAFT.md](references/phases/PHASE_4_DRAFT.md) | Draft instructions |
| [references/phases/PHASE_5_EDITORIAL.md](references/phases/PHASE_5_EDITORIAL.md) | Editorial + Quality + Present instructions |
| [templates/article-plan.md](templates/article-plan.md) | Article planning document template |

---

<failed_attempts>
## What DOESN'T Work

- **Not reloading voice profile and writing standards fresh at Draft time.** Voice and standards load in every phase — they inform connection-finding in Comprehend and structural decisions in Design. But by Draft time they've been in context for three phases and may be compacted. The mandatory session break before Draft exists so they reload fresh, as the LAST documents loaded before calibration. The Draft phase's loading gate enforces this order. If voice and standards loaded early in the Draft session and other documents followed, generation quality degrades.

- **Running all phases in one context window.** Context compaction silently degrades voice profile instructions, writing standards, and evidence curation rules. The draft reverts to default LLM prose. The session architecture exists to prevent this.

- **Feature-matching the voice profile instead of adopting the role.** The voice profile describes a person, not a style. The agent's default is to scan for features (short sentences, action verbs, dry humor) and reproduce them — which produces prose that performs style traits without inhabiting the person. The fix is not better feature-matching. It is understanding who the person is and writing as them. The gates are diagnostic tests that confirm the role is active, not checklists to execute.

- **Writing about the author instead of as the author.** When the voice profile describes the article's author, the agent's default is to write about them in third person, quoting them as a source. The calibration gate can capture correct analytical understanding ("Who is this person? A practitioner who...") while the agent never inhabits the role — it writes a journalist's profile piece instead of writing as the author. The fix is not editing third person into first person (that produces stitched voice). The fix is the `<role>` block in the article plan: a first-person identity assignment written during Design and encountered by the Draft session as a system-level instruction about who it *is*, not content about who it should *try to be*. The calibration gate verifies the role block is active, not constructs the role from scratch.

- **Constructing the role at Draft time instead of inheriting it.** When calibration asks the agent to build role understanding from scratch — "Who is this person? How do they think?" — the agent produces correct analytical comprehension but writes from its own default identity anyway. Understanding a role and inhabiting it are different. The fix: the Design phase writes a `<role>` block into the article plan as a first-person identity assignment. The Draft session encounters it as an instruction about who it is, not as content to process. Calibration then verifies the role is active rather than constructing it.

- **Dropping guardrails during role adoption.** When told to "write as this person," the agent fabricates narrative details (days of the week, settings, feelings) to make the voice feel lived-in. Restating the guardrail as a prohibition ("do not fabricate") doesn't fix this — prohibitions don't interrupt narrative generation. The fix is the per-section protocol's narrative inventory step: before writing, list the narrative details that exist in the research documents. That inventory is exhaustive. During generation, write from the inventory, not from imagination.

- **Treating editorial as text editing rather than voice-checked structural revision.** The editorial phase's default failure is to find surface-level issues (word swaps, link fixes, reference corrections) while leaving the voice and argument structure unexamined. Every editorial round must start with a voice fidelity check against the actual voice profile document — not against a memory of what the draft should sound like.

- **Treating the outline as a template to fill.** The draft must feel like someone thinking through the evidence. If a section feels like it's executing the outline rather than reasoning through the evidence, the drafting mode has slipped.

- **Drafting sections as adjacent containers rather than parts of a single structure.** The agent's default is to treat each section as a self-contained unit organized by topic. The fix is the structural plan from Design: per-section metaprompts with thinking orientations, closing handoffs, and key evidence references that connect sections into a single movement.

- **Producing generic structural plans instead of metaprompts.** The structural plan must give the drafting session enough orientation to write without re-deriving the story: per-section metaprompts (thinking stance, what to look for, what the reader should arrive at), key evidence references, and closing handoffs.

- **Delivering conclusions before the evidence earns them.** The thesis sentence from the outline is where the article *arrives*, not where it starts.

- **Skipping comprehension.** Loading documents and immediately planning sections produces an article organized by what was loaded, not by what it means.

- **Structure before Comprehend (premature structural commitment).** Finding the story before understanding the evidence locks in a structure that resists reframing when comprehension reveals something different. The story should emerge from understanding the evidence, not precede it. When detailed section structures were built before Comprehend, they created inertia — the agent treated them as commitments even when the evidence suggested a different story. The fix: Comprehend first (understand the evidence), then Design (find the story and build the plan).

- **Structural plans that become pre-drafts.** When the structural plan describes what the prose should contain — with paragraph-level detail about scenes, evidence deployment, and transitions — the drafting agent paraphrases the plan instead of writing from research. The fix: structural plans as metaprompts (thinking orientations that tell the agent what stance to take and what to look for, not what the prose contains). The agent still re-reads research, finds material, writes from it. The plan tells it how to think, not what to write.

- **Verbose plans and logs that consume Draft session context.** The plan and process log are loaded at Draft time alongside voice profile and writing standards. Every line in the plan and log competes with voice and standards for context attention — and voice and standards lose that competition silently. The discipline: plans contain metaprompts (thinking orientations), not pre-draft content. Logs contain reasoning and self-corrections, not restated source material. If a plan section reads like a summary of what the prose should say, it's pre-draft content. If a log entry restates what a research document contains, it's duplicated context. Both degrade Draft session quality by pushing voice and standards deeper into context.

- **Single-pass drafting.** The initial draft is never the best version. The editorial cycle is where the argument actually gets built.

- **Loading archived drafts.** Loading a previous draft anchors the agent on that draft's structure and phrasing. Draft from the research, the outline, and the voice profile — never from a previous draft.

- **Skipping voice and standards loading in cold-start sessions.** Sessions B and C start without voice or standards in memory. The agent's default is to jump to drafting or editing without loading them. The result: guardrails fire but have nothing to enforce against. The phase files enforce this through loading gates — do not skip them.

- **Skipping STOPs.** The agent's default is to execute all phases without stopping. This produces a draft built on unchecked assumptions. In autonomous execution environments, nothing forces a pause — the agent has momentum and continues.

- **Softening the evidence.** "Approximately," "many," "significant" soften specificity into generality. Use the actual numbers from the research.

- **Embedding all evidence instead of curating.** Select 2–3 findings per section that carry the structural argument. Hyperlink the rest. Curation is pacing.

- **Verbose process logs that consume context window.** The log records reasoning, decisions, and self-corrections — not summaries of source material. One sentence per document, one-line loading records, no duplication of plan content. Editorial rounds add to the log after the Draft session loads — their size doesn't affect Draft context, but they should still be compressed (table format, one row per finding) to stay useful.
</failed_attempts>
