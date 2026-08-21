# Audience Matrix

The navigation layer for the audience profile artifact. The matrix names the dimensions, lays out the cells, and points at the sub-profile modules. The matrix is read by humans and by the downstream building-context-libraries skill.

This document is allowed to discuss research methodology and cross-cell reasoning. The sub-profile modules are not.

---

## Audience Question

[Verbatim from user at Phase 1 startup.]

This question scoped dimension selection. Every dimension below is selected to help answer some part of it.

---

## Dimensions

### Dimension 1: [Name]

- **Values:** [value 1] / [value 2] / [value 3] / [...]
- **What this cut is:** [one paragraph — what does this dimension distinguish?]
- **Why it carries decision weight here:** [one paragraph — what about the organization's audience question makes this cut consequential?]
- **Sources that drove the choice:** [signal log entries, dimension candidates, modeled-data claims]
- **Considered-and-rejected alternatives:** [if any — pointer to process log]

### Dimension 2: [Name]

[Same fields]

---

## Matrix Structure

State the matrix structure committed to at Phase 3 STOP:

- **Default single matrix** — one rectangular 2D grid; all audience-kinds fit the shared column structure.
- **Variant A — single matrix with non-rectangular coverage** — one grid with intentionally empty cells where the column dimension doesn't apply to specific rows.
- **Variant B — two related 2D matrices** — Matrix A is the rectangular acquisition matrix; Matrix B uses row-specific column names that match each audience-kind's natural decision shape.

See [ARCHITECTURE.md, Matrix Structure Variants](../references/ARCHITECTURE.md#matrix-structure-variants) for the decision protocol and the rationale that drove this choice.

## Matrix

(For default or Variant A:)

|              | [D2 value 1] | [D2 value 2] | [D2 value 3] |
| ------------ | ------------ | ------------ | ------------ |
| [D1 value 1] | [coord]<br/>[status] | [coord]<br/>[status] | [coord]<br/>[status] |
| [D1 value 2] | [coord]<br/>[status] | [coord]<br/>[status] | [coord]<br/>[status] |
| [D1 value 3] | [coord]<br/>[status] | [coord]<br/>[status] | [coord]<br/>[status] |

(For Variant B, present both matrices:)

### Matrix A: [name — e.g., Audience-acquisition]

|              | [shared col 1] | [shared col 2] | [shared col 3] | [shared col 4] |
| ------------ | -------------- | -------------- | -------------- | -------------- |
| [Row 1] | [coord]<br/>[status] | [coord]<br/>[status] | [coord]<br/>[status] | [coord]<br/>[status] |
| [Row 2] | [coord]<br/>[status] | [coord]<br/>[status] | [coord]<br/>[status] | [coord]<br/>[status] |

### Matrix B: [name — e.g., Cross-audience and operational]

| Row | Col 1 | Col 2 | Col 3 | Col 4 |
|-----|-------|-------|-------|-------|
| **[Row 1]** | [coord]<br/>[status]<br/>*[row-specific col 1 name]* | [coord]<br/>[status]<br/>*[row-specific col 2 name]* | [coord]<br/>[status]<br/>*[row-specific col 3 name]* | [coord]<br/>[status]<br/>*[row-specific col 4 name]* |
| **[Row 2]** | [coord]<br/>[status]<br/>*[row-specific col 1 name]* | [coord]<br/>[status]<br/>*[row-specific col 2 name]* | [coord]<br/>[status]<br/>*[row-specific col 3 name]* | [coord]<br/>[status]<br/>*[row-specific col 4 name]* |

**Legend:**
- **substantive** — Multiple sources support; full module → `modules/[coord].md`
- **thin** — One or two sources weakly support; short module → `modules/[coord].md` (treat as starting hypothesis)
- **modeled-only** — No client/competitive sources; module from tested modeled-data → `modules/[coord].md`
- **empty** — Sources show this cut isn't engaged by this organization (intentional)
- **gap** — Substantive module would belong here; current sources insufficient (note source kind needed in coverage section)

---

## Cell Rationale

One paragraph per non-empty cell. Each paragraph answers three things:
- What the cell captures.
- Why it matters for the audience question.
- What in the sources made this cell visible as distinct from adjacent cells (the differentiating reasoning move).

### [coord]: [D1 value] × [D2 value] — status: [substantive / thin / modeled-only]

[One paragraph addressing all three elements above.]

[Repeat for each substantive / thin / modeled-only cell.]

---

## Coverage and Gaps

### Cells intentionally empty

- **[coord]: [D1 value] × [D2 value]** — [why this cut isn't engaged by the organization, sourced]

### Coverage gaps

- **[coord]: [D1 value] × [D2 value]** — [what kind of source would fill this gap; what kind of research would the organization need to commission?]

### Modeled-only cells (extra-thin inferential basis)

- **[coord]: [D1 value] × [D2 value]** — [note that this module's basis is tested modeled-data; downstream library design should treat as starting hypothesis subject to refinement when direct or competitive sources become available]

---

## Load Triggers

For each substantive / thin / modeled-only cell, the plain-language trigger conditions under which the downstream library agent should load this module.

| Cell | Module | `load_when:` |
| ---- | ------ | ------------ |
| [coord] | `modules/[coord].md` | [trigger phrasing] |
| [coord] | `modules/[coord].md` | [trigger phrasing] |

Examples of well-shaped triggers, drawn from different domains to signal range:
- `load_when: writing first-touch content for individual prospects` *(nonprofit fundraising)*
- `load_when: drafting season-launch content for new local fans` *(sports league launch)*
- `load_when: producing a partnership pitch deck for a peer NGO` *(institutional partnership)*
- `load_when: writing renewal communications for sustaining donors` *(donor stewardship)*

Avoid trigger phrasings that just restate the cell coordinate ("when generating for IND-CON") — the trigger should describe the user-recognizable task that activates the cell.

---

## Agent-Needs Alignment

Which agent generation tasks each substantive cell most directly serves.

| Cell | Primary tasks served |
| ---- | -------------------- |
| [coord] | [tasks from agent-needs.md] |
| [coord] | [tasks from agent-needs.md] |

---

## Open Conflicts

Conflicts surfaced during Comprehend that the matrix structure did not resolve. The downstream library skill should see these.

- **[Conflict name]:** [one-sentence description — pointer to `comprehension-artifacts/conflicts.md` for the full record]

---

## Handoff to building-context-libraries

This artifact is upstream input for context library design. The library skill's Phase 2 (Comprehend) should:

1. Read this matrix first to understand the audience space.
2. Read each module in `modules/` to see the decision-frame content.
3. Consult `source-index.md` to avoid re-reading sources already analyzed.
4. Optionally consult `process-log.md` for considered-and-rejected reasoning and modeled-data tests.

The library skill decides how audience context lives in the library — as a shared module, per-agent module, addendum, or conditional modules with `load_when:` triggers. The cells and triggers above are inputs to that decision, not commitments to a specific library shape.
