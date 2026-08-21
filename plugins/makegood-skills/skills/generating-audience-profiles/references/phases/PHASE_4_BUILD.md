# Phase 4: Build

**Session:** C (after mandatory break from Design)
**Input:** Matrix document (with confirmed dimensions, cell coordinates, status assignments), source-index, recognition artifacts, tested modeled-data pictures.
**Output:** Sub-profile modules in `modules/` for every substantive / thin / modeled-only cell. Finalized matrix document.

---

## Read first

Re-read [../ARCHITECTURE.md](../ARCHITECTURE.md) before starting Phase 4. The runtime perspective discipline and the modeled-data discipline are most consequential during module writing — the rules need to be fresh.

---

## Module-writing order

Write substantive cells first. Then thin cells. Then modeled-only cells. The order matters because:

- Substantive cells anchor the matrix vocabulary. Their decision frames become the language patterns the other modules echo.
- Thin cells benefit from substantive-cell vocabulary already being set.
- Modeled-only cells require the most care — write them after the build agent's vocabulary is calibrated by the source-grounded modules.

---

## Per-Module Protocol

For each module, follow this exact sequence. Do not batch steps across modules.

### Step 1: Runtime Frame Set

Before writing anything for the module, write the following statement to `process-log.md`:

> "I am writing module [cell coordinate] for the downstream runtime library agent. That agent has its loaded library context modules and the audience module triggered for the current task. It does not have the source documents, the process log, the matrix, or knowledge of how this module was built. Sentences in this module that reference 'the research,' 'compared to other cells,' 'the peer dossiers showed,' or any other build-perspective phrasing are contamination. The module's job is to shift this runtime agent's generation when this audience dimension is active."

This is a commitment gate. The act of writing the statement is what re-anchors the runtime frame before module text generation begins.

### Step 2: Re-read the cell's source basis

Open the matrix document and re-read the cell rationale and source basis. Then re-read the specific recognition artifacts and tested modeled-data claims that support this cell. The per-source notes for the relevant sources should be re-opened — do not write from build-state memory.

### Step 3: Substantive Source Surface

Before writing prose, list 3–7 specific patterns from the just-re-read sources that this module will capture. Each pattern gets:

- **Pattern name** (in source vocabulary where possible)
- **Source pointer** (which source, which per-source note)
- **Shape** — what does the pattern tell the runtime agent to do? (decision frame? trust signal? framing to avoid?)

The Substantive Source Surface is the planning artifact. The module's prose executes this plan. If the plan reveals the cell is thinner than the Phase 3 status assignment said, update the status and consider whether the module should be thin or modeled-only instead.

Save the surface to `process-log.md` under the module's section.

### Step 4: Write the module

Use [../../templates/sub-profile-module.md](../../templates/sub-profile-module.md) as scaffold. The module has six sections:

1. **Cell coordinate.** Verbatim from the matrix.
2. **What this audience is doing when they encounter our content.** One paragraph — the decision they are in the middle of, not their biography.
3. **What carries weight with them.** Bulleted decision frames. Each bullet is a generation directive in essence (even if phrased as observation about the audience).
4. **What loses them.** Bulleted framings/claims/asks that cause withdrawal.
5. **When generating for this audience, prioritize.** Bulleted generation directives in direct language.
6. **Source basis.** One paragraph naming the source classes and specific citations. For modeled-data contributions, name the modeled claim, its references (where identifiable), and how it was tested.

Save to `modules/[cell-coordinate].md`.

**Length target:** Per-cell budget as set in `agent-needs.md` (typically 200–600 words; cross-audience-leverage, modeled-only, or sub-structured cells may run 700–1100 words). The discipline is to make every sentence shift agent behavior. Modules that run over the cell's per-cell budget without documented reason are typically restating the matrix or narrating the research; modules that come in under the budget by compressing decision frames out are typically dropping operationally consequential content. Self-check verifies the module either fits the budget or has documented reason to exceed it.

### Step 5: Per-module self-check

Before marking the module complete, run through:

1. **Runtime frame check.** Re-read the module as the runtime library agent — context modules loaded, the user's task, this module. Do all sentences make sense? Any sentence that doesn't is contamination.

2. **Build-perspective contamination scan.** Search the module text for these phrases (or close variants): "the research," "the sources showed," "compared to other cells," "the peer dossier," "we found that," "based on competitive analysis." Any match is contamination — remove or rewrite.

3. **Persona-shape scan.** Search for: a named individual, biographical detail (age range, occupation, family situation) not anchored to a stated client-defining audience attribute, channel-as-behavior framings ("uses Instagram nightly" vs. "is reachable primarily through visual social channels"). Any match needs rewriting.

4. **Source coverage check.** Every claim in sections 3, 4, and 5 should trace to the Substantive Source Surface. If a claim doesn't, either add the source pointer or remove the claim.

5. **Modeled-data discipline check.** If the module incorporates modeled-data, the source basis section explicitly names the modeled claim, its references, and how it was tested. If modeled-data appears as a regular sourced claim without that signal, the discipline has slipped.

6. **Decision-frame test.** Re-read sections 3, 4, and 5. Does each bullet shift agent generation? A bullet that an agent could read and continue generating identically has failed. Replace with a bullet that names a generation directive.

### Step 6: Log the module

After self-check passes, log a one-line status to `build-state.md`:

```markdown
- modules/[cell-coordinate].md: complete, [N] words, [status: substantive / thin / modeled-only]
```

And a longer entry to `process-log.md` under the module's section:

```markdown
### Module [cell-coordinate]
- Status: [substantive / thin / modeled-only]
- Substantive Source Surface (final): [3–7 patterns, copied from Step 3]
- Source-basis citation count: [N citations]
- Modeled-data contribution: [none / [N] claims tested and incorporated]
- Self-check: [passed / re-written N times]
- Notes: [anything the build agent or user should know]
```

---

## When a Module Fails

If the self-check reveals failures, do not rewrite from scratch. Identify the upstream step that caused the failure:

| Failure mode | Upstream step to redo |
|--------------|----------------------|
| Runtime frame contamination | Step 1 (Runtime Frame Set) — re-anchor and regenerate sections |
| Source claims that don't trace | Step 2 + 3 (Re-read and Substantive Source Surface) — re-derive the surface |
| Persona-shape leakage | Step 1 (commitment was insufficient) and Step 3 (surface contained biographical detail it shouldn't) |
| Decision-frame failure | Step 3 (surface was descriptions, not decision frames) |
| Modeled-data discipline slip | Step 5 check — re-test the modeled claim against recognition artifacts |

Regenerate from the corrected upstream step. The within-session-rewrite oscillation pattern (try again with vibes-based fixes) produces worse modules, not better ones — the fix is upstream, not at the prose layer.

---

## Finalize the matrix document

After all modules are written, return to the matrix document and:

1. **Confirm cell links.** Every substantive/thin/modeled-only cell coordinate in the grid links to its module file.
2. **Update status assignments.** If any cell's status changed during module-writing (e.g., what was "substantive" became "thin" because the Substantive Source Surface was thinner than expected), update both the grid and the rationale.
3. **Add a coverage summary.** Top-level summary: "N substantive, N thin, N modeled-only, N intentionally empty, N coverage gap. Total cells: N."
4. **Add the handoff section.** A short final section that points the downstream building-context-libraries skill at the artifact structure and notes the open conflicts it should consider:

```markdown
## Handoff to building-context-libraries

This artifact is upstream input for context library design. The library skill's Phase 2 (Comprehend) should:

1. Read `audience-matrix.md` first to understand the audience space.
2. Read each module in `modules/` to see the decision-frame content.
3. Consult `source-index.md` to avoid re-reading sources already analyzed.
4. Optionally consult `process-log.md` for considered-and-rejected reasoning and modeled-data tests.

Open conflicts the library skill should consider: [list from conflicts.md and process log]
```

---

## GATE: Phase 4 complete

Before declaring the build complete, write the following statements to `process-log.md`:

- "Modules written: [N substantive, N thin, N modeled-only]."
- "Self-check passes: [N modules passed first time, N required upstream-fix regeneration]."
- "Final matrix coverage: [N substantive / N total cells]."
- "Modeled-data contributions: [N modules incorporated tested modeled-data]."
- "Open conflicts handed off: [N]."

Update `build-state.md`:
- Phase: 4 (Build) complete
- Status: artifact complete
- Output path: [OUTPUT_PATH]
- Ready for: building-context-libraries consumption

Present to the user:

- "Build complete. Artifact at [OUTPUT_PATH]."
- "Substantive modules: [N]. Thin: [N]. Modeled-only: [N]. Intentionally empty cells: [N]. Coverage gaps: [N]."
- "Open conflicts for downstream library design: [N — list briefly]."
- "Recommended next step: pass [OUTPUT_PATH] to building-context-libraries (or to library design conversation) as Class B (audience research synthesis) input."

The user reads the matrix and modules, audits the process log if they want to see how it was derived, and either accepts or requests revisions.
