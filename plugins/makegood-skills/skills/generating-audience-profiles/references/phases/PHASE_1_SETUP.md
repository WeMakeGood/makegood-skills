# Phase 1: Setup

**Session:** A (Setup + Comprehend Pass 1)
**Input:** User-supplied source path, output path, audience question, library handoff context.
**Output:** `source-index.md` (inventory only), `audience-needs-assessment.md`, `initial-expectations.md`, `process-log.md`, `build-state.md`.

> **CRITICAL RULES — Read these first:**
> - **Read each source fully before writing its source-index entry.** Full reading is what supports accurate classification and substantive analytical framing. (Earlier testing showed that skim-and-infer produced contaminated speculation; full reading produces strong work.)
> - **The source-index entry is structural, not content-extractive.** Once a source is read, its content is in working memory — but the source-index entry must describe what kind of document the source is, NOT what it says about audiences. The structural-claim discipline (allowed/disallowed verb patterns) is documented in Step 3 and is checked at the Phase 1 GATE.
> - **The audience-needs assessment is analytical.** Sections A (purpose) and B (operating environment) are the framing layer — depth and source citations are appropriate. Sections C (candidates) and D (comparison) are the candidates layer — compressed, uncited, sketch-depth. Pass 1 grounds the candidates; over-deep Phase 1 candidates anchor Pass 1 and waste work.
> - **The audience-needs assessment challenges the audience definitions the organization started with.** It surfaces audiences the explicit framing didn't name, disaggregates cuts the framing collapses, names tensions in the framing itself. This is Make Good's value-add.
> - **This phase ends with a STOP.** The user confirms source classifications, audience-needs assessment, and BLOCKING gaps before Phase 2 begins.

---

## Read first

Before doing any setup work, read [../ARCHITECTURE.md](../ARCHITECTURE.md) if you have not already. The source class taxonomy, runtime perspective, and audience question scoping are all referenced below.

---

## Step 1: Confirm the audience question

The audience question is what the organization would use these profiles to *decide*. It scopes dimension selection. If the user did not provide it at startup, ask now.

Acceptable forms:
- A decision: "How should our content shift between first-time prospects and active donors?"
- A distinction the organization is trying to act on: "What separates the funders who renew from the ones who lapse?"
- A capability the artifact should enable: "We need to write differently for our two main partner types."

Not acceptable forms:
- "Tell us about our audience." (Too generic to scope dimensions.)
- "Who is our audience?" (Description-shaped, not decision-shaped.)

If the user offers a description-shaped question, reframe it: "What would your team be using that audience picture to decide differently?"

Write the audience question, verbatim, into `process-log.md` under `## Audience Question`.

---

## Step 2: Note the library handoff context

If the user named an existing context library at startup ("this will feed into the library we built for [organization]") or said one is being built in parallel, note it in `process-log.md` under `## Library Handoff Context`. The build skill's Comprehend phase will read the matrix and modules; knowing the target library lets you avoid producing artifact shapes the library skill can't consume cleanly.

If no library is named, the artifact is built to the default handoff shape described in [ARCHITECTURE.md](../ARCHITECTURE.md#downstream-handoff-to-building-context-libraries).

This step comes early because the audience-needs assessment in Step 4 references organizational context that the library handoff often clarifies.

---

## Step 3: Load and classify sources (inventory only)

Read every file in `<SOURCE_PATH>`. For each source, classify into one of the four source classes (see [ARCHITECTURE.md, Source Classes](../ARCHITECTURE.md#source-classes)):

- **Class A:** Direct audience research (interviews, surveys, ethnographic notes)
- **Class B:** Competitive/sector research (peer dossiers, sector synthesis memos)
- **Class C:** Internal strategy and program documents (theory of change, strategic plans, brand guidelines)
- **Class D:** *Reserved.* Class D (LLM-modeled audience knowledge) is generated in Phase 2 Pass 2, not loaded here. Phase 1 inventories only file-based sources.

**Source ambiguity:** Some sources straddle classes (a peer-org case study written by the client may carry both Class B competitive analysis and Class C internal framing). Classify by primary character and note the secondary class in the source-index entry.

**Read fully before writing the entry.** This is the architectural prevention against the failure mode where source-index entries get written from titles, format specs, or pre-read inference. The entry is written AFTER reading, not before. If you find yourself filling fields from speculation about what a source likely contains, stop and read the source.

**Update the source index after reading each file — do not batch.** Memory blurs across sources. Read one, update its entry, read the next.

**Write `source-index.md`** with one entry per source. The entry captures the source's identity — what kind of document it is, where it sits in the source set — NOT what the source reveals about audiences.

```markdown
## [Source title]

- **Path:** [relative path from SOURCE_PATH]
- **Class:** [A / B / C, plus secondary if applicable]
- **Date / vintage:** [when this source was produced, if knowable]
- **Audience-relevance scope:** [structural claim only — see allowed/disallowed patterns below]
- **Read status:** read
```

### The structural-claim discipline (CRITICAL)

The "Audience-relevance scope" field is where the source-index contamination failure happens. Even after a full read, the entry must describe **what kind of document this is**, not **what the source says about audiences**. Audience-content claims live in Pass 1 per-source notes — populating them in the source-index pre-anchors Pass 1 and the audience-needs assessment.

**Allowed patterns** (genuinely structural):

- "Peer-org dossier following the standard Dossier Format."
- "Internal strategy doc; Make Good's own evaluation of the organization."
- "Sector synthesis memo addressing the principals directly."
- "Sector prompt; research planning artifact, not audience research."
- "Format specification document."
- "Combined dossier covering two operators plus a landscape overview."

**Disallowed patterns** (content extraction smuggled in as structural description):

- "Documents [specific audience segment] as unclaimed white space." → content claim
- "Names the [N] constituency buckets the [client artifact] uses." → content claim
- "Maps the [domain] landscape across [named peer-orgs]." → content claim
- "Identifies competitor audience targeting." → content claim
- "Documents what audience segments each competitor reaches." → content claim
- "Includes Audience Profile, Marketing & Messaging, and Visual Design sections." → arguably structural if the document's format is being described, but the moment you start naming what's in those sections, it becomes content extraction

**The test:** *Could this sentence be written by someone who has only seen the document's title and confirmed its format, without reading its substance?* If yes, it's structural. If the sentence requires having read the content for substance, it's content extraction and belongs in Pass 1.

**The honest constraint:** A full read of each source is required for accurate classification (skim-and-infer caused a different failure mode in earlier testing). Once content is read, it is in working memory. The discipline is not to pretend the content isn't there — it is to keep the source-index entry restricted to *what kind of document this is*, leaving the *what does the document say about audiences* work for Pass 1 per-source notes where it belongs.

If a source turns out to be irrelevant to audience work (e.g., visual design assets, internal scheduling memos), exclude it and note the reason in the "Sources excluded" section of source-index.md.

The source-index is the inventory and the Pass 1 reading checklist. The audience-content claims about each source live in the per-source notes Pass 1 produces.

---

## Step 4: Initial audience-needs assessment

This is the analytical step Phase 1 commits to. The audience question names what the organization wants to *decide*. The source set is what the organization commissioned to inform those decisions. Together they signal what the organization is investigating. But they do not, by themselves, name the audiences the organization needs to engage to succeed.

**Your job in this step is to think analytically about the organization's purpose and produce an audience-needs assessment.**

The assessment has two layers, governed by different rules:

- **Framing layer (sections A and B):** Organizational purpose and operating environment. Depth is appropriate here — this is the analytical frame that justifies the audience candidates. Source citations are allowed when they ground the framing.
- **Candidates layer (sections C and D):** The audience candidates themselves and the comparison to the explicit framing. **This layer is compressed and uncited.** Candidates are sketches Pass 1 will ground, not pre-drafts of sub-profile modules. Over-deep candidates anchor Pass 1 reading and waste work when Pass 1 refines them.

Write to `<OUTPUT_PATH>/audience-needs-assessment.md`:

### A. The organization's purpose, as you read it (framing layer — depth OK)

2–4 paragraphs naming what this organization is trying to accomplish. Source citations are allowed where they ground the analysis (specific evidence about the organization's positioning, founder background, market moment). Do not pretend to certainty you don't have — if the purpose is multi-part or contested, say so.

Examples of well-shaped purpose statements:
- *"This is a new sports league launching its first season. Its purpose is to build a sustainable American audience for an unfamiliar sport from zero, against a competitive set that already commands established fan attention."*
- *"This is a long-established conservation nonprofit transitioning from grant-funded operations to a diversified funding base. Its purpose is to grow individual giving without losing the institutional-funder relationships that currently sustain it."*

### B. The organization's operating environment (framing layer — depth OK)

2–3 paragraphs naming the constraints, opportunities, and competitive pressures. What is the organization differentiating from? What is it competing for? What is structurally hard about what it is trying to do? Source citations are allowed and useful here.

### C. Audience-needs assessment (candidates layer — compressed and uncited)

Given the purpose (A) and operating environment (B), **which audiences does this organization need to engage to succeed?**

Produce 4–8 audience candidates. For each, the format is strict:

```markdown
### C[N]. [Audience name described by decision orientation, not biography]

- **Why necessary:** [1–2 sentences connecting this audience to the organization's purpose. No specific source citations — the argument stands on the purpose-and-environment logic itself.]
- **Agent work:** [1–2 sentences on the writing or decision tasks the downstream library agent would need to do for this audience.]
- **Source-set expectation:** [1 line — which source class is likely most informative.]
```

**Hard constraints on the candidates layer:**

- **No specific source citations.** The candidates-layer fields stand on the audience-needs logic itself, not on evidentiary detail. Specifically forbidden in candidate-field prose:

  - **No statistics or numerical evidence** (e.g., revenue figures from a peer-org's strategic pivot, audience-share percentages, conversion rates from a specific case study).
  - **No named events, dates, or properties from sources** (e.g., a specific event the principals attended, a dated peer-org milestone, a named entertainment property's audience ranking, a named era from a peer-org's history).
  - **No named peer organizations, playbooks, or specific examples drawn from sources** (e.g., "[Peer-org]'s endemic-then-mainstream sponsor sequence," "[Peer-property]'s city-qualifier mechanism," "[Peer-org]'s infrastructure-before-brand sequencing," "[Peer-property]'s venue routing pattern").
  - **No specific sector references in candidate-field prose** (e.g., "per Sector 02," "(Sectors 02, 04, 08)"). The **source-set-expectation field** is the one place where source-class references are OK — and even there, name only the class and sector number, not the specific dossier content. "Class B — Sector 02" is allowed. "Class B — Sector 05 [named-peer-property] dossier on [specific transferable pattern]" is not allowed (the parenthetical names content).

  The test for each candidate field: *Could a reader who has not read any of the source documents understand this sentence?* If understanding requires having read a specific source for substance, the citation needs to be removed and the underlying point either generalized or moved to Pass 1.

  What this leaves room for: general references to organizational context the framing layer established ("the family positioning," "the touring model," "the stated audience"), general sport/industry knowledge that doesn't depend on specific sources, and the audience-needs logic itself.

- **No paragraphs in the candidate fields.** 1–2 sentences per field, hard cap. Candidates are sketches, not pre-drafts of sub-profile modules.
- **Roughly equivalent depth across candidates.** If one candidate's rationale is three times longer than another's, the assessment is doing too much work for that candidate.

Why these constraints: Pass 1 will test the candidates against source content. Pass 2 will refine them. Phase 3 will commit. Anything written in the candidates layer that gets reshaped in Pass 1 or Pass 2 is wasted work — and worse, it anchors Pass 1 reading toward confirmation of the rich Phase 1 sketch rather than fresh recognition.

The candidates should NOT all be audiences the audience question or the source set explicitly names. Some should be analytically derived from the purpose and operating environment — audiences the organization needs but hasn't articulated, or audiences the question's framing collapses. This is the value-add Make Good brings to audience design.

### D. Comparison to what the question/source set names (candidates layer — terse)

A short section comparing your audience candidates to what's already named in the audience question or signaled by the source set:

- **Audiences your assessment includes that the explicit framing doesn't.** 1 line per candidate, naming the candidate and the brief reason.
- **Audiences the explicit framing includes that your assessment doesn't.** 1 line per audience, with the interpretation you favor.
- **Audiences the framing collapses that your assessment disaggregates (or vice versa).** 1 line per collapse/disaggregation.

The differences are the most useful Pass 1 tests — they're the questions Pass 1 reading should answer. Keep this section terse: it's a list of questions for Pass 1, not an argument.

**The assessment is a working artifact, not a commitment.** Pass 1 will test it. Pass 2 will refine it. Phase 3 will commit to which audiences and which dimensions anchor the matrix.

---

## Step 5: Initial expectations (written against the audience-needs assessment)

Before reading any source for substance (and yes — Step 3 read for inventory/classification, not for substance), write expectations about each audience in your audience-needs assessment.

**For each audience candidate in the assessment**, write 2–4 expectations of the form:

> "I expect to find that [audience] is [motivated by / sensitive to / shaped by / distinguishing on] X."

These are predictions, not assertions. They will be confirmed, refuted, or refined during Pass 1.

The expectations are written against your assessment, not against the source-set's named audiences. This is what makes Pass 1's expectations-vs-findings reflection diagnostic — expectations and findings have different sources, so the comparison produces real signal.

Save expectations to `<OUTPUT_PATH>/initial-expectations.md`.

**Also write:** "Expectations I think may be wrong" — 2–4 self-flagged predictions that surface where your analysis is least confident. Surprises against these are not failures; they're the analysis working.

---

## Step 6: Initialize working files

Create the following files in `<OUTPUT_PATH>`:

- **`build-state.md`** — Session resume state. Use [../../templates/build-state.md](../../templates/build-state.md) as scaffold.
- **`process-log.md`** — Running reasoning log. Use [../../templates/process-log.md](../../templates/process-log.md) as scaffold.
- **`comprehension-artifacts/`** — Empty directory; per-source notes go here in Phase 2 Pass 1.

Populate `build-state.md` with:
- Phase: 1 (Setup)
- Status: in progress (complete after STOP)
- Audience question (one line)
- Library handoff (one line)
- Source count by class
- Audience-needs assessment: [N] audience candidates
- Initial expectations: [N] expectations
- Next phase: 2 (Comprehend Pass 1), pending Phase 1 STOP
- Next phase file: `references/phases/PHASE_2_COMPREHEND.md`

---

## GATE: Phase 1 work complete (pre-STOP self-check)

Before presenting to the user, write the following statements to `process-log.md`. Each statement is also a discipline check — if the answer reveals a failure, fix before proceeding to the STOP.

**Source-index discipline:**

- "Audience question recorded verbatim: [yes/no]"
- "Library handoff context noted: [yes/no]"
- "Sources read fully before source-index entries written: [yes/no — confirm read-before-write discipline held]"
- "Sources loaded and classified: [N] total — [N_A] Class A, [N_B] Class B, [N_C] Class C, [N_excluded] excluded"
- "Source-index 'Audience-relevance scope' entries scanned for content extraction: [yes — N entries checked]. Any entries using verbs like 'Documents X,' 'Names Y,' 'Maps Z,' 'Identifies W' where the content claim could only be written after reading the source for substance? [list any flagged entries, or 'none — all entries pass the structural test']"

**Audience-needs assessment discipline:**

- "Audience-needs assessment written: [N] audience candidates"
- "Framing layer (sections A and B) — depth and source citations as needed: [confirmed]"
- "Candidates layer (sections C and D) scanned for source citations: [yes — N candidates checked]. For each candidate field that is NOT the source-set-expectation line, scan for these four failure patterns: (a) numerical evidence, (b) named events / dates / properties from sources, (c) named peer organizations / playbooks / specific examples drawn from sources, (d) specific sector references in candidate-field prose. If any pattern appears in any candidate field other than source-set-expectation, the discipline failed regardless of intent. Source-set-expectation fields are checked for content-extraction from named dossiers (naming the dossier and the specific pattern is a violation; 'Class B — Sector [N]' is allowed). [list any flagged candidates and the specific pattern found, or 'none — candidates layer is uncited as required']"
- "Candidates layer scanned for length: [yes]. Any candidate field longer than 2 sentences? [list any flagged candidates, or 'none — candidates are at sketch depth']"
- "Comparison to explicit framing produced: [N] candidates not in original framing, [N] in framing but not in assessment, [N] tier/kind disaggregations noted"

**Expectations and gaps:**

- "Initial expectations written against assessment: [N] expectations covering [N] audiences"
- "BLOCKING gaps identified: [list or 'none']"

**If the source-index scan or the candidates scan flags entries, the fix is mandatory before STOP.** Move the flagged content to a working notes section of `process-log.md` for use during Pass 1, and rewrite the source-index entries or candidate fields to comply with the structural-and-compressed disciplines. Do not present to the user with known-contaminated artifacts.

---

## STOP — Phase 1 Review

**Present to the user:**

- **Source inventory** — counts by class, list of excluded sources with reasons, any sources that surfaced surprises during reading (genre, vintage, or relevance different from what the source path/name suggested)
- **Audience-needs assessment** — the organization's purpose statement, operating environment, the audience candidates with rationale, and the comparison to what the audience question and source set explicitly name
- **Initial expectations** — by audience, including the self-flagged "expectations likely wrong" set
- **BLOCKING gaps** — places where the audience-needs assessment requires information that's missing from the source set and from your inference (e.g., "your assessment includes a 'host-city local' audience, but no source addresses local-market dynamics — Pass 1 will not be able to test this without additional sources or a confirmed modeled-only path")
- **Conflicts or tensions surfaced during inventory** — any source-set characteristics that complicate the work (e.g., "the synthesis memos contain strategic recommendations to the organization, which means classifying them as pure Class B understates their Class C character")

**Ask:**

Confirmation questions:
- Does the purpose statement match what the organization is actually trying to do?
- Are the source classifications correct? Any sources I should re-classify or exclude?
- Are there additional sources I should include before Pass 1?
- For BLOCKING gaps — can you provide the missing information, accept the gap as a documented limitation, or is the audience-needs assessment itself off in a way that the gap exposes?

Challenge questions (these invite the user into the analytical work; they should be asked explicitly, not collapsed into the confirmation set):
- Which audience candidates in the assessment surprise you, and which feel obvious?
- Which candidates feel too confident — where do you suspect Pass 1 will refine or refute?
- Which audiences feel underweight or missing? Are there audiences the organization needs to engage that the assessment didn't surface?
- For the comparison to the explicit framing — which differences feel productive (the assessment caught something the question missed) vs. which feel like the assessment overreached (the explicit framing was right)?

The confirmation questions establish what the user agrees with; the challenge questions surface what the user knows that the assessment doesn't yet. Both kinds of input shape Pass 1.

**Do not proceed to Phase 2 until the user has responded to both kinds of questions.** Pass 1 is structured to test the candidates against the sources; the user's challenge-question responses tell Pass 1 which candidates to test hardest.

---

## After the STOP

Update `process-log.md`:
- Record the user's confirmation (verbatim) and any adjustments made
- If the audience-needs assessment was revised, save the original and revised versions; the revision is itself diagnostic of where the agent's analysis diverged from the organization's actual situation

Update `build-state.md`:
- Phase 1: complete
- User-confirmed audience-needs assessment: [N] audiences
- Next: Phase 2 Pass 1 (Recognition)
- Next phase file: `references/phases/PHASE_2_COMPREHEND.md`

**Phase 1 stays in Session A** — continue directly into Phase 2 Pass 1.
