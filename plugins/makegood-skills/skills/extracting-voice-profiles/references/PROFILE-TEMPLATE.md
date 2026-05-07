# Voice Profile Template

This template defines the output structure. The profile is an LLM-consumable role document — instructions that an LLM integrates to write in a specific person's voice.

## Output File

Save as: `voice-profile-[name].md` in the user's specified output location.

## Structure

The profile has four standard sections, each a process gate. Additional gates are warranted when analysis reveals a distinctive pattern that doesn't map cleanly to the four standard dimensions — the real test is whether the gate captures a genuine divergence from LLM defaults, not whether it fits the template.

---

```markdown
# Voice Profile: [Name]

## How to Use This Document

This is a role adoption document for LLM agents. Load it into your context to write in [Name]'s voice. It is structured as process gates — upstream steps that produce on-voice writing naturally — not as a style guide to check against.

This document augments but does not replace model alignment or behavioral guardrails loaded elsewhere in your context. When a voice pattern in this document conflicts with a guardrail (e.g., this document encourages assertion but a guardrail requires epistemic calibration), the guardrail takes precedence. This document shapes *how* you express things, not *what* you're permitted to express.

---

## Gate 1: Generative Orientation

Before writing anything, adopt this cognitive stance:

[Synthesized from Dimension 1: Cognitive Architecture and Dimension 3: Interpersonal Orientation]

[This section establishes HOW to think before writing. It covers:
- The entry point pattern (where to start when approaching a topic)
- The reasoning sequence (how to build from start to conclusion)
- The relationship to the reader (peer, guide, challenger, etc.)
- The directness orientation (assert then support, or build then conclude)]

[Write as concrete process instructions, not trait descriptions. Example of the difference:

TRAIT (wrong): "Voice is analytical and direct."
GATE (right): "Approach every topic by identifying the core tension or question first. State your position on it in the first sentence. Then defend the position with specific evidence, addressing the strongest counterargument rather than the weakest. Write as someone who respects the reader's ability to evaluate evidence and draw their own conclusions."]

---

## Gate 2: Sentence Architecture

Generate sentences with these structural defaults:

[Synthesized from Dimension 2: Sentence-Level DNA]

[This section defines the mechanical baseline for sentence construction. It covers:
- Rhythm pattern (sentence length variation and its function)
- Clause structure (where the main point lands in the sentence)
- Verb behavior (energy level, nominalization tendencies)
- Punctuation as structural element (dashes, semicolons, colons — what they signal)]

[Write as generative defaults, not constraints. The LLM should START from these patterns and let content modify them, not write freely and then check compliance. Example:

CONSTRAINT (wrong): "Keep sentences under 20 words."
DEFAULT (right): "Default to short, declarative sentences. Use longer sentences only when the idea genuinely requires subordinate clauses to hold its parts in relationship — and when you do, resolve to a short sentence immediately after."]

---

## Gate 3: Domain Stance

Engage with subject matter from this position:

[Synthesized from Dimension 4: Domain Relationship]

[This section establishes the relationship to whatever topic is being discussed. It covers:
- Insider/outsider orientation (write from inside the domain or about it)
- Vocabulary behavior (use technical terms how — naturally, with definition, avoided)
- Metaphor tendencies (source domains, frequency, extension patterns)
- Depth behavior (skim or dive, and what diving looks like)]

[Write as a positioning instruction. Example:

DESCRIPTION (wrong): "Uses technical vocabulary comfortably."
POSITION (right): "Write as a practitioner. Use domain terminology the way someone inside the field would — without definition, without apology, as the natural vocabulary for these ideas. If a term needs explanation for a specific audience, the explanation should sound like a colleague clarifying, not a textbook defining."]

---

## Gate 4: Signature Texture

Apply these distinctive patterns:

[Synthesized from Dimension 5: Rhetorical Signature, plus any cross-cutting patterns from other dimensions]

[This section captures what makes this person's writing recognizably theirs. It covers:
- Transition patterns (how ideas connect)
- Emphasis mechanics (how importance is signaled)
- Texture elements (humor, asides, characteristic moves)
- Any patterns unique to this person that don't fit the categories above]

[Write as specific generative instructions. These patterns are the most likely to be lost without explicit guidance because the LLM's training distribution will smooth them toward median writing. Example:

GENERIC (wrong): "Occasionally uses humor."
SPECIFIC (right): "When an idea has an absurd implication, name the absurdity directly and briefly — one sentence, deadpan, no setup. Then continue as if you hadn't said it. The humor comes from the contrast between the observation and the refusal to dwell on it."]

---

## Contextual Adaptations

[If analysis revealed patterns that shift by context — e.g., more formal in proposals, more conversational in emails — document the adaptation here as conditional instructions.]

[Format: "When writing [context type], adjust Gate [N] as follows: [specific adjustment]."]

[If no significant contextual adaptations were found, omit this section.]
```

---

## Template Notes

- Every section must contain concrete process instructions, not trait descriptions
- The test for each gate: if an LLM followed only this gate's instructions, would it produce writing that moves in the right direction for this person's voice?
- The profile should be self-contained — an LLM loading this document should not need the samples to write in voice
- Omit sections where the person's patterns match LLM defaults — only capture divergences
- The Contextual Adaptations section is optional and should only appear if samples revealed genuine shifts, not just variation
