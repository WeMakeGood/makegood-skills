---
name: generating-audience-profiles
description: Generates audience profile research artifacts as upstream input for building-context-libraries. Produces a matrix of audience dimensions and activatable sub-profile metaprompts from mixed source sets (competitive/sector research, internal strategy documents, occasional direct audience research, LLM-modeled audience knowledge). Profiles are decision-frame modules that shape agent behavior when an audience dimension is active, not character sketches. Use when user says generate audience profiles, build audience matrix, design audience modules, research audiences, develop audience definitions for a context library, or create audience research artifacts. Activates when research documents, strategy materials, or peer organization dossiers are provided via file path or directory, even when accompanied by additional context files.
---

# Generating Audience Profiles

<purpose>
Marketing and communications agencies build audience definitions by boxing the audience into
a specific human shape — "Mary, 34, two children, Instagram every night." That shape helps a
human marketer imagine the audience. It actively hurts an LLM. The model anchors on the
specific data points ("Mary," "Instagram," "two children") as locked context, generalizes
them into procedural rules, and loses the organization's actual decision question: how should
this output shift when this audience is what we're addressing?

This skill exists because LLM-useful audience context is structurally different. It is a
matrix of audience dimensions plus activatable sub-profile metaprompts — decision-frame
modules that shape how the agent generates when a dimension is active. The matrix shape
allows RAG-style loading of only the dimensions relevant to the current session, instead of
ambient persona context that distorts every output.

The skill produces a research synthesis artifact. It is upstream of building-context-libraries:
its output becomes a source document the library build then consumes, alongside the
organization's other research, to design audience-aware agents. The output is structured for
that downstream use — the matrix and modules are organized so library design can pick them up
without re-comprehending.

Audience profile design also runs across multiple sessions because the failure mode is the
same one building-context-libraries documented: synthesis on saturated source context
collapses into sector-applicable generalities rather than organization-specific patterns. The
session architecture mirrors that skill deliberately.
</purpose>

## Core Concept

**You are producing source material for an agent, not a description for a human.**

The matrix names the audience dimensions that carry decision weight for this organization. Each cell that warrants substance becomes a sub-profile module — a metaprompt the runtime agent loads when that dimension is active. The sub-profile says how to generate, decide, or prioritize when addressing this audience cut. It does not describe a person.

| Level | What It Is | Test |
|-------|-----------|------|
| **Persona** (wrong) | Named individual with biographical detail | Reader can imagine the person; agent generalizes the details into rules |
| **Description** (insufficient) | Demographic + psychographic + behavioral summary | Agent reads it and continues generating the way it would have anyway |
| **Decision-frame module** (target) | What carries weight, what loses them, what to prioritize when generating | Agent's output measurably shifts when the module is loaded |

**The downstream library agent's perspective is the writing frame.** A sub-profile module is read by an agent that has its loaded context modules (F0, S0, organizational identity, etc.), the audience module that was triggered for the current session, and the user's task. The module exists to shift that agent's generation. Sentences that only make sense to someone reading the audience research as research — methodology notes, source debates, comparative reasoning across cells — belong in the process log and the matrix-level documentation, not inside a sub-profile module.

**The matrix is navigation; the modules are substance.** A reader of the matrix can see the shape of the audience space and know which cells have substance and which are intentionally empty. A reader of a single module gets the decision frames for that cell, nothing more.

See [references/ARCHITECTURE.md](references/ARCHITECTURE.md) for the full design philosophy, the source classes, the dimension selection logic, the matrix structure, sub-profile shape, the downstream handoff to building-context-libraries, and what "modeled-data as a source class" requires under F0.

---

## Critical Rules

**ANALYTICAL POSTURE:** The skill produces audience definitions, not source extracts. The source set is evidence — it does not, by itself, name the audiences the organization needs to engage. Phase 1 produces an audience-needs assessment with two layers: a framing layer (purpose and operating environment — depth and source citations appropriate) and a candidates layer (the audience cuts themselves — compressed, uncited, sketch-depth). Pass 1 grounds the candidates in source content. Pass 2 refines. Phase 3 commits the final audience set the matrix will organize. The committed audience set is the analytical product, not the source-named set. The value-add is challenging the audience definitions the organization started with — including surfacing audiences the explicit framing didn't name and disaggregating cuts the framing collapsed.

**SOURCING:** Every claim in a sub-profile module must trace to a source. Sources come in four classes — see ARCHITECTURE.md — and each requires a different citation form. Direct research cites the document. Competitive/sector research cites the dossier and what was extracted. Internal strategy documents cite the document and the inferential step. LLM-modeled audience knowledge is a source class governed by F0: name what the model is drawing on, prefer linkable references when the model can identify them, and treat any modeled claim as a hypothesis to be tested against the other source classes before it appears in a module. If a claim cannot be sourced, name the gap — do not fill it.

**SOURCE-INDEX HYGIENE:** The source-index produced in Phase 1 captures source identity (path, class, vintage, structural identity) — not what each source says about audiences. The structural-claim discipline is enforced by allowed/disallowed verb patterns documented in PHASE_1_SETUP.md Step 3: "Peer-org dossier following the standard format" is allowed; "Documents [specific audience segment] as unclaimed white space" is not, because the latter could only be written by someone who has read the source for substance. A full read of each source is required for accurate classification — but the entry text stays structural. Audience-content claims live in Pass 1 per-source notes. The Phase 1 GATE explicitly scans every entry for content-extraction smuggled in as structural description; the Pass 1 Step 0 GATE prevents per-source notes from being written before every source has been read into context.

**EPISTEMIC CALIBRATION:** A reader of any module must be able to tell from the language alone whether each statement is drawn directly from sources, inferred from cross-source patterns, or your synthesis. Sourced claims read as direct statement. Inferences read with inferential language. Modeled-data contributions read with their own signal ("Trained-data picture suggests X; client sources confirm/refute/refine: Y"). Markers are scaffolding for the build process; remove them before the artifact ships, but only if the natural language alone carries the signal.

**RUNTIME FRAME:** Every sub-profile module is written for the runtime library agent — an agent with no access to your sources, your process log, or the rest of the matrix. Before writing any module, commit to the runtime frame. Sentences that reference "the research showed" or "compared to the other cells" are build-perspective contamination. The module says what the runtime agent should do when this dimension is active. It does not narrate how you decided.

**MATRIX BEFORE MODULES:** The dimensions that organize the matrix carry the most consequential design decision. Wrong dimensions produce profiles that look correct but don't shift agent behavior because they aren't cutting the audience space along lines that actually matter for this organization. The Design phase commits to dimensions before any module is written. If module-writing reveals the dimensions are wrong, fix the dimensions — do not paper over the problem in the prose.

**SUGGESTED DEFAULTS ARE NOT COMMITMENTS:** The skill ships with starter dimension pairs the user can adopt or replace. The default is offered to accelerate Phase 3; it does not pre-empt source-driven derivation. If sources point to different dimensions, name that and propose the source-driven set.

**MODELED-DATA IS A FIRST-CLASS BUT TESTED SOURCE:** Direct audience research is increasingly scarce. LLM-modeled audience knowledge is a permitted input under F0, with these requirements: (1) surface the modeled picture explicitly before drawing on it, (2) name what the model is drawing on and link to references where the model can identify them, (3) test the modeled picture against client and competitive sources, marking what's confirmed, refuted, or refined, (4) the module draws from the tested picture, not the raw modeled one. Modeled-data that hasn't been tested against other sources stays in the process log, not in a module.

**PROFESSIONAL CHALLENGE:** When a user proposes dimensions that the sources don't support, when a requested profile would lock the agent on biographical detail rather than decision frames, or when the matrix is being expanded into cells the sources can't ground — cite the concern, offer an alternative. The skill's job is to produce profiles that work as agent context, not profiles that match a familiar persona shape.

**TWO-PASS COMPREHENSION:** Phase 2 has two passes with a mandatory session break between them. Pass 1 is recognition with sources loaded — per-source notes, signal log, expectations-vs-findings, conflicts. Pass 2 is synthesis with sources mostly out of context — dimension candidates, cross-source patterns, modeled-data tests, agent-needs. The break is what allows synthesis to do the lateral work that distinguishes organization-specific dimensions from sector-applicable generalities.

**MATRIX EMPTINESS IS A SIGNAL, NOT A GAP:** Cells that lack source coverage stay empty. Empty cells tell the downstream library agent — and the user — that this dimension intersection isn't substantively covered by current research. Filling empty cells with thin content makes the matrix less useful, not more. The matrix is honest about what's known.

---

## Reference Files

Read the phase instruction file before each phase. Re-read after any context compaction.

| File | Purpose |
|------|---------|
| [references/ARCHITECTURE.md](references/ARCHITECTURE.md) | Runtime perspective, source classes (including modeled-data), suggested-default dimension pairs, matrix shape, sub-profile module shape, downstream handoff to building-context-libraries |
| [references/phases/PHASE_1_SETUP.md](references/phases/PHASE_1_SETUP.md) | Load sources, classify by source class, identify the client's audience question, write initial expectations |
| [references/phases/PHASE_2_COMPREHEND.md](references/phases/PHASE_2_COMPREHEND.md) | Pass 1 (recognition) and Pass 2 (synthesis); modeled-data picture surfacing and testing |
| [references/phases/PHASE_3_DESIGN.md](references/phases/PHASE_3_DESIGN.md) | Dimension selection, matrix construction, cell prioritization |
| [references/phases/PHASE_4_BUILD.md](references/phases/PHASE_4_BUILD.md) | Sub-profile module writing with per-module gates |
| [templates/](templates/) | Build-state, process-log, source-index, matrix, sub-profile module, suggested-default dimensions |

---

## Build Process

4 phases across 3 sessions. Phase 2 (Comprehend) splits internally into two passes with a mandatory session break between them.

| Phase | Name | Instruction File | Function |
|-------|------|------------------|----------|
| 1 | Setup | [PHASE_1_SETUP.md](references/phases/PHASE_1_SETUP.md) | Confirm audience question, inventory and classify sources, produce audience-needs assessment (analytical, from organizational context), write initial expectations against the assessment. Ends with a STOP — user confirms before Phase 2. |
| 2 | Comprehend (two passes) | [PHASE_2_COMPREHEND.md](references/phases/PHASE_2_COMPREHEND.md) | Pass 1: read all sources (Step 0 gate), write recognition artifacts, test audience-needs assessment against sources. Ends with STOP — user reviews recognition. Pass 2: surface and test modeled-data picture, synthesize dimension candidates and cross-source patterns. |
| 3 | Design | [PHASE_3_DESIGN.md](references/phases/PHASE_3_DESIGN.md) | Commit to dimensions, construct matrix, prioritize cells, propose ownership for the downstream library |
| 4 | Build | [PHASE_4_BUILD.md](references/phases/PHASE_4_BUILD.md) | Write sub-profile modules with per-module gates; finalize matrix document |

### Session Architecture

| Session | Phases | Why Together |
|---------|--------|-------------|
| A | Setup + Comprehend Pass 1 (Recognition) | Recognition needs source documents fresh in context |
| **MANDATORY BREAK** | | Synthesis needs sources mostly out of context, recognition artifacts loaded |
| B | Comprehend Pass 2 (Synthesis) + Design | Synthesis feeds directly into dimension selection and matrix structure; both need cognitive room sources would consume |
| **MANDATORY BREAK** | | Build needs the per-module protocol fresh, not buried under dimension reasoning |
| C | Build | Each sub-profile module is self-contained — resume from `build-state.md`; per-module protocol re-reads relevant sources targetedly |

**Both breaks are mandatory.** Single-pass synthesis on a saturated source context collapses toward sector-applicable rather than organization-specific dimensions. Build session resets keep the per-module gates fresh; building all modules in the same session as Design produces modules that paraphrase the matrix instead of standing as runtime agent context.

---

<phase_start>
## Starting a New Build

1. **Ask the user:**
   - "Where are your source documents?" → `SOURCE_PATH`
   - "Where should I create the audience profile artifact?" (default: `./audience-profiles/`) → `OUTPUT_PATH`
   - "What's the organization's audience question — what would they be using these profiles to decide?" (used to scope dimension selection)
   - "Is there an existing context library this will feed into, or is one being built?" (informs handoff format)

2. **Read the Phase 1 instruction file:** [references/phases/PHASE_1_SETUP.md](references/phases/PHASE_1_SETUP.md)

3. **Begin Phase 1.**
</phase_start>

---

<phase_resume>
## Resuming a Build

If `<OUTPUT_PATH>/build-state.md` exists:

1. **Read `build-state.md`** — it names the current phase, what's done, and what's next.
2. **Read the phase instruction file** it points to.
3. **Continue from where work left off.**

If `build-state.md` does not exist but `source-index.md` does:

1. **Read `source-index.md`** — check its status field and reading checklist.
2. **Determine the current phase** from the index status.
3. **Create `build-state.md`** to track progress going forward.
</phase_resume>

---

## The Process Log

A running document the agent writes throughout every phase, saved to `<OUTPUT_PATH>/process-log.md`. Started at the beginning of Phase 1, updated continuously.

**What goes in:** Dimension candidates considered and rejected; modeled-data picture and how it was tested; conflicts between sources; convergences across sources; cells that lack coverage and why they stay empty; reasoning the runtime modules deliberately omit.

**What it's for:** The process log is part of the deliverable. The downstream library agent reads the matrix and modules to design library structure; the user reads the process log to understand how the matrix was derived, including what was considered and rejected. The log makes the artifact auditable. It is not draft prose for the modules — it is the build agent's reasoning, preserved separately.

---

## Output Requirements

**ALWAYS save artifacts to files in `<OUTPUT_PATH>`. Do not output the matrix or modules inline in chat.**

The deliverable is a directory containing:

```
<OUTPUT_PATH>/
├── audience-matrix.md              # Top-level matrix with dimensions, cells, status
├── modules/                        # One sub-profile module per substantive cell
│   ├── [dimension-coordinate].md
│   └── ...
├── source-index.md                 # Source inventory by class (Phase 1 output — structural scope only)
├── audience-needs-assessment.md    # Phase 1 analytical output: purpose, environment, audience candidates
├── initial-expectations.md         # Phase 1 predictions against the audience-needs assessment
├── process-log.md                  # Build agent reasoning across all phases
├── build-state.md                  # Session resume state
└── comprehension-artifacts/        # Pass 1 per-source notes (audience content lives here, not in source-index)
    └── ...
```

After each phase, confirm the artifacts created or updated: "Phase [N] complete. Artifacts: [list]."

---

<failed_attempts>
## What DOESN'T Work

- **Extractive posture instead of analytical posture.** The agent reads the audience question as "what audiences should I extract from these sources?" and builds expectations around audiences the sources or the question explicitly name. This collapses the skill's value-add — Make Good's job is to challenge audience definitions, not amplify them. The fix is the Phase 1 audience-needs assessment: an analytical commitment to *which audiences the organization needs to engage to accomplish its purpose*, derived from the audience question + library handoff + source-set structure as signals about the organization's context, NOT from source content. Pass 1 then tests the assessment against sources.

- **Source-index entries written from titles, format specs, or pre-read inference.** The agent skims directory structure and top-level reference docs, then fills "audience-relevant content" fields with confident-sounding speculation about what each unread source likely says. Pass 1 then starts contaminated — its expectations and per-source notes echo the Phase 1 priors rather than reading sources fresh. The fix has two parts: (1) Step 3 requires reading each source fully before writing its entry (which is what produces good classification), and (2) the "Audience-relevance scope" field is governed by an explicit structural-claim discipline (allowed/disallowed verb patterns) that catches content extraction smuggled in as structural description. "Peer-org dossier following the standard format" is allowed; "Documents [specific audience segment] as unclaimed white space" is not.

- **Source-index entries that describe what a source says, even after a full read.** Once a source is read for classification, the content is in working memory. The path of least resistance is to write "Documents X" or "Names Y" or "Maps Z" — verbs that look structural but encode content claims that could only be made after reading for substance. The Phase 1 GATE explicitly scans every entry for this pattern and requires flagged entries to be rewritten before STOP. The audience-content claims belong in Pass 1 per-source notes; the source-index stays at structural identity.

- **Audience-needs assessment over-grounded in source content.** Even when the source-index discipline holds, the assessment itself can pre-empt Pass 1 by citing specific statistics, named events, peer-org revenue figures, or specific historical examples drawn from the source set. This collapses the candidates layer into a draft sub-profile module rather than a sketch. Pass 1 then anchors on the rich assessment rather than reading sources fresh. The fix: a two-layer assessment structure where the framing layer (purpose and operating environment) is depth-OK and citation-OK, but the candidates layer (sections C and D) is compressed and uncited. Candidates are 1–2 sentences per field. Source-specific evidence enters in Pass 1.

- **Persona-shaped output.** "Mary, 34, two children, uses Instagram nightly" is exactly the failure mode this skill exists to prevent. A persona anchors the agent on biographical specifics it then generalizes into rules. The fix is not "make the persona more accurate"; it is to abandon the persona shape entirely. Output is decision frames, not character sketches.

- **Dimensions imported from default starter pairs without source check.** The suggested-default dimensions are starter scaffolding for Phase 3. When they are adopted without checking whether the sources actually organize audience reality along those cuts for *this* client, the matrix produces profiles that look correct and don't shift agent behavior. The Phase 3 gate exists to surface this: the default is offered; the source-driven dimensions are what get committed to.

- **Modeled-data treated as ambient knowledge.** When the agent draws on the model's trained-data picture of an audience without naming it as a source class, two failures follow: F0 sourcing discipline is violated silently, and the modeled picture goes untested against client/competitive sources. The fix is the Phase 2 Pass 2 protocol: surface the modeled picture explicitly, name what the model is drawing on, then test it against the other source classes. Modeled-data is a source class with its own discipline — not a background ingredient.

- **Filling every matrix cell.** When the matrix is treated as a grid to populate, the build agent generates thin content for cells the sources don't cover, and the thin content looks the same as the substantive content. The matrix loses its diagnostic value. The fix is the empty-cell discipline: cells without source coverage stay empty, and the matrix-level documentation says so.

- **Modules that narrate the research.** "Our research across peer organizations and the client's strategy documents suggests this audience values…" The runtime agent has no access to "our research." The module exists to shift the runtime agent's generation, not to summarize how the build agent decided. Build-perspective contamination phrases get caught at the Phase 4 runtime-frame check.

- **Sector-applicable generalities.** When synthesis runs on a saturated source context, the dimensions that surface are the dimensions any agency would name for any client in this sector. The two-pass comprehension structure exists to prevent this. Pass 2's structural advantage is sources mostly out of context, recognition artifacts loaded — that's where the organization-specific cuts become visible. Skipping the session break collapses the architecture.

- **Treating the artifact as standalone deliverable.** The output of this skill is upstream input for building-context-libraries. When the artifact is treated as a finished marketing deliverable, the prose drifts toward client presentation rather than agent context. The Phase 4 runtime-frame gate keeps the writing oriented toward the downstream library agent's perspective.

- **Skipping the process log.** Without the log, the matrix is unauditable — the user cannot see what was considered and rejected, what conflicts surfaced, what the modeled picture contributed. The log is not optional documentation; it is part of the deliverable, and the downstream library design depends on it.

- **Running all phases in one session.** Context compaction silently degrades the runtime-frame instructions and the modeled-data discipline. By the time module-writing happens, the build agent has reverted to persona-shaped output because the instructions governing transformation are gone. The mandatory session breaks exist for the same reason building-context-libraries documented: lateral cognitive work and per-module gates need fresh context.

- **Locking dimensions before Comprehend.** When the user names the dimensions they want in Phase 1 and the skill commits to them before sources have been read, the comprehension phase becomes confirmation-seeking rather than dimension-finding. Suggested defaults are starters; user preferences are inputs; sources are what decide.
</failed_attempts>
