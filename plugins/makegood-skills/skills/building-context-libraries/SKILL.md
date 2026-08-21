---
name: building-context-libraries
description: Builds modular context libraries that change how AI agents behave with organizational knowledge. Transforms source documents (transcripts, strategy docs, process documents, interviews) into metaprompt modules — system prompt components that shape agent decision-making. Use when user says build context library, create context library, create agent context, build knowledge base, transform documents into agent context, build domain context, or create organizational context modules. Also use when resuming or continuing an in-progress build — resume context library, continue the library build, pick up where we left off — since the build spans multiple sessions with mandatory breaks between them, and when migrating an existing library to the current skill version. Activates when organizational source documents are provided via file path or directory, or when a build-state file from a previous session is present.
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

See [references/ARCHITECTURE.md](references/ARCHITECTURE.md) for the full module design philosophy, runtime perspective, synthesis vs. inventory (the discrimination test), single source of truth and use-shapes, shape reference (G1 as worked example), content transformation rules, and token management.

---

## Critical Rules

**When these rules pull against each other,** the order is: the rules governing what may appear in a runtime file (RUNTIME PERSPECTIVE, SOURCING, named individuals, reported speech) are absolute — no other rule licenses a violation. The rules governing *how* content is shaped (TRANSFORM DON'T TRANSCRIBE, use-shapes, load discipline) are next, and they are settled at a phase gate rather than at write-time; if the shape a rule demands is wrong for the content, that is a planning failure to raise, not a rule to bend. The rules governing *depth* (SUBSTANCE OVER SHORTHAND, token budget as room) yield to both: a thinner module that states only what the sources support beats a richer one that doesn't.

**RUNTIME PERSPECTIVE:** Every module is read by a runtime agent that has only its loaded modules and the user's input. No sources, no build documents, no proposal, no library. Before writing any module section, the build agent commits to the runtime frame (Phase 4, Step 1). Sentences that only make sense inside the build — "the source set," "the library doesn't carry," "in some 2025-era sources," named source files — are contamination. The contamination test is not whether specific phrases appear; it is whether the sentence makes sense to a reader who knows nothing about how the module came to exist.

**The frame has a second half, and it trips no phrase at all.** A context library carries the understanding distilled from the sources — never the sources themselves catalogued, never the current state of the deliverable it helps produce, never an inventory of what is missing or undecided, never the provenance or confidence grade of what was learned, never the alternatives a decision ruled out. Specific content anchors the agent instead of teaching it to reason, and naming a thing raises it: an absence inventory primes every concept it lists. A statement the agent's own output will falsify is an instruction with an expiry date, and in always-load content no conversation can displace it. The test on every candidate line: **does this teach a durable behavior, or instantiate a specific, volatile, or absent fact?** Durable behavior stays, framed positively; an instantiated fact is cut, or inverted to the rule it was standing in for. Do not strip a positive rule because it contains a negation — "never invent X" is a rule and belongs; "X does not exist" is an inventory and does not. Enforced at the Phase 3 GATE, Phase 4's Step 4 surface and Step 5 plan, and self-check 7. See ARCHITECTURE.md, "Synthesis, Not Inventory."

**PLANNING PRECEDES PROSE:** The Build phase's per-module protocol has 7 steps. Steps 4 (Substantive Source Surface) and 5 (Section Plan) are planning artifacts the build agent commits to *before* generating prose. The plan names section shape, owned-content use-shape (from the proposal's Ownership and Use-Shape table), source patterns, which source language is preserved verbatim, and extracted reasoning from any reported speech or named individual. Writing executes the plan. When prose drifts from the plan, the failure-recovery protocol (Phase 4, "When a Module Fails") fixes the upstream planning step — it does not regenerate prose from scratch.

**TWO-PASS COMPREHENSION:** Phase 2 has two passes with a mandatory session break between them. Pass 1 is recognition — sources loaded, observational artifacts (per-source notes, signal log, expectations-vs-findings, conflicts) written at the moment of reading. Pass 2 is synthesis — sources mostly out of context, recognition artifacts loaded, pattern-pointers and convergences and cross-domain parallels and agent-needs generated with cognitive room to do the lateral work. Single-pass synthesis on a saturated source context produces sector-applicable rather than organization-specific patterns; the two-pass structure prevents this. The session break is what makes Pass 2's structural advantage real.

**SOURCING:** Every fact in the library must trace to a source document. Before stating any claim about the organization, locate its source. If you cannot locate a source, state what's missing rather than approximating. NEVER invent details. NEVER fill gaps.

**SUBSTANCE OVER SHORTHAND:** Modules capture what the just-read sources reveal, not what comprehension findings or process-log entries summarized. The Substantive Source Surface (Phase 4, Step 4) requires patterns to come from the source files re-read in the same turn — not from earlier summaries. Comprehension shorthand crowding out source substance is a recurring failure mode; the surface is where it gets caught.

**EPISTEMIC CALIBRATION:** The reader should always be able to tell whether a claim is sourced from documents, inferred from cross-document patterns, or your analytical interpretation — because your language makes the distinction clear. Sourced claims read as direct statement. Inferences read with inferential language ("the sources suggest," "this pattern indicates," "across documents X and Y, the organization appears to"). Analytical synthesis reads as the build agent's reasoning ("on the basis of these patterns, the module captures"). The language carries the signal; markers are scaffolding. Use `[PROPOSED]` only when natural language alone won't carry enough signal during the build — and remove before delivery.

**PROFESSIONAL CHALLENGE:** When a user's proposed module structure contradicts what the sources support, when an approach has known pitfalls (taxonomy-based modules, content-copying, over-compression), or when assumptions aren't grounded in sources — cite the concern, offer an alternative.

**TRANSFORM, DON'T TRANSCRIBE:** Before writing any module section, identify the organizational reasoning it provides and whether an agent could apply it to situations the author didn't anticipate. Modules provide reasoning context — how the organization thinks — not procedures or exhaustive rules. Prescriptive "If X, do Y" rules are rare, reserved for genuine constraints where violation causes real harm.

**SINGLE SOURCE OF TRUTH IS A USE-SHAPE COMMITMENT:** Naming an owner is necessary but not sufficient. The proposal's Ownership and Use-Shape table commits every using module to one of four shapes — cross-reference, subset, invocation by name, or reach-beyond. Restatement is not one of the shapes. Build executes the table; it does not redecide it at write-time.

**LOAD DISCIPLINE IS A CLASSIFICATION; DELIVERY IS THE SEPARATE QUESTION OF HOW IT REACHES THE AGENT.** Every loadable item is classified as always-load (governs every output that agent produces — agent's runtime judgment about whether to load it is unreliable) or conditional (applies only in specific task or audience contexts, with a `load_when:` trigger in plain language). The classification is per-agent — the same module may be always-load for one agent and conditional for another. Container (module vs. addendum) and load discipline are independent dimensions: a reference addendum can be always-load, a shared module can be conditional. The classification is decided in Design (Phase 3 Load-Discipline Classification table), not at agent-write time. **The classification renders as `@`-include directives in `## Required Reading` (always-load) and a triggers table in `## Conditional Loads` (conditional) — not as YAML frontmatter, not as a prose mirror of the manifest.** Always-load content reaches the agent's system prompt from turn one — Claude Code expands `@` directives natively; for runtimes that don't process `@` (Claude.ai project upload, generic API integrations), the bundled build script produces self-contained deployment bundles offline. The agent never participates in always-load delivery. **G1_agent_behavioral_standards has an `@`-directive in Required Reading whenever it appears. G2_natural_prose_standards has an `@`-directive in Required Reading whenever it appears.** Both are hard rules — not judgment calls — enforced at the Phase 3 GATE, the Phase 4 self-check, and the validation script. See ARCHITECTURE.md, "Always-Load Delivery."

**NAMED INDIVIDUALS DO NOT APPEAR IN MODULES:** When a named individual informs a section, the Section Plan extracts the reasoning before prose is written; the name does not travel into the module. A runtime agent has no referent for a person it was never introduced to, and proper nouns anchor prose to specific personalities rather than giving the agent a way of thinking. Name-removal happens during planning, not as a post-hoc edit.

**REPORTED SPEECH DOES NOT APPEAR IN MODULES; THE ORGANIZATION'S TERMS DO:** A quote framed as something someone said — "the team noted," "as one founder put it" — fails for the same reason a name does. Extract the reasoning and write it as instruction. But the organization's own terms for itself, its roles, and its methods are preserved verbatim *inside* that instruction: a module written in the organization's vocabulary teaches an agent to use it, and a module that paraphrases the vocabulary away leaves the agent describing a way of talking it cannot reproduce. The Section Plan commits which language is preserved before prose is written (Phase 4, Step 4).

**CONVERGENCE AWARENESS:** When source documents describe the same underlying pattern differently, the convergence reveals something about the organization that neither document says alone. Explore intersections rather than filing information into the first plausible module.

**CONFLICT RESOLUTION:** When source documents contradict, surface the conflict to the user. Do not silently pick one version.

**REDO SESSIONS HAVE A SEPARATE PROTOCOL:** When a previous Build attempt was rolled back, the redo-session protocol (Phase 4) physically separates retrospective documents and prior-attempt artifacts from the working set. The build agent regenerates from the proposal and sources, not from retrospective examples. The user provides a list of named failure patterns to avoid; the names go in build-state, the documents do not enter context.

---

## Reference Files

Read the phase instruction file before each phase. Re-read after any context compaction.

| File | Purpose |
|------|---------|
| [references/ARCHITECTURE.md](references/ARCHITECTURE.md) | Runtime agent's perspective, synthesis vs. inventory and the discrimination test, module design, single source of truth and the four use-shapes, load discipline (always-load vs. conditional, G1/G2 hard rule, trigger discipline), always-load delivery (`@`-includes for Claude Code, build-script bundles for other runtimes, the all-inclusive variant), guardrails as a versioned dependency (G1/G2 vendored from makegood-guardrails, the lock, resolve/update/check), G1 as a worked shape reference, content transformation, token management, stakes classification |
| [references/TEMPLATES.md](references/TEMPLATES.md) | Templates for build-state, process-log, source-index, modules by tier, agent definition (with `@`-include Required Reading + Conditional Loads table), addendum, proposal with Ownership and Use-Shape and Load-Discipline Classification tables |
| [templates/build-deploy-bundles.py](templates/build-deploy-bundles.py) | Build script copied into output libraries during Phase 4. Resolves `@`-include directives into self-contained agent bundles (`--all-inclusive` for runtimes where conditional fetch is unreliable), and resolves pinned guardrail versions (`--resolve-guardrails` — including the G2-backstop splice for G2 ≥ 2.0.0, `--update-guardrails`, guardrail drift + upstream-newer notices in `--check`). |
| [templates/guardrails.lock](templates/guardrails.lock) | Lock-file template copied into a new library's root during Phase 4; pins the G1/G2/G2-backstop versions the library vendors from `makegood-guardrails`. See ARCHITECTURE.md, "Guardrails as a Versioned Dependency." |
| [templates/library-README.md](templates/library-README.md) | Deployment-doc template copied into output libraries' README. Explains the bundle approach for library consumers (humans deploying the library to runtimes). |
| [references/COMPREHENSION_TEMPLATES.md](references/COMPREHENSION_TEMPLATES.md) | Templates for Phase 2's eight comprehension artifacts (per-source notes, signal log, expectations-vs-findings, conflicts, pattern-pointers, convergences, cross-domain parallels, agent-needs) |
| [references/FAILURE_MODES.md](references/FAILURE_MODES.md) | The full catalogue of production failure modes and where each one's prevention lives. Read when diagnosing a failed module, redoing a rolled-back build, or changing the protocol |
| Phase files in [references/phases/](references/phases/) | Self-contained instructions per phase, including [PHASE_M_MIGRATION.md](references/phases/PHASE_M_MIGRATION.md) for migrating libraries between skill versions |

---

## Build Process

4 phases across 4 sessions. Phase 2 (Comprehend) is internally split into two passes (recognition and synthesis) with a mandatory session break between them.

| Phase | Name | Instruction File | Function |
|-------|------|------------------|----------|
| 1 | Setup | [PHASE_1_SETUP.md](references/phases/PHASE_1_SETUP.md) | Load sources, create manifest, classify, identify agent needs and initial expectations |
| 2 | Comprehend (two passes) | [PHASE_2_COMPREHEND.md](references/phases/PHASE_2_COMPREHEND.md) | Pass 1: read all sources, write recognition artifacts (per-source notes, signal log, expectations-vs-findings, conflicts). Pass 2: synthesize with sources mostly out of context (pattern-pointers, convergences, cross-domain parallels, agent-needs). |
| 3 | Design | [PHASE_3_DESIGN.md](references/phases/PHASE_3_DESIGN.md) | Propose module architecture, agent definitions, ownership and use-shape assignments |
| 4 | Build | [PHASE_4_BUILD.md](references/phases/PHASE_4_BUILD.md) | Write modules with per-module gates, build addenda, validate |

### Session Architecture

**This table is the single statement of the session map.** The phase files execute it; where a phase file describes its own session boundary, it describes this one.

| Session | Phases | Why Alone |
|---------|--------|-----------|
| A | Setup + Comprehend Pass 1 (Recognition) | Recognition needs source documents fresh in context |
| **MANDATORY BREAK** | | Synthesis needs sources mostly out of context, recognition artifacts loaded |
| B | Comprehend Pass 2 (Synthesis) | Synthesis needs the cognitive room the source set would consume |
| **MANDATORY BREAK** | | Design's loading gate re-reads every source; Pass 2's premise is that it has not |
| C | Design | Structural reasoning needs the full source set in context *and* the transformation rules fresh |
| **MANDATORY BREAK** | | Build needs the per-module protocol fresh, not buried under structural reasoning |
| D | Build | Each module is self-contained — resume from `build-state.md`; per-module protocol re-reads relevant sources targetedly |

**All three breaks are mandatory.** The Pass 1/Pass 2 break is what allows synthesis to do the lateral cognitive work G1's Analytical Depth Requirements ask for — moves that are difficult or impossible from inside saturated source context. The Pass 2/Design break exists because the two phases need opposite context states: Design cannot assign organizational reasoning to modules without every source loaded, and Pass 2 cannot synthesize with them loaded. Running both in one session means one of the two is working against its own premise. The Design/Build break keeps the per-module protocol fresh, rather than buried under a session of structural reasoning.

Build may extend into Session E if the library is large. Each module is self-contained.

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

The patterns below produced failed builds in production, and each one is a default the build agent must actively hold off *while writing*. Each entry names what was tried, why it failed, and where the architectural prevention now lives.

- **Build-perspective contamination in modules:** The build agent has source files, the proposal, and the build process in working context, and slips that perspective into module text — "the source set," "the library doesn't carry," "in some 2025-era sources," named source-file paths. The runtime agent has none of those referents. *Now prevented by:* the Runtime Frame Set commitment (Phase 4, Step 1) before any other writing work; explicit contamination phrases listed in ARCHITECTURE.md and the module template's BUILD REMINDERS; runtime-frame checks 5–7 in the per-module self-check.

- **Source contents catalogued instead of synthesized:** Comprehension output — a vision pass over a photo set, a document review, a transcript read — reproduced in a module as a table or index the agent reaches back into. It carries no source filename, so the contamination scan passes it; the module becomes an index of a source set, goes stale as the sources change, and teaches the agent to describe rather than to reason. The originating step is the Substantive Source Surface, where "patterns from the just-read sources" reads easily as "list what they hold." *Now prevented by:* the surface's reconstructability discriminator (Phase 4, Step 4 — an entry that could be rebuilt back into its source is inventory, not understanding, and negative space informs the surface without appearing on it); "Guiding, Not Cataloging" extended to name the source set as the second catalogue form (ARCHITECTURE.md); the source-inventory signal in self-check 7; and the Phase 3 GATE rule barring a proposal row from assigning what the sources contain as a module's content.

- **Build reasoning rendered as runtime content:** Modules and addenda carrying "What Is Not Established," an unknowns register, a description of the deliverable as it currently stands, or an evidence grade attached to a heading ("first contact — well evidenced"). Every one of these is correct *build* reasoning — Phase 2 mines negative space deliberately, the state of the thing being changed is what the build is looking at, and provenance is how facts get verified — and every one of them self-invalidates in a runtime file: an absence inventory goes false the day the gap closes, a current-state description the first time the agent does its job. Naming an absence also primes the concept the module meant to suppress. The skill instructed two of these directly: the addenda definition licensed "catalogs, inventories," and Building Addenda asked for source attribution, which the addendum template shipped as a `*Source:*` footer. *Now prevented by:* the boundary line in Phase 2 and COMPREHENSION_TEMPLATES (negative space, source inventories, and provenance live in `_comprehension/` and do not cross); the Phase 3 GATE rule; the self-invalidation test in ARCHITECTURE.md; self-check 7's absence-inventory, current-state, and provenance signals, each carrying the inversion instruction so the behavior survives the cut; the addenda definition and Building Addenda rewritten around what the agent may state and where volatile truth lives; the `*Source:*` footer removed from the addendum template and a BUILD REMINDERS block added to it; and validate_library.py's advisory section 6 across `modules/`, `addenda/`, and `agents/`.

- **A worked example built on a fact the build had flagged pending:** The most vivid illustration available is usually the most contested one — the flagship asset, the disputed claim, the thing a scheduled interview will resolve. Placed in an always-load module it is rebuilt into the system prompt every turn, so a correction made in conversation cannot displace it; the agent meets the stale example again on the next turn. The volatile-data rule sent changing figures to addenda and said nothing about the example a section teaches with. *Now prevented by:* `Illustration or worked example` is a committed field in the Section Plan (Phase 4, Step 5) carrying a durability requirement — an example resting on a fact flagged pending, contested, or to-be-confirmed is disqualified; the volatile-vs-durable test in ARCHITECTURE.md now governs examples and not only data; and the module quality checklist verifies it.

- **Language flattening:** The organization's own terms for itself, its roles, and its methods get paraphrased into directive prose. Every individual paraphrase looks like transformation, and the result is a library that describes a vocabulary no agent can reproduce — the modules read as machine-written because they are, and every agent loading them inherits that register. *Now prevented by:* distinctive terminology is a named extraction category (ARCHITECTURE.md); `Language to preserve` is a committed field in the Substantive Source Surface; naming/illustration is a section shape; and self-check 15 runs G2's practitioner-voice gate against the module's own prose.

- **Metaprompt-vs-prose drift:** Module sections read as third-person explanation rather than instruction to the agent — "About Us" prose, historical narratives, peer-comparison explanations. The transformation test ran *after* writing, producing line-edits when the failure was at the shape level. *Now prevented by:* shape committed in Section Plan before writing; the shape is one of five named options (reasoning context | decision framework | prescriptive rule | cross-reference | reach-beyond signal); G1 in templates/guardrails/ is the worked example for mixed-shape modules (ARCHITECTURE.md, "Shape Reference: G1 as a Worked Example"); plan-vs-prose checks 1–3 in self-check compare prose against the plan, not against an abstract test.

**The full catalogue — 22 further failure modes, including every one whose prevention sits at a phase gate rather than at write-time — is in [references/FAILURE_MODES.md](references/FAILURE_MODES.md).** Read it when diagnosing a module that failed self-check, when redoing a build after a rollback, or when changing the protocol. The entries above are the ones that operate at the sentence level; the rest are prevented upstream and do not need to be in context while prose is generated.
</failed_attempts>
