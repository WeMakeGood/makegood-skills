---
standards_id: longform
standards_name: Longform Feature Standards
derived_from: "Distilled from 10 feature articles across multiple authors in a major American magazine, 2025–2026. These standards capture craft patterns of the longform feature tradition, not the editorial voice of any single publication."
purpose: Load when drafting long-form feature articles — analysis, reported commentary, personal essay, cultural criticism.
---

# Writing Standards: Longform Features

## How to Use This Document

This is a craft standards module for LLM agents. Load it alongside a voice profile at the point of generation — not at session bootstrap — to write according to longform feature conventions. It is structured as process gates — upstream steps that produce on-genre writing naturally — not as a checklist to verify against.

These standards were distilled from the craft patterns of accomplished longform feature writing. They represent a tradition, not a publication — the same principles appear across the best feature journalism, essay writing, and analytical commentary regardless of masthead.

This document shapes how prose works at the craft level. It does not determine whose voice leads — load a voice profile for that. When a writing standard in this document and a voice profile suggest different approaches, the voice profile takes precedence for individual expression; this document takes precedence for citation conventions, evidence handling, and structural rules.

This document augments but does not replace model alignment or behavioral guardrails loaded elsewhere in your context. Epistemic calibration, sourcing discipline, and other behavioral standards still apply.

---

## Process Gate 1: Enter Through the Concrete

Before drafting any opening — for the article, a section, or a passage — complete this sequence:

1. Identify the most concrete, specific element available: a scene, a quote, a fact, a moment, a person acting. This is your entry point.
2. Open there. Not with what the element means, not with why it matters, not with the thesis it supports. Open with the element itself — the thing that happened, the words that were said, the situation as it exists.
3. Only after the reader has the concrete reality in hand, widen to the stakes, the pattern, or the argument it belongs to. The concrete element earns the abstraction that follows.

This sequence applies at every scale. The article opens with a specific situation and widens to its stakes. Each section opens with a specific development and widens to its implications. Each analytical passage begins with something observable before interpreting it.

The closing reverses this: return to the opening's concrete frame, but with its meaning transformed by everything the article has established. The closing does not summarize. It reframes.

Between sections, do not bridge with connective language ("Now let's turn to," "Another important factor," "It's also worth considering"). Instead, close the current section by surfacing an unanswered tension — a consequence not yet explored, a question the evidence has raised but not resolved. Open the next section where that tension lives. The reader crosses the gap on the question, not on a bridge phrase.

---

## Process Gate 2: Evidence Enters Through the Narrative's Door

Before introducing any evidence — a research finding, a historical fact, a data point, a quoted source — complete this sequence:

1. Identify the narrative moment the evidence speaks to. What has the reader just encountered in the article — what situation, what question, what tension — that this evidence illuminates?
2. Establish that moment first. The reader should already be inside the story or argument before the evidence arrives.
3. Introduce the evidence through the narrative's door: lead with the finding, the fact, or the number — what was discovered, what happened, what the data shows. The source attribution follows or is linked, not fronted. The reader encounters the evidence as something that belongs to the story being told, not as a report about a study.

When quoting a source directly, use the quote only when the speaker's specific phrasing carries weight the paraphrase would lose — because the words reveal stance, character, or argument in a way summary cannot. If the quote delivers routine information, paraphrase instead.

When presenting data, always provide the context that gives the number meaning: a comparison, a baseline, a before-and-after, a human consequence. No number arrives alone.

Do not frame evidence as important. If a finding needs you to announce its importance ("significantly," "notably," "it is worth noting"), it is not yet in the right position. Move it to where its importance is structural — where the narrative has created the need for exactly this information. The placement does the work.

---

## Process Gate 3: Land, Don't Elaborate

Before completing any passage that has moved through evidence, analysis, or dense information, complete this sequence:

1. Identify what the evidence or analysis *means* — the single claim, judgment, or implication that the passage supports.
2. State it in the shortest declarative sentence the meaning will bear. This sentence is the landing. It names what the reader should take from the passage and moves the article forward.
3. Test the landing: does it change how the reader sees what came before? If yes, it's a resolution. If it restates what the passage already showed, it's a summary — cut it and let the evidence stand.

After the landing, move on. Do not elaborate on the landing, restate it in different words, or add a qualifying sentence that softens its force. The short sentence after the dense passage is the article's rhythm signature. It is how the prose breathes.

This applies at paragraph level (a short sentence resolving a complex paragraph), at section level (a short paragraph resolving a dense section), and at article level (the closing reframe resolving the entire piece).

---

## Writing Discipline

These are not a separate checklist. They are consequences of the three gates above, stated explicitly because the LLM's statistical defaults resist them.

**Lead with what was found, not who found it.** When presenting research, reporting, or expert analysis, the finding comes first. Name the source by role or institution if needed for credibility; link to the full source. Do not front-load attribution ("According to Dr. Smith at Harvard..."). The reader cares about what was discovered. The researcher's identity matters only when it is itself part of the story. (Consequence of Gate 2.)

**Use em-dashes for mid-thought pivots.** When a sentence needs a qualification, aside, or pivot that would break momentum if set off in parentheses or a separate sentence, use an em-dash. This is longform prose's primary tool for keeping complex sentences in motion without losing the reader. Dashes hold the thought open; periods close it. (Consequence of Gate 3 — maintaining density without losing clarity.)

**Earn evaluation through accumulation.** Do not assert that something is important, dangerous, unprecedented, or significant. Accumulate the evidence that makes the evaluation self-evident, then land with a declarative sentence that names the conclusion the evidence supports. The reader arrives at the judgment through the evidence, not through the writer's announcement. (Consequence of Gates 2 and 3.)

**Keep the opening frame alive.** The person, event, or situation that opens the article is not scaffolding to be discarded. It recurs — in callbacks, in new developments, in the closing reframe. The frame is the article's through-line. If analytical passages have drifted far from the opening frame, find the connection back before closing the section. (Consequence of Gate 1.)

**Render the abstract through the concrete.** When the argument requires an abstract concept — systemic failure, political transformation, cultural shift — present it through a specific instance the reader can see. The instance carries the abstraction; the abstraction does not introduce the instance. (Consequence of Gate 1.)

---

## Revision Backstop

The three process gates handle the architecture. This backstop catches the LLM's strongest statistical defaults — words, phrases, and structures so deeply embedded in the training distribution that they slip through even with good gate framing.

**When you find one of these, don't just swap the word or restructure the sentence.** Return to the relevant process gate and rewrite from the generative instruction. The flagged item is a symptom; the slipped gate is the problem.

### Banned Language

These words and phrases do not appear in accomplished longform feature prose. Their presence is an immediate signal that the writing has drifted from the craft tradition:

- "It is important to note that"
- "It should be noted that"
- "This is significant because"
- "It's worth mentioning"
- "In conclusion"
- "As we have seen"
- "Let's explore"
- "Let's examine"
- "Delve into"
- "Shed light on"
- "Plays a crucial role"
- "Navigate" (as metaphor for handling difficulty)
- "Landscape" (as metaphor for a field or situation)
- "Realm"
- "Myriad" (as adjective)
- "Pivotal"
- "Underscores"
- "Facilitates"
- "Leverages"
- "Utilizes"

### Flagged Language

These words appear occasionally in quality longform prose but LLMs overuse them. Their appearance usually signals a slipped gate — check whether the passage follows the relevant gate's sequence before deciding to keep the word:

- "Notably" — usually means evidence isn't placed where its importance is structural (Gate 2)
- "Significantly" — same diagnosis as "notably"
- "However" at the start of a sentence — often a bridge phrase replacing the implicit-question transition (Gate 1)
- "Furthermore" / "Moreover" — additive transitions that signal topical arrangement rather than question-driven structure (Gate 1)
- "Ultimately" — often precedes a summary rather than a landing (Gate 3)
- "Indeed" — usually decorative emphasis; if the evidence is placed correctly, emphasis is structural
- "Crucial" / "Critical" — importance-framing that should be earned by placement (Gate 2)

### Structural Flags

- **A paragraph that opens by summarizing what the article just covered** signals report mode, not feature writing. Each section opens with new information or a new angle, not a recap.
- **A passage that introduces evidence with the source before the finding** ("According to a 2023 study by researchers at...") signals that Gate 2 has slipped. The finding leads; the source follows.
- **A closing paragraph that restates the article's thesis** signals that Gate 3 has slipped. The closing reframes the opening; it does not summarize the argument.
- **A transition sentence that names the topic of the next section** ("Another factor worth considering is the economic impact") signals that Gate 1 has slipped. The transition should be an implicit question, not a topic announcement.

---

## Scope

This module covers craft-level standards for longform feature writing: analysis, reported commentary, personal essay, and cultural criticism. It was distilled from the craft patterns of accomplished feature journalism across multiple authors. It does not cover hard news, newsletters, or audio/podcast conventions. It is not a voice profile — it does not capture any individual author's thinking patterns or rhetorical signature. It is not behavioral guardrails — epistemic calibration and sourcing discipline are governed by documents loaded elsewhere. Load this module when drafting longform feature prose. Skip it when the target is a different genre or format (e.g., academic writing, technical documentation, short-form news).
