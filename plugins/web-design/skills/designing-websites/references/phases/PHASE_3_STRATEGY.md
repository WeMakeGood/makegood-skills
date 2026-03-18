# Phase 3: Strategy

> **PROCESS GATES — Read these first:**
> - **Comprehension Before Strategy:** Every strategy decision must cite a comprehension finding. Before defining a CTA, name the comprehension insight that supports it. Before defining an audience journey, reference the reasoning pattern from Phase 2 that reveals how that audience thinks. If a strategy decision has no comprehension grounding, it's a generic marketing pattern — generate one that does.
> - **Alternative Before Commitment:** Before committing to any conversion strategy, generate at least one alternative approach. Name what each gains and loses. Then choose. This gate prevents defaulting to the first plausible structure.
> - **Second-Order Before Finalizing:** Before finalizing CTAs, answer: what does this CTA create downstream? What visitor needs does it leave unaddressed? What does this funnel structure make harder to find?
> - **Log, Don't Document:** Strategy decisions go in the process log. The sitemap carries CTA and audience assignments directly. No separate strategy files — they consume context window space that voice profile and writing standards need during content generation.

---

## What This Phase Does

Transform comprehension findings into conversion decisions: CTA hierarchy, audience journeys, and conversion paths. The output is strategy decisions logged to the process log — not separate documents. Phase 4 (Sitemap) implements these decisions directly.

**Why no strategy documents:** The old approach generated three files (calls-to-action.md, audience-analysis.md, conversion-strategy.md) that restated comprehension findings in marketing-template format. These consumed context window space without adding information the sitemap didn't already carry. Worse, the agent loaded them during content generation sessions where they competed with voice profile and writing standards for context attention — and voice always lost.

---

<phase_strategy_load>
## Step 0: Load Session B Context

**GATE:** Load in this order before any strategy work:

1. `<OUTPUT_PATH>/build-state.md`
2. `<OUTPUT_PATH>/process-log.md`
3. `<OUTPUT_PATH>/source-index.md` — contains the Website Content Mappings from Phase 2 that connect comprehension findings to specific sources
4. All source documents listed in the source index (re-read)
5. Agent definition (if provided — from context library manifest in build state)
6. All context modules listed in the agent definition's frontmatter (re-read each)

Write to build state: "Session B loaded: build-state, process-log, [count] source files re-read, agent definition [yes/no], [count] context modules re-read"

If you believe you already know the sources from a previous session, you are likely post-compaction. Re-read anyway.
</phase_strategy_load>

---

<phase_strategy_build>
## Step 1: Define CTA Hierarchy

Using the requirements from Phase 1 and reasoning patterns from Phase 2:

**Core philosophy: Interest + Intent → Action.** Every piece of content converts user interest and intent into a specific action. There are no "informational only" pages.

Define:
- **Primary CTA** — the single most important action. Button text, destination, urgency level.
- **Secondary CTA** — the fallback for visitors not ready for the primary. Button text, destination.
- **Tertiary CTAs** — supporting actions (newsletter, social follow, resource download).

**Before committing:** Does the CTA language reflect how the organization talks (from Comprehend), or does it sound like generic web marketing? "Schedule a Consultation" might be accurate but "Let's Talk About Your Project" might better match an organization that thinks relationally. If context modules define how the organization communicates, the CTA language should be consistent with that.

---

## Step 2: Define Audience Journeys

Using comprehension findings (Step 4 from Phase 2):

For each audience segment, define the journey — not as a marketing funnel, but as a sequence of questions the visitor is trying to answer:

- What brings them to the site? (entry point and intent)
- What question are they trying to answer first?
- What do they need to see before they trust this organization?
- What moves them from "interested" to "ready to act"?
- What CTA matches their readiness?

**Audience reasoning test:** For each segment, can you describe what they'd type into a search engine? If not, the segment is too abstract.

---

## Step 3: Define Conversion Paths

Map how each audience segment moves from entry to action:

- Which pages serve which segments?
- Where do journeys converge on CTAs?
- What obstacles prevent conversion and what content addresses them?

**Before committing to a strategy:** Generate at least one alternative conversion approach. Name what each gains and what it loses. Choose — and log why. This is required, not optional.
</phase_strategy_build>

---

## Step 4: Log Strategy Decisions

**Write all strategy decisions to the process log.** This is the only output of this phase — there are no strategy files.

Log under `Phase 3: Strategy`:

```
**CTA Hierarchy:**
- Primary: [action] — [button text] — [destination] — [rationale from comprehension]
- Secondary: [action] — [button text] — [destination] — [rationale]
- Tertiary: [actions]

**Audience Journeys:**
- [Segment]: [entry] → [questions they ask] → [trust signals needed] → [CTA]
- [Segment]: [entry] → [questions they ask] → [trust signals needed] → [CTA]

**Conversion Paths:**
- [Segment entry → page sequence → CTA destination]

**Alternative Strategy Considered:**
- [What it was, what it gains, what it loses, why rejected]

**Comprehension Findings That Drove Decisions:**
- [Which insights from Phase 2 shaped which strategy choices]
```

Also update the build state Requirements Summary with finalized CTAs and audience segments.

---

## GATE

Write to build state:
- "Strategy decisions logged to process-log: [yes]"
- "Primary CTA: [specific action with button text]"
- "Primary conversion path: [entry → action]"
- "Alternative strategy considered: [what it was and why chosen/rejected]"
- "[N] audience segments with defined journeys"
- "Comprehension findings that shaped strategy: [which insights drove which decisions]"

---

## STOP

**Present to the user:**
- Primary and secondary CTAs with rationale grounded in comprehension findings
- Audience journeys — not marketing funnel stages, but the questions each segment is trying to answer
- Conversion paths with the alternative you considered
- How comprehension findings shaped the strategy (this shows the user that strategy reflects *their* organization, not a template)
- Any concerns or gaps

**Ask:**
- Are these CTAs correct? Does the primary action feel right?
- Do the audience journeys match how your people actually behave?
- Does the conversion strategy make sense?
- Anything missing?

**Do not proceed to sitemap until the user confirms the strategy.** Strategy decisions lock in everything downstream — changing CTAs after the sitemap is built means rebuilding the sitemap.

**After the user responds, log corrections or confirmations to `process-log.md`.**

---

## After This Phase

Update build state:
- **Current phase:** Phase 4 (Sitemap)
- **Next phase file:** `references/phases/PHASE_4_SITEMAP.md`

Proceed directly to Phase 4 in the same session.
