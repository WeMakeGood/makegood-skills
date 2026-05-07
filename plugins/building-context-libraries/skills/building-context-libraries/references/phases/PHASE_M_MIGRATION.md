# Phase M: Migration

> **CRITICAL RULES — Read these first:**
> - This is a one-time, opt-in phase loaded only when the bootstrap detects format mismatches between artifacts on disk and the current skill version.
> - Migrations are **versioned**. Each migration brings artifacts from one specific format version to the next. The migration set ships with named migrations applied in order.
> - Migrations are **interactive where they require judgment**. Format-mechanical changes can run automatically; classification or content changes that depend on per-library reasoning require user input.
> - Migrations are **bounded**. Phase M does not refactor content, restructure architecture, or rewrite modules. It transforms artifact shapes to the current skill version's expected shapes. Substantive rebuilds belong to a redo session, not a migration.

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

When a new migration ships, add a row above. Migrations below this point are the actual migration content.

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
- `F0_agent_behavioral_standards` → `always_load` (hard rule, no exceptions)
- `S0_natural_prose_standards` → `always_load` if present in this agent's set (hard rule for any agent that writes anything)

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
- F0_agent_behavioral_standards in `always_load`? (Required if present in the agent's set.)
- S0_natural_prose_standards in `always_load`? (Required if present in the agent's set.)
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
  - [classified items, in a sensible order — typically F0, F1+ foundation, S0, S1+ shared, D specialized, then always-loaded reference addenda]
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
Hard-rule applications: [list of agents where F0/S0 was hard-rule placed in always_load]
Classification decisions requiring judgment: [list of (agent, item, classification) tuples where the user diverged from the recommendation]
Trigger refinements: [list of triggers refined for discipline]
Backup: <OUTPUT_PATH>/_pre_migration_backup/
```

---

## After Migration

Run `python scripts/count_tokens.py <OUTPUT_PATH>/modules <OUTPUT_PATH>/agents` to confirm:
- No errors (no remaining old-format manifests, no hard-rule violations).
- All agents within budget.
- Token counts match expectations from the original manifest's `estimated_tokens` field (within reason — the new count includes always-loaded reference addenda that the old format excluded).

If the script reports issues, return to the relevant migration step and correct.

**Update build-state.md:**
- Note that migration ran on [date], applied [list of migrations].
- Reset "Current Phase" to whatever phase the user invoked migration from.

**Hand back to the bootstrap.** The bootstrap resumes from where it paused before migration.

---

## Adding a New Migration

When a new format change ships in a future skill version:

1. Add a row to the Migration Index above with the new migration's name, from-version, and to-version.
2. Add a `## Migration: [name] ([from] → [to])` section below, structured the same way as existing migrations: trigger, why required, steps, validation, log entry.
3. Add the trigger pattern to the bootstrap's directory scan (TEMPLATES.md, "Session Bootstrap" → migration signals).
4. Update the validation script(s) to detect the old format and refuse with a pointer to PHASE_M_MIGRATION.md.

The migration set grows over time. Older migrations are not rewritten — a library upgrading across multiple versions runs each applicable migration in sequence.
