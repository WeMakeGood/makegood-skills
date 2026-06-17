# Changelog

All notable changes to this skill are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this skill follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
