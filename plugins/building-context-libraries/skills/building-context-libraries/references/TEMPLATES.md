# Templates

## Process Log Template

The process log captures the reasoning chain across the entire build — decisions, corrections, user direction, and the evolution of understanding. Build-state tracks *where you are*. The process log tracks *how you got here and what was decided along the way*.

Create at `<OUTPUT_PATH>/process-log.md` during Phase 1 (Setup). Update it throughout every phase.

```markdown
# Process Log

**Library:** [Name or description]
**Created:** YYYY-MM-DD

---

## How to Use This Log

This log records the reasoning history of the build. It survives context compaction and session breaks — when you resume, read this log to understand decisions already made.

**What to log:**
- Decisions about structure, scope, or module design (and *why*)
- User corrections and direction changes (the most valuable entries)
- Comprehension insights that shaped the proposal
- Module-level decisions during Build (what was included, cut, or restructured)
- Conflicts resolved and how
- Anything the next session needs to know that isn't captured in build-state or the proposal

**What NOT to log:**
- Source summaries (those belong in comprehension findings in build-state)
- Completion status (that's build-state's job)
- Module content (that's in the modules)

**Format:** Date-stamped entries, newest first. Keep entries concise — reasoning and decisions, not narratives.

---

## Log Entries

### [YYYY-MM-DD] — Phase [N]: [Phase Name]

**[Decision/Correction/Insight]:** [What happened and why it matters]

---
```

---

## Build State Template

The build state file tracks progress across sessions. It is the first file any resumed session reads.

Create at `<OUTPUT_PATH>/build-state.md` during Phase 1 (Setup).

```markdown
# Build State

**Library:** [Name or description]
**Source path:** [SOURCE_PATH]
**Output path:** [OUTPUT_PATH]
**Target model:** [Model name and context window size]
**Created:** YYYY-MM-DD

---

## Current Phase

**Phase:** [1-Setup | 2-Comprehend | 3-Design | 4-Build]
**Read this phase file next:** references/phases/PHASE_[N]_[NAME].md (in the skill directory, not the output directory)

---

## Session Bootstrap (mandatory for every session)

**Step 0 — Redo Triage.** Before reading any other file in this directory, do these two things in order:

**A. Scan the output directory.** List the files and subdirectories in `<OUTPUT_PATH>/`. Look for redo signals:

- A `_retrospective_archive/` directory (definitive — a prior redo protocol ran)
- Files with audit/retrospective/post-mortem/failure-analysis names at the top level (likely — a retrospective was produced but not yet archived)
- A `modules/`, `addenda/`, or `agents/` directory containing files that aren't accounted for in build-state's checklist (suspicious — partial work from a prior attempt may exist)
- A `_comprehension/` directory containing artifacts that aren't accounted for in build-state's Phase 2 status (suspicious — partial Pass 1 or Pass 2 work from a prior attempt may exist)
- A `_scratch/` directory containing per-module plan files that aren't accounted for in build-state's Module Build Checklist (suspicious — partial Phase 4 work from a prior attempt may exist)
- A build-state's "Redo Session" field marked "yes" (definitive)

**B. Ask the user.** "Is this a redo session after a rolled-back build? [yes/no]" If your scan in (A) found any redo signal, mention what you found in the question — e.g., "I noticed `_retrospective_archive/` exists. Is this a redo session?"

If the user says **yes** OR your scan found a definitive redo signal, follow the redo-session protocol in PHASE_4_BUILD.md before continuing the bootstrap below.

If the user says **no** but your scan found a suspicious-but-not-definitive signal (orphan module files, unfamiliar audit-shaped documents), pause and resolve the discrepancy before continuing. Do not proceed past the triage step until the working set is clear.

If the user says **no** and no signals were found, continue:

1. Read this file (build-state.md)
2. Read process-log.md — the reasoning history of decisions made so far
3. Read the phase instruction file above
4. Read references/ARCHITECTURE.md
5. Read proposal.md (if Phase 3+)

If you believe you already know the rules, you are likely post-compaction. Re-read anyway.

---

## Mid-Session Rollback

If the user rolls back the build mid-session — for example, says "let's roll this back to Comprehend and start over" or "the proposal isn't right; we need to redo Design" — treat this as the start of a redo session even though no session boundary occurred:

1. Stop current work.
2. Update `build-state.md` to reflect the rolled-back phase (mark later phases pending again, update the "Current Phase" pointer).
3. If Phase 4 work has already produced module/addendum/agent files for this attempt, run the redo-session protocol (Phase 4) to archive them.
4. If the rollback returns to or before Phase 2 and `_comprehension/` artifacts exist from the rolled-back attempt, run the redo-session protocol to archive them — the same anchoring failure mode that affects module files affects comprehension artifacts (Pass 2 of a fresh attempt would otherwise generate from the prior attempt's pattern-pointers and convergences instead of from the sources).
5. If Phase 4 plans exist in `_scratch/` from the rolled-back attempt, archive those too.
6. Confirm with the user what is in the working set after the rollback before proceeding.

The redo-session protocol applies to mid-session rollbacks the same way it applies to between-session redos. The principle — physical separation between current attempt and prior attempt — does not depend on whether a session boundary occurred.

---

## Redo Session

**Is this a redo session?** no / yes (date: YYYY-MM-DD)

If yes, the user provides a list of named failure patterns to architecturally avoid this attempt. Names only — no examples, no rewrite suggestions, no document content.

**Known failure patterns to avoid (this attempt):**

- *(populated by user at start of redo session)*

**Retrospective documents** (audit.md, post-mortem.md, etc.) have been moved to `_retrospective_archive/` and are NOT part of the working set. Do not read them. The named pattern list above is the only carryover from the previous attempt.

---

## Phase Completion

| Phase | Status | Notes |
|-------|--------|-------|
| 1. Setup | pending / complete | |
| 2. Comprehend | pending / complete | |
| 3. Design | pending / complete | |
| 4. Build | pending / complete | |

---

## Module Build Checklist (Phase 4)

One line per module. Status only. Substantive reasoning belongs in process-log, not here.

| Module | Status | Sources Re-Read | Tokens |
|--------|--------|-----------------|--------|
| F0_agent_behavioral_standards | complete | (template — verbatim) | [est] |
| S0_natural_prose_standards | complete | (template — verbatim) | [est] |
| F1_organizational_identity | complete | identity.md, history.md | [est] |
| [Module ID] | pending / complete | [files] | [est] |

---

## Addenda Build Checklist (Phase 4)

| Addendum | Status | Notes |
|----------|--------|-------|
| [Addendum ID] | pending / complete | |

---

## Agent Definition Checklist (Phase 4)

| Agent | Status | Total Tokens | Budget % |
|-------|--------|-------------|----------|
| [Agent name] | pending / complete | [est] | [X]% |

---

## User Decisions Log

Record conflicts resolved, gaps accepted, scope changes, and any other user decisions:

- *(none yet)*

---

## Source Loading Confirmations

Each phase records what sources were loaded at session start:

- *(populated by phase loading gates)*

---

## Phase 2 Status

Substantive Phase 2 findings live in `<OUTPUT_PATH>/_comprehension/`, not in build-state. This section tracks terse status only — counts and completion marks.

**Pass 1 (Recognition):** pending / in-progress / complete
- Sources read: [count] / [total]
- Per-source notes written: [count]
- Signal log entries: [count] ([open] / [resolved] / [user-attention])
- Conflicts surfaced: [count] ([real] / [apparent] / [time-travel] / [other])
- Source signal-density breakdown: thick [count], medium [count], thin [count]

**Pass 1 STOP reviewed:** pending / complete (date)

**Pass 2 (Synthesis):** pending / in-progress / complete
- Pattern-pointers: [count] (all surface-specificity checks passed: yes/no)
- Convergences: [count]
- Cross-domain parallels: [count or "none surfaced"]
- Agent roles refined: [count]
- Sources re-read during synthesis: thick [count], medium [count], thin [count]

**Pass 2 STOP reviewed:** pending / complete (date)
```

---

## Source Index Template

The source index is the manifest for the entire build.

```markdown
# Source Index

**Generated:** YYYY-MM-DD
**Source path:** [SOURCE_PATH]
**Output path:** [OUTPUT_PATH]
**Status:** indexing | comprehending | ready | building | complete

---

## Source Files

| File | Type | Signal | Build Relevance | Key Topics | Notes |
|------|------|--------|-----------------|------------|-------|
| [path/to/file.md] | strategy | clear | active | [topics] | [notes] |
| [path/to/transcript.md] | transcript | buried | active | [topics] | [notes] |
| [path/to/legacy-doc.md] | reference | clear | active | [topics] | Pre-reorg but operationally current |

### Build Relevance Values
- `active` — Content is current and should inform module writing. **This is the default.** Most source files are active.
- `superseded` — Content has been replaced by a newer source. Note which source supersedes it. Do NOT read during Build unless the newer source references it.

**CRITICAL:** "Legacy," "pre-reorg," "old," or "reference" labels do NOT mean superseded. A document from before a reorganization often describes operational reality that hasn't changed. Only mark a source as `superseded` if a newer source explicitly replaces its content. When in doubt, mark `active`.

### Type Values
- `strategy` — Positioning, decisions, strategic direction
- `operational` — Processes, structures, procedures
- `transcript` — Conversational, may be messy
- `interview` — Q&A format
- `notes` — Meeting notes, informal
- `reference` — Supporting material
- `financial` — Financial data, pricing
- `legal` — Legal documents, agreements

### Signal Values
- `clear` — Organizational knowledge stated directly; use as reference during module writing
- `buried` — Meaning embedded in conversational artifacts, filler, or unstructured notes; Comprehend extracts the patterns directly

---

## HOW TO USE THIS INDEX

1. **Read files in order** — process each file in the checklist below
2. **Update the checklist** — after reading each file, mark it [x] and add notes
3. **Add conflicts/gaps** — record issues in the sections below
4. **Do not skip files** — every file must be read
5. **Do not proceed** to Comprehend until all files are read and user approves

---

## Reading Checklist

- [ ] 1. `[path/to/file.md]` — *notes: [add after reading]*
- [ ] 2. `[path/to/another.md]` — *notes: [add after reading]*

---

## Conflicts Identified

- *(none yet)*

---

## Gaps Identified

- *(none yet)*

---

## Initial Agent Needs Assessment

[Populated during Setup — what agents need to do, initial role identification]
```

---

## Foundation Module Template

```markdown
---
module_id: F#
module_name: [Name]
tier: foundation
purpose: "[What organizational reasoning does this module provide?]"
last_updated: YYYY-MM-DD
---

<!-- BUILD REMINDERS (remove from final module):

This module is being read by a runtime agent that has only its loaded modules and the user's input. It does not know about source files, the build, the library, the proposal, or anything outside its modules. Sentences that only make sense inside the build are contamination. See ARCHITECTURE.md, "The Runtime Agent's Perspective."

Contamination phrases — if any appear, the sentence is wrong-shaped:
- "the source set" / "the sources" / "source documents" / "in some sources"
- "the library" / "this library" / "the build"
- Any source filename or path
- Dates attached to document provenance ("in 2025-era sources")
- "as documented in" / "per the [document type]"
- Any sentence explaining why content is or isn't in the module

Each section was committed to a Section Plan (Phase 4, Step 5) before being written. The plan named:
- The shape (reasoning context | decision framework | prescriptive rule | cross-reference | reach-beyond signal)
- The owned content the section needs (with use-shape from the proposal's Ownership and Use-Shape table)
- The source patterns the section encodes
- The extracted reasoning from any quote or named-individual content (not the quote, not the name)

Verify after writing: each section reflects what the plan committed to. If a section drifts to a different shape, the upstream plan was wrong — redo the plan, do not edit the prose.

For shape reference: F0 in templates/guardrails/ is a worked example of mixed-shape content. See ARCHITECTURE.md, "Shape Reference: F0 as a Worked Example."

HIGH-STAKES content (legal names, EINs, addresses, titles, dates, financials): copy EXACTLY from sources.

DURABILITY:
- No volatile specifics (counts, prices, named lists). Move to addenda. Process parameters are durable.
- Guide, don't catalog. Principles, not inventories.
- Respect proposal scope. Cross-reference content owned elsewhere; do not restate.
-->

<!-- VERIFICATION LOG (remove before delivery)
| Fact | Source File | Exact Source Text |
|------|-------------|-------------------|
| [fact] | [file] | [exact quote] |
-->

# [Module Name]

## Purpose

[What organizational reasoning does this module provide?]

## Scope

**Included:** [What this covers]
**Not Included:** [What's elsewhere] → See [Module]

---

## [Reasoning Domain]

[Organizational reasoning context: principles, values, tradeoffs.
Written as instructions to the agent, not explanations about the organization.
Include reach-beyond signals for when to load addenda, invoke skills, or ask the user.]

---

## Cross-References

- [Module Name]: [Relationship]

---

## Agent Instructions

When using this module:
- [How this reasoning applies to the agent's work]
- [What to prioritize when this domain's values are in tension]
```

---

## Shared Module Template

```markdown
---
module_id: S#
module_name: [Name]
tier: shared
purpose: "[What organizational reasoning does this module provide?]"
used_by: [agent types]
last_updated: YYYY-MM-DD
---

<!-- BUILD REMINDERS (remove from final module):
Same as Foundation template — re-read sources, transformation test, durability checks.
-->

<!-- VERIFICATION LOG (remove before delivery)
| Fact | Source File | Exact Source Text |
|------|-------------|-------------------|
-->

# [Module Name]

## Purpose

[What organizational reasoning does this module provide?]

## Scope

**Included:** [What this covers]
**Not Included:** [What's elsewhere] → See [Module]

---

## [Reasoning Domain]

> **Requires [Foundation Module]** for organizational context.

[Organizational reasoning context for this cross-functional domain.
Written as instructions to the agent — principles, decision frameworks, reach-beyond signals.]

---

## Cross-References

**Requires:** [Foundation modules]
**Related:** [Other modules]

---

## Agent Instructions

- [How this reasoning applies to the agent's work]
- [What to prioritize when values are in tension]
```

---

## Specialized Module Template

```markdown
---
module_id: D#
module_name: [Name]
tier: specialized
purpose: "[Domain-specific question this answers]"
used_by: [specific agents]
last_updated: YYYY-MM-DD
---

<!-- BUILD REMINDERS (remove from final module):
Same as Foundation template — re-read sources, transformation test, durability checks.
-->

<!-- VERIFICATION LOG (remove before delivery)
| Fact | Source File | Exact Source Text |
|------|-------------|-------------------|
-->

# [Module Name]

## Purpose

[What domain-specific reasoning does this module provide?]

## Scope

**Included:** [Domain content]
**Not Included:**
- [General info] → See [Foundation Module]
- [Cross-functional] → See [Shared Module]

---

## [Domain Reasoning]

> **Requires [Shared Module]** for methodology.
> **Requires [Foundation Module]** for org context.

[Domain-specific reasoning context: how the organization thinks about this specific domain.
Written as instructions — principles, decision frameworks, reach-beyond signals.]

---

## Cross-References

**Requires:** [Modules needed for context]

---

## Agent Instructions

- [How this domain reasoning applies to the agent's work]
- [What to prioritize in this domain when values are in tension]
```

---

## Agent Definition Template

Agent definitions are **system prompt preambles** — they are loaded into the agent's context at runtime. Write them as instructions TO the agent, not documentation ABOUT the agent.

The file has two sections: the runtime system prompt (what the agent reads) and build metadata (what humans managing the library reference, hidden from the agent in an HTML comment).

```markdown
---
agent_name: [Name]
agent_domain: [domain]
purpose: "[What this agent does]"
modules:
  foundation:
    - F1_[name]
    - F0_agent_behavioral_standards
  shared:
    - S1_[name]
    - S0_natural_prose_standards  # if external-facing
  specialized:
    - D1_[name]
addenda:
  - addendum_name: "[what data]"
estimated_tokens: [total]
last_updated: YYYY-MM-DD
---

# [Agent Name]

You are [the organization]'s [domain] agent. [2-3 sentences: what you do, what decisions you make, what you produce. Written as identity — "You handle...", "You advise...", "You create..." — not as description.]

## Your Context

Load these modules in order. They provide the organizational knowledge you need to do your work:

**Foundation (always loaded):**
- `modules/foundation/F0_agent_behavioral_standards.md` — behavioral process gates (all agents)
- `modules/foundation/F1_[name].md` — [what this gives you]

**Shared:**
- `modules/shared/S1_[name].md` — [what this gives you]
- `modules/shared/S0_natural_prose_standards.md` — prose standards (if external-facing)

**Specialized:**
- `modules/specialized/D1_[name].md` — [what this gives you]

## When to Reach Beyond Your Modules

Your modules give you the organization's reasoning patterns. They don't contain everything — by design. Know when to reach for more:

**Load an addendum** when you need specific data your modules reference but don't contain:

| Addendum | Load When |
|----------|----------|
| `addenda/[name].md` | [Specific trigger — e.g., "When building proposals that include pricing"] |

**Invoke a skill** when you need a capability beyond your context:
- [e.g., "Use the drafting-articles skill for long-form content production"]
- [e.g., "Use the writing-case-studies skill when asked to produce a case study"]

**Ask the user** when you encounter:
- Situations where organizational values are in tension and the right tradeoff isn't clear from your modules
- Requests that require judgment about organizational direction or strategy
- Information gaps your modules flag but don't resolve

## Domain Guidelines

[Behavioral extensions specific to this agent's domain. Only include guidance beyond what the standard guardrail modules provide.]

**Do:**
- [Domain-specific behavioral instruction]

**Don't:**
- [Domain-specific anti-pattern]

[Optional: escalation rules, verification requirements, domain constraints]

<!-- BUILD METADATA (not part of the agent's runtime context)
Token Budget:
- Foundation: [X] tokens
- Shared: [X] tokens
- Specialized: [X] tokens
- Total: [X] tokens ([X]% of per-agent limit)
- Addenda: not counted (loaded on demand)
- Budget assessment: [well-served / potentially underserved / over-budget]

Module Rationale:
| Module | Why This Agent Needs It |
|--------|----------------------|
| [ID] | [What decisions this enables] |

Build Notes:
- [Any decisions made during the build about this agent's module set]
-->
```

---

## Addendum Template

```markdown
---
addendum_id: A#_[name]
addendum_name: [Name]
purpose: "[What reference data this provides]"
referenced_by: [which modules]
update_frequency: "[quarterly | annually | on-demand | when-changed]"
last_updated: YYYY-MM-DD
---

<!-- VERIFICATION LOG (remove before delivery)
| Data Point | Source File | Exact Source Text |
|------------|-------------|-------------------|
-->

# [Addendum Name]

> **Reference data.** This addendum contains volatile data that changes as the
> business evolves. Modules reference this file rather than embedding its contents.

---

## [Data Section]

[Tables, lists, rates, bios, catalogs — reference data only.
No behavioral instructions. No "When X, do Y."
HIGH-STAKES content copied exactly from source.]

---

*Source: [source files]*
*Last verified: YYYY-MM-DD*
```

---

## Proposal Template

**The proposal describes STRUCTURE, not content. Zero organizational information.**

```markdown
# Context Library Proposal

## Library Overview

- Source documents: [count] ([types])
- Target model: [model] ([context window])
- Agents: [count] ([roles])

## Module Architecture

### Foundation Modules

| ID | Name | Purpose | Sources | Est. Tokens |
|----|------|---------|---------|-------------|
| F1 | [Name] | [Reasoning it provides] | [Files] | [Est] |

### Shared Modules

| ID | Name | Purpose | Used By | Sources | Est. Tokens |
|----|------|---------|---------|---------|-------------|
| S1 | [Name] | [Reasoning it provides] | [Agents] | [Files] | [Est] |

### Specialized Modules

| ID | Name | Purpose | Used By | Sources | Est. Tokens |
|----|------|---------|---------|---------|-------------|
| D1 | [Name] | [Reasoning it provides] | [Agents] | [Files] | [Est] |

### Addenda

| ID | Name | Data Contents | Referenced By | Sources | Update Freq |
|----|------|-------------|---------------|---------|-------------|
| A1 | [Name] | [What data] | [Modules] | [Files] | [Freq] |

## Ownership and Use-Shape

Each content area has exactly ONE owner. Every other module that needs the content uses one of four shapes — committed here, not decided at write-time.

**Use-shapes:**
- **cross-reference** — pointer only, no restatement
- **subset (X)** — restate the named subset (one phrase or short sentence) and cross-reference; X names the subset
- **invocation by name** — name the thing without describing it
- **reach-beyond** — module instructs agent to load addendum/invoke skill when needed

| Content Area | Owner | Used By | Use-Shape |
|--------------|-------|---------|-----------|
| [Identity / positioning content] | [Foundation owner] | [Other modules] | Cross-reference. |
| [Constants used by adaptations] | [Owner module] | [Adaptation modules] | Cross-reference at top; using-module content begins with the adaptation, not with restated constants. |
| [Standard, protocol, or framework set] | [Methodology module or addendum] | [Modules that need to invoke standards by name] | Invocation by name. |
| [Volatile data — figures, lists, named items] | [Addendum] | [Modules that need the data] | Reach-beyond ("when needing X, load addendum Y"). |

The bracketed placeholders are intentional — examples that name concrete content areas tend to anchor the next build on those exact areas. Replace each placeholder with the content area for the actual library being built.

Every row where Used By is non-empty must have a use-shape. A row without a use-shape is incomplete.

## Agent Definitions

| Agent | Role | Foundation | Shared | Specialized | Total | Budget % |
|-------|------|-----------|--------|-------------|-------|----------|
| [Name] | [What it does] | F1,F_abs | S1,S_nps | D1 | [X]K | [X]% |

## Gaps and Limitations

### Blocking
- [Gap]: [Impact] — **resolved by [how]**

### Limiting
- [Gap]: [Impact] — proceeding with noted limitation

### Enhancing
- [Gap]: low priority

## Build Plan

Recommended module build order:
1. [Module] — [rationale]
2. [Module] — shares sources with #1, build together for cross-reference checking

---

PHASE 4 RULES (embedded for compaction defense):
- Read ARCHITECTURE.md before writing any module — including "The Runtime Agent's Perspective" and "Shape Reference: F0 as a Worked Example."
- Modules are read by a runtime agent that has no awareness of sources, the build, or the library. Sentences that only make sense inside the build are contamination.
- Per-module protocol (PHASE_4_BUILD.md) has 7 steps. The Substantive Source Surface (Step 4) and Section Plan (Step 5) are planning artifacts the agent commits to BEFORE writing prose. Do not skip them.
- Re-read sources in the same turn you write each module.
- Use the Ownership and Use-Shape table above. Every section that needs owned content uses the committed shape — cross-reference, subset, invocation by name, or reach-beyond. Restatement is not one of the shapes.
- Quotes and named individuals from sources do not appear in modules. Extract the reasoning before generating, in the Section Plan. Quote-extraction is the default path.
- Modules tell the agent when to reach beyond themselves — load addenda, invoke skills, or ask the user.
- Token budget is room for useful content, not a ceiling.
- When a module fails self-check or user review, follow the failure-recovery protocol (PHASE_4_BUILD.md). Diagnose the upstream planning gap; do not regenerate prose from scratch.

---

**Awaiting approval to proceed with build.**
```
