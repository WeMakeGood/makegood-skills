# Architecture: Generating Audience Profiles

This document explains why the artifact is shaped the way it is. Read it once at the start of Phase 1. Re-read after context compaction or when starting a new session.

---

## The Runtime Agent's Perspective

A sub-profile module is read by an agent that has:
- Its loaded context library modules (organizational identity, methodology, voice/prose standards, F0 behavioral standards)
- The audience module(s) triggered for the current task
- The user's task

It does not have:
- Your source documents
- Your process log
- The rest of the matrix
- Any knowledge of how the module was built

Sentences inside a sub-profile module must make sense to a reader with only that context. The runtime agent is the writing frame. Sentences like "the research showed," "compared to the other cells in the matrix," "based on the peer dossier review" are contamination — they reference the build process, which doesn't exist for the runtime agent.

This is the same discipline building-context-libraries documents under "the runtime agent's perspective." The pattern transfers because the artifact is consumed the same way: loaded into a system prompt, used to shape generation.

**The matrix document is the exception.** The matrix is read by humans (the build user, the library designer) and by the building-context-libraries skill during its own Comprehend phase. It can — and should — discuss dimension reasoning, cell coverage, conflicts surfaced. The matrix is the navigation; the matrix is allowed to narrate. The sub-profile modules are not.

---

## The Failure Mode This Skill Counteracts

Marketing/communications agencies build audience definitions as personas: a named individual with demographics, psychographics, behaviors, channels, and goals, written in present-tense narrative ("Mary, 34, two children, uses Instagram nightly after the kids go to bed"). For human marketers, this works — the named-individual specificity helps imagine the audience.

For LLM agents, this fails in three specific ways:

1. **Generalization of specifics.** The model encounters "Instagram nightly" and treats it as an audience-defining behavior rather than one indicative example. Subsequent generation may unconsciously gate on Instagram-relevance.

2. **Biographical anchoring crowds out decision context.** "Mary, 34, two children" loads the model's named-person attention pathways. Generation drifts toward content addressed to Mary-the-person rather than content responsive to the dimensions Mary was meant to represent.

3. **No decision shift.** The persona describes an audience. It does not tell the agent what to do differently when generating for that audience. Outputs read as if the persona weren't loaded — the same generic content with surface-level address adjustments.

This skill produces a structurally different artifact for that reason. The output is not a description of audience members; it is a set of decision frames that shift agent generation when an audience dimension is active.

---

## Source Classes

Audience research sources fall into four classes. Each requires a different citation form and a different level of inferential weight. The Phase 1 classification step assigns every loaded source to a class.

### Class A: Direct audience research

**What it is:** Audience interviews, surveys, ethnographic notes, user feedback, focus group transcripts, recorded usability sessions. The audience speaking in their own voice.

**Citation form:** Cite the document and (where possible) the speaker/respondent identifier within it. "Interview-04 (returning donor, 2022)" or "Survey 2023 Q3, item 14."

**Inferential weight:** Highest. Direct research is what the other classes are tested against.

**Reality check:** This class is increasingly rare in client engagements. Response rates have dropped, budget for primary research has shrunk, and LLM-modeled audience knowledge has displaced some of what direct research used to provide. When Class A sources exist, they are precious; when they don't exist, the skill works around the absence rather than pretending Class A is the foundation.

### Class B: Competitive/sector research

**What it is:** Peer organization dossiers, sector synthesis memos, market positioning research, adjacent-industry case studies. Audience patterns inferred from how comparable organizations engage their audiences and what works/fails in adjacent sectors.

**Citation form:** Cite the dossier and the specific pattern extracted. "[Peer-org] dossier: donor segmentation by climate vs. biodiversity framing." Include the inferential step — what the dossier said and what was extracted from it as audience-relevant.

**Inferential weight:** Strong for patterns that recur across multiple peer organizations; weaker for patterns from a single comparator.

**Typical shapes:** Directories of peer organization dossiers covering the client's sector. Sector synthesis memos that group research across adjacent industries the client wants to learn from. Market positioning research comparing the client to its competitive set.

### Class C: Internal strategy and program documents

**What it is:** Theory of change, program designs, fundraising materials, brand guidelines, strategic plans, board memos, internal positioning documents. Audience patterns inferred from what the organization says it's trying to do and for whom.

**Citation form:** Cite the document and the inferential step. "Strategic Plan 2025: programmatic emphasis on smallholder farmers as primary beneficiary cohort → audience dimension of beneficiary-proximate vs. beneficiary-distant donors."

**Inferential weight:** Strong for what the organization itself intends; weaker as a description of who the audience actually is, since intent and reality diverge.

### Class D: LLM-modeled audience knowledge

**What it is:** What the model has absorbed about this audience type from training data — typical motivations, decision triggers, common framings, what moves them, what they distrust. The model's prior on the audience.

**Why it's a permitted source under F0:** Direct audience research is scarce. Pre-trained models have absorbed substantial audience-relevant data — published research, journalism, marketing analyses, behavioral studies, polling. Treating that absorbed knowledge as an unstated background rather than a citable source class violates F0's sourcing discipline. Naming it as a source class and citing it appropriately is what makes its use defensible.

**Citation form:** Modeled-data citations require three components:
1. **The modeled claim, stated.** "Trained-data picture suggests first-time individual donors evaluating climate giving are giving-skeptic more than climate-skeptic — i.e., the question is whether donation moves outcomes, not whether climate is real."
2. **Linkable references where the model can identify them.** "This appears consistent with [Indiana University Lilly Family School of Philanthropy donor surveys] and [Giving USA reports on donor motivation]." Use real, verifiable references where the model can name them; mark inferences without specific sources as such.
3. **The test against other classes.** "Confirmed by [client strategy doc on lapsed-donor reactivation]; partially refuted by [peer-org dossier on a different framing approach]; refined by [client interview-02 noting beneficiary-proximate framing performs better in this geography]."

**Inferential weight:** Modeled-data starts as a hypothesis. It enters a sub-profile module only after testing against at least one other source class. Untested modeled-data stays in the process log.

**When modeled-data is the only available source for a dimension:** This happens. Some audience dimensions are not covered by client sources or peer research. The protocol is to (a) name the gap explicitly in the matrix-level documentation, (b) include the modeled-data picture with its references, (c) mark the cell as "modeled-only" so the downstream library agent and the user can see the inferential basis is thinner.

---

## The Audience Question

Before dimensions can be selected, the organization's actual audience question must be named. This is what the user is asked at Phase 1 setup: "What would the organization be using these profiles to decide?"

Examples:
- "How should our content shift between first-time prospects and active donors?"
- "What framing differences matter between institutional funders and individual major donors?"
- "How does a partnership pitch to a peer NGO differ from a sponsorship pitch to a corporate?"
- "What separates a fan who attends one live event from a fan who follows the league season-long?"

The audience question scopes dimension selection. A skill that produces a 5x4 matrix for an organization whose actual decision question is binary (prospect vs. donor) has produced false complexity. A skill that produces a 2x2 matrix for an organization with five distinct funder relationships has compressed real distinctions away.

The audience question lives at the top of the matrix document. Every dimension selected must answer some part of it.

---

## Suggested Default Dimensions

The skill ships with starter dimension pairs the user can adopt or replace. The Phase 3 protocol offers them; sources decide what gets committed.

**Pair 1: Engagement stage × Relationship type**
- Engagement stage: discovery → consideration → active → sustaining → lapsed
- Relationship type: individual / institutional / partner organization / press

**Pair 2: Decision authority × Motivation orientation**
- Decision authority: self / influenced / institutional approval / committee
- Motivation orientation: outcome-oriented / belief-oriented / belonging-oriented / fiduciary

**Pair 3: Channel × Information appetite**
- Channel: direct (email, mail, conversation) / social / earned media / events
- Information appetite: headline / explanatory / deep-dive / data-and-citations

**Pair 4: Proximity × Stake**
- Proximity: beneficiary / beneficiary-proximate / observer / beneficiary-distant
- Stake: financial / reputational / mission-alignment / professional

**When the default pair fits:** Use it as the matrix axes, with the Phase 3 gate confirming sources support those cuts for this client.

**When no default pair fits:** Derive dimensions from sources directly. Phase 3 documents why the defaults were rejected and what the source-driven dimensions are. The process log records the considered-and-rejected reasoning.

**Why two dimensions, not more:** A 3D or 4D matrix is unreadable as navigation. Two dimensions give a flat grid with comprehensible cell coordinates. Sub-profile modules can themselves carry nuance within a cell — they do not need more matrix dimensions to express depth. Where genuine 3D structure exists in the sources, or where some audience-kinds operate on decision shapes the default column dimension would distort, build two related 2D matrices rather than a single 3D matrix. See "Matrix Structure Variants" below for the structural options (default single matrix, single matrix with non-rectangular coverage, two related 2D matrices) and the Phase 3 decision protocol.

---

## Matrix Shape

The matrix document (`audience-matrix.md`) is the navigation layer. It contains:

1. **The audience question.** Stated at the top, exactly as the user phrased it at Phase 1.
2. **The two dimensions and their values.** With one-line rationale for why these dimensions were chosen for this organization.
3. **The grid.** Cells contain coordinate, status (substantive / thin / modeled-only / intentionally empty), and a link to the sub-profile module file when one exists.
4. **Cell rationale.** A short paragraph per substantive cell explaining what the cell captures and why it matters. (This is *about* the cell; the module *is* the cell.)
5. **Coverage and gaps.** Which cells are empty, which are modeled-only, what kinds of sources would fill them.
6. **Triggers.** For each substantive cell, plain-language `load_when:` triggers that tell the downstream library skill when to load this module.

The matrix is the artifact a human reads to understand what was built. The sub-profile modules are what the runtime agent loads.

---

## Matrix Structure Variants

The default matrix shape is a single rectangular 2D grid: one set of audience-kind rows × one set of engagement-stage (or other) columns, where every cell uses the same column structure and a cell at any intersection is meaningful.

For most engagements, this default holds. For organizations with audience structures that don't reduce cleanly to a single rectangular grid, two variant structures are available.

### Variant A: Single matrix with non-rectangular coverage

When most audience-kinds fit a shared column structure but a few don't, the matrix can be built as a single grid with **intentionally empty cells** where the column dimension doesn't apply to specific rows.

**When to use:**
- 1–2 audience-kinds out of a larger set have non-standard column applicability
- The "intentionally empty" status carries diagnostic information about how those audience-kinds differ from the others
- The column structure remains the right cut for most of the matrix

**What it looks like:**
- Single grid with explicit empty cells in the cell-status assignment
- Matrix documentation explains why each empty cell is empty
- Cell rationale section addresses the empty cells alongside the substantive cells

**Cost:** Documentation overhead is modest. Reader must understand why some cells are empty. The empty cells signal something real about the audiences.

### Variant B: Two related 2D matrices

When the audience-kinds split into two structurally distinct groups along whether the column dimension is the natural decision-shape, the matrix can be built as **two related 2D matrices** — one rectangular acquisition-style matrix, one with row-specific column structure for the cross-audience-and-operational cells.

**When to use:**
- A meaningful subset of audience-kinds operates on decision shapes the column dimension would distort (e.g., audiences that don't go through a discovery stage because they already know the property; audiences that operate on institutional-fit cycles rather than consumer engagement-stage progression; audiences that are market-typed rather than staged)
- Forcing those audience-kinds into the standard column structure would require >25% of cells to be intentionally empty, *or* would force misleading column labels (e.g., labeling a column "discovery" when the audience doesn't experience discovery)
- The cross-audience-and-operational audience-kinds are themselves substantial enough to warrant their own matrix rather than footnoting

**What it looks like:**
- **Matrix A**: Rectangular acquisition matrix with audience-kind rows × shared stage columns
- **Matrix B**: Cross-audience-and-operational matrix with audience-kind rows × row-specific column names that match each audience-kind's actual decision shape
- The matrix document presents both matrices, with explicit dimension-rationale for the row-specific column structure in Matrix B
- A cross-cutting decision frames section captures audience-kinds that don't fit either matrix (e.g., sponsors, athlete-facing content as task category)

**Matrix B row-specific column example shape:**

```
| Row                    | Col 1            | Col 2         | Col 3              | Col 4                |
|------------------------|------------------|---------------|--------------------|----------------------|
| [Pre-primed audience]  | recognition      | consideration | active-attendance  | sustaining-community |
| [Institutional partner]| fit-and-respect  | partnership   | active-collaboration | sustaining         |
| [Market-typed audience]| market-type-A    | market-type-B | market-type-C      | market-type-D        |
| [Mediated audience]    | first-mediation  | considered    | active             | sustaining           |
```

The four columns per row are different shapes by design. The column names match the audience-kind's natural decision progression rather than forcing a generic stage axis onto audiences whose decisions don't progress that way.

**Cost:**
- More documentation work — both matrices need dimension-rationale, both need cell rationale, the row-specific column structure needs explicit defense
- The matrix document narrative spends more words explaining the structure
- Downstream library design has more architectural context to consume

**Benefits:**
- Every cell in Matrix B is operationally meaningful for its row (no "intentionally empty because the stage doesn't apply" cells)
- The runtime agent loading a Matrix B module gets a column-name that accurately describes the audience's state, not a generic stage label that misleads
- The two-matrix split is itself diagnostic: it tells the downstream library agent that the cross-audience-and-operational cells require different runtime-agent treatment from the acquisition cells

### Decision protocol for matrix structure

Phase 3 commits to the matrix structure. The decision is made by counting:

1. **How many audience-kinds fit the shared column structure cleanly?** If all → default single matrix. If all-but-1-or-2 → Variant A (single matrix with non-rectangular coverage). If a substantive subset doesn't fit → consider Variant B.

2. **Would forcing the non-fitting audience-kinds into the shared columns require misleading column labels?** If yes → Variant B (the misleading labels would produce wrong runtime-agent behavior). If no, just empty cells → Variant A is workable.

3. **Are the non-fitting audience-kinds themselves substantial enough to warrant their own matrix?** If they are 3+ audience-kinds with their own internal coherence → Variant B. If they are isolated outliers → Variant A.

Phase 3 STOP presents the user with the proposed structure (default, A, or B) and the reasoning. The user can adjust or commit. Once committed, Phase 4 module-writing proceeds against the structure.

### What both variants share

In all three matrix-structure cases (default, A, B), the following discipline holds:

- Cell status categories apply unchanged (substantive / thin / modeled-only / intentionally empty / coverage gap)
- The runtime agent's perspective discipline applies unchanged (module bodies don't reference matrix structure)
- The downstream handoff to building-context-libraries works the same way — the library skill consumes whatever matrix structure was committed
- Per-cell `load_when:` triggers are required for all substantive / thin / modeled-only cells regardless of which matrix the cell sits in

---

## Sub-Profile Module Shape

Every sub-profile module is a short metaprompt. The typical length is 200–600 words; complex audience matrices with cross-audience-leverage cells, multi-cross-cutting attributes (e.g., substance-preservation register × touchpoint-segmentation × multigenerational framing), or modeled-only status may run to 700–1100 words. The per-cell budget is set in Pass 2's `agent-needs.md` document on the basis of the cell's complexity and is reaffirmed at the Phase 3 STOP. Compressing below the budget to hit 200–600 forces dropping decision frames that are operationally consequential; running above the budget without justification means the module is doing work the matrix-level documentation or other cells should be carrying. The discipline is to write the minimum length needed to shift agent generation, not to hit a fixed target.

The module contains:

1. **Cell coordinate.** "Engagement stage: consideration × Relationship type: individual major donor."
2. **What this audience is doing when they encounter our content.** One paragraph. The decision they are in the middle of, not their biography.
3. **What carries weight with them.** Bulleted decision frames: what kinds of evidence, framing, or appeal increases their likelihood of moving toward what the organization wants.
4. **What loses them.** Bulleted: framings, claims, or asks that cause withdrawal. Often the inverse of what carries weight, sometimes specific.
5. **When generating for this audience, prioritize.** Bulleted generation directives: "outcome-specific over metric-aggregated"; "showing the work before naming the ask"; "ground-truth over framework."
6. **Source basis.** One paragraph naming the source classes the module draws on and the citations. Brief — the matrix document carries the longer methodology discussion.

What a sub-profile module does NOT contain:
- A named individual ("Mary," "the Smiths")
- Biographical detail (age, family, occupation) unless it's a stated client-defining audience attribute (e.g., for a youth services org, "under 18" is a defining attribute, not biographical color)
- Channel specifics framed as behavior ("uses Instagram nightly") rather than as channel guidance ("Instagram-first audiences engage with this content at a different cadence than email-first audiences — adjust pacing accordingly")
- Demographic generalizations not anchored to a source
- Research narration ("Our peer dossier analysis found…")

---

## Cell Status Categories

Every cell in the matrix has a status:

- **Substantive** — Multiple sources support the cell's decision frames. A full sub-profile module exists.
- **Thin** — One or two sources weakly support the cell. A short sub-profile exists but the matrix-level documentation flags it as thin. The downstream library agent should treat the module as a starting hypothesis.
- **Modeled-only** — No client or competitive sources address this cell directly; the sub-profile draws from tested modeled-data. Module exists with explicit modeled-data citations.
- **Intentionally empty** — Sources don't support a meaningful sub-profile here, and the absence is itself informative (e.g., "this client doesn't engage this audience cut, by design"). No module; matrix documentation notes the reason.
- **Coverage gap** — A substantive sub-profile would belong here, but current sources are insufficient. Matrix documentation names what kind of source would fill it.

The status field is what makes the matrix diagnostic. A matrix where every cell is "substantive" either reflects unusually rich source coverage or — more often — a build agent that papered over thin coverage. The Phase 4 gate explicitly checks status assignments.

---

## Downstream Handoff to building-context-libraries

The output of this skill is upstream input for building-context-libraries. The handoff format matters because the library skill's Phase 2 (Comprehend) needs to recognize and consume the artifact efficiently.

**What the library skill expects to find:**

1. **`audience-matrix.md`** — The navigation document. The library skill reads this first to understand the audience space.
2. **`modules/`** — A directory of sub-profile modules. The library skill treats these as candidate inputs for the library's own audience module(s). It may consolidate, restructure, or reshape them — the audience research artifact is *input* to library design, not the final library audience module.
3. **`source-index.md`** — So the library skill knows what sources have already been analyzed and can avoid re-reading from scratch.
4. **`process-log.md`** — Optional but valuable. Tells the library skill what dimension framings were considered and rejected, what the modeled-data contributed, what conflicts surfaced.

**What the library skill does with the artifact:**

The library skill's Phase 3 (Design) decides where audience context lives in the library — as a single shared module, a per-agent module, an addendum, or a set of conditional modules with `load_when:` triggers. The matrix's cell-level triggers and status fields feed that decision.

The library skill may also reshape sub-profiles. A cell that this skill produced as a stand-alone module may become a section of a broader audience module in the library, or a sub-profile module that the library loads conditionally. The decision is the library skill's; this skill's job is to produce well-sourced, well-shaped *input* to that decision.

**What this skill should NOT produce:**

- A finished library audience module ready to drop in unmodified
- An agent definition (that's the library skill's job)
- Load-discipline classification (always-load vs. conditional) — that's a library-level decision

The artifact is research synthesis, organized for downstream library design. It is not itself a finished library module.

---

## Modeled-Data Discipline (Detailed)

This is the most consequential discipline in the skill, because it governs how the absence of direct audience research is handled. Get this wrong and the skill produces well-shaped artifacts grounded in sycophantic hallucination.

### Phase 2 Pass 2 protocol for modeled-data

1. **Surface the modeled picture explicitly.** Before drawing on it, write the model's current picture of this audience down. Treat it as a source document being produced. Include:
   - Motivations the model attributes to this audience
   - Decision triggers
   - Common framings that resonate / repel
   - Trust signals
   - Distrust signals
   - What the model believes the audience is currently navigating (cultural moment, sector dynamics)

2. **Identify what the model is drawing on.** Where possible, name specific sources the model can identify: published research, recurring journalism, polling, sector reports, longitudinal studies. Link to them when the model can produce verifiable references. Mark claims without identifiable sources as "model inference from aggregated training data" — this is honest, F0-compliant, and tells the user the inferential basis.

3. **Test against client/competitive sources.**
   - **Confirmed:** Other source classes support the modeled claim. Module-eligible.
   - **Refuted:** Other source classes contradict the modeled claim. Module-ineligible. The conflict goes in the process log.
   - **Refined:** Other source classes adjust the modeled claim — narrowing it, qualifying it, or specifying the conditions under which it holds. The refined claim is module-eligible; the refinement is part of the citation.
   - **Untested:** No other source class addresses the claim. Stays in the process log unless the cell is "modeled-only."

4. **In the sub-profile module, signal the modeled-data contribution.** Language like "Trained-data picture suggests X, refined by client sources to Y" is acceptable in the source-basis section. Direct module body language can read as a regular sourced claim once the testing is complete — the citation carries the signal.

### What this discipline prevents

- **Sycophantic audience pictures.** The model defaults to flattering, action-encouraging pictures of any audience. Testing against client sources catches when reality is more complicated.
- **Stale audience pictures.** Training data has a cutoff. Sector dynamics change. Client sources (often more recent) catch staleness.
- **Sector-applicable defaults masquerading as client-specific insight.** The model's picture of "first-time individual donors" is the sector average; the client's actual first-time donors may diverge in ways the sector picture flattens. Testing surfaces the divergence.

---

## What Belongs Where

| Item | Goes in |
|------|---------|
| Decision frames for runtime agent | Sub-profile module |
| Dimension selection reasoning | Matrix document + process log |
| Considered-and-rejected dimensions | Process log |
| Modeled-data picture before testing | Process log |
| Tested modeled-data contributions | Sub-profile module (with citations) |
| Conflicts between sources | Process log + matrix coverage section |
| Cell status (substantive/thin/modeled-only/empty) | Matrix document |
| Load triggers (`load_when:`) | Matrix document, per cell |
| Source list | source-index.md |
| Per-source recognition notes | comprehension-artifacts/ |
| Build process narration | Process log only — never sub-profile modules |
| Citation form for sources | Sub-profile module source-basis section + source-index.md |

If a piece of substance is appearing in the wrong place, the fix is to move it, not to duplicate it.
