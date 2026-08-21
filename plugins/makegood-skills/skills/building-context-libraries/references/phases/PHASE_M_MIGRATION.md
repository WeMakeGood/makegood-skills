# Phase M: Migration

> **CRITICAL RULES — Read these first:**
> - This is a one-time, opt-in phase loaded only when the bootstrap detects format mismatches between artifacts on disk and the current skill version.
> - Migrations are **versioned**. Each migration brings artifacts from one specific format version to the next. The migration set ships with named migrations applied in order.
> - Migrations are **interactive where they require judgment**. Format-mechanical changes can run automatically; classification or content changes that depend on per-library reasoning require user input.
> - Migrations are **bounded**. Phase M does not refactor content, restructure architecture, or rewrite modules. It transforms artifact shapes to the current skill version's expected shapes. Substantive rebuilds belong to a redo session, not a migration.

---

## Contents

- What This Phase Does
- When This Phase Runs
- Migration Index
- Migration Session Setup
- Migration: agent-manifest-load-discipline (1.4.x → 1.5.0)
- Migration: agent-include-and-bundles (1.5.x → 1.6.0)
- Migration: guardrails-versioning (1.6.x → 1.7.0)
- Migration: g2-backstop-splice (1.7.x → 1.8.0)
- Migration: guardrail-g-namespace (1.9.x → 1.10.0)
- Migration: script-version-refresh (1.10.x → 1.11.0)
- After Migration
- Adding a New Migration

---

## What This Phase Does

Brings library artifacts to the current skill version when the bootstrap detects format mismatches. The phase is invoked only when needed, runs its applicable migrations in order, and returns control to the bootstrap.

The migration set is **append-only**. New format changes ship as new migrations; existing migrations are not rewritten. A library being upgraded across multiple versions runs each applicable migration in sequence.

---

## When This Phase Runs

The bootstrap (TEMPLATES.md, "Session Bootstrap") detects migration signals during its directory scan. If signals are present and the user chooses **migrate**, the bootstrap loads this phase before continuing.

Migration is distinct from redo:

- **Redo session** = a previous attempt was rolled back; physical separation of prior-attempt artifacts (modules, plans, comprehension, retrospectives) into `_retrospective_archive/` so the new attempt regenerates from sources.
- **Migration** = artifacts on disk are correct but use an outdated format; the migration transforms shapes to current version, preserving the content.

A library can need both. If it does, run migration first (so subsequent redo work uses current shapes), then redo.

---

## Migration Index

Each migration has: a name, a from-version, a to-version, what triggers it, and the steps it runs. Migrations are applied in order from the library's current version to the skill's current version.

**Skill versions and the migrations between them:**

| From | To | Migration Name | Trigger |
|------|-----|----------------|---------|
| 1.4.x | 1.5.0 | `agent-manifest-load-discipline` | Agent manifests use tier-grouped `modules:` (foundation/shared/specialized) and separate `addenda:` |
| 1.5.x | 1.6.0 | `agent-include-and-bundles` | Agent files use `always_load:` / `conditional:` YAML frontmatter blocks |
| 1.6.x | 1.7.0 | `guardrails-versioning` | Library has a hand-owned behavioral-standards module (`F0_` pre-rename, `G1_` after) in `modules/foundation/` but no `guardrails.lock` at the root (hand-owned guardrails, not yet a versioned dependency) |
| 1.7.x | 1.8.0 | `g2-backstop-splice` | Build-state records a skill/script version behind 1.8.0 (the generic tooling-stale signal — no artifact-shape change; the 1.8 script adds G2-backstop splice support and the `--check` upstream-newer notice) |
| 1.9.x | 1.10.0 | `guardrail-g-namespace` | `guardrails.lock` declares `F0`, `S0`, or `S0_BACKSTOP` keys, and/or `modules/foundation/F0_agent_behavioral_standards.md` / `modules/shared/S0_natural_prose_standards.md` exist |
| 1.10.x | 1.11.0 | `script-version-refresh` | The vendored `scripts/build-deploy-bundles.py` reports `--version` below 1.11.0, or build-state records a script version below 1.11.0. Every library built before 1.11.0 matches, because the script's `SCRIPT_VERSION` constant was stale from 1.8.0 through 1.10.0 |

When a new migration ships, add a row above. Migrations below this point are the actual migration content, in version order.

**A library several versions behind runs every applicable migration in sequence**, in Migration Index order. Read the applicable set off the index above rather than reciting a sequence — the set grows with each release, and a hard-coded chain goes stale silently the next time one ships. The bootstrap presents the plan as a single user-facing operation; internally it is separate migrations applied in order, which preserves the append-only architecture.

---

<phase_migration_session_setup>
## Migration Session Setup

**Step 0: Load the relevant context.**

1. Read the current skill version's [SKILL.md](../../SKILL.md), [ARCHITECTURE.md](../ARCHITECTURE.md), and [TEMPLATES.md](../TEMPLATES.md). Migrations transform artifacts to match these.
2. Read `<OUTPUT_PATH>/build-state.md` — confirm the library's current state and the user's stated migration intent.
3. Read this file (PHASE_M_MIGRATION.md).

**Step 1: Identify the applicable migrations.**

Detect which migration(s) apply based on the bootstrap's findings:

- Check each agent file in `<OUTPUT_PATH>/agents/` for the trigger pattern of each migration in the index above.
- For each agent file, list which migrations apply.
- Confirm with the user: "I will run [N] migrations: [list]. Each migration is a one-way transformation. Proceed?"

**STOP.** Wait for user confirmation before running any migration.

**Step 2: Pre-migration backup.**

Before running migrations, copy the artifacts that will change to `<OUTPUT_PATH>/_pre_migration_backup/`. The backup is a safety net; the migration is meant to succeed, but a backup makes errors recoverable.

Confirm the backup is complete before proceeding.
</phase_migration_session_setup>

---

## Migration: agent-manifest-load-discipline (1.4.x → 1.5.0)

**Trigger:** Agent file frontmatter contains `modules:` with `foundation:` / `shared:` / `specialized:` subkeys, or contains a top-level `addenda:` list.

**What this migration does:** Replaces the tier-grouped `modules:` field and the separate `addenda:` list with a unified `always_load:` / `conditional:` classification. The classification depends on per-agent reasoning (does this item govern *every* output this specific agent produces?) and cannot be done mechanically — the migration is interactive.

### Why this migration is required

The pre-1.5 manifest format produced a documented runtime failure: agents skipped loading items they judged unnecessary for the immediate task, then produced output that violated those items' standards. The classification removes the runtime judgment by naming `always_load` items explicitly. See SKILL.md, "Failed Attempts" → "Manifest classification leaving load decisions to runtime judgment."

### Steps

For each agent file with the trigger pattern:

**M1.1: Parse the existing manifest.**

- Read the agent file.
- Extract the full set of items: every module under `modules.foundation`, `modules.shared`, `modules.specialized`, and every entry under `addenda`.
- Note the agent's purpose, domain, and role from the frontmatter and body — these inform classification reasoning.

**M1.2: Apply hard-rule classifications.**

Without asking the user:
- `G1_agent_behavioral_standards` → `always_load` (hard rule, no exceptions)
- `G2_natural_prose_standards` → `always_load` if present in this agent's set (hard rule for any agent that writes anything)

**M1.3: Classify remaining items interactively.**

For each remaining item, present to the user:

```
Agent: [agent name]
Item: [item name]
Container: [module | addendum]
Original tier (if module): [foundation | shared | specialized]
Item purpose (from item's frontmatter or first paragraph): [purpose]

Classification options:
- always_load: this item governs every output this agent produces
- conditional: this item applies only in specific task or audience contexts

Recommended classification: [recommendation based on heuristics, see below]
Recommended load_when: [if conditional, a draft trigger to refine]

Your classification: [user input]
Your load_when: [if conditional, user input]
```

**Heuristics for the recommendation:**

- Foundation modules (F1, F2, F3) — recommend `always_load` (they typically describe organizational identity / verification discipline / voice that governs every output).
- Reference addenda containing universal organizational data (legal entity, current senior leaders, project portfolio orientation) — recommend `always_load`.
- Shared modules — recommend based on the item's purpose vs. the agent's role: is the content something every output of this agent depends on?
- Specialized modules (D-prefix) — typically `always_load` for the agent they were designed for; otherwise the agent shouldn't have it.
- Funder/cultural/region/peer/project addenda — recommend `conditional` with a `load_when:` trigger drafted from the item's name (e.g., `funders/A_funder_climate` → "Work is anchored in climate-focused foundations as the funder type").
- Sector / methodology addenda whose content is volatile — recommend `conditional` with a trigger drafted from the addendum's purpose.

The recommendation is a starting point for the user, not the final answer. The user's classification overrides the recommendation.

**M1.4: Validate trigger discipline.**

For each `conditional` item, verify the `load_when:` trigger meets the Trigger Discipline (one axis, plain "when X" phrasing, right-side specificity — see ARCHITECTURE.md, "Trigger Discipline").

If a trigger fails the discipline, present the failure to the user and offer to refine.

**M1.5: Verify hard rules.**

Before writing the migrated manifest:
- G1_agent_behavioral_standards in `always_load`? (Required if present in the agent's set.)
- G2_natural_prose_standards in `always_load`? (Required if present in the agent's set.)
- Every conditional item has a `load_when:` trigger?

If any check fails, fix before writing.

**M1.6: Write the migrated manifest.**

Replace the agent file's frontmatter with the new shape:

```yaml
---
agent_name: [unchanged]
agent_domain: [unchanged]
purpose: [unchanged]
always_load:
  - [classified items, in a sensible order — typically G1, F1+ foundation, G2, S1+ shared, D specialized, then always-loaded reference addenda]
conditional:
  - module: [item name]
    load_when: "[trigger]"
  - addendum: [item path]
    load_when: "[trigger]"
estimated_tokens: [recompute from always_load items only]
last_updated: [today's date — note migration in process-log]
---
```

The body of the agent file may need adjustment to mirror the manifest's classification (group items by load discipline rather than by tier). For now, leave the body's existing tier-grouped prose intact; the manifest is what governs runtime load behavior. Body restructuring is optional polish that the user can do after migration if desired.

**M1.7: Log the migration.**

In `<OUTPUT_PATH>/process-log.md`, add an entry:

```
### [YYYY-MM-DD] — Migration: agent-manifest-load-discipline (1.4.x → 1.5.0)

Migrated agent files: [list]
Hard-rule applications: [list of agents where G1/G2 was hard-rule placed in always_load]
Classification decisions requiring judgment: [list of (agent, item, classification) tuples where the user diverged from the recommendation]
Trigger refinements: [list of triggers refined for discipline]
Backup: <OUTPUT_PATH>/_pre_migration_backup/
```

If `agent-include-and-bundles` (1.5.x → 1.6.0) also applies, run it next on the now-1.5-shaped manifests.

---

## Migration: agent-include-and-bundles (1.5.x → 1.6.0)

**Trigger:** Agent file frontmatter contains `always_load:` and/or `conditional:` YAML blocks.

**What this migration does:** Replaces the YAML manifest blocks with `@`-include directives in `## Required Reading` and a triggers table in `## Conditional Loads`. Adds the deployment-bundle build script and updates the library's directory structure to support `deploy/` bundles. The transformation is mostly mechanical — the YAML manifest carries everything the new shape needs, including `load_when:` triggers — so this migration runs without per-item user input.

### Why this migration is required

The pre-1.6 manifest format produced a documented runtime failure: in non-`@`-aware runtimes (notably Claude.ai project upload), agents treated the YAML manifest as metadata the runtime didn't process and the prose mirror ("read these files before responding") as discretionary tool work the agent could choose to skip, batch, or partially execute. Always-load content didn't reach the system prompt reliably. The `@`-include shape (Claude Code expansion) plus build-script bundles (offline expansion for other runtimes) removes the agent's runtime judgment from content delivery. See ARCHITECTURE.md, "Always-Load Delivery."

### Steps

For each agent file with the trigger pattern:

**M2.1: Parse the existing manifest.**

- Read the agent file.
- Extract `always_load:` items (each as a string item identifier).
- Extract `conditional:` items (each as a `module:`/`addendum:` + `load_when:` pair).
- Note the agent's identity fields (agent_name, agent_domain, purpose, last_updated).

**M2.2: Resolve item identifiers to file paths.**

For each item identifier:
- Look up the file path. Modules: search `modules/foundation/`, `modules/shared/`, `modules/specialized/` for a file matching the identifier (e.g., `G1_agent_behavioral_standards` → `modules/foundation/G1_agent_behavioral_standards.md`).
- Addenda: the identifier typically already includes the subdirectory (e.g., `funders/A_funder_climate` → `addenda/funders/A_funder_climate.md`).

If any identifier doesn't resolve to a file, surface to the user before continuing — this signals a manifest inconsistency that predates the migration.

**M2.3: Identify or choose the escalation role name.**

Phase 3 in 1.6 commits a library-wide escalation role name ("Engagement Principal," "Engagement Lead," "Project Sponsor," "User," etc.) used in every agent file's `## Ask the [Role]` block. Pre-1.6 libraries don't have this decision recorded.

- Check `<OUTPUT_PATH>/build-state.md` for an existing role-name decision (some libraries may have one informally).
- If none, ask the user: "What role name should the agent files use in their escalation block? Common choices: Engagement Principal, Engagement Lead, Project Sponsor, User. The role name is library-wide — every agent file uses the same name."
- Record the chosen name in `build-state.md` under "Library decisions."

**M2.4: Identify existing escalation content.**

Pre-1.6 agent files often have escalation guidance in a "When to Reach Beyond Your Context" section under "Ask the user" subsection. Extract those bullets — they become the `## Ask the [Role]` block content in the new shape.

If an agent file has no existing escalation content, leave the new block with a placeholder note: `[Escalation triggers — populate from agent-needs.md or ask the user]`. The user can fill these in post-migration.

**M2.5: Write the migrated agent file.**

Replace the agent file with the new shape:

```markdown
---
agent_name: [unchanged from old frontmatter]
agent_domain: [unchanged]
purpose: "[unchanged]"
last_updated: [today's date]
---

# [Agent Name — unchanged from old body]

[Identity paragraph — unchanged from old body]

## Required Reading

@modules/foundation/G1_agent_behavioral_standards.md
@[resolved path for each always_load item, in the same order as the old YAML]
...

## Conditional Loads

Load the file when its trigger applies to the work at hand.

| File | Load when |
|------|-----------|
| `[resolved path]` | [load_when trigger from old YAML] |
| ... | ... |

## Ask the [Role chosen in M2.3]

Escalate when you encounter:

- [each bullet extracted in M2.4]

## Domain Guidelines

[unchanged from old body — Do/Don't lists]

<!-- BUILD METADATA (preserved from old body if present, or regenerated)
Token Budget:
- Always-loaded items total: [recompute from new always-load set]
- Per-agent budget: [unchanged]
- Utilization: [recompute]
- Conditional items: not counted (loaded only when triggered)
- Budget assessment: [recompute]

Item Rationale:
[preserved from old body if present; otherwise note "rationale not present in pre-1.6 file"]

Build Notes:
- 2026-XX-XX migration: agent-include-and-bundles (1.5.x → 1.6.0). YAML manifest replaced with @-includes + table. Escalation role name: [chosen name].
-->
```

The previous body sections — `## Your Context`, `### Always Loaded`, `### Conditional`, `## When to Reach Beyond Your Context` — are removed. They duplicated the manifest and (in the case of "Always Loaded") were the prose mirror that produced the discretionary-tool-work failure mode.

**M2.6: Drop in the build script.**

- Copy `templates/build-deploy-bundles.py` from the skill into `<OUTPUT_PATH>/scripts/build-deploy-bundles.py`.
- Add `deploy/` to the library's `.gitignore` (create the file if it doesn't exist).

**M2.7: Build the bundles.**

Run `cd <OUTPUT_PATH> && scripts/build-deploy-bundles.py` to produce the standard bundles. If any `@`-directive fails to resolve, the script reports the missing target — fix the agent file (typically a path mismatch from M2.2) and re-run.

Optionally run `scripts/build-deploy-bundles.py --all-inclusive` to produce the all-inclusive variants. Skip unless the user has a runtime that needs them.

**M2.8: Drop in the library README.**

- Copy `templates/library-README.md` from the skill into `<OUTPUT_PATH>/README.md`. If a README already exists, copy the deployment-doc content as a new section rather than overwriting.

**M2.9: Update count_tokens.py expectations.**

The new count_tokens.py (1.6) parses agent files by reading the `## Required Reading` and `## Conditional Loads` sections rather than YAML frontmatter. Run it once: `python scripts/count_tokens.py <OUTPUT_PATH>/modules <OUTPUT_PATH>/agents`. If it reports parse errors, the agent file's section structure is malformed — return to M2.5 and fix.

**M2.10: Log the migration.**

In `<OUTPUT_PATH>/process-log.md`, add an entry:

```
### [YYYY-MM-DD] — Migration: agent-include-and-bundles (1.5.x → 1.6.0)

Migrated agent files: [list]
Escalation role name chosen: [name]
Agents with placeholder escalation blocks (post-migration follow-up needed): [list, if any]
Build script installed: scripts/build-deploy-bundles.py
Bundles built: [count] standard bundles in deploy/agents/
All-inclusive bundles built: [count, or "not built — defer until runtime requires"]
Backup: <OUTPUT_PATH>/_pre_migration_backup/
```

---

## Migration: guardrails-versioning (1.6.x → 1.7.0)

**Trigger (either):**
- **(a) Not yet converted:** the library has a hand-owned behavioral-standards module in `modules/foundation/` (`F0_agent_behavioral_standards.md` pre-rename, `G1_` after) but no `guardrails.lock` at its root — guardrails are hand-owned copies, not a versioned dependency. Run the full migration (M3.1–M3.7).
- **(b) Converted but tooling stale:** the library already has a `guardrails.lock` and vendored guardrails, but its build-state records a script/skill version behind the running skill (or its on-disk `scripts/build-deploy-bundles.py --version` is behind). Only the vendored script needs refreshing. Run the **script-refresh-only path**: skip M3.1–M3.3 and M3.5 (the lock and vendored modules are already correct), run **M3.4** (refresh the script + update build-state versions), then **M3.6** (rebuild bundles) and **M3.7** (log). This is a legitimate migration whose only effect is bringing the version-locked script current.

**What this migration does:** For case (a), converts the library from owning hand-copied G1/G2 modules to consuming them as a pinned, vendored dependency from `makegood-guardrails` — introduces `guardrails.lock`, refreshes the build script, and re-vendors G1/G2 at the version the library already effectively runs, so it is **zero-behavior-change**. For case (b), refreshes only the version-locked build script. In neither case does the migration change which guardrail *version* the agents run; adopting a newer version (e.g. for a new process gate) is a separate, deliberate `--update-guardrails` afterward.

This migration has one interactive judgment in case (a) (matching the library's current G1/G2 to an upstream version); the rest is mechanical, and case (b) is fully mechanical.

### Why this migration is required

Before 1.7, every library carried its own hand-copied G1/G2. Across many libraries these copies drifted — the same guardrail existed in incompatible versions with no record of which library ran which, and no way to propagate a fix without editing every copy by hand. The versioned-dependency model makes the guardrail version an explicit, recorded fact per library (`guardrails.lock`) and makes adopting a change a deliberate, auditable bump rather than a silent hand-edit. See ARCHITECTURE.md, "Guardrails as a Versioned Dependency."

### Steps

**M3.1: Back up the current guardrail modules.**

Copy `modules/foundation/G1_agent_behavioral_standards.md` and `modules/shared/G2_natural_prose_standards.md` (and any other present guardrail modules) into `<OUTPUT_PATH>/_pre_migration_backup/`. This is the recovery point — the migration overwrites these files with vendored copies.

**M3.2: Match the library's current guardrails to an upstream version. (Interactive — this is the judgment step.)**

For G1 and G2 separately:
- Compare the library's current module body (frontmatter and banners aside) against the tagged versions in `makegood-guardrails`. The simplest check: for each candidate tag, fetch the upstream module and diff its body against the library's.
- **If the body matches a tagged version exactly,** that is the version to pin — vendoring it back is a no-op on behavior. Proceed.
- **If the body matches no tag** (the library hand-edited its G1/G2), STOP and surface to the user: show the diff against the closest upstream version and present the fork — (a) pin the closest version and accept that the hand edits are dropped (the upstream version supersedes them), or (b) the hand edits are deliberate and should be carried upstream into `makegood-guardrails` as a new version before migrating. Do not guess. Local edits to a guardrail are exactly the kind of divergence this system exists to make visible, not silently overwrite.

Record the matched version per module in `build-state.md`.

**M3.3: Write `guardrails.lock`.**

Copy `templates/guardrails.lock` into `<OUTPUT_PATH>/guardrails.lock`. Set `declared:` G1 and G2 to the versions matched in M3.2 (not necessarily the skill's defaults — the point is to preserve current behavior). Leave the `resolved:` shas as `null`; the next step fills them.

**M3.4: Refresh the version-locked build script.**

The build script is a skill-versioned artifact: each library vendors a copy, and that copy can fall behind the skill the same way artifact shapes can. **Any migration refreshes the vendored script as part of its work** — this is a general migration responsibility, not specific to this migration.

Copy `templates/build-deploy-bundles.py` into `<OUTPUT_PATH>/scripts/`, overwriting the existing one. Confirm the new version: `<OUTPUT_PATH>/scripts/build-deploy-bundles.py --version`. Then update build-state's **Vendored build-deploy-bundles.py version** and **Built with skill version** lines to the current values. (For the 1.6 → 1.7 script specifically: it adds `--resolve-guardrails`, `--update-guardrails`, and guardrail drift detection in `--check`; the bundle-build behavior is unchanged.)

**M3.5: Resolve and re-vendor.**

Run `cd <OUTPUT_PATH> && scripts/build-deploy-bundles.py --resolve-guardrails`. This fetches the matched versions, overwrites `modules/foundation/G1...` and `modules/shared/G2...` with the vendored copies (now carrying the GENERATED banner), and fills the `resolved:` shas in the lock. Needs network access to `makegood-guardrails`.

Verify: the vendored files carry the banner, and — because M3.2 matched the current version — the body below the banner is identical to the backed-up original (confirm with a diff against `_pre_migration_backup/`, ignoring the banner line). A non-trivial body diff here means the version match in M3.2 was wrong; stop and recheck.

**M3.6: Rebuild bundles.**

Run `scripts/build-deploy-bundles.py`. The only change to the bundles versus pre-migration is the banner comment and the `version:` frontmatter line in the G1/G2 sections — no behavioral content changes. Confirm `--check` reports guardrails matching the locked versions and no bundle drift.

**M3.7: Log the migration.**

Add to `process-log.md`:

```
### [YYYY-MM-DD] — Migration: guardrails-versioning (1.6.x → 1.7.0)

Converted hand-owned G1/G2 to versioned dependency from makegood-guardrails.
Pinned: G1 @ [version], G2 @ [version] (matched to library's current content — zero behavior change).
guardrails.lock written; build script updated to resolving version; modules re-vendored; bundles rebuilt.
Hand-edit resolution (if any): [none | describe the fork taken in M3.2].
Backup: <OUTPUT_PATH>/_pre_migration_backup/
```

If the user wants to additionally adopt a newer guardrail version (e.g. the latest G1 with a new process gate), that is a post-migration step: `scripts/build-deploy-bundles.py --update-guardrails G1=<newer>`, then rebuild. Keep it distinct from the migration in the log — migration = adopt the *system*; update = adopt a *version*.

---

## Migration: g2-backstop-splice (1.7.x → 1.8.0)

**Trigger:** the generic tooling-stale signal — build-state records a skill or script version behind 1.8.0, or the on-disk `scripts/build-deploy-bundles.py --version` reports < 1.8.0. There is no artifact-shape change in this migration: a 1.7 library's lock, vendored modules, agents, and bundles are all valid under 1.8 tooling.

**What this migration does:** refreshes the version-locked build script (script-refresh path, per M3.4's general responsibility). The 1.8.0 script adds:

- **G2-backstop splice support.** G2 2.0.0 upstream splits into a durable core (gates) and an independently versioned `g2-backstop` artifact (the current-generation prose-signature list, maintained by harvest — see the makegood-guardrails repo's `HARVEST_PLAN.md`). The lock gains an `G2_BACKSTOP` key; at resolve time the backstop body is spliced into the vendored G2 between `BACKSTOP:BEGIN/END` markers, so agents still receive a single G2 file. Libraries pinned to G2 1.x resolve unchanged through the legacy path.
- **`--check` upstream-newer notice.** Report-only `[NEWER]` lines when upstream has a newer tagged version than the library declares, so stale libraries surface themselves. Adoption stays deliberate.

**The migration does not change guardrail versions.** Per the migration/update distinction (M3.7): migration = adopt the *system*; update = adopt a *version*.

### Steps

**M4.1: Refresh the version-locked build script.**

As M3.4: copy `templates/build-deploy-bundles.py` into `<OUTPUT_PATH>/scripts/`, confirm with `--version` (expect 1.8.0), update build-state's **Vendored build-deploy-bundles.py version** and **Built with skill version** lines.

**M4.2: Verify nothing changed.**

Run `scripts/build-deploy-bundles.py --check`. Expected output for a library still pinned to G1 1.x / G2 1.x: guardrails match their locked versions, bundles in sync, plus `[NEWER]` notices for G1 2.0.0 / G2 2.0.1 — **the notices are informational, not drift**; they are the new script doing its job.

**M4.3: Offer the guardrail adoption (interactive — STOP for the user's decision).**

The natural post-migration step is adopting the 2026-07-15 guardrail releases, and it is a **behavioral change** requiring the user's explicit yes:

- **G1 2.0.0** (major): Gates 3–5 gain arming conditions (they no longer fire on fixed-framing, low-consequence, or instance-scoped work); new "Where the Gates Run" section (gates execute in reasoning, outputs carry products not ceremony); Gate 1's verbatim refusal template becomes a phrased-as-needed requirement.
- **G2 2.0.1** (major vs 1.x; 2.0.1 is the sector-neutrality wording patch): core/backstop split; the Practitioner Voice gate routes to a loaded voice profile first; new fourth gate "Write in the Medium's Shape."
- **g2-backstop 1.0.0**: the current-generation tic list (provisional pending first harvest).

If the user accepts:

```
cd <OUTPUT_PATH> && scripts/build-deploy-bundles.py --update-guardrails G1=2.0.0 G2=2.0.1 G2_BACKSTOP=1.0.0
scripts/build-deploy-bundles.py            # rebuild bundles
scripts/build-deploy-bundles.py --check    # confirm: guardrails ok, no drift, no NEWER
```

(`--update-guardrails` adds the `G2_BACKSTOP` declaration to the lock automatically — it is the one guardrail key a library legitimately adds after the fact.) If the user declines, the library stays pinned and fully functional; `--check` keeps reporting the `[NEWER]` notices as a standing reminder.

**M4.4: Log the migration.**

Add to `process-log.md`:

```
### [YYYY-MM-DD] — Migration: g2-backstop-splice (1.7.x → 1.8.0)

Build script refreshed to 1.8.0 (G2-backstop splice support, --check upstream-newer notice).
Guardrail versions unchanged by the migration.
Post-migration guardrail update: [declined | adopted G1 2.0.0, G2 2.0.1, g2-backstop 1.0.0 — bundles rebuilt].
```

---

## Migration: guardrail-g-namespace (1.9.x → 1.10.0)

The guardrail modules were renamed upstream: `F0` → `G1`, `S0` → `G2`, `S0_BACKSTOP` → `G2_BACKSTOP`. The `F`/`S` prefixes were context-library tier markers that meant nothing in the guardrails repo and collided with libraries using `F`/`S`/`D` for their own modules.

**This migration is optional in the strict sense** — the upstream `f0-v*` and `s0-v*` tags were retained, so an un-migrated lock keeps resolving successfully. It resolves *silently*, though: nothing tells the library that newer versions exist under different keys, because the old tags stop at F0 2.1.0 and S0 2.0.1. A library that never migrates is pinned to the pre-rename line forever.

**Steps:**

1. In `guardrails.lock`, rename the keys in both `declared` and `resolved`: `F0` → `G1`, `S0` → `G2`, `S0_BACKSTOP` → `G2_BACKSTOP`. Set versions to `G1: 3.0.0`, `G2: 3.0.0`, `G2_BACKSTOP: 2.0.0` — content-identical to F0 2.1.0 / S0 2.0.1 / backstop 1.1.0, so this is zero-behavior-change.
2. Update the `vendored:` and `spliced_into:` paths to the new filenames. **Keep the tier directories** — `modules/foundation/` and `modules/shared/` are the library's namespace, not the guardrails repo's, and the rename does not touch them.
3. Rename the vendored module files on disk to match.
4. Update every reference to the old identifiers across `modules/`, `agents/`, and `addenda/` — including `@`-include directives in Required Reading, which break silently if the path is wrong.
5. Re-vendor the build script from the skill's `templates/build-deploy-bundles.py` (1.10.0+ knows the new constants; earlier versions look for `S0_backstop.md` upstream and fail).
6. Run `--resolve-guardrails` and confirm the splice lands: the vendored G2 file should contain the backstop body between its `BACKSTOP:BEGIN/END` markers.
7. Run `validate_library.py` and confirm it still passes.

**Verification:** `--resolve-guardrails` prints a migration notice whenever it sees pre-rename keys. Its absence after migration is the signal that step 1 took.

---

## Migration: script-version-refresh (1.10.x → 1.11.0)

No artifact shape changed in 1.11.0. This migration exists because the build script's `SCRIPT_VERSION` constant went stale: it read 1.8.0 from the 1.8.0 release through 1.10.0, while the script's code changed twice in that window (the guardrail-key rename in 1.10.0, and the `--check` all-clear fix). Every library built in that window therefore records a script version that understates what it carries — and a library built with 1.9.x or earlier carries code that is genuinely behind.

The consequence is the bootstrap's tooling-stale signal reading wrong in both directions: a current library reports as stale forever, and a genuinely stale script cannot be distinguished from a current one. The migration re-establishes a truthful record.

**Steps:**

1. Check what the library carries: `<OUTPUT_PATH>/scripts/build-deploy-bundles.py --version`. Any answer below 1.11.0 means the record cannot be trusted — the constant, not the code, is what was stale.
2. Re-vendor the script from the skill's `templates/build-deploy-bundles.py`. If the library was built with 1.10.0, this is a no-op on behavior and corrects the version the script reports. If it was built earlier, it also brings the guardrail-key constants and the `--check` fix.
3. Set build-state's **Vendored build-deploy-bundles.py version** to the value `--version` now reports, and **Built with skill version** to the running skill version.
4. Run `cd <OUTPUT_PATH> && scripts/build-deploy-bundles.py --check`. Bundles built by the older script are byte-identical where the code was identical; a DRIFT report here means the earlier script produced different output and the bundles need rebuilding (`scripts/build-deploy-bundles.py`, then `--all-inclusive` if the library uses that variant).

**Verification:** `--version` reports the running skill's version, and build-state's two version lines match it. The bootstrap stops offering this migration.

**This migration is required before trusting any future tooling-stale signal.** A library that skips it keeps a false version record, and the next migration keyed to version comparison will misfire on it.

---

## After Migration

Run `python scripts/count_tokens.py <OUTPUT_PATH>/modules <OUTPUT_PATH>/agents` to confirm:
- No errors (no remaining old-format manifests, no hard-rule violations).
- All agents within budget.
- Token counts match expectations from the original manifest's `estimated_tokens` field (within reason — the new count includes always-loaded reference addenda that the old format excluded).

If the 1.5 → 1.6 migration ran, additionally confirm: `cd <OUTPUT_PATH> && scripts/build-deploy-bundles.py --check` reports no drift, and every agent has both a source file in `agents/` and a standard bundle in `deploy/agents/`.

If any check reports issues, return to the relevant migration step and correct.

**Update build-state.md:**
- Note that migration ran on [date], applied [list of migrations].
- Set **Built with skill version** and **Vendored build-deploy-bundles.py version** to the current values (confirm the script version with `scripts/build-deploy-bundles.py --version`). These are what the bootstrap reads to detect a future tooling drift.
- Reset "Current Phase" to whatever phase the user invoked migration from.

**Hand back to the bootstrap.** The bootstrap resumes from where it paused before migration.

---

## Adding a New Migration

When a new format change ships in a future skill version:

1. Add a row to the Migration Index above with the new migration's name, from-version, and to-version.
2. Add a `## Migration: [name] ([from] → [to])` section below, structured the same way as existing migrations: trigger, why required, steps, validation, log entry.
3. Add the trigger pattern to the bootstrap's directory scan (TEMPLATES.md, "Session Bootstrap" → migration signals).
4. Add detection to whichever script reads the affected artifact, and be specific about which one that is. `count_tokens.py` is the format gate for agent files — it parses Required Reading and the Conditional Loads table, and it refuses (exit 1) on a pre-1.6 manifest or a hard-rule violation. `validate_library.py` inspects modules, addenda, and agent files for structure and reports advisory findings; it does not refuse. A migration that changes agent-file shape belongs in the first; one that changes module or addendum shape belongs in the second. Saying "the validation scripts" without naming one leaves the detection unwritten.

**If the skill version bump changes the build script**, bump `SCRIPT_VERSION` in `templates/build-deploy-bundles.py` to match, and ensure the migration re-vendors the script and updates build-state's version lines (as M3.4 does generally). The script is a version-locked artifact: a library can be fully current on artifact *shapes* yet carry a stale script. That is itself a migration trigger — see the bootstrap's "build-state records a skill or script version behind the running skill" signal. A migration whose only effect is refreshing the script is legitimate; not every migration changes artifact shapes.

The migration set grows over time. Older migrations are not rewritten — a library upgrading across multiple versions runs each applicable migration in sequence.
