# Phase 2: Comprehend (Two Passes)

**Pass 1 session:** A (continues from Setup)
**Pass 2 session:** B (after mandatory break)
**Input:** Source-index, initial expectations, sources themselves.
**Output:** Pass 1 — recognition artifacts in `comprehension-artifacts/`. Pass 2 — dimension candidates, modeled-data picture (surfaced and tested), agent-needs document.

---

## Why two passes

Single-pass synthesis on a saturated source context collapses toward sector-applicable rather than organization-specific patterns. Lateral cognitive moves — cross-source convergences, the move from "what these sources say" to "what these sources reveal about how this organization thinks about its audiences" — get crowded out when sources dominate context.

The two-pass structure is the architectural fix. Pass 1 reads sources with sources in context, producing observational artifacts at the moment of reading. Pass 2 synthesizes with sources mostly out of context and recognition artifacts loaded — that's where dimension candidates and tested modeled-data become possible.

The mandatory session break between passes is what makes the structural advantage real. Skipping it collapses both passes into one and surrenders the architectural advantage.

---

# Pass 1: Recognition

## Pass 1, Step 0: Load all sources

**GATE:** Before any per-source note is written, read every source file listed in `source-index.md`. Not skim — read. The recognition that follows depends entirely on having actual source content in context, not on the source-index's structural notes.

1. Read `<OUTPUT_PATH>/source-index.md` — the complete file list with classifications.
2. Read `<OUTPUT_PATH>/audience-needs-assessment.md` — the analytical frame Pass 1 will test.
3. Read `<OUTPUT_PATH>/initial-expectations.md` — the predictions Pass 1 will surface confirmations/refutations against.
4. Read every source file in the index, in order. **Read each one fully.**
5. After every source is read, write to `process-log.md` under `### Pass 1, Step 0`:
   - "Sources loaded for Pass 1: [N] of [N total] read in this session."
   - "Source-set surprises against Phase 1's inventory framing: [list, or 'none' — places where reading revealed the source's audience-relevance differs from what the source-index entry's structural scope suggested]."

**If the source set is too large to read in one context window, read in clusters** — but every source must be read before per-source notes for the cluster are written. Per-source notes are still captured at the moment of reading regardless of cluster boundaries; the cluster boundary is for context-window management, not for the recognition discipline.

**Do not proceed to Step 1 until every source is loaded.** Recognition built on partial reading produces partial observations, and the expectations-vs-findings check at the end of Pass 1 fails silently — what got skipped never registers as missing.

---

## Step 1: Per-source notes

For each source listed in `source-index.md`, read it fully and produce a per-source note in `comprehension-artifacts/[source-slug].md`. Use [../../templates/per-source-note.md](../../templates/per-source-note.md) as the scaffold.

**Required fields:**

1. **Source title and class** (copy from source-index).
2. **Audience-relevant content extracted.** What does this source say or imply about the organization's audiences? Use direct paraphrase, not transformation. (Pass 2 is where transformation happens.)
3. **Distinctive vocabulary.** Phrases or terms the source uses that name audience cuts or audience behaviors. Capture verbatim — vocabulary is a strong signal of how the source thinks about audience.
4. **Distinctive evasions.** What this source notably does *not* say or does *not* name. If a peer dossier discusses every audience type but never mentions younger donors, that absence is data.
5. **Surprises.** Things in the source that contradicted your initial expectations (from `initial-expectations.md`). Name the expectation and what the source actually showed.
6. **Conflicts.** Things in the source that contradict other sources read so far. Name both.
7. **Gaps.** What you expected to find in this source but didn't.

**Write per-source notes at the moment of reading.** Do not batch them. The observational fields lose fidelity if delayed.

---

## Step 2: Signal log

Maintain a running file `comprehension-artifacts/signal-log.md` as you work through Pass 1. Use [../../templates/signal-log.md](../../templates/signal-log.md).

Whenever a pattern becomes visible across two or more sources, write it down. The signal log is rough — it's the build agent's working notes. Patterns that recur get refined in Pass 2; patterns that turned out to be single-source noise get dropped.

Format:
```markdown
## [Pattern name in source vocabulary if possible]

- **First observed:** [Source X]
- **Recurring in:** [Source Y, Source Z]
- **What the pattern is:** [one sentence]
- **Why it might matter:** [one sentence on audience-relevance]
- **Open question:** [if any]
```

---

## Step 3: Expectations-vs-findings reflection

Once all sources have per-source notes, return to `initial-expectations.md` and write a reflection at the bottom under `## Reflection (post Pass 1)`. For each initial expectation:

- **Confirmed:** Sources confirmed this. Note the supporting sources.
- **Refuted:** Sources contradicted this. Note the contradicting sources and what they showed instead.
- **Refined:** Sources adjusted the picture. State the refined version.
- **Untested:** No sources addressed this expectation. Note whether the absence is a real gap or whether the question was misdirected.

Then write: "Things I expected to find but didn't." This is the negative space — expectations that no source addressed. Some are gaps in research coverage; others are signs the expectation was wrong; others are organizational findings (the organization doesn't think about this dimension at all, and that's data).

---

## Step 4: Conflicts log

Create `comprehension-artifacts/conflicts.md`. List every cross-source conflict surfaced during Pass 1.

Format:
```markdown
## Conflict: [short name]

- **Sources in conflict:** [Source X says A; Source Y says B]
- **Audience-relevance:** [why this matters for audience dimensions]
- **Resolution candidate:** [if obvious]
- **Status:** [open / proposed resolution]
```

Conflicts go to the user for resolution, but not yet. Pass 2 may resolve some conflicts by reframing the dimension. The Phase 3 design step surfaces the remaining ones.

---

## GATE: Pass 1 work complete (pre-STOP self-check)

Before presenting to the user, write the following statements to `process-log.md`:

- "All sources loaded before per-source notes were written: [yes/no — confirm Step 0's read-everything-first gate held]."
- "Per-source notes complete: [N] of [N total] sources, [N] artifacts in `comprehension-artifacts/`."
- "Signal log entries: [N] patterns logged."
- "Expectations reflection complete: [N] confirmed, [N] refuted, [N] refined, [N] untested, [N] things expected but not found."
- "Audience-needs assessment tested against sources: [N] audience candidates confirmed, [N] refuted, [N] refined, [N] new audiences surfaced from sources that the assessment didn't predict."
- "Open conflicts logged: [N]."

---

## STOP — Pass 1 Recognition Review

Before the mandatory session break, the user reviews recognition outputs. This is the recognition validation point — catching contamination here is much cheaper than catching it after Pass 2 has built synthesis on top of bad observations.

**Present to the user:**

- **Signal log** — cross-source patterns surfaced during reading, with source pointers and audience-relevance.
- **Expectations-vs-findings reflection** — what was expected and confirmed, refuted, or refined; what was expected but not found (negative space); what was found that wasn't expected.
- **Audience-needs assessment refinement** — for each audience candidate from Phase 1: did Pass 1 confirm, refute, or refine it? Were new audiences surfaced from sources that the assessment didn't predict? This is the most diagnostic output of Pass 1 — it tells the user whether the Phase 1 analytical move held up against the sources.
- **Conflicts** — what conflicts you saw across sources, and what user input each needs.
- **Sources that turned out to be less or more relevant than the Phase 1 inventory classification predicted.**

**Ask:**

Confirmation questions:
- For the audience-needs assessment refinement — do the confirmations, refutations, and new audience candidates match what you'd expect from this organization's sources? Are there audiences that should be added or removed before Pass 2 synthesis?
- For conflicts — are they real, apparent, or artifacts of source vintage / different organizational states?
- For the negative space (expectations not found in sources) — are these gaps in source coverage, signs the expectation was wrong, or organizational findings (the organization doesn't think about this dimension at all)?
- Are there source-set characteristics that emerged during reading that should reshape what Pass 2 synthesizes?

Challenge questions (these invite the user into the analytical work; they surface refinements the agent's own scan didn't catch):
- Which of my refinements surprises you, and which seem too confident?
- For any audience candidate marked "confirmed" — does any of those confirmations feel like the agent confirming what it already believed rather than testing it against the sources?
- Which conflicts in the conflicts log should I treat as already-resolved by what you know (the organization has handled this internally) vs. genuinely open?
- Which sources did I underweight or misread? Were there sources I treated as low-signal that actually carry more weight, or vice versa?
- Are any new audience candidates I should be considering — audiences the sources surfaced but I haven't named?

The confirmation questions establish what the user agrees with; the challenge questions tell Pass 2 which findings to test hardest in synthesis and which to treat as already-validated.

**Do not proceed past Pass 1 STOP until the user has responded to both kinds of questions.** If the user identifies refinements, log them to `process-log.md` and reflect them in the audience-needs assessment before Pass 2 begins.

---

## After the Pass 1 STOP

Update `process-log.md` with the user's review notes and any refinements to the audience-needs assessment.

Update `build-state.md`:
- Phase: 2 (Comprehend), Pass 1 complete and STOP-reviewed
- Audience-needs assessment status: [N] candidates after Pass 1 refinement
- Next: Pass 2 (after mandatory session break)
- Next phase file: this file, continuing from "Pass 2: Synthesis"

**END SESSION A.** The session break is mandatory. Do not continue into Pass 2 in the same session. Pass 2 needs sources mostly out of context and recognition artifacts loaded — continuing in the same session collapses the architectural advantage.

---

# Pass 2: Synthesis

**Begin in a new session.** Read `build-state.md` to confirm Pass 1 is complete. Re-read [../ARCHITECTURE.md](../ARCHITECTURE.md).

Sources are now mostly out of context. Recognition artifacts (per-source notes, signal log, expectations reflection, conflicts) are loaded. This is where dimension candidates and tested modeled-data become visible.

---

## Step 5: Surface the modeled-data picture

For each audience the organization addresses, produce a modeled-data picture. Use [../../templates/modeled-data-picture.md](../../templates/modeled-data-picture.md) as scaffold. Save to `comprehension-artifacts/modeled-data-[audience].md`.

**Required fields:**

1. **Audience identified.** "First-time individual donors evaluating climate giving." "Institutional foundation program officers in the conservation space." Describe by decision orientation, not biography.
2. **Motivations the model attributes to this audience.** What does the model believe moves them?
3. **Decision triggers.** What kinds of moments or information shift them?
4. **Common framings that resonate.** What framings does the model believe land?
5. **Common framings that repel.** What framings does the model believe cause withdrawal?
6. **Trust signals.** What kinds of evidence or framing build trust?
7. **Distrust signals.** What kinds of evidence or framing erode trust?
8. **Current moment.** What does the model believe this audience is currently navigating — sector dynamics, cultural moment, recent events?
9. **Identifiable references.** Where the model can name specific sources (published research, recurring journalism, polling, sector reports), list them with links where possible. Mark claims without identifiable sources as "model inference from aggregated training data."

**The modeled-data picture is treated as a source document being produced.** You are producing a Class D source for testing. Do not skip the references step — F0 sourcing discipline requires it.

---

## Step 6: Test the modeled-data picture against client/competitive sources

For each claim in the modeled-data picture, mark its status against Pass 1's recognition artifacts:

- **Confirmed:** Per-source notes or signal log support this claim. Module-eligible.
- **Refuted:** Per-source notes or signal log contradict this claim. Module-ineligible — note the conflict in the modeled-data document.
- **Refined:** Per-source notes adjust the claim. Write the refined version. Module-eligible.
- **Untested:** Recognition artifacts don't address the claim. Stays in process log; not module-eligible unless the cell that needs it ends up "modeled-only" (see ARCHITECTURE.md).

Mark each claim in `comprehension-artifacts/modeled-data-[audience].md` with its status. The marked file becomes the input to Phase 3 and Phase 4 for that audience.

---

## Step 7: Dimension candidates

The signal log identified cross-source patterns. The modeled-data picture identified motivations, decision triggers, and framings. Pass 2's synthesis step is to propose dimension candidates — cuts of the audience space that the sources together suggest are decision-meaningful for this organization.

**Process:**

1. Re-read the audience question (in `process-log.md`).
2. Re-read the audience-needs assessment as refined after the Pass 1 STOP — the committed audience set is the input to dimension candidates.
3. Re-read the signal log and the tested modeled-data pictures.
4. List dimension candidates. A dimension candidate is a cut of the audience space — e.g., "engagement stage," "decision authority," "channel," "motivation orientation." For each:
   - Name the cut
   - List 3–7 values along the cut (e.g., engagement stage: discovery / consideration / active / sustaining / lapsed)
   - Cite which signal log entries and which tested modeled-data claims support the cut
   - Note which suggested-default pair (if any) it overlaps with — see [ARCHITECTURE.md, Suggested Default Dimensions](../ARCHITECTURE.md#suggested-default-dimensions)

Aim for 3–6 dimension candidates. The Design phase will narrow to two (or two related 2D matrices).

Save dimension candidates to `comprehension-artifacts/dimension-candidates.md`.

---

## Step 8: Agent-needs document

What will the downstream library agent need to do with these audience profiles? List the kinds of generation tasks the library will be supporting:

- Long-form content (articles, reports, case studies)?
- Short-form content (social, email subject lines, ad copy)?
- Strategy documents (proposals, decks, briefs)?
- Conversational (chat, Q&A, response drafting)?
- Internal-facing or external-facing?

For each kind of task, name what the agent will need from an audience profile to do that task well. This shapes Phase 4 — sub-profile modules are written to serve the agent-needs, not to be exhaustive descriptions.

**Set the per-cell module-length budget.** The default Sub-Profile Module Shape is 200–600 words (see ARCHITECTURE.md). For complex matrices with cross-audience-leverage cells, multi-cross-cutting attributes, or modeled-only status, individual cells may need 700–1100 words. Set per-cell budgets in the agent-needs document based on:

- **Simple cells** (residual-curiosity, low-decision-frame-density): 200–400 words.
- **Standard cells** (clear audience-kind with standard cross-cutting attributes): 400–600 words.
- **Cross-audience-leverage cells** (audiences whose decisions affect how other audiences engage with the property): 500–700 words; the cross-audience-effect framing needs space.
- **Modeled-only cells** (no direct/competitive source coverage): 400–600 words; the modeled-only-status framing and the modeled-data citation need explicit treatment.
- **Sub-structured cells** (cells with internal sub-structure like market-type): 400 words for the main module plus 150–250 words per sub-cell.

Document the per-cell budget explicitly in the agent-needs document. Phase 4 reaffirms the budget at the start of module writing and Phase 4's per-module self-check verifies the module either fits the budget or has documented reason to exceed it.

Save to `comprehension-artifacts/agent-needs.md`.

---

## GATE: Pass 2 complete

Before proceeding to Phase 3, write the following statements to `process-log.md`:

- "Modeled-data pictures produced and tested: [N] audiences, [N] confirmed claims, [N] refuted, [N] refined, [N] untested."
- "Dimension candidates: [N], with citations to signal log and tested modeled-data."
- "Agent-needs document complete: [list the kinds of tasks the library will support]."
- "Per-cell module-length budgets set in agent-needs document: [yes/no — confirm budgets specified for every committed candidate]."
- "Remaining open conflicts from Pass 1: [N]."

**Modeled-data references verifiability scan.** For each modeled-data picture, scan the Identifiable References list for the failure pattern that surfaces in this skill's testing: vague gestures at organization names without specific verifiable studies (e.g., "Pew Research" without a named report; "Tokyo Foundation reports" without a specific publication; "American Gaming Association data" without a specific dataset). These references look authoritative but are not actually citable.

For each flagged reference:
- If the model can name a specific verifiable source (named study, dated report, public dataset with URL) → replace the vague gesture with the specific citation.
- If the model cannot → mark explicitly as "model inference from aggregated training data" or "model inference from aggregated [domain] research patterns 2018–2024" or equivalent honest framing.

Vague gestures at real organizations without specific studies are a category of citation that reads as authoritative while being inference. F0 sourcing discipline requires explicit framing.

Write to `process-log.md`:
- "Modeled-data references scanned for verifiability: [yes — N pictures checked]. Vague-organization-name failures found and addressed: [list any flagged references, the picture they appeared in, and the resolution — specific citation added or explicit modeled-inference framing applied; or 'none — all references either verifiable or already marked as model inference']."

Update `build-state.md`:
- Phase: 2 (Comprehend), Pass 2 complete
- Next: Phase 3 (Design)
- Next phase file: `references/phases/PHASE_3_DESIGN.md`

**Continue into Phase 3 in the same session (Session B).** Pass 2 and Design belong together because dimension candidates feed directly into matrix construction.
