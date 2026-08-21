# Phase 3: Design

**Session:** B (continues from Comprehend Pass 2)
**Input:** Dimension candidates, tested modeled-data pictures, agent-needs document, audience question.
**Output:** `audience-matrix.md` (draft — populated with structure, dimension rationale, cell coordinates, status assignments, triggers, but no sub-profile modules yet).

---

## Step 1: Offer the suggested defaults and the source-driven candidates side by side

Before committing dimensions, surface both options to the user:

1. **Suggested defaults that fit best.** From the four pairs in [../ARCHITECTURE.md, Suggested Default Dimensions](../ARCHITECTURE.md#suggested-default-dimensions), identify which pair (if any) best fits this organization. The fit test is whether the dimension candidates from Pass 2 overlap substantially with one of the default pairs.

2. **Source-driven dimensions.** From the dimension candidates in `comprehension-artifacts/dimension-candidates.md`, propose two dimensions that best answer the organization's audience question and that the sources support strongest.

If the suggested default and the source-driven proposal converge (the default pair *is* what sources drove toward), name the convergence — that's a strong signal.

If they diverge, present both and recommend the source-driven option. Defaults are starter scaffolding; sources are what decide.

Write the proposal in `process-log.md` under `## Phase 3 Dimension Proposal`. Format:

```markdown
### Suggested-default pair considered: [Pair name]
- Fit assessment: [strong / moderate / weak]
- Why: [one paragraph]

### Source-driven proposal
- Dimension 1: [name and values]
- Dimension 2: [name and values]
- Rationale: [why these cuts, what signal log entries and dimension candidates support them]

### Recommended commitment: [default / source-driven / hybrid]
- Rationale: [one paragraph]
```

---

## Step 1.5: Generalization check

Before presenting the proposal to the user, run a generalization check on the proposed dimensions. This prevents the failure mode where a dimension looks right because it fits how the sources happen to be organized, but doesn't actually capture audience structure for this organization.

Answer three questions in `process-log.md` under `## Phase 3 Generalization Check`:

1. **What specific features of these sources is this dimension proposal depending on?** Name them concretely. (E.g., "Dimension 1 depends on three of the five peer-org dossiers using 'engagement stage' language explicitly. Dimension 2 depends on the client's strategic plan organizing programmatic emphasis by beneficiary proximity.")

2. **Would the same dimension surface if the sources were reorganized or reclassified?** If yes — the dimension captures something about the organization's audience reality that any reasonable read of these sources would surface. If no — the dimension may be capturing how this source set happens to be structured rather than the underlying audience problem. Be specific about which.

3. **What would falsify this dimension as the right cut?** Name a plausible source or finding that, if it appeared, would refute the dimension as the right structural choice for this organization. If no plausible source could test it, the dimension is anecdotal rather than structural — reconsider.

If any answer reveals the dimension is exploiting source-set artifacts rather than capturing audience structure, return to dimension candidates and propose alternatives before presenting to the user. The check survives the proposal, not the other way around.

---

## Step 2: STOP — confirm dimensions with the user

Present the proposal to the user. Ask: "Commit to these dimensions, adjust them, or reject and re-derive?"

**Do not proceed without user confirmation.** Dimensions are the most consequential decision in the build. Getting them wrong means every sub-profile module is shaped along axes that don't matter for the organization. The skill cannot recover from wrong dimensions by writing better modules.

If the user adjusts: update the proposal. If the user rejects: return to Pass 2 dimension candidates and propose alternatives. Loop until the user commits.

Write the user's confirmation, verbatim, to `process-log.md`.

---

## Step 2.5: Matrix-structure decision

Before constructing the grid, decide which matrix structure to use. Three options are available, documented in [ARCHITECTURE.md, Matrix Structure Variants](../ARCHITECTURE.md#matrix-structure-variants):

1. **Default**: Single rectangular 2D grid where every audience-kind fits the shared column structure cleanly.
2. **Variant A — single matrix with non-rectangular coverage**: 1–2 audience-kinds have intentionally empty cells where the column dimension doesn't apply.
3. **Variant B — two related 2D matrices**: A substantive subset of audience-kinds operates on decision shapes the column dimension would distort. Matrix A is the rectangular acquisition matrix; Matrix B has row-specific column names that match each audience-kind's actual decision shape.

### Apply the decision protocol

Run the three-question protocol from ARCHITECTURE.md:

1. **How many audience-kinds fit the shared column structure cleanly?** Count.
   - All → default single matrix.
   - All-but-1-or-2 → Variant A.
   - A substantive subset doesn't fit → consider Variant B.

2. **Would forcing the non-fitting audience-kinds into the shared columns require misleading column labels?**
   - Yes (e.g., labeling a column "discovery" for an audience that doesn't experience discovery because they already know the property) → Variant B.
   - No, just empty cells → Variant A is workable.

3. **Are the non-fitting audience-kinds themselves substantial enough to warrant their own matrix?**
   - 3+ audience-kinds with their own internal coherence → Variant B.
   - Isolated outliers → Variant A.

Write the proposed structure and reasoning to `process-log.md` under `## Phase 3 Matrix-Structure Proposal`.

### Present to the user

Present the proposed structure with the reasoning. Ask: "Commit to this matrix structure, adjust, or consider an alternative?"

If Variant B is proposed, present both the Variant B structure *and* what the Variant A version would look like for comparison — Variant B has higher documentation overhead and the user should commit knowingly.

If the user adjusts: update. If the user commits: write the confirmation to `process-log.md` verbatim.

**Do not proceed to Step 3 without user confirmation of the matrix structure.** Changing the structure after cell construction begins is costly — many of Step 3 and Step 4's decisions depend on the structure.

---

## Step 3: Construct the matrix

Once dimensions and matrix structure are confirmed, build the grid. Use [../../templates/audience-matrix.md](../../templates/audience-matrix.md) as the scaffold.

**For default single matrix or Variant A:**

```markdown
|              | [D2 value 1] | [D2 value 2] | [D2 value 3] | ... |
| ------------ | ------------ | ------------ | ------------ | --- |
| [D1 value 1] | [cell coord] | [cell coord] | [cell coord] | ... |
| [D1 value 2] | [cell coord] | [cell coord] | [cell coord] | ... |
| ...          | ...          | ...          | ...          | ... |
```

**For Variant B (two related 2D matrices):**

Build both matrices. Matrix A uses the shared column structure; Matrix B uses row-specific column names that match each audience-kind's natural decision shape. The Matrix B table form:

```markdown
| Row | Col 1 | Col 2 | Col 3 | Col 4 |
|-----|-------|-------|-------|-------|
| [Audience-kind 1] | [row-specific col 1] | [row-specific col 2] | [row-specific col 3] | [row-specific col 4] |
| [Audience-kind 2] | [row-specific col 1] | [row-specific col 2] | [row-specific col 3] | [row-specific col 4] |
```

The column names differ per row by design. The dimension-rationale in Step 5 must defend the row-specific column structure explicitly.

Cell coordinates use a short identifier (e.g., `IND-CON` for "Individual × Consideration"). The coordinate names the cell and becomes the module filename when a module is written for it.

---

## Step 4: Assign cell status

For every cell in the grid, assign one of the five status categories (see [ARCHITECTURE.md, Cell Status Categories](../ARCHITECTURE.md#cell-status-categories)):

- **Substantive** — Multiple sources support; full module to be written in Phase 4.
- **Thin** — One or two sources weakly support; short module to be written with thin flag.
- **Modeled-only** — No client/competitive sources; module written from tested modeled-data only.
- **Intentionally empty** — Sources show this cut isn't engaged by this organization; no module.
- **Coverage gap** — Substantive module would belong here, but current sources insufficient; no module, matrix notes the source kind that would fill it.

**Source the status assignment.** For each cell, cite the recognition artifacts and dimension candidates that support the status. The matrix's `## Cell Rationale` section captures this — one paragraph per substantive/thin/modeled-only cell.

**Resist the urge to make every cell substantive.** A matrix where every cell is substantive almost always reflects paper-over rather than rich coverage. The Phase 3 gate explicitly checks this.

---

## Step 5: Write the matrix-level documentation

Populate the matrix document's narrative sections:

1. **Audience question** (verbatim from Phase 1).
2. **Dimension rationale** — one paragraph per dimension explaining what the cut is, why it carries decision weight for this organization, what sources drove the choice. Reference the considered-and-rejected alternatives from `process-log.md`.
3. **Cell rationale** — one paragraph per substantive/thin/modeled-only cell, answering three things:
   - What the cell captures.
   - Why it matters for the audience question.
   - **What in the sources made this cell visible as distinct from adjacent cells** — the reasoning move that differentiated it. Without this third element, the rationale narrates the conclusion without exposing how the cell was distinguished from its neighbors; downstream library design then can't tell whether the cell-level distinction is robust or an artifact of how the matrix was assembled.
4. **Coverage and gaps** — Which cells are empty, which are modeled-only, what source kinds would fill the gaps.
5. **Load triggers** — For each substantive cell, plain-language `load_when:` triggers. Examples drawn from different domains to signal range:
   - `load_when: writing first-touch content for individual prospects` *(nonprofit fundraising)*
   - `load_when: drafting season-launch content for new local fans` *(sports league launch)*
   - `load_when: producing a partnership pitch deck for a peer NGO` *(institutional partnership)*
   - `load_when: writing renewal communications for sustaining donors` *(donor stewardship)*

   Triggers describe the user-recognizable task that activates the cell. Phrasing that just restates the cell coordinate ("when generating for IND-CON") is not a trigger — it's a label.
6. **Conflicts to resolve at downstream library design** — Any conflicts from `conflicts.md` that the matrix structure didn't resolve. The downstream library skill needs to know about them.

---

## Step 6: Note the agent-needs alignment

In the matrix document's final section, name which `agent-needs.md` tasks each substantive cell most directly serves. Example:

```markdown
## Agent-Needs Alignment

| Cell | Primary tasks served |
| ---- | -------------------- |
| IND-DIS | Long-form content (acquisition articles), short-form (social, ad copy) |
| IND-CON | Email sequences, case studies |
| INST-ACT | Strategy documents (proposals, decks, briefs) |
```

This helps the downstream library skill decide loading discipline — cells that serve many task types may warrant always-load classification at the library level; cells serving narrow tasks fit conditional loading.

---

## GATE: Phase 3 complete

Before proceeding to Phase 4, write the following statements to `process-log.md`:

- "Dimensions committed: [D1: values], [D2: values]."
- "Generalization check complete: [the dimensions hold beyond the way these sources are organized / surfaced concerns and revised before user presentation]."
- "Matrix constructed: [N] total cells, [N] substantive, [N] thin, [N] modeled-only, [N] intentionally empty, [N] coverage gap."
- "Substantive-cell ratio justified: [yes — name the source basis / no — flag and review]."
- "Cell rationale includes differentiating reasoning move for every substantive/thin/modeled-only cell: [yes/no]."
- "Load triggers written for all substantive cells: [yes/no]."
- "Conflicts unresolved at design level: [N]."

Update `build-state.md`:
- Phase: 3 (Design) complete
- Next: Phase 4 (Build) — after mandatory session break
- Next phase file: `references/phases/PHASE_4_BUILD.md`

**STOP.** End Session B. The session break before Build is mandatory. Do not continue into Phase 4 in the same session.
