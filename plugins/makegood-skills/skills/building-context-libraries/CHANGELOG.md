# Changelog

All notable changes to this skill are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this skill follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

[1.5.0]: https://github.com/WeMakeGood/building-context-libraries/releases/tag/v1.5.0
[1.4.2]: https://github.com/WeMakeGood/building-context-libraries/releases/tag/v1.4.2
