---
name: building-context-libraries
description: Builds modular context libraries that change how AI agents behave with organizational knowledge. Transforms source documents (transcripts, strategy docs, process documents, interviews) into metaprompt modules — system prompt components that shape agent decision-making. Use when user says build context library, create context library, create agent context, build knowledge base, transform documents into agent context, build domain context, or create organizational context modules. Activates when organizational source documents are provided via file path or directory.
---

# Building Context Libraries

<purpose>
Claude defaults to copying content from sources — restating facts in cleaned-up form feels
productive but produces modules useless as agent context. This skill exists because context
libraries must contain metaprompting (instructions that change how agents behave), not content
(facts agents can parrot back). The skill enforces transformation at every phase through
commitment gates that require demonstrating behavioral change before any module is written.
</purpose>

## Core Concept

**You are creating system prompt components for LLM agents, not documentation for humans.**

Modules are metaprompts. They change how agents *behave* — what they decide, how they respond, what they prioritize. A module that an agent could ignore without changing its behavior is a failed module.

| Level | What It Is | Test |
|-------|-----------|------|
| **Content** (wrong) | Facts copied from sources | Agent behavior unchanged if removed |
| **Context** (minimum) | Processed knowledge shaping decisions | Agent makes different choices with it loaded |
| **Metaprompting** (target) | Behavioral instructions with decision logic | Agent acts on it without interpretation |

**The runtime agent's perspective is the writing frame.** A module is read by an agent that has its loaded modules and a user message — nothing else. No source files, no build documents, no awareness of how the module came to exist. Sentences that only make sense to someone who knows about the build are contamination, not context. See [references/ARCHITECTURE.md](references/ARCHITECTURE.md), "The Runtime Agent's Perspective."

**Planning precedes writing.** The Build phase's per-module protocol commits to a Substantive Source Surface (what specifically from the just-read sources will appear) and a Section Plan (shape, owned-content use-shape, extracted reasoning from quotes/names) *before* prose is generated. Drift between plan and prose means the plan was wrong; redo the plan, do not edit the prose.

See [references/ARCHITECTURE.md](references/ARCHITECTURE.md) for the full module design philosophy, runtime perspective, single source of truth and use-shapes, shape reference (F0 as worked example), content transformation rules, and token management.

---

## Critical Rules

**RUNTIME PERSPECTIVE:** Every module is read by a runtime agent that has only its loaded modules and the user's input. No sources, no build documents, no proposal, no library. Before writing any module section, the build agent commits to the runtime frame (Phase 4, Step 1). Sentences that only make sense inside the build — "the source set," "the library doesn't carry," "in some 2025-era sources," named source files — are contamination. The contamination test is not whether specific phrases appear; it is whether the sentence makes sense to a reader who knows nothing about how the module came to exist.

**PLANNING PRECEDES PROSE:** The Build phase's per-module protocol has 7 steps. Steps 4 (Substantive Source Surface) and 5 (Section Plan) are planning artifacts the build agent commits to *before* generating prose. The plan names section shape, owned-content use-shape (from the proposal's Ownership and Use-Shape table), source patterns, and extracted reasoning from any quote or named individual. Writing executes the plan. When prose drifts from the plan, the failure-recovery protocol (Phase 4, "When a Module Fails") fixes the upstream planning step — it does not regenerate prose from scratch.

**TWO-PASS COMPREHENSION:** Phase 2 has two passes with a mandatory session break between them. Pass 1 is recognition — sources loaded, observational artifacts (per-source notes, signal log, expectations-vs-findings, conflicts) written at the moment of reading. Pass 2 is synthesis — sources mostly out of context, recognition artifacts loaded, pattern-pointers and convergences and cross-domain parallels and agent-needs generated with cognitive room to do the lateral work. Single-pass synthesis on a saturated source context produces sector-applicable rather than organization-specific patterns; the two-pass structure prevents this. The session break is what makes Pass 2's structural advantage real.

**SOURCING:** Every fact in the library must trace to a source document. Before stating any claim about the organization, locate its source. If you cannot locate a source, state what's missing rather than approximating. NEVER invent details. NEVER fill gaps.

**SUBSTANCE OVER SHORTHAND:** Modules capture what the just-read sources reveal, not what comprehension findings or process-log entries summarized. The Substantive Source Surface (Phase 4, Step 4) requires patterns to come from the source files re-read in the same turn — not from earlier summaries. Comprehension shorthand crowding out source substance is a recurring failure mode; the surface is where it gets caught.

**EPISTEMIC CALIBRATION:** The reader should always be able to tell whether a claim is sourced from documents, inferred from cross-document patterns, or your analytical interpretation — because your language makes the distinction clear. Sourced claims read as direct statement. Inferences read with inferential language ("the sources suggest," "this pattern indicates," "across documents X and Y, the organization appears to"). Analytical synthesis reads as the build agent's reasoning ("on the basis of these patterns, the module captures"). The language carries the signal; markers are scaffolding. Use `[PROPOSED]` only when natural language alone won't carry enough signal during the build — and remove before delivery.

**PROFESSIONAL CHALLENGE:** When a user's proposed module structure contradicts what the sources support, when an approach has known pitfalls (taxonomy-based modules, content-copying, over-compression), or when assumptions aren't grounded in sources — cite the concern, offer an alternative.

**TRANSFORM, DON'T TRANSCRIBE:** Before writing any module section, identify the organizational reasoning it provides and whether an agent could apply it to situations the author didn't anticipate. Modules provide reasoning context — how the organization thinks — not procedures or exhaustive rules. Prescriptive "If X, do Y" rules are rare, reserved for genuine constraints where violation causes real harm.

**SINGLE SOURCE OF TRUTH IS A USE-SHAPE COMMITMENT:** Naming an owner is necessary but not sufficient. The proposal's Ownership and Use-Shape table commits every using module to one of four shapes — cross-reference, subset, invocation by name, or reach-beyond. Restatement is not one of the shapes. Build executes the table; it does not redecide it at write-time.

**LOAD DISCIPLINE IS A CLASSIFICATION:** Every loadable item in an agent's manifest is classified as `always_load` (governs every output that agent produces — agent's runtime judgment about whether to load it is unreliable) or `conditional` (applies only in specific task or audience contexts, with a `load_when:` trigger written in plain language). The classification is per-agent — the same module may be `always_load` for one agent and `conditional` for another. Container (module vs. addendum) and load discipline are independent dimensions: a reference addendum can be `always_load`, a shared module can be `conditional`. The classification is decided in Design (Phase 3 Load-Discipline Classification table), not at agent-write time. **F0_agent_behavioral_standards is `always_load` whenever it appears. S0_natural_prose_standards is `always_load` whenever it appears.** Both are hard rules — not judgment calls — enforced at the Phase 3 GATE, the Phase 4 self-check, and the validation script.

**QUOTES AND NAMED INDIVIDUALS DO NOT APPEAR IN MODULES:** When a source quote or named individual informs a section, the Section Plan extracts the reasoning before prose is written. The quote is evidence of the reasoning; the reasoning is what appears in the module. Quote-extraction and name-removal happen during planning, not as post-hoc edits.

**CONVERGENCE AWARENESS:** When source documents describe the same underlying pattern differently, the convergence reveals something about the organization that neither document says alone. Explore intersections rather than filing information into the first plausible module.

**CONFLICT RESOLUTION:** When source documents contradict, surface the conflict to the user. Do not silently pick one version.

**REDO SESSIONS HAVE A SEPARATE PROTOCOL:** When a previous Build attempt was rolled back, the redo-session protocol (Phase 4) physically separates retrospective documents and prior-attempt artifacts from the working set. The build agent regenerates from the proposal and sources, not from retrospective examples. The user provides a list of named failure patterns to avoid; the names go in build-state, the documents do not enter context.

---

## Reference Files

Read the phase instruction file before each phase. Re-read after any context compaction.

| File | Purpose |
|------|---------|
| [references/ARCHITECTURE.md](references/ARCHITECTURE.md) | Runtime agent's perspective, module design, single source of truth and the four use-shapes, load discipline (always_load vs. conditional, F0/S0 hard rule, trigger discipline), F0 as a worked shape reference, content transformation, token management, stakes classification |
| [references/TEMPLATES.md](references/TEMPLATES.md) | Templates for build-state, process-log, source-index, modules by tier, agent definition (with always_load/conditional manifest), addendum, proposal with Ownership and Use-Shape and Load-Discipline Classification tables |
| [references/COMPREHENSION_TEMPLATES.md](references/COMPREHENSION_TEMPLATES.md) | Templates for Phase 2's eight comprehension artifacts (per-source notes, signal log, expectations-vs-findings, conflicts, pattern-pointers, convergences, cross-domain parallels, agent-needs) |
| Phase files in [references/phases/](references/phases/) | Self-contained instructions per phase, including [PHASE_M_MIGRATION.md](references/phases/PHASE_M_MIGRATION.md) for migrating libraries between skill versions |

---

## Build Process

4 phases across 3 sessions. Phase 2 (Comprehend) is internally split into two passes (recognition and synthesis) with a mandatory session break between them.

| Phase | Name | Instruction File | Function |
|-------|------|------------------|----------|
| 1 | Setup | [PHASE_1_SETUP.md](references/phases/PHASE_1_SETUP.md) | Load sources, create manifest, classify, identify agent needs and initial expectations |
| 2 | Comprehend (two passes) | [PHASE_2_COMPREHEND.md](references/phases/PHASE_2_COMPREHEND.md) | Pass 1: read all sources, write recognition artifacts (per-source notes, signal log, expectations-vs-findings, conflicts). Pass 2: synthesize with sources mostly out of context (pattern-pointers, convergences, cross-domain parallels, agent-needs). |
| 3 | Design | [PHASE_3_DESIGN.md](references/phases/PHASE_3_DESIGN.md) | Propose module architecture, agent definitions, ownership and use-shape assignments |
| 4 | Build | [PHASE_4_BUILD.md](references/phases/PHASE_4_BUILD.md) | Write modules with per-module gates, build addenda, validate |

### Session Architecture

| Session | Phases | Why Together |
|---------|--------|-------------|
| A | Setup + Comprehend Pass 1 (Recognition) | Recognition needs source documents fresh in context |
| **MANDATORY BREAK** | | Synthesis needs sources mostly out of context, recognition artifacts loaded |
| B | Comprehend Pass 2 (Synthesis) + Design | Synthesis feeds directly into module structure decisions; both need cognitive room sources would consume |
| **MANDATORY BREAK** | | Build needs the per-module protocol fresh, not buried under structural reasoning |
| C | Build | Each module is self-contained — resume from `build-state.md`; per-module protocol re-reads relevant sources targetedly |

**Both breaks are mandatory.** The Pass 1/Pass 2 break is what allows synthesis to do the lateral cognitive work F0's Analytical Depth Requirements ask for — moves that are difficult or impossible from inside saturated source context. The Pass 2/Design break (formerly the only mandatory break) keeps the metaprompt transformation rules fresh during structural reasoning.

Build may extend into Session D if the library is large. Each module is self-contained.

---

<phase_start>
## Starting a New Build

1. **Ask the user:**
   - "Where are your source documents?" → `SOURCE_PATH`
   - "Where should I create the context library?" (default: `./context-library/`) → `OUTPUT_PATH`
   - "What domain agents will use this library?" (optional — can be derived in Comprehend)

2. **Read the Phase 1 instruction file:** [references/phases/PHASE_1_SETUP.md](references/phases/PHASE_1_SETUP.md)

3. **Begin Phase 1.**
</phase_start>

---

<phase_resume>
## Resuming a Build

If `<OUTPUT_PATH>/build-state.md` exists:

1. **Read `build-state.md`** — it tells you the current phase, what's done, and what's next.
2. **Read the phase instruction file** it points to.
3. **Continue from where work left off.**

If `build-state.md` does not exist but `source-index.md` does:

1. **Read `source-index.md`** — check its status field and reading checklist.
2. **Determine the current phase** from the index status.
3. **Create `build-state.md`** to track progress going forward.
</phase_resume>

---

<failed_attempts>
## What DOESN'T Work

The patterns below produced failed builds in production. Each entry names what was tried, why it failed, and where the architectural prevention now lives.

**Architectural failures the protocol now prevents structurally:**

- **Build-perspective contamination in modules:** The build agent has source files, the proposal, and the build process in working context, and slips that perspective into module text — "the source set," "the library doesn't carry," "in some 2025-era sources," named source-file paths. The runtime agent has none of those referents. *Now prevented by:* the Runtime Frame Set commitment (Phase 4, Step 1) before any other writing work; explicit contamination phrases listed in ARCHITECTURE.md and the module template's BUILD REMINDERS; runtime-frame checks 5–6 in the per-module self-check.

- **Single-source-of-truth drift across modules:** Naming an owner without specifying use-shape leaves the build agent to decide at write-time how a using module incorporates owned content — and the path of least resistance is to restate. *Now prevented by:* the proposal's Ownership and Use-Shape table commits every using module to one of four shapes (cross-reference, subset, invocation, reach-beyond); restatement is not a shape; the Section Plan applies the shape from the table before prose is generated.

- **Quote and named-individual contamination:** Source quotes get imported with attribution; named individuals from sources appear in modules as carriers of organizational reasoning. The path of least resistance after re-reading sources is to import the content. *Now prevented by:* Section Plan's mandatory quote/individual handling — extract the reasoning in the plan before generating prose; the plan does not contain the quote-as-text-to-include or the name-as-person-to-attribute. Quote-extraction is the default path because the plan forces it before prose.

- **Metaprompt-vs-prose drift:** Module sections read as third-person explanation rather than instruction to the agent — "About Us" prose, historical narratives, peer-comparison explanations. The transformation test ran *after* writing, producing line-edits when the failure was at the shape level. *Now prevented by:* shape committed in Section Plan before writing; the shape is one of five named options (reasoning context | decision framework | prescriptive rule | cross-reference | reach-beyond signal); F0 in templates/guardrails/ is the worked example for mixed-shape modules (ARCHITECTURE.md, "Shape Reference: F0 as a Worked Example"); plan-vs-prose checks 1–3 in self-check compare prose against the plan, not against an abstract test.

- **Within-session correction oscillation:** When a module fails, the default move is "rewrite differently," producing oscillation between failure modes — narrative prose to inverted rules to flattened gate-sets. Each correction overrode the prior attempt rather than refining the underlying judgment. *Now prevented by:* the failure-recovery protocol (Phase 4, "When a Module Fails") — name the failure mode, locate the upstream planning step that caused it, redo the planning step, regenerate the affected sections from the corrected plan. The build agent cannot rewrite without first naming the upstream cause.

- **Build-state log explosion:** The per-module protocol's commitment-gate answers, source-grounding statements, and SSoT cross-checks all landed in build-state, producing 40+ multi-paragraph entries that defeated build-state's purpose as session bootstrap. *Now prevented by:* Step 8 explicitly separates terse build-state status (one line per module) from substantive process-log reasoning (one entry per module) from scratch planning artifacts (Steps 1, 2, 4, 5 — kept in working context, not persisted). Build-state stays usable as a resume reference.

- **Retrospective documents anchoring redo attempts:** When a Phase 4 build is rolled back and an audit/post-mortem document exists, the next attempt is anchored by the retrospective's specific examples, producing a near-copy of the failed work with the same structural problems redistributed. *Now prevented by:* the redo-session protocol (Phase 4) — retrospective documents and prior-attempt module files are physically moved to `_retrospective_archive/` and not read during the attempt; the user provides a list of *named failure patterns* (names only, no examples) that goes in build-state. The build agent regenerates from proposal and sources.

- **Design specifies ownership but not use-shape:** The old proposal's table assigned each content area to one canonical home but did not specify how using modules incorporate the content. Build invented restatement as the use-shape. *Now prevented by:* Phase 3 requires both ownership and use-shape for every shared content area; rows without a use-shape fail the GATE and STOP.

- **Mechanical source re-read without substantive engagement:** The per-module re-read protocol prevented writing-from-stale-memory but did not check whether what was written reflected what was read. Modules passed the re-read protocol and still missed source substance. *Now prevented by:* the Substantive Source Surface (Phase 4, Step 4) — after re-reading, the build agent surfaces 3–7 specific patterns from the just-read sources that this module will capture, with source pointers; self-check verifies the surface's patterns are present in the module, not just facts.

- **Comprehension shorthand crowding out source substance:** Phase 2's prose-shaped LOG outputs ("2-3 sentences: the organizational reasoning this source reveals") became cached working memory the build agent reached for instead of the sources during Build. Modules captured the build agent's interpretation of the sources rather than what the sources actually say. *Now prevented by:* Phase 2 outputs are pattern-pointers, not summaries (pattern name + source pointer + shape — never the substance of what the pattern says); the Substantive Source Surface explicitly forbids "from comprehension findings."

- **Single-pass comprehension on saturated source context:** Phase 2 originally read all sources and produced consolidated outputs in one pass. For source sets in the 100+ file / 250K+ token range, synthesis collapsed toward summarizing what the sources collectively said rather than identifying the underlying organizational reasoning; lateral cognitive moves (cross-domain parallels, deeper-level convergences, reframing) were crowded out by source dominance; and outliers got averaged into the dominant signal. *Now prevented by:* Phase 2 splits into Pass 1 (recognition with sources loaded — per-source notes, signal log, expectations-vs-findings, conflicts) and Pass 2 (synthesis with sources mostly out of context, recognition artifacts loaded — pattern-pointers, convergences, cross-domain parallels, agent-needs). Mandatory session break between passes makes the structural advantage real.

- **Negative space invisible to comprehension:** "What I expected to find but didn't find" is one of the strongest comprehension signals — and the previous Phase 2 had no artifact for it. Absences registered as "wasn't covered" rather than as "I expected this and it isn't here." *Now prevented by:* Phase 1 produces an Initial Expectations deliverable (what the build agent expects to find in the sources, per agent role); Phase 2 Pass 1 produces an expectations-vs-findings reflection that explicitly lists what was expected but not found, with an interpretation (organizational finding, sourcing gap, or wrong expectation).

- **Recognition observations lost between sources:** When the build agent noticed a surprise, conflict, or distinctive vocabulary in source #43, the observation often blurred away by source #87 because the LOG format had no slot for it. *Now prevented by:* per-source notes (one file per source) capture observational fields (surprises, conflicts, gaps) and signal-collection fields (distinctive vocabulary, distinctive evasions) at the moment of reading. The signal log captures cross-source patterns as they become visible. Both feed Pass 2 synthesis.

- **Manifest classification leaving load decisions to runtime judgment:** Earlier agent manifests grouped modules by tier (foundation/shared/specialized) and listed addenda separately as reach-beyond. Runtime agents read this as "items available to load when the situation calls for it" and made their own load-time judgments. In production, this produced the originating failure: an agent skipped loading S0 because it judged the immediate task didn't need prose discipline, then produced output that violated S0's standards. The same pattern hit reference addenda — agents generated content from inference instead of from loaded reference data because they didn't recognize the work as needing the reference. *Now prevented by:* the manifest's `always_load` / `conditional` classification (Phase 3 Load-Discipline Classification table) — items that govern every output are loaded universally, items that apply only in specific contexts have plain-language `load_when:` triggers; container (module vs. addendum) and load discipline are independent dimensions; F0 and S0 are hard-rule `always_load` whenever they appear, enforced at three layers (Phase 3 GATE, Phase 4 self-check, validation script).

**Recurring patterns the protocol still requires awareness of (not architecturally prevented):**

- **A separate synthesis phase:** The old architecture spent an entire session rewriting transcripts into "clean working documents." This produced restatements, not insights. Comprehension handles messy sources directly — the behavioral pattern is what matters, not a polished rewrite.

- **Running all phases in one session:** Context compaction destroys metaprompt transformation rules. By the time the agent reaches module writing, it has reverted to copying content because the instructions governing transformation are gone. The mandatory session break exists so Design and Build start with fresh rules.

- **Deriving agents after building modules:** The old architecture built modules first, then designed agents to use them. Agent definitions belong in Design because who needs what context is a structural question that shapes module architecture.

- **Proposing structure before understanding sources:** The default is to read source titles, guess at a taxonomy, and propose modules. Comprehension forces the agent to understand what the organization actually *does* before committing to any structure.

- **Token minimization:** The old architecture's budget framing ("warning at 80%") produced lean agents that lacked the context to make good decisions. An agent using 60% of its budget isn't efficient — it's underserved.

- **Source-index classifications as skip permissions:** Labels like "legacy," "pre-reorg," or "reference only" assigned during Setup triage get carried into Build as authority on what to read. The proposal's source assignments are authoritative; the source-index classifications are not.

- **AI-centrism in module content:** The build agent gravitates toward AI-related content in sources and builds modules around it, underweighting work that predates or exists alongside AI adoption. AI is part of the organizational story, not its summary.

- **Validation as a separate phase:** Quality built into per-module commitment gates catches problems at the source. A final-stage validation pass cannot fix modules that were written as content instead of metaprompts — the structural problem is upstream.
</failed_attempts>
