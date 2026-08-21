# Process Log

The build agent's running reasoning log. Updated throughout every phase. Part of the deliverable — the downstream library skill and the user both consult this to understand how the matrix was derived.

This document is allowed to narrate the build process. The sub-profile modules are not.

---

## Audience Question

[Verbatim from user at Phase 1 startup.]

---

## Library Handoff Context

[Named library / no library / library being built in parallel. Any notes on what the downstream library skill expects.]

---

## Phase 1 (Setup)

### Source classification notes

[Anything notable about source classification — sources that straddled classes, sources whose audience-relevance was indirect, sources marked low priority and why.]

### Initial expectations

[Pointer to `initial-expectations.md`. Summary of how many expectations were written and across how many audiences.]

### Phase 1 completion statement

[Verbatim from the Phase 1 GATE.]

---

## Phase 2 Pass 1 (Recognition)

### Per-source-note log

[One short line per source as you finish its note. Just a status log, not a substantive summary — the per-source notes carry the substance.]

### Signal log highlights

[Patterns that emerged across multiple sources during Pass 1. Brief; the signal log file carries the full record.]

### Expectations reflection summary

[What was confirmed, refuted, refined, untested. What was expected but not found.]

### Conflicts surfaced

[One line per conflict. Full conflict records live in `conflicts.md`.]

### Pass 1 completion statement

[Verbatim from the Pass 1 GATE.]

---

## Phase 2 Pass 2 (Synthesis)

### Modeled-data pictures produced

For each audience for which a modeled-data picture was generated:

#### [Audience name — by decision orientation]

- **Modeled motivations:** [summary]
- **Modeled decision triggers:** [summary]
- **Modeled framings that resonate / repel:** [summary]
- **Modeled trust / distrust signals:** [summary]
- **Identifiable references:** [list — with links where the model could produce them]
- **Test results:** [N confirmed against client/competitive sources, N refuted, N refined, N untested]
- **Notes on testing:** [anything important — sources that strongly refuted, refinements that changed the picture meaningfully]

### Dimension candidates considered

For each candidate (whether ultimately recommended or not):

#### [Dimension name]

- **Values:** [list]
- **Source basis:** [signal log entries, tested modeled-data claims supporting this cut]
- **Audience-question fit:** [does this dimension help the organization decide what they said they need to decide?]
- **Status:** [proposed / rejected / hybrid]

### Agent-needs summary

[Pointer to `agent-needs.md`. Brief summary of what kinds of generation tasks the downstream library will support.]

### Pass 2 completion statement

[Verbatim from the Pass 2 GATE.]

---

## Phase 3 (Design)

### Dimension proposal

[The proposal presented to the user — suggested-default consideration, source-driven proposal, recommendation.]

### User confirmation

[Verbatim user response committing to dimensions.]

### Cell rationale (cross-cell observations)

[Anything that became visible when looking at the grid as a whole — patterns of cell substance, cells that surprised, status distribution observations.]

### Phase 3 completion statement

[Verbatim from the Phase 3 GATE.]

---

## Phase 4 (Build)

For each module written, a section:

### Module [cell-coordinate]

- **Runtime Frame Set:** [verbatim commitment statement from Step 1]
- **Substantive Source Surface (final):**
  - [Pattern 1 — name, source pointer, shape]
  - [Pattern 2 — name, source pointer, shape]
  - [...]
- **Modeled-data contributions:** [none / list of tested claims incorporated]
- **Self-check results:**
  - [Pass / re-written N times — what was caught and what upstream step was redone]
- **Final length:** [N words]
- **Final status:** [substantive / thin / modeled-only]
- **Notes:** [anything the user or downstream library skill should know]

### Phase 4 completion statement

[Verbatim from the Phase 4 GATE.]

---

## Conflicts handed off to downstream library design

[List of conflicts from `conflicts.md` that the matrix structure did not resolve. The downstream library skill needs to see these.]

---

## Audit trail of revisions

[If the user requested revisions after Phase 4, log them here. Each revision: what was requested, what was changed, what the new state is.]
