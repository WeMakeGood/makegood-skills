# Build State

<!--
This file tracks progress across sessions. Read this FIRST when resuming a build.
It tells you: what phase you're in, what's done, what's next, and what to read.
-->

**Library:** [Library Name]
**Source path:** [SOURCE_PATH]
**Output path:** [OUTPUT_PATH]
**Agents:** [list of target agents]
**Last updated:** YYYY-MM-DD

---

## Current Phase

**Phase:** [1 - Index | 2 - Synthesize | 3 - Analyze | 4 - Propose | 5 - Build | 6 - Agents | 7 - Validate]

> **MANDATORY BOOTSTRAP — Complete these reads before any work:**
> 1. Read the phase instruction file: `references/phases/[PHASE_FILE].md`
> 2. Read `references/ARCHITECTURE.md` — module design rules, single source of truth, token management
> 3. Read `<OUTPUT_PATH>/proposal.md` — module scopes, shared source ownership, build plan
>
> These reads are mandatory for every session start AND after any context compaction. If you believe you already know the rules, you are likely post-compaction. Re-read anyway — this has caused three build failures.

---

## Phase Completion Status

| Phase | Status | Notes |
|-------|--------|-------|
| 1 - Index | pending | |
| 2 - Synthesize | pending | |
| 3 - Analyze | pending | |
| 4 - Propose | pending | |
| 5 - Build | pending | |
| 6 - Agents | pending | |
| 7 - Validate | pending | |

Status values: `pending`, `in-progress`, `complete (pending approval)`, `complete`

---

## Module Build Checklist (Phase 5)

<!-- Populated after proposal approval. Track each module individually. -->

<!-- PER-MODULE PRE-FLIGHT (run for EVERY module, unconditionally):
1. Re-read the phase instruction file and ARCHITECTURE.md
2. Re-read this module's scope from proposal.md
3. Re-read working sources for this module
4. Check completed modules that share sources — cross-reference, don't duplicate
5. Write the module, then remove its verification log before moving on
If you believe you already know these rules, you are post-compaction. Re-read anyway. -->

### Foundation
- [ ] F0_agent_behavioral_standards — copied from templates
- [ ] S0_natural_prose_standards — copied from templates
- [ ] F1_[name] — [status]

### Shared
- [ ] S1_[name] — [status]

### Specialized
- [ ] D1_[name] — [status]

### Addenda
- [ ] A1_[name] — [status]

---

## Agent Definition Checklist (Phase 6)

- [ ] [agent-name] — [status]

---

## User Decisions Log

<!-- Record decisions made during the build so they're not lost across sessions. -->

### Conflicts Resolved
- [Conflict]: [User's decision] (Phase [N])

### Gaps Accepted
- [Gap]: [User's decision — proceed without, or defer] (Phase [N])

### Scope Changes
- [Change]: [What was added/removed and why] (Phase [N])

---

## Session History

<!-- Optional: track when sessions start/end for debugging. -->

| Session | Date | Phases Covered | Notes |
|---------|------|----------------|-------|
| 1 | YYYY-MM-DD | 1-2 | |
