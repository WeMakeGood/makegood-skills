# Failure Modes

## Contents

- Why this file exists
- Architectural failures the protocol now prevents structurally
- Recurring patterns the protocol still requires awareness of

---

## Why This File Exists

Every pattern below produced a failed build in production. Each entry names what was tried, why it failed, and where the architectural prevention now lives.

Read this file when diagnosing a module that failed self-check, when a build is being redone after a rollback, or when changing the protocol — the "*Now prevented by:*" pointers are what a change would be removing. The entries whose prevention has to be held in mind *while prose is being written* are the ones that stayed in SKILL.md; these are the rest.

An entry here is not a checklist item. The prevention is structural — a gate, a planning artifact, a table the build executes. The names are for diagnosis, not for monitoring.

---

## Architectural Failures the Protocol Now Prevents Structurally

- **Single-source-of-truth drift across modules:** Naming an owner without specifying use-shape leaves the build agent to decide at write-time how a using module incorporates owned content — and the path of least resistance is to restate. *Now prevented by:* the proposal's Ownership and Use-Shape table commits every using module to one of four shapes (cross-reference, subset, invocation, reach-beyond); restatement is not a shape; the Section Plan applies the shape from the table before prose is generated.

- **Reported-speech and named-individual contamination:** Source quotes get imported with attribution; named individuals appear in modules as carriers of organizational reasoning. The path of least resistance after re-reading sources is to import the framing along with the content. *Now prevented by:* the Section Plan's quote/individual handling commits each to EXTRACT or PRESERVE before prose exists — the reasoning is extracted and the speaker framing dropped, or the organization's term is preserved verbatim inside instruction shape. Neither outcome carries a name or a speaker frame.

- **Design-phase terminology substitution:** A rationale cell in the Ownership and Use-Shape table instructs Build to express a term as some tidier phrase — "source uses X (client-originated) — modules should express this as Y." It reads as tidying, Build follows it precisely, and the organization's word never reaches a module without any Build rule being violated, because the substitution was authorized a phase earlier. *Now prevented by:* the table assigns where content lives and does not rewrite vocabulary; a term proposed for replacement leaves the table and becomes an explicit question at the Phase 3 STOP; the proposal carries a Terminology table whose default is carry-through.

- **Within-session correction oscillation:** When a module fails, the default move is "rewrite differently," producing oscillation between failure modes — narrative prose to inverted rules to flattened gate-sets. Each correction overrode the prior attempt rather than refining the underlying judgment. *Now prevented by:* the failure-recovery protocol (Phase 4, "When a Module Fails") — name the failure mode, locate the upstream planning step that caused it, redo the planning step, regenerate the affected sections from the corrected plan. The build agent cannot rewrite without first naming the upstream cause.

- **Build-state log explosion:** The per-module protocol's commitment-gate answers, source-grounding statements, and SSoT cross-checks all landed in build-state, producing 40+ multi-paragraph entries that defeated build-state's purpose as session bootstrap. *Now prevented by:* Step 8 explicitly separates terse build-state status (one line per module) from substantive process-log reasoning (one entry per module) from scratch planning artifacts (Steps 1, 2, 4, 5 — kept in working context, not persisted). Build-state stays usable as a resume reference.

- **Retrospective documents anchoring redo attempts:** When a Phase 4 build is rolled back and an audit/post-mortem document exists, the next attempt is anchored by the retrospective's specific examples, producing a near-copy of the failed work with the same structural problems redistributed. *Now prevented by:* the redo-session protocol (Phase 4) — retrospective documents and prior-attempt module files are physically moved to `_retrospective_archive/` and not read during the attempt; the user provides a list of *named failure patterns* (names only, no examples) that goes in build-state. The build agent regenerates from proposal and sources.

- **Design specifies ownership but not use-shape:** The old proposal's table assigned each content area to one canonical home but did not specify how using modules incorporate the content. Build invented restatement as the use-shape. *Now prevented by:* Phase 3 requires both ownership and use-shape for every shared content area; rows without a use-shape fail the GATE and STOP.

- **Mechanical source re-read without substantive engagement:** The per-module re-read protocol prevented writing-from-stale-memory but did not check whether what was written reflected what was read. Modules passed the re-read protocol and still missed source substance. *Now prevented by:* the Substantive Source Surface (Phase 4, Step 4) — after re-reading, the build agent surfaces 3–7 specific patterns from the just-read sources that this module will capture, with source pointers; self-check verifies the surface's patterns are present in the module, not just facts.

- **Single-pass comprehension on saturated source context:** Phase 2 originally read all sources and produced consolidated outputs in one pass. For source sets in the 100+ file / 250K+ token range, synthesis collapsed toward summarizing what the sources collectively said rather than identifying the underlying organizational reasoning; lateral cognitive moves (cross-domain parallels, deeper-level convergences, reframing) were crowded out by source dominance; and outliers got averaged into the dominant signal. *Now prevented by:* Phase 2 splits into Pass 1 (recognition with sources loaded — per-source notes, signal log, expectations-vs-findings, conflicts) and Pass 2 (synthesis with sources mostly out of context, recognition artifacts loaded — pattern-pointers, convergences, cross-domain parallels, agent-needs). Mandatory session break between passes makes the structural advantage real.

- **Negative space invisible to comprehension:** "What I expected to find but didn't find" is one of the strongest comprehension signals — and the previous Phase 2 had no artifact for it. Absences registered as "wasn't covered" rather than as "I expected this and it isn't here." *Now prevented by:* Phase 1 produces an Initial Expectations deliverable (what the build agent expects to find in the sources, per agent role); Phase 2 Pass 1 produces an expectations-vs-findings reflection that explicitly lists what was expected but not found, with an interpretation (organizational finding, sourcing gap, or wrong expectation).

- **Recognition observations lost between sources:** When the build agent noticed a surprise, conflict, or distinctive vocabulary in source #43, the observation often blurred away by source #87 because the LOG format had no slot for it. *Now prevented by:* per-source notes (one file per source) capture observational fields (surprises, conflicts, gaps) and signal-collection fields (distinctive vocabulary, distinctive evasions) at the moment of reading. The signal log captures cross-source patterns as they become visible. Both feed Pass 2 synthesis.

- **Manifest classification leaving load decisions to runtime judgment:** Earlier agent manifests grouped modules by tier (foundation/shared/specialized) and listed addenda separately as reach-beyond. Runtime agents read this as "items available to load when the situation calls for it" and made their own load-time judgments. In production, this produced the originating failure: an agent skipped loading G2 because it judged the immediate task didn't need prose discipline, then produced output that violated G2's standards. The same pattern hit reference addenda — agents generated content from inference instead of from loaded reference data because they didn't recognize the work as needing the reference. *Now prevented by:* per-agent always-load / conditional classification (Phase 3 Load-Discipline Classification table) — items that govern every output are loaded universally, items that apply only in specific contexts have plain-language `load_when:` triggers; container (module vs. addendum) and load discipline are independent dimensions; G1 and G2 are hard-rule always-load whenever they appear, enforced at three layers (Phase 3 GATE, Phase 4 self-check, validation script).

- **Always-load classification correct, delivery mechanism unreliable:** The 1.5 manifest format encoded the classification as YAML frontmatter (`always_load:` / `conditional:` blocks) plus a prose mirror in the agent file body that named each item again as "items in your context every time." Claude Code's runtime didn't process the YAML as instruction; non-Claude-Code runtimes (Claude.ai project upload, Cowork, generic API integrations) treated the prose mirror as discretionary tool work the agent could choose to skip, batch, or partially execute. In testing, an agent ignored the load instruction entirely on first turn, then loaded the files slowly and sequentially as ten separate tool turns when pressed. The classification was correct; the artifact didn't deliver the content. *Now prevented by:* `@`-include directives in `## Required Reading` (Claude Code expands natively) plus a build script that resolves `@`-includes offline into self-contained deployment bundles for non-`@`-aware runtimes. The agent never participates in always-load delivery — it's content in the system prompt from turn one, regardless of runtime. See ARCHITECTURE.md, "Always-Load Delivery."

- **Comprehension shorthand crowding out source substance:** Phase 2's prose-shaped LOG outputs ("2-3 sentences: the organizational reasoning this source reveals") became cached working memory the build agent reached for instead of the sources during Build. Modules captured the build agent's interpretation of the sources rather than what the sources actually say. *Now prevented by:* Phase 2 outputs are pattern-pointers, not summaries (pattern name + source pointer + shape — never the substance of what the pattern says); the Substantive Source Surface explicitly forbids "from comprehension findings."

---

## Recurring Patterns the Protocol Still Requires Awareness of

These are not architecturally prevented. They are defaults that reassert themselves whenever the protocol is loosened.

- **A separate synthesis phase:** The old architecture spent an entire session rewriting transcripts into "clean working documents." This produced restatements, not insights. Comprehension handles messy sources directly — the behavioral pattern is what matters, not a polished rewrite.

- **Running all phases in one session:** Context compaction destroys metaprompt transformation rules. By the time the agent reaches module writing, it has reverted to copying content because the instructions governing transformation are gone. The mandatory session breaks exist so Comprehend Pass 2, Design, and Build each start with fresh rules.

- **Deriving agents after building modules:** The old architecture built modules first, then designed agents to use them. Agent definitions belong in Design because who needs what context is a structural question that shapes module architecture.

- **Proposing structure before understanding sources:** The default is to read source titles, guess at a taxonomy, and propose modules. Comprehension forces the agent to understand what the organization actually *does* before committing to any structure.

- **Token minimization:** The old architecture's budget framing ("warning at 80%") produced lean agents that lacked the context to make good decisions. An agent using 60% of its budget isn't efficient — it's underserved.

- **Source-index classifications as skip permissions:** Labels like "legacy," "pre-reorg," or "reference only" assigned during Setup triage get carried into Build as authority on what to read. The proposal's source assignments are authoritative; the source-index classifications are not.

- **AI-centrism in module content:** The build agent gravitates toward AI-related content in sources and builds modules around it, underweighting work that predates or exists alongside AI adoption. AI is part of the organizational story, not its summary.

- **Validation as a separate phase:** Quality built into per-module commitment gates catches problems at the source. A final-stage validation pass cannot fix modules that were written as content instead of metaprompts — the structural problem is upstream.
