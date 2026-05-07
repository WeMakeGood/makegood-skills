---
standards_id: web-explainer
standards_name: Web Explainer Standards
derived_from: "Distilled from 15 web feature articles across 13+ authors at a business and innovation publication, 2025–2026. These standards capture craft patterns of the web-first explanatory journalism tradition, not the editorial voice of any single publication."
purpose: Load when drafting web-first explainers, business/tech features, trend analyses, and reader-service journalism — articles that teach while they tell.
---

# Writing Standards: Web Explainers

## How to Use This Document

This is a craft standards module for LLM agents. Load it alongside a voice profile at the point of generation — not at session bootstrap — to write according to web-first explanatory journalism conventions. It is structured as process gates — upstream steps that produce on-genre writing naturally — not as a checklist to verify against.

These standards were distilled from the craft patterns of accomplished web-first business and innovation journalism. They represent a tradition — the same principles appear across the best explanatory web features regardless of masthead. The defining characteristic of this tradition is that it teaches while it tells: articles are structured around the reader's questions, expert voices do the heavy explanatory lifting, and the writer's conversational presence keeps complex material accessible.

This document shapes how prose works at the craft level. It does not determine whose voice leads — load a voice profile for that. When a writing standard in this document and a voice profile suggest different approaches, the voice profile takes precedence for individual expression; this document takes precedence for structure, evidence handling, and reader-service conventions.

This document augments but does not replace model alignment or behavioral guardrails loaded elsewhere in your context. Epistemic calibration, sourcing discipline, and other behavioral standards still apply.

---

## Process Gate 1: Start With Why the Reader Should Care

Before drafting the opening of the article or any section, complete this sequence:

1. Identify what the reader already knows or assumes about this topic. They arrived because something caught their attention — a headline, a question, a development. Meet them there.
2. Open with the tension, surprise, or stake that makes this worth reading — in the first sentence or two. Not background. Not context. The thing that makes the reader lean in. This can be a striking stat, a provocative question, a counterintuitive claim, or a concrete development that upends expectations.
3. Only after the hook has landed, provide the context needed to understand it. The context earns its place by serving the hook, not the other way around.

This sequence applies at every scale. The article opens with the biggest hook. Each section opens with a smaller hook — a question the reader now has, a development that shifts the frame, a "so what" that demands exploration. Subheadings are not neutral labels but compressed arguments or questions that advance the article's thesis and let the reader scan.

Structure the article around the reader's questions, not around your analytical arc. After each section, ask: what does the reader want to know next? Open the next section there. The organizing principle is the reader's curiosity, not the writer's argument.

Close by looking forward, not back. End with an implication, an unresolved tension, an expert quote that opens the frame wider, or an honest acknowledgment of what's still unknown. The closing does not summarize what the article just said.

---

## Process Gate 2: Let Experts Teach

Before incorporating any expert source, complete this sequence:

1. Identify what the reader needs to understand at this point in the article — the concept, the mechanism, the "why" behind the "what."
2. Find the expert quote that explains it in accessible, vivid terms. The best quotes in this tradition don't validate the writer's point — they teach the reader something the writer's prose set up but didn't yet deliver.
3. Frame the quote with just enough context for the reader to understand who is speaking and why their perspective matters. Then let the quote do the work.

Expert quotes in this tradition carry the explanatory payload. The writer's prose establishes the situation and the question; the expert's words deliver the insight. If the writer is paraphrasing everything and dropping in one illustrative quote, the convention has been inverted. The quote is the explanation, not decoration for it.

When presenting data, attach the consequence in the same sentence or the sentence immediately after. A statistic without its "so what" is inert. The reader should encounter the number and its meaning together — what it costs, who it affects, how it compares to what came before, why it matters right now. If you need a separate paragraph to explain why a number is significant, the number wasn't placed where its significance is clear.

When reaching out to companies or organizations for comment, include the response — or note the attempt even when there's no response. "X did not respond to a request for comment" is a transparency signal, not filler. It tells the reader the journalist did the work.

---

## Process Gate 3: Talk to the Reader, Not at Them

Before writing any passage, check the register: would you say this to a smart friend who doesn't work in this field? If not, rewrite it so you would.

1. Use contractions, rhetorical questions, and direct address naturally. The prose should feel like a knowledgeable person explaining something interesting over coffee — not a briefing paper or an academic analysis.
2. Anchor unfamiliar concepts in things the reader already knows. Cultural references, consumer products, everyday experiences — these are not decoration but the explanatory mechanism. If the reader needs to already understand your field to follow the analogy, the analogy has failed.
3. The writer's evaluative voice is present throughout — not separated into a labeled opinion section, not hedged with distancing language. When something is a problem, say it's a problem. When a strategy seems misguided, say so and show why. The reader trusts the writer's judgment because it's grounded in the evidence the article has presented.

Keep paragraphs short — 1 to 3 sentences is the default. Single-sentence paragraphs are not throwaway lines; they're pivots, landings, or transitions that do structural work. A paragraph longer than 4 sentences in this tradition signals that the writer is explaining when they should be showing, or that two ideas have been compressed.

---

## Writing Discipline

These are not a separate checklist. They are consequences of the three gates above, stated explicitly because the LLM's statistical defaults resist them.

**Hook first, context second.** Every opening — article, section, paragraph — earns the reader's attention before asking for their patience. If the first sentence could be cut without losing the hook, it's context masquerading as an opening. (Consequence of Gate 1.)

**Use subheadings as argument.** Subheadings appear every 3–5 paragraphs and advance the article's thesis. They are scannable — a reader who reads only the subheadings should get the article's argument in compressed form. Neutral labels ("Background," "Analysis," "Conclusion") waste this opportunity. (Consequence of Gate 1.)

**Data with consequences, always.** No number arrives without its meaning attached. The stat and its "so what" belong in the same breath — the same sentence or the sentence immediately after. If a stat needs a paragraph of explanation to land, it's placed wrong. (Consequence of Gate 2.)

**Explain through culture, not through abstraction.** When a concept needs grounding, reach for the cultural reference, the consumer product, the everyday experience the reader already has. The reader should never need specialized knowledge to follow the analogy. (Consequence of Gate 3.)

**Evaluate in plain language.** When the evidence supports a judgment, state it directly: "That's the problem." "This seems misguided." "Unfortunately, it's getting worse." The writer's evaluative voice is a feature of the tradition, not something to hedge or disclaim. Ground it in the evidence just presented and move on. (Consequence of Gate 3.)

---

## Revision Backstop

The three process gates handle the architecture. This backstop catches the LLM's strongest statistical defaults — words, phrases, and structures so deeply embedded in the training distribution that they slip through even with good gate framing.

**When you find one of these, don't just swap the word or restructure the sentence.** Return to the relevant process gate and rewrite from the generative instruction. The flagged item is a symptom; the slipped gate is the problem.

### Banned Language

These words and phrases do not appear in accomplished web-first explanatory journalism. Their presence signals that the writing has drifted from the craft tradition:

- "It is important to note that"
- "It should be noted that"
- "In conclusion"
- "As we have seen"
- "As previously mentioned"
- "Let's delve into"
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
- "Stakeholders"
- "Paradigm"
- "Synergy" (unless quoting someone)
- "Robust" (as generic intensifier)

### Flagged Language

These words appear occasionally in quality web journalism but LLMs overuse them. Their appearance usually signals a slipped gate:

- "Notably" / "Significantly" — usually means the data isn't placed where its significance is structural (Gate 2)
- "However" at the start of a sentence — often a formal bridge where a casual pivot ("But") would serve the conversational register better (Gate 3)
- "Furthermore" / "Moreover" / "Additionally" — additive transitions that signal listing rather than question-driven structure (Gate 1)
- "It remains to be seen" — a closing cliché; if the future is uncertain, name what's uncertain and why (Gate 1)
- "Experts say" without naming the expert — violates the teaching-through-experts convention (Gate 2)
- "In today's world" / "In an era of" — throat-clearing; start with the specific thing that's happening (Gate 1)
- "Ultimately" — often precedes a summary rather than a forward-looking close (Gate 1)

### Structural Flags

- **An opening paragraph that provides background before the hook** signals that Gate 1 has slipped. The hook comes first — even if the reader needs context, the context follows the thing that makes them want it.
- **An article organized by topic rather than by reader questions** signals that Gate 1 has slipped. Each section should answer the question the reader has *at that point in the article*, not cover a topic in the writer's outline.
- **An expert quote used only to validate the writer's point** signals that Gate 2 has slipped. Quotes should teach — deliver insight the writer's prose set up but didn't complete. If the quote merely agrees with the preceding paragraph, it's redundant.
- **A passage that explains a concept in technical or abstract terms when a cultural reference would do** signals that Gate 3 has slipped. Ground it in something the reader already knows.
- **A closing paragraph that summarizes the article** signals that Gate 1 has slipped. Look forward, not back.
- **A paragraph longer than 4 sentences** signals compression. Split it.
- **Neutral subheadings** ("Background," "Overview," "Key Findings") signal missed opportunity. Subheadings should advance the argument.

---

## Scope

This module covers craft-level standards for web-first explanatory journalism: business features, tech explainers, trend analyses, design coverage, and reader-service articles. It was distilled from the craft patterns of accomplished web-first business and innovation journalism across multiple authors. It does not cover longform narrative features, structured analytical journalism, or personal essays — for those, load the appropriate baseline standards. It is not a voice profile — it does not capture any individual writer's thinking patterns or rhetorical signature. It is not behavioral guardrails — epistemic calibration and sourcing discipline are governed by documents loaded elsewhere. Load this module when drafting web-first features that need to teach while they tell. Skip it when the target is a different genre or format.
