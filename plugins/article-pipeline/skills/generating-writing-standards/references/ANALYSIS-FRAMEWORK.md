# Writing Standards Analysis Framework

This document defines the analytical dimensions used to extract writing standards from publication or genre samples. Each dimension produces process gates — upstream requirements for the writing LLM — not descriptive checklists.

## Contents

- Why Dimensions, Not Checklists
- The Publication Test
- Dimension 1: Structural Discipline (including section opening conventions, voice stance under subject shift, LLM-default traps)
- Dimension 2: Evidence Handling
- Dimension 3: Prose Mechanics
- Analysis Process (5 steps)
- What to Prioritize

---

## Why Dimensions, Not Checklists

A checklist-based writing standard says: "Use evidence to support claims." This names a target and hopes the LLM hits it.

A dimension-based writing standard says: "Before introducing any research finding, establish the narrative moment or reader experience it speaks to. The finding enters through a door the narrative has opened." This establishes a generative sequence that produces evidence-grounded prose as a natural consequence.

Every dimension below should yield process gates, not descriptions of good practice.

---

## The Publication Test

Throughout analysis, apply this test to every candidate pattern: **Would a different author publishing in the same venue follow this rule?**

If yes — it's a publication standard. Include it.
If no — it's an individual voice pattern. Exclude it (it belongs in a voice profile, not a writing standard).
If it depends on context — it may be a contextual adaptation. Note the conditions.

---

## Dimension 1: Structural Discipline

How the publication structures argument, narrative, and information at the article level and the section level. This shapes how an LLM organizes prose before it writes any sentences.

**What to extract:**

- **Opening conventions:** How do articles begin? With a scene, a claim, a question, a specific person or moment? How quickly does the opening arrive at the article's central tension? What's the relationship between the opening and the reader's search intent or existing knowledge?

- **Closing conventions:** How do articles end? With a summary, a question, a callback to the opening, an open thread? Does the closing transform the opening frame or merely return to it?

- **Section architecture:** How are sections structured internally? Do they build arguments linearly, or layer recognition → evidence → understanding? Is there a consistent pattern to how sections relate to each other (each answers a question the previous one creates, vs. topical arrangement)?

- **Transition mechanics:** How do articles move between sections and between ideas? Explicit connectives? Juxtaposition? Questions as transitions? Bridge paragraphs? White space?

- **Evidence pacing:** How dense is evidence relative to analysis and narrative? Are there consistent patterns — evidence passages followed by connection passages, or evidence woven continuously through narrative?

- **Frame persistence:** Does the opening frame (person, event, question) remain present throughout the article, or does it set up the article and then disappear? How does the publication maintain narrative continuity through analytical passages?

- **Section opening conventions:** How do individual sections begin — with the concrete (a scene, a detail, a moment) or with a thesis that previews what the section will prove? This is a high-value extraction point because LLMs default to opening sections with preview/thesis sentences ("This section explores..." or delivering the conclusion before the evidence earns it). If the publication consistently opens sections through the concrete, this divergence from LLM defaults should become a structural flag in the module.

- **Voice stance under subject shift:** When the article's subject changes — describing someone else's experience, reporting on an organization, presenting a case study — does the author's established voice stance hold, or does it drift? LLMs default toward journalistic distance whenever the subject shifts away from the author's direct experience, regardless of the article's POV. If the publication maintains a consistent stance (practitioner involvement, essayist reflection, editorial authority) across subject shifts, this is a high-value divergence. If it deliberately shifts register for different subjects, note the convention.

**What this becomes in the module:**

A process gate that requires the writing LLM to make structural decisions before drafting — where to open, how to connect sections, how to pace evidence and narrative. The gate establishes the publication's structural logic as an upstream requirement.

**Cross-validation:** Structural patterns should be consistent across samples from different authors. If a structural pattern appears only in one author's work, it's a voice pattern, not a publication standard.

**LLM-default traps in this dimension:** Two structural patterns are especially resistant to correction even with well-written gates: (1) opening sections with a thesis/preview sentence before evidence earns it, and (2) drifting toward journalistic distance whenever the subject shifts away from the author's direct experience. Both are deeply embedded in LLM training distributions. If the publication's samples show different conventions, these should produce structural flags in the revision backstop — they are the patterns most likely to slip through.

---

## Dimension 2: Evidence Handling

How the publication presents, cites, and integrates evidence. This shapes how an LLM treats claims, data, and sources.

**What to extract:**

- **Citation convention:** How are sources cited? Inline hyperlinks? Footnotes? Author-name academic style? Parenthetical references? No formal citation at all? What appears in the prose vs. what appears in links?

- **Source presentation:** When a research finding is presented, what's the emphasis — the finding itself, the researchers who produced it, the institution, or the methodology? How much context does the publication provide about a source before presenting its findings?

- **Claim-evidence relationship:** Does the publication lead with claims then support them? Lead with evidence then derive claims? Weave claims and evidence together? Is this consistent across article types?

- **Data presentation:** How are numbers, statistics, and quantitative findings presented? Inline with narrative? Set apart in their own passages? With comparison context (to what baseline)? With sourcing?

- **Evidence curation vs. exhaustiveness:** Does the publication present every relevant finding, or curate a few findings and let the rest stay in links? How does it signal which findings are the structural load-bearers?

- **Evaluative restraint:** How does the publication handle evaluative claims — assertions of importance, quality, impact? Does it assert evaluations directly, earn them through evidence, or avoid them? How does it handle qualifiers?

**What this becomes in the module:**

A process gate that requires the writing LLM to handle evidence according to the publication's conventions before incorporating it into prose. The gate establishes rules for citation, selection, and integration.

**Cross-validation:** Evidence handling is usually the most consistent dimension across authors within a publication — it's often enforced by editorial standards. Strong patterns here are high-confidence.

---

## Dimension 3: Prose Mechanics

The sentence-level and paragraph-level patterns characteristic of the publication. This shapes how an LLM constructs individual sentences and paragraphs.

**What to extract:**

- **Sentence rhythm:** What's the characteristic sentence-length pattern? Not an average, but a rhythm — short-short-long? Consistently medium? Variable with short sentences for emphasis after dense passages?

- **Paragraph architecture:** How long are paragraphs typically? Do they contain one idea or develop an idea across multiple sentences? How do paragraphs relate to each other — each building on the previous, or each introducing a new angle?

- **Verb and language preferences:** Does the publication favor active or state verbs? Simple or complex vocabulary? Technical terminology or plain language? Does it use the simplest accurate word or the most precise? Are there characteristic verb patterns (e.g., leading with the action)?

- **Attribution style:** How does the publication attribute information? "According to" with the source? Inline description of the finding? Assertions without attribution (rare in quality journalism)? How does it handle indirect reference vs. direct quotation?

- **Distinctive anti-patterns:** What does the publication consistently NOT do that LLMs would default to? No synonym cycling? No throat-clearing openings? No "it is important to note" framing? No passive constructions for active events? These absences are high-value standards.

- **Punctuation as craft:** Does the publication use em-dashes, semicolons, colons in characteristic ways? Do these punctuation patterns serve a craft function (e.g., dashes for mid-thought pivots, colons for setup-delivery)?

**What this becomes in the module:**

Writing discipline entries and revision backstop items. Prose mechanics often produce the most granular, actionable standards — specific structural defaults and specific words/phrases to flag.

**Cross-validation:** Prose mechanics may show more author-level variation than the other dimensions. Distinguish between publication-level patterns (no attribution by author name, consistent evidence density) and individual patterns (characteristic use of dashes, sentence fragment emphasis). Publication-level patterns become standards; individual patterns belong in voice profiles.

---

## Analysis Process

### Step 1: Read all samples through once

Before analyzing any dimension, read all samples through. Note initial impressions — what feels consistent across samples, what varies. This first pass establishes the publication's "center of gravity" before detailed analysis begins.

### Step 2: Work through dimensions in order

For each dimension:

1. Return to the samples with this dimension's questions in mind
2. For each sample, identify candidate patterns with specific evidence (quote or cite)
3. After analyzing all samples, cross-validate: which patterns are consistent across samples and authors?
4. Distinguish publication standards from individual voice patterns (the Publication Test)
5. Compare each candidate against LLM defaults: does this add information, or would the LLM already do this?

### Step 3: Identify interactions between dimensions

Some patterns span dimensions — the way evidence is paced (Dimension 1) interacts with how it's cited (Dimension 2) and how the surrounding sentences are structured (Dimension 3). Note these interactions — they often produce the most important process gates because they capture something holistic about the publication's craft.

### Step 4: Prioritize by divergence from LLM defaults

Rank all identified patterns by how much they diverge from what an LLM would naturally produce. The highest-divergence patterns are the most valuable standards — without them, the LLM's output won't read like this publication. Low-divergence patterns can be omitted.

### Step 5: Synthesize into gates

The three dimensions are analytical entry points, not a 1:1 map to gates. A single process gate may draw from multiple dimensions. The module needs 3 gates — synthesize the most important findings into 3 process gates that, if followed, produce the publication's craft as a natural consequence.

---

## What to Prioritize

The highest-value patterns are those where:
- The publication's convention is consistent across authors and articles
- An LLM writing the same content would do it differently
- The pattern is craft-level (how to write) not content-level (what to write about)
- Following the pattern produces recognizably "on-genre" prose

The lowest-value patterns are those where:
- The publication does what any competent writer would do
- The pattern matches LLM defaults
- The pattern is content-specific rather than craft-specific
- Only one author exhibits the pattern
