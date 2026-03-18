---
standards_id: structured-analysis
standards_name: Structured Analytical Journalism Standards
derived_from: "Distilled from 12 feature articles across 11+ authors at a structured analytical news platform, 2025–2026. These standards capture craft patterns of the structured analytical journalism tradition, not the editorial format or brand of any single publication."
purpose: Load when drafting analytical journalism that separates reporting from interpretation — scoops, political analysis, business coverage, geopolitical reporting.
---

# Writing Standards: Structured Analytical Journalism

## How to Use This Document

This is a craft standards module for LLM agents. Load it alongside a voice profile at the point of generation — not at session bootstrap — to write according to structured analytical journalism conventions. It is structured as process gates — upstream steps that produce on-genre writing naturally — not as a checklist to verify against.

These standards were distilled from the craft patterns of a rigorous analytical journalism tradition that architecturally separates reporting from interpretation. The same principles appear across the best analytical journalism regardless of masthead — the discipline of making the boundary between fact and opinion legible to the reader.

This document shapes how prose works at the craft level. It does not determine whose voice leads — load a voice profile for that. When a writing standard in this document and a voice profile suggest different approaches, the voice profile takes precedence for individual expression; this document takes precedence for evidence handling, structural rules, and the separation of reporting from analysis.

This document augments but does not replace model alignment or behavioral guardrails loaded elsewhere in your context. Epistemic calibration, sourcing discipline, and other behavioral standards still apply.

---

## Process Gate 1: Separate What You Know From What You Think

Before drafting, divide your material into two categories and keep them architecturally separate throughout:

1. **Reported material** — facts, events, quotes, data, sourced claims. This is what the reporting established. It belongs in passages where the prose register is neutral, tight, and factual. No evaluation, no hedging qualifiers that imply opinion, no importance-framing. Present the facts and let them accumulate.

2. **Analytical material** — your interpretation, evaluation, prediction, or judgment about what the reported material means. This belongs in clearly distinct passages where the prose register shifts to first-person, direct, and openly evaluative. When you move into analysis, commit to it — state what you think plainly, without distancing language ("some might argue," "it remains to be seen").

The reader must always be able to tell which mode they're in. The boundary can be signaled by section breaks, paragraph spacing, a shift in register, or explicit framing — but it must be legible. If a passage blends reported facts with your evaluation and the reader can't tell where one ends and the other begins, the passage has failed.

This separation is not about being "objective" in the reporting sections — curation, emphasis, and sequencing are all editorial choices. It's about transparency: the reader knows what happened (reporting) and what the journalist makes of it (analysis) because the structure makes the distinction unmistakable.

---

## Process Gate 2: Let Sources and Quotes Carry the Weight

Before writing any reported passage, complete this sequence:

1. Identify the strongest direct quotes available from your sources. These are quotes where the speaker's specific phrasing reveals stance, consequence, or tension that paraphrase would flatten.
2. Build the reported passage around those quotes. The prose sets up the context; the quote delivers the payload. Sentences move toward the quote, not away from it.
3. Attribute with specificity. Name the source when possible. When a source is anonymous, identify their role and their relationship to the information — not just "a person familiar with the matter" but which side of the matter they're familiar with. The reader should be able to assess the source's vantage point.

Quotes in this tradition are not decorative. They are the primary evidence vehicle. A reported passage that paraphrases everything and drops in one illustrative quote has inverted the convention. The reporting *is* what sources said, placed in context by the journalist's framing.

When presenting data, attach the consequence. A number alone is inert — pair it with what changed, what it costs, who it affects, or what it means relative to a baseline. The reader encounters the number through its impact, not as an isolated statistic.

---

## Process Gate 3: Include the Strongest Counter-Argument

Before finalizing any analytical piece, complete this sequence:

1. Identify the strongest counter-argument to your analysis — the one that could change a reasonable reader's mind. Not a straw man, not a weak objection, not a token nod to "both sides." The genuine competing view.
2. Present it with the same sourcing rigor you applied to the reporting. Quote or cite its strongest proponent. Give it enough space to be persuasive on its own terms.
3. Place it where the reader encounters it after your analysis, not before. The counter-argument functions as a stress test on what you've just argued — it earns its weight by being strong enough to make the reader reconsider.

This is not balance for balance's sake. It's an epistemic discipline: if your analysis can't survive contact with its strongest objection, the reader deserves to know that. The counter-argument section is where the article earns the reader's trust — by demonstrating that the journalist engaged with the best version of the opposing view, not a convenient one.

If no credible counter-argument exists, that itself is worth noting — but the bar for claiming unanimity is high.

---

## Writing Discipline

These are not a separate checklist. They are consequences of the three gates above, stated explicitly because the LLM's statistical defaults resist them.

**Keep paragraphs short — 1 to 3 sentences is the norm.** Each paragraph delivers a single unit of information and moves the article forward. Dense analytical passages still break into short paragraph units. A paragraph longer than 4 sentences in this tradition signals that two ideas have been compressed into one. (Consequence of Gates 1 and 2 — short paragraphs maintain the pace and clarity that structured analytical journalism requires.)

**Move forward, never circle back.** Each sentence advances the article. Do not restate what the previous sentence established, summarize what a section just covered, or preview what the next section will address. If the reader needs a fact to understand the current sentence, the fact should have appeared earlier. If it didn't, place it now and move on — don't frame it as a recap. (Consequence of Gate 1 — the reporting sections accumulate facts in sequence; circling back blurs the accumulation.)

**Shift register between reporting and analysis.** In reported passages, write tight — wire-service rhythm, neutral language, no evaluation. In analytical passages, write in first person, make direct claims, allow conversational phrasing. The register shift itself signals the boundary between reporting and interpretation. If the prose sounds the same in both modes, the reader can't tell which mode they're in. (Consequence of Gate 1.)

**Make analysis direct, not hedged.** When you move into analytical passages, state your assessment plainly. "This is a problem because" not "This could potentially be seen as problematic." "The bigger risk is" not "One might argue that the bigger risk could be." The structural separation from the reporting gives you permission to be direct — the reader knows this is your interpretation because the structure told them so. Use that permission. (Consequence of Gate 1.)

**Attribute with vantage point, not just anonymity.** When sources are anonymous, give the reader enough to assess the source's position: "a senior official who opposed the strikes" tells the reader more than "a person familiar with the matter." When two sides of a dispute are sourcing, make clear which side each source represents. The reader should be able to map the information to its origin. (Consequence of Gate 2.)

---

## Revision Backstop

The three process gates handle the architecture. This backstop catches the LLM's strongest statistical defaults — words, phrases, and structures so deeply embedded in the training distribution that they slip through even with good gate framing.

**When you find one of these, don't just swap the word or restructure the sentence.** Return to the relevant process gate and rewrite from the generative instruction. The flagged item is a symptom; the slipped gate is the problem.

### Banned Language

These words and phrases do not appear in accomplished structured analytical journalism. Their presence signals that the writing has drifted from the craft tradition:

- "It is important to note that"
- "It should be noted that"
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
- "Underscores"
- "Facilitates"
- "Leverages"
- "Utilizes"

### Flagged Language

These words appear occasionally in quality analytical journalism but LLMs overuse them. Their appearance usually signals a slipped gate:

- "However" at the start of a sentence — often a bridge phrase where juxtaposition would suffice (Gate 1)
- "Furthermore" / "Moreover" — additive transitions that signal the article is listing rather than accumulating (Gate 1)
- "Notably" / "Significantly" — importance-framing that belongs in the analytical passages, not the reporting; if it appears in a reported passage, the evidence isn't placed where its importance is structural (Gate 1)
- "Indeed" — usually decorative; if the evidence is placed correctly, emphasis is structural
- "Some argue that" / "Critics say" — vague attribution that violates Gate 2's specificity requirement; name the critic or describe their vantage point
- "It remains to be seen" — hedging that belongs nowhere; in reporting, state the uncertainty directly; in analysis, make your assessment (Gate 1)
- "Ultimately" — often precedes a summary rather than a forward-moving conclusion

### Structural Flags

- **A passage that blends a sourced claim with the journalist's evaluation in the same sentence** signals that Gate 1 has slipped. Separate the fact from the interpretation — even if they're in adjacent sentences.
- **A reported passage that paraphrases extensively and uses one quote for color** signals that Gate 2 has slipped. Quotes should carry the factual payload, not decorate it.
- **An analytical section that hedges every claim with "could," "might," "perhaps"** signals that Gate 1 has slipped in the other direction — the writer hasn't committed to the analysis the structure permits.
- **An article that presents its argument without including a genuine counter-view** signals that Gate 3 has been skipped. The absence of a counter-argument is not a sign of consensus — it's a sign of incomplete reporting or intellectual complacency.
- **A paragraph longer than 4 sentences** signals compression. Split it — each unit of information gets its own paragraph.

---

## Scope

This module covers craft-level standards for structured analytical journalism: scoops, political analysis, business and financial coverage, geopolitical reporting, and media analysis. It was distilled from the craft patterns of a rigorous analytical news platform across multiple authors and beats. It does not cover longform narrative features, personal essays, or cultural criticism — for those, load the longform feature standards instead. It is not a voice profile — it does not capture any individual journalist's thinking patterns or rhetorical signature. It is not behavioral guardrails — epistemic calibration and sourcing discipline are governed by documents loaded elsewhere. Load this module when drafting analytical journalism where the separation of reporting from interpretation is a priority. Skip it when the target is a different genre or format.
