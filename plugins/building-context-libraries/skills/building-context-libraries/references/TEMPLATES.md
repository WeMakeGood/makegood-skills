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

1. Read this file (build-state.md)
2. Read process-log.md — the reasoning history of decisions made so far
3. Read the phase instruction file above
4. Read references/ARCHITECTURE.md
5. Read proposal.md (if Phase 3+)

If you believe you already know the rules, you are likely post-compaction. Re-read anyway.

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

| Module | Status | Tokens | Notes |
|--------|--------|--------|-------|
| F0_agent_behavioral_standards | pending | — | Copied from template |
| S0_natural_prose_standards | pending | — | Copied from template |
| [Module ID] | pending / complete | [est] | |

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

## Comprehension Findings (Phase 2)

[Populated during Phase 2 — reasoning patterns, convergences, tensions, refined agent roles]
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
- Re-read working sources BEFORE writing. Do not write from memory.
- Re-read this module's SCOPE from the proposal. Do not include addenda or other-module content.
- This module should provide REASONING CONTEXT — the organization's principles, values, and ways of thinking. Not fact sheets. Not procedure manuals.
- HIGH-STAKES content (legal names, EINs, addresses, titles, dates, financials): copy EXACTLY.

TRANSFORMATION TEST — every section:
1. Is this written as an INSTRUCTION to the agent, or as an EXPLANATION about the organization? If it explains, rewrite as instruction. No narrative prose. No "about us" writing. No third-person descriptions.
2. Does this give the agent reasoning it can apply to NOVEL situations? If it only works for pre-specified scenarios, transform it.
3. Is this reasoning context (primary), a decision framework (secondary), or a prescriptive rule (rare)? Most content should be reasoning context.
4. Does this module tell the agent when to REACH BEYOND itself — load addenda, invoke skills, or ask the user?
5. Does any section contain quoted material used as content? Quotes are evidence during comprehension, not module content. Extract the reasoning the quote proves and state it as an instruction.

DURABILITY CHECKS:
- No volatile specifics (counts, prices, named lists). Move to addenda. BUT: process parameters are durable.
- Guide, don't catalog. Capture principles, not inventories.
- Respect scope boundaries. Test against the proposal, not source proximity.
- Don't box out possibilities. Capture reasoning and tradeoffs, not exhaustive "If X, do Y" rules.
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

## Shared Source Ownership

| Source File | Content Area | Owned By | Cross-Referenced By |
|-------------|-------------|----------|---------------------|

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
- Read ARCHITECTURE.md before writing any module.
- Modules provide reasoning context — how the organization thinks. Not procedures. Not "If X, do Y" rules.
- Re-read sources in the same turn you write each module.
- Check Shared Source Ownership before writing — cross-reference, don't restate.
- Every module should tell the agent when to reach beyond itself — load addenda, invoke skills, or ask the user.
- Token budget is room for useful content, not a ceiling.

---

**Awaiting approval to proceed with build.**
```
