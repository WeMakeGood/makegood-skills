# Changelog

All notable changes to this skill are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this skill follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.10.0] — 2026-08-10

### Changed
- **Guardrail keys renamed: F0 → G1, S0 → G2, S0_BACKSTOP → G2_BACKSTOP.** The F/S prefixes were context-library tier markers that meant nothing in the guardrails repo and collided with libraries using F/S/D for their own modules. `build-deploy-bundles.py` constants, the lock template, the vendored reference copies, and all skill prose move to the new names. `tag_for()` needed no change — it derives tags from the lock key mechanically.
- **Vendored paths keep their tier directories** (`modules/foundation/`, `modules/shared/`). Those are the *library's* namespace, not the guardrails repo's, and the rename does not touch them.

### Fixed
- **`--check` no longer reports `[ok] guardrails match locked versions` when the check did not run.** The guardrail check requires PyYAML; without it the run printed a `[WARN]` and then the `[ok]` line anyway, because the all-clear tested only for `DRIFT`. On a machine where `python3` resolves to a Homebrew interpreter without PyYAML — while the system interpreter has it — this reported a clean guardrail state that had never been verified. A skipped check now prints `[--] guardrail check did not run`.
- **Migration detection strings no longer use post-rename filenames to detect pre-rename libraries.** The 1.10.0 rename sweep replaced `F0_agent_behavioral_standards.md` with `G1_` inside the 1.6→1.7 migration trigger and the guardrails-versioning case description — both of which exist to detect libraries built *before* the rename, which have `F0_` files. Those triggers could no longer fire.

### Added
- **`guardrail-g-namespace` migration (1.9.x → 1.10.0)** in `PHASE_M_MIGRATION.md`, with a bootstrap trigger for locks declaring `F0`/`S0`/`S0_BACKSTOP` keys. Optional in the strict sense — the retained tags keep old locks resolving — but a library that never migrates is pinned to the pre-rename line, since the old tags stop at F0 2.1.0 / S0 2.0.1.
- **A migration notice for pre-rename locks.** The old `f0-v*` / `s0-v*` tags were deliberately retained so un-migrated libraries keep resolving — which means the rename is silent by default: a library pinned to F0 fetches successfully and never learns G1 exists. End-to-end testing confirmed this, contradicting the design note that predicted a loud failure. `--resolve-guardrails` now prints the old→new mapping once when it sees pre-rename keys, and stays quiet for migrated locks.

## [1.9.1] — 2026-08-10

### Changed
- **The Ownership and Use-Shape table assigns where content lives; it does not rewrite the organization's vocabulary.** A rationale cell reading "source uses X (client-originated) — modules should express this as Y" reads as tidying, and Build follows it precisely: the organization's word never reaches a module, and no Build rule is violated because the substitution was authorized a phase earlier. Terminology substitution now fails the Phase 3 gate and goes to the user as an explicit question at STOP.
- **"Client-originated" and "colloquial" describe a term's history, not its status.** Repetition across sources is what makes a term the organization's own — terms picked up from clients, a founder's earlier field, or a sector's shorthand are the organization's once it uses them.

### Added
- **A Terminology table in the proposal.** Recurring terms with the sources that evidence them, and a decision column defaulting to "Carry through." Populated from the signal log; read by Build's `Language to preserve` field. Any other decision is the user's, recorded with their reason.
- **A STOP question surfacing recurring terms** for the user to rule on, asked only where there is a specific reason to question a term, with the reason named.
- **New failure mode: Design-phase terminology substitution.** Recorded in `SKILL.md`'s failed-attempts.

### Driven by
The v1.9.0 test found the flattening instruction one phase upstream of the rules that were supposed to prevent it. In the Make Good library's proposal, an ownership-table note instructed Build to replace the organization's term for its own role with a generic phrase; the shipped module opens with that exact substitute. Build had not drifted — Design had decided, and Build executed correctly.

## [1.9.0] — 2026-08-10

### Changed
- **Verbatim source language is permitted where a module names or illustrates.** `ARCHITECTURE.md`'s "Do NOT include" list opened with "Verbatim quotes (synthesize the meaning instead)," restated in nine further places. The rule was right about *reported speech* — "the team mentioned that," a name attached to organizational reasoning — and wrong about *phrasing*. Both failed under one prohibition, so the organization's own terms for itself were paraphrased away along with the speaker framing. Reported speech and named individuals remain prohibited, with their rationale now stated: a runtime agent has no referent for a person it was never introduced to, and proper nouns anchor prose to personalities rather than teaching a way of thinking.
- **"What to extract" gains a fifth category: distinctive terminology and self-characterization.** The closed four-item list (facts, principles, processes, positions) had no slot for what an organization calls itself, so that language was discarded before any rule about quotes applied. This was the deeper cause; the quote ban was the visible one.
- **The transcript-transformation worked example is now three-way.** It previously showed right-vs-reported-speech and concluded "it's just transcription with quotation marks," teaching that quotation marks are the defect. A flattened counter-example is now shown alongside, and the lesson is stated: reported speech fails on its framing, flattening fails by saying the same thing in nobody's words, and the correct version keeps the organization's terms inside instruction shape.
- **`validate_library.py` duplication check is advisory and excludes quoted spans.** It exact-matched normalized five-word sentence prefixes and exited non-zero, so the same preserved term in two modules failed the build while a paraphrase of it passed silently. Single source of truth is enforced upstream by the proposal's Ownership and Use-Shape table; this check is a prompt to consult that table, not a gate.

### Added
- **Sixth section shape: naming/illustration.** A section carrying the organization's idiom had no shape to be committed to and would fail self-check 1. Added to the shape hierarchy in `ARCHITECTURE.md` and to all three enumerations in the Section Plan and Substantive Source Surface.
- **`Language to preserve` field in the Substantive Source Surface.** Verbatim is now a planned commitment, parallel to shape — never a write-time impulse. Quote exactly, keep it short, and "none" is a common and legitimate answer.
- **EXTRACT / PRESERVE branch in the Section Plan's quote handling.** The field had one outcome; it now has two, and the choice is made before prose exists.
- **The signal log joins the Phase 4 session loading gate.** Phase 2 captured distinctive vocabulary verbatim (`COMPREHENSION_TEMPLATES.md`, "Distinctive vocabulary"; signal-log entries typed `recurring vocabulary`) and Build loaded no comprehension artifacts at all, so the terms were captured and never reached the builder. Loaded as an index, not as material to write from — the source is still re-read in the same turn.
- **Self-check 14: run S0's practitioner-voice gate against the module's own prose.** The skill ships S0 — which tells runtime agents to write in a practitioner's vocabulary and sentence rhythms — and applied no prose standard to the modules it writes. A module is prose an agent reads on every task; prose that reads as machine-generated teaches a machine register that every downstream output inherits.
- **New failure mode: language flattening.** Recorded in `SKILL.md`'s failed-attempts and the Phase 4 failure-mode list. The library previously had no vocabulary for "modules lost the organization's voice," so the failure could not be named, diagnosed, or routed.

### Driven by
A built library was measured against its own sources: 14 modules from 54 source files and ~129,000 tokens of organizational material contained **zero preserved human sentences**. Every blockquote was a cross-reference pointer. A source transcript that explicitly asked for a term to survive — *"I need to make sure we don't have an AI model that, when it's helping me edit, edits out the things I explicitly say"* — produced a module with that term paraphrased away.

The token argument ran backwards from expectation: module prose used 46 words to state what the source stated in 16. Preserving language is cheaper than paraphrasing it, and the paraphrase is what carries no voice.

## [1.8.1] — 2026-07-20

### Changed
- **Seed default bumped to `S0_BACKSTOP: 1.1.0`.** `templates/guardrails.lock` now seeds new libraries at the first harvest-measured backstop (upstream `s0-backstop-v1.1.0`, 2026-07-20 Opus 4.8 + Sonnet 5 pass), and `templates/guardrails/S0_backstop.md` reference copy refreshed to the 1.1.0 compiled-artifact body. No tooling change — `build-deploy-bundles.py` is unchanged (still `SCRIPT_VERSION` 1.8.0), so no migration is required; existing libraries adopt the new backstop the normal way, `--update-guardrails S0_BACKSTOP=1.1.0`. F0 (2.0.0) and S0 core (2.0.1) seed defaults are unchanged.

### Driven by
The first real harvest replacing recollection with measurement — the point of the whole system. Upstream: makegood-guardrails s0-backstop-v1.1.0.

## [1.8.0] — 2026-07-15

### Added
- **S0-backstop splice support in `build-deploy-bundles.py`.** S0 2.0.0 upstream splits into a durable core (gates) and the independently versioned `s0-backstop` artifact — the current-generation prose-signature list, maintained by measurement rather than recollection (see makegood-guardrails' `HARVEST_PLAN.md` for the harvest protocol). The lock gains an `S0_BACKSTOP` key; `--resolve-guardrails` fetches core and backstop at their respective tags and splices the backstop body (frontmatter stripped) into the vendored S0 between `BACKSTOP:BEGIN/END` markers. Agents still receive a single S0 file; only the tooling knows it's composed. Libraries pinned to S0 1.x resolve unchanged through the legacy path. `--update-guardrails S0_BACKSTOP=<ver>` may *add* the key to a lock that lacks it (the one guardrail a library legitimately adds after the fact); `--check` verifies a composed S0 by re-composing core + backstop at their locked tags.
- **`--check` upstream-newer notice.** One `git ls-remote` (no clone) compares each declared guardrail version against the highest semver tag upstream and prints report-only `[NEWER]` lines with the exact `--update-guardrails` command to adopt. Stale libraries surface themselves; adoption stays deliberate — the notice never fails the run and nothing auto-updates.
- **Migration `s0-backstop-splice` (1.7.x → 1.8.0)** in PHASE_M_MIGRATION.md. Script-refresh only (no artifact-shape change); triggered by the generic tooling-stale signal. Includes an interactive post-migration offer to adopt F0 2.0.0 / S0 2.0.1 / s0-backstop 1.0.0, kept distinct from the migration per the migration-vs-update principle.

### Changed
- **`templates/guardrails.lock`** seeds new libraries at F0 2.0.0 / S0 2.0.1 / S0_BACKSTOP 1.0.0.
- **`templates/guardrails/` reference copies refreshed** to F0 2.0.0 and S0 2.0.1, plus a new `S0_backstop.md` reference copy.
- **`SCRIPT_VERSION` → 1.8.0.**

### Driven by
The 2026-07-15 guardrails audit: S0's backstop list was authored from recollection of what AI prose sounds like — stale by construction (training-cutoff staleness plus a model's partial blindness to its own generation's tics). Splitting the volatile list from the durable gates gives harvest-measured updates a versioned artifact to land in, distributed through the existing lock pipeline. Upstream releases: makegood-guardrails f0-v2.0.0, s0-v2.0.1, s0-backstop-v1.0.0.

## [1.7.0] — 2026-06-16

### Added
- **Guardrails (F0/S0) are now a pinned versioned dependency, not hand-copied files.** F0_agent_behavioral_standards and S0_natural_prose_standards are owned by a separate repository, [makegood-guardrails](https://github.com/WeMakeGood/makegood-guardrails), which publishes them as independently semver-tagged modules. A library declares the versions it uses in a `guardrails.lock` at its root and vendors them into `modules/`. This removes the drift that hand-copied guardrails accumulate across many libraries, makes each library's guardrail version an explicit recorded fact, and makes adopting a guardrail change (e.g. a new process gate) a deliberate, auditable bump rather than a silent edit. See ARCHITECTURE.md, "Guardrails as a Versioned Dependency."
- **`build-deploy-bundles.py` gains guardrail resolution.** `--resolve-guardrails` fetches the declared versions and vendors them into `modules/` with a `GENERATED` banner; `--update-guardrails KEY=VERSION` is the deliberate upgrade (bump declared + re-resolve); `--check` additionally reports (report-only) when a vendored guardrail has been hand-edited away from its locked version. The default bundle build is unchanged and stays fully offline — resolution is a separate network step.
- **`templates/guardrails.lock`** (new template). Copied into a new library's root during Phase 4; pins the F0/S0 versions to vendor.
- **Phase M migration `guardrails-versioning` (1.6.x → 1.7.0).** Converts an existing hand-owned-guardrails library to the versioned-dependency system. Zero-behavior-change: it matches the library's current F0/S0 to an upstream version and pins that. One interactive judgment — when a library's guardrails were hand-edited and match no upstream version, the migration stops and surfaces the fork rather than silently overwriting. Bootstrap detects the signal (F0 present, no `guardrails.lock`) and offers the migration. The migration has a second path (case b) for libraries already on the system whose vendored build script is stale — it refreshes only the script.
- **The build script is now a version-locked artifact.** `build-deploy-bundles.py` carries a `SCRIPT_VERSION` (reported by `--version`) tied to the skill version. A library's `build-state.md` records both the skill version it was built with and the vendored script version (new "Skill & Tooling Version" block). This closes a drift class the rest of the system otherwise left open: a library can be fully current on artifact *shapes* yet carry a stale build script. The bootstrap now treats a recorded-version-behind (or a missing version block) as a migration signal, and migrations refresh the vendored script as a general responsibility — so the skill keeps each library's tooling current rather than the library refreshing itself.

### Changed
- **Phase 4 build sequence** now vendors guardrails (copy `guardrails.lock`, run `--resolve-guardrails`) before building bundles. The build fails loudly if the guardrails repo is unreachable rather than producing a library whose agents reference missing F0/S0.
- **`templates/guardrails/F0` and `S0` are now reference-only**, not the seed — kept for the worked-example shape lesson and offline inspection, clearly labeled. Libraries vendor from makegood-guardrails. (This also corrects a `module_id: F#` typo that the old seed would have propagated into new libraries.)

### Dependencies
- The guardrail subcommands of `build-deploy-bundles.py` require **PyYAML**. The import is deferred and guarded — the default bundle build (and `--all-inclusive`) still run with no external dependencies; only `--resolve-guardrails` / `--update-guardrails` / guardrail drift in `--check` need it, and they fail with an install hint if it's absent.
- Builds and the 1.7 migration require **network access** to the makegood-guardrails repo. Resolution is the only networked step; a built library rebuilds bundles fully offline thereafter.

## [1.6.0] — 2026-05-07

### Added
- **`@`-include + build-script delivery for always-load content.** Agent files now declare always-load items as `@`-include directives in a `## Required Reading` section. Claude Code expands `@` directives natively at load time. For runtimes that don't process `@` (Claude.ai project upload, Cowork, generic API integrations), the bundled `build-deploy-bundles.py` script resolves directives offline into self-contained `deploy/agents/<name>.md` bundles. Always-load content reaches the agent's system prompt from turn one regardless of runtime — the agent never participates in always-load delivery.
- **`--all-inclusive` bundle variant.** For runtimes where work-time fetch of conditional addenda is unreliable, the build script supports an `--all-inclusive` flag that produces `deploy/agents/<name>.all-inclusive.md` — bundles that inline every conditional addendum's content alongside required-reading content. The Conditional Loads table is preserved so the agent retains per-work selectivity over already-loaded content. Trade-off: token weight on every turn vs. runtime independence from fetch reliability. Documented as the fallback variant; standard bundle remains the default.
- **`## Ask the [Role]` escalation block in agent definitions.** Renders the agent-needs synthesis's escalation triggers (situations where the agent should defer rather than answer). Phase 3 commits a library-wide role name ("Engagement Principal," "Engagement Lead," "Project Sponsor," "User," etc.) used in every agent file's escalation block.
- **Escalation triggers in agent-needs synthesis.** Phase 2 Pass 2's `agent-needs.md` artifact gains an "Escalation triggers" section per agent — patterns surfaced from sources where the right move is deferral, distinct from reach-beyond mechanics.
- **`templates/build-deploy-bundles.py`** (vendored). Self-contained Python script (~250 lines) with no external dependencies. Resolves `@`-includes recursively (cycle detection, depth limit), handles both standard and all-inclusive variants, supports `--check` for drift detection in CI.
- **`templates/library-README.md`** (deployment doc). Copied into output libraries during Phase 4 to explain the bundle approach for library consumers — when to use the standard bundle, when to use the all-inclusive variant, how to rebuild after edits.
- **`agent-include-and-bundles` migration (1.5.x → 1.6.0)** in PHASE_M_MIGRATION.md. Mostly mechanical — the YAML manifest carries everything the new shape needs, including `load_when:` triggers. Pre-1.5 libraries run both migrations in sequence (1.4.x → 1.5.0, then 1.5.x → 1.6.0); the bootstrap presents this as a single user-facing migration plan.

### Changed
- **Agent definition shape rewritten.** Frontmatter shrinks to identity-only (agent_name, agent_domain, purpose, last_updated). The previous `always_load:` / `conditional:` YAML blocks are removed — they were declarative manifests no runtime processed as instruction. The previous `## Your Context` descriptive section (which named what each module gave the agent) is removed — module purpose surfaces from each module's own `## Purpose` section at expansion time. The runtime artifacts are `## Required Reading` (`@`-directives, no surrounding prose) and `## Conditional Loads` (table with one row per file).
- **`count_tokens.py` parser updated.** Reads `## Required Reading` and `## Conditional Loads` from the agent file body instead of YAML frontmatter. Detects both pre-1.5 (tier-grouped) and 1.5 (YAML-block) formats and refuses with a pointer to the migration phase. Detects malformed Required Reading sections (missing or no `@`-directives) and refuses.
- **Phase 4 build flow.** Agent-writing step now copies `templates/build-deploy-bundles.py` into `<OUTPUT_PATH>/scripts/`, adds `deploy/` to `.gitignore`, runs the script to verify bundles build cleanly, and copies `templates/library-README.md` into the library README. Final Validation adds `build-deploy-bundles.py --check` for drift detection.
- **Phase 3 GATE** records the library-wide escalation role name decision in build-state.

### Removed
- The YAML `always_load:` / `conditional:` frontmatter blocks. The classification reasoning lives in Phase 3's table (in the proposal); the runtime artifacts are `@`-directives and the conditional table.
- The `## Your Context` and `### Always Loaded` / `### Conditional` descriptive body sections. They duplicated the manifest and produced the prose-mirror failure mode.

### Driven by
A production failure where agents in non-`@`-aware runtimes (notably Claude.ai project upload) treated the YAML manifest as metadata the runtime didn't process, and the prose mirror ("read these files before responding") as discretionary tool work the agent could choose to skip, batch, or partially execute. Always-load content didn't reach the system prompt reliably. The 1.5 classification was correct; the artifact didn't deliver the content. The `@`-include + bundle approach removes the agent and the runtime's RAG/retrieval mechanisms from the always-load delivery path entirely. See SKILL.md, "Failed Attempts" → "Always-load classification correct, delivery mechanism unreliable," and ARCHITECTURE.md, "Always-Load Delivery."

## [1.5.0] — 2026-05-07

### Added
- **Load-discipline classification.** Agent manifests now use `always_load:` and `conditional:` (with `load_when:` triggers per conditional item) instead of tier-grouped lists. Container (module vs. addendum) and load discipline are independent dimensions. Per-agent classification: the same item can be always-load for one agent, conditional for another.
- **F0/S0 hard rule.** F0 (behavioral standards) and S0 (natural prose standards) are always-load whenever they appear in any agent's set, enforced at three layers (Phase 3 gate, Phase 4 self-check, `count_tokens.py` validation).
- **Trigger Discipline.** `load_when:` triggers must name a single diagnostic axis (audience type, task type, content type, domain), use plain "when X" phrasing, and reference the work rather than the agent's judgment about the work.
- **Load-Discipline Classification table** in Phase 3, sibling to the Ownership and Use-Shape table — every (item, agent) pair classified.
- **Migration phase (`PHASE_M_MIGRATION.md`).** Versioned, append-only migration loaded on demand when the bootstrap detects format mismatches. Ships with the 1.4 → 1.5 agent-manifest migration.

### Changed
- **`count_tokens.py` rewritten.** Parses always-load/conditional, sums tokens from always-load items only, hard errors on F0/S0 in conditional or on old-format manifests.
- **Token-budget rule.** Always-load items count toward the 10% per-agent budget regardless of container; conditional items don't count. Earlier rule confused container with load discipline.
- **Bootstrap scan** detects pre-1.5 manifest patterns and offers migrate/proceed/redo branching.

### Driven by
A production failure where agents skipped loading items they judged unnecessary, including S0 (prose standards) and A0 (legal-entity reference data), and produced output that violated those items' standards. Pre-1.5 left load decisions to runtime judgment; this version makes them a structural commitment.

## [1.4.2] — 2026-04-19

### Added
- **Per-module Section Plan** committed before prose generation. Section shape, owned-content use-shape, and reasoning extraction all decided in the plan, written to `_scratch/[module-id]-plan.md`.
- **Substantive Source Surface** (Phase 4 Step 4) requiring patterns from just-read sources rather than comprehension shorthand. Includes a sector-genericity test.
- **Failure-recovery protocol.** When a module fails, name the failure mode, locate the upstream planning step, redo the planning step, regenerate from the corrected plan.
- **Redo-session protocol** with physical separation: retrospective documents and prior-attempt artifacts move to `_retrospective_archive/` before a redo begins. Bootstrap detects redo signals automatically.
- **Phase 2 split into Pass 1 (Recognition) and Pass 2 (Synthesis)** with mandatory session break. Eight comprehension artifacts written to `_comprehension/`, including cross-domain parallels, expectations-vs-findings, and per-source notes.
- **Initial Expectations per agent role** in Phase 1 — comparator Pass 1's expectations-vs-findings reflection needs.
- **Generalization Check** in Phase 3 STOP — asks whether the proposed architecture is right for this organization or only for prior builds.
- **Worked examples** in `COMPREHENSION_TEMPLATES.md` using a generic fictional organization.

### Changed
- **Runtime-perspective frame** established upstream of writing (Phase 4 Step 1) so build-perspective contamination is caught during planning, not self-check.
- **Proposal table** changed from "Shared Source Ownership" to "Ownership and Use-Shape" — every using module commits to one of four shapes (cross-reference, subset, invocation by name, reach-beyond). Restatement is not a shape.
- **Build-state discipline restored** — terse status only; substantive content lives in `process-log`, `_comprehension/`, or `_scratch/`.
- **Session architecture:** 3 sessions (was 2). Setup + Pass 1 in Session A, Pass 2 + Design in Session B, Build in Session C.

### Driven by
Two failed Phase 4 builds in production that exposed architectural failure modes the prior skill documented but did not prevent. This version restructures the skill so the patterns become hard to produce, not just warned against.

---

[1.6.0]: https://github.com/WeMakeGood/building-context-libraries/releases/tag/v1.6.0
[1.5.0]: https://github.com/WeMakeGood/building-context-libraries/releases/tag/v1.5.0
[1.4.2]: https://github.com/WeMakeGood/building-context-libraries/releases/tag/v1.4.2
