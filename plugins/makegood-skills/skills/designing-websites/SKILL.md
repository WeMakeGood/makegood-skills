---
name: designing-websites
description: Designs website content strategy and generates all content assets through interactive phased workflow. Starts with CTAs and business goals, then builds audience analysis, sitemap, and page content with user review at each stage. Use when planning a new website, creating website content strategy, building site architecture, or generating website copy. Triggers on website design, content strategy, sitemap creation, or website planning requests.
---

# Designing Websites

<purpose>
Claude's default when asked to build a website is to produce pages — an About page, a Services
page, a Contact page — organized by convention rather than conversion. This produces sites where
every page exists because "websites have one" rather than because it moves a visitor toward
action. This skill counters that default through CTA-first strategy (define what visitors should
do before deciding what pages exist), a comprehension phase (understand the organization's
reasoning before writing its content), and page-level outlining (every section justifies its
existence before full content is written).

The skill runs across multiple sessions because website content generation exceeds a single
context window. Source documents, strategy, and sitemap decisions fill context before content
writing begins. If voice profile and writing standards are provided, they must be fresh when
content generation starts — not buried under strategy documents from earlier phases. The
mandatory session break before content generation exists to reload them last.
</purpose>

## Critical Rules

**SOURCING:** Every claim about the organization must trace to a source document or user statement. Before stating any organizational fact, locate its source. If you cannot locate a source, use `{{needs-input: description}}` — never fill gaps with plausible-sounding content.

**EPISTEMIC CALIBRATION:** The user should always be able to tell whether content comes from their input, is inferred from patterns in their input, or is your strategic recommendation — because your language makes the distinction clear.

**PROFESSIONAL CHALLENGE:** If the user's proposed CTAs are weak, their audience analysis is incomplete, or their sitemap has dead ends — say so directly. Challenge unclear business goals before proceeding. Your job is to produce an effective website, not to validate the user's initial ideas.

**NATURAL PROSE:** Write as the practitioner who would create this content if AI didn't exist. Adopt their vocabulary and rhythm. Revision backstop — these words signal voice drift: pivotal, crucial, vital, testament to, underscores, highlights, vibrant, tapestry, delve, foster, garner, leverage, landscape (figurative), holistic, robust, synergy, cutting-edge, groundbreaking, nestled, showcases, boasts, elevate. Also avoid: "Not only X but Y," "serves as," "stands as," vague attribution ("experts say"), formulaic balance ("Despite challenges, [positive]").

---

## Interaction Model

**GATE** — a self-check. The agent writes a commitment statement to the build state before proceeding. Gates do not require user input.

**STOP** — a user interaction point. The agent presents its work and waits for the user to respond before proceeding. The agent never proceeds past a STOP without user input.

Every phase ends with a GATE followed by a STOP. Without stops, the agent runs all phases in a single pass, producing content built on unchecked assumptions.

---

## Build Process

7 phases across 3-4 sessions. Each phase has a dedicated instruction file containing everything needed.

| Phase | Name | Instruction File | Function |
|-------|------|------------------|----------|
| 1 | Gather | [PHASE_1_GATHER.md](references/phases/PHASE_1_GATHER.md) | Collect requirements, source docs, context library paths |
| 2 | Comprehend | [PHASE_2_COMPREHEND.md](references/phases/PHASE_2_COMPREHEND.md) | Understand org reasoning before strategy |
| 3 | Strategy | [PHASE_3_STRATEGY.md](references/phases/PHASE_3_STRATEGY.md) | CTAs, audience analysis, conversion strategy |
| 4 | Sitemap | [PHASE_4_SITEMAP.md](references/phases/PHASE_4_SITEMAP.md) | Flow-based sitemap, template assignments |
| 5 | Outline | [PHASE_5_OUTLINE.md](references/phases/PHASE_5_OUTLINE.md) | Per-page section outlines with purpose statements |
| 6 | Content | [PHASE_6_CONTENT.md](references/phases/PHASE_6_CONTENT.md) | Full page content generation |
| 7 | Validation | [PHASE_7_VALIDATION.md](references/phases/PHASE_7_VALIDATION.md) | Structural checks, package delivery |

**Before starting any phase:** Read the phase instruction file. It contains all procedures and gates for that phase.

### Session Architecture

| Session | Phases | Why Together |
|---------|--------|-------------|
| A | Gather + Comprehend | Comprehension needs source documents fresh in context |
| **MANDATORY BREAK** | | Strategy needs comprehension findings fresh, not buried under source material |
| B | Strategy + Sitemap | Strategy feeds directly into sitemap decisions. Two user STOPs: after Strategy (validate CTAs), after Sitemap (validate structure). |
| **MANDATORY BREAK** | | Content generation needs voice/standards fresh, not buried under strategy |
| C | Outline + Content | Outlining catches structural problems before full content is written |
| D | Validation | May combine with C if context permits |

**The boundaries between A→B and B→C are mandatory** — content generation needs a full context window with voice profile and writing standards loaded last.

---

<phase_start>
## Starting a New Project

1. **Ask the user for paths:**
   - "Where are your source documents?" — may be multiple directories
   - "Do you have a context library for this organization?"
   - "Where should I create the project?" (default: `./tmp/<project-name>/`) → `OUTPUT_PATH`

2. **Read the Phase 1 instruction file:** [references/phases/PHASE_1_GATHER.md](references/phases/PHASE_1_GATHER.md)

3. **Begin Phase 1.** — The phase reads all sources before asking any questions about the organization.
</phase_start>

---

<phase_resume>
## Resuming a Project

If `<OUTPUT_PATH>/build-state.md` exists:

1. **Read `build-state.md`** — it tells you the current phase, what's done, and what's next.
2. **Read `process-log.md`** — the reasoning history of decisions made so far.
3. **Read the phase instruction file** it points to.
4. **Continue from where work left off.**
</phase_resume>

---

## The Process Log

A running document the agent writes throughout every phase, saved to `<OUTPUT_PATH>/process-log.md`. Started at the beginning of Phase 1, updated continuously.

**What goes in:** Decisions and their reasoning, user corrections, comprehension insights, strategy alternatives considered, gaps identified. Newest entries first.

**What does NOT go in:** Source summaries, completion status (that's build-state's job), restated content from strategy documents.

**Why it matters:** Without a process log, each session starts from scratch. The agent re-derives decisions already made, or contradicts them. The log is what makes multi-session work coherent.

---

## Reference Files

| File | Purpose |
|------|---------|
| [references/TEMPLATES.md](references/TEMPLATES.md) | Build state, process log, source registry, page outline templates |
| [references/CONTENT-FORMAT.md](references/CONTENT-FORMAT.md) | Content file structure, template syntax, placeholder conventions |
| [references/FORMS-CPTS.md](references/FORMS-CPTS.md) | Form specs, CPT/ACF definitions |
| [references/TECHNICAL-CONTEXT.md](references/TECHNICAL-CONTEXT.md) | WordPress platform specifics |
| Phase files in [references/phases/](references/phases/) | Self-contained instructions per phase |

---

## Example: Community Land Trust

Shows the shape of output at each phase — not a template to reproduce.

**Phase 1 (Gather) — process log entry:**
```
Primary CTA: "Apply for homeownership" — user's exact words
Secondary CTA: "Donate to the land trust"
Audience segments: 2 — prospective homebuyers, donors/supporters
Context library: agent definition at context-library/agents/web-content.md,
  3 modules (F1_organizational_identity, S1_community_engagement, S3_housing_programs),
  voice profile at S0_natural_prose_standards.md
Source documents read and indexed: 7 (brand guide, 3 program docs, interview synthesis,
  existing site copy, annual report)
```

**Phase 2 (Comprehend) — process log entry:**
```
Organizational reasoning: This org thinks about homeownership as community
stability, not individual wealth-building. Sources consistently frame buyers
as "community members joining the land trust" not "customers purchasing homes."
The distinction matters for website voice — the site should read like a
neighbor explaining how the program works, not a real estate listing.

Convergence: Brand guide says "permanently affordable" and program docs describe
the resale formula — same principle, different registers. Website should use
"permanently affordable" (audience language) and link to the formula (proof).

Tension: Annual report emphasizes growth metrics (units built, families served)
but interview synthesis reveals the org sees itself as "small by design."
Website needs to reconcile scale language with intentional-community identity.

Audience reasoning: Prospective buyers search "affordable housing [city]" and
"how to buy a house with low income" — they're solving a problem, not shopping
for a land trust. The site must answer their question before explaining the model.
```

**Phase 3 (Strategy) — process log entry:**
```
CTA Hierarchy:
- Primary: "Start your application" — /apply — from comprehension: org frames
  this as joining a community, but buyers search for housing solutions. CTA
  bridges both: application starts the relationship.
- Secondary: "Support permanently affordable housing" — /donate — from
  comprehension: donors respond to "permanently" (durability) not "affordable"
  (charity).

Alternative considered: Lead with "Learn about community land trusts" as
primary CTA to educate before converting. Rejected — comprehension finding
shows buyers arrive with a problem to solve, not curiosity about a model.
Education is a trust signal on the journey, not the destination.
```

**Phase 4 (Sitemap) — excerpt:**
```
### Find a Home (/find-a-home/)
- Template: page
- CTA: Primary — "Start your application"
- Audience: Prospective homebuyers
- Purpose: Answer "can I afford a home here?" with available properties and
  eligibility, leading to application
- Sources:
  - #5 (program docs) — eligibility criteria, available property types
  - #7 (S1_community_engagement) — how org frames "finding a home" vs. "buying a house"

### How It Works (/how-it-works/)
- Template: page
- CTA: Primary — "Start your application"
- Audience: Prospective homebuyers (consideration stage)
- Purpose: Explain the land trust model as the answer to "what's the catch?" —
  the trust signal needed between interest and application
- Sources:
  - #3 (brand guide) — "permanently affordable" language
  - #5 (program docs) — resale formula, ground lease mechanics
  - #7 (S1_community_engagement) — community stability framing (not wealth-building)
  - #9 (interview synthesis) — founder's explanation of why the model works
```

**Phase 5 (Outline) — excerpt:**
```
# How It Works
**CTA:** Primary — "Start your application"
**Primary audience:** Prospective homebuyers in consideration stage
**Page purpose:** Remove the "what's the catch?" barrier between interest and application

### 1. The Problem
**Purpose:** Validate the visitor's experience — housing is unaffordable,
  they've been looking, traditional paths don't work
**Source:** comprehension finding — buyers arrive solving a problem
**Key content:** Acknowledge the housing reality without statistics (needs-input
  for local data)

### 2. How Community Land Trusts Work
**Purpose:** Explain the model as a solution to their problem, not as an
  abstract concept
**Source:** S1_community_engagement module + program docs
**Key content:** Ground lease explained in buyer terms, not legal terms

### 3. What "Permanently Affordable" Means for You
**Purpose:** Address the resale question (the actual "catch" people worry about)
**Source:** brand guide "permanently affordable" language + resale formula from
  program docs
**Key content:** Honest explanation of equity and resale — this is where trust
  is built or lost

### 4. Start Your Application
**Purpose:** Convert consideration to action
**Handoff:** Link to /apply with reassurance that applying is exploring, not committing
```

---

<failed_attempts>
## What DOESN'T Work

- **Starting with pages.** "We need an About page" before "What do we want visitors to do?" produces pages that exist because websites have them, not because they serve a conversion goal. The skill starts with CTAs, not pages.

- **Skipping comprehension.** Jumping from requirements gathering to strategy produces generic marketing patterns — "awareness → consideration → decision" funnels that could belong to any organization. Comprehension forces the agent to understand how *this* organization thinks before proposing *its* conversion strategy. Without it, a nonprofit gets the same funnel as a SaaS company.

- **Running all phases in one session.** Context compaction silently degrades voice profile, writing standards, and source material. By the time the agent reaches content generation, it's reverted to default web copy because the instructions governing voice are gone. The session architecture exists to prevent this.

- **Loading voice/standards early in the content session.** Voice profile and writing standards must be the LAST documents loaded before content generation begins. If loaded at session start and followed by strategy docs and sitemap, they compact and the agent produces generic prose that sounds like AI writing about the industry rather than a person in it.

- **Generating content without page outlines.** Going from sitemap to full content produces pages with unclear section flow, redundant content across pages, and sections that exist for convention ("Our Values," "Our Approach") rather than because they move a visitor toward the CTA. Outlines catch this before full content is written.

- **Separate strategy documents.** The old approach generated three files (calls-to-action.md, audience-analysis.md, conversion-strategy.md) that restated comprehension findings in marketing-template format. These consumed context window space without adding information the sitemap didn't carry. Worse, loading them in the content session competed with voice profile and writing standards for context attention — and voice always lost. Strategy decisions belong in the process log. The sitemap carries CTA and audience assignments directly.

- **Inventing details.** Creating plausible-sounding company history, statistics, or testimonials because it makes the content feel complete. These always ring false and erode trust. Missing information is a placeholder, not a blank to fill.

- **Single conversion strategy.** Defaulting to the first plausible CTA hierarchy without considering alternatives. The first idea is rarely the best — and the second idea often reveals assumptions in the first.

- **Dead-end pages.** Pages with no CTA become navigation dead ends. Every page must exit toward a conversion action, even if the action is soft (newsletter signup, related content).

- **Not logging decisions.** Without a process log, each session starts from scratch. The agent re-derives decisions already made, or worse, contradicts them silently.

- **"Everyone" as audience.** If you can't name specific audience segments with distinct entry points and intents, the site can't speak to anyone effectively.
</failed_attempts>
