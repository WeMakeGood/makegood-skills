# Writing Standards Module Template

This template defines the output structure. The module is an LLM-consumable document — craft-level instructions that an LLM integrates to write according to a specific publication or genre's standards.

## Output File

Save as: `writing-standards-[name].md` in the user's specified output location.

## Structure

The module has three process gates, a writing discipline section, and a revision backstop. The gates are synthesized from the three analytical dimensions but do not need to map 1:1 — each gate captures the most important craft principle the analysis revealed, drawing from whichever dimensions support it.

---

```markdown
---
standards_id: [name — lowercase, hyphens]
standards_name: [Human-Readable Name]
derived_from: [source description — e.g., "10 Atlantic feature articles, 2024-2025, multiple authors"]
purpose: [one sentence — when to load this module]
---

# Writing Standards: [Name]

## How to Use This Document

This is a craft standards module for LLM agents. Load it alongside a voice profile at the point of generation — not at session bootstrap — to write according to [publication/genre] conventions. It is structured as process gates — upstream steps that produce on-genre writing naturally — not as a checklist to verify against.

This document shapes how prose works at the publication level. It does not determine whose voice leads — load a voice profile for that. When a writing standard in this document and a voice profile suggest different approaches, the voice profile takes precedence for individual expression; this document takes precedence for citation conventions, evidence handling, and structural rules.

This document augments but does not replace model alignment or behavioral guardrails loaded elsewhere in your context. Epistemic calibration, sourcing discipline, and other behavioral standards still apply.

---

## Process Gate 1: [Name — e.g., "Structure by Story, Not by Topic"]

Before writing, complete this sequence:

[Upstream sequence requirement synthesized from the analysis. This is the single most important craft principle for this publication/genre — the one that shapes the largest difference between "LLM-default prose" and "prose that reads like this publication."

Write as a concrete generative instruction: what the LLM must do BEFORE or WHILE writing. Not what to avoid. Not what the prose should look like. What to DO.

Example of the difference:

CHECKLIST (wrong): "Articles should have a narrative structure with evidence woven in."
GATE (right): "Before drafting any section, identify the reader's experience that the section speaks to — what they've seen, felt, or assumed from their own work. Open the section there. Evidence enters through the reader's experience, not through its own introduction. If you're writing 'Research shows that...' without first establishing what the reader already recognizes, the evidence has entered through its own door."]

---

## Process Gate 2: [Name — e.g., "Evidence Enters Through the Narrative"]

Before presenting any evidence or data, complete this sequence:

[Second most important craft principle. Same format as Gate 1.]

---

## Process Gate 3: [Name — e.g., "Start Concrete, Earn the Abstract"]

Before writing any opening — for the article, a section, or a passage — complete this sequence:

[Third most important craft principle. Same format as Gate 1.]

---

## Writing Discipline

These are not a separate checklist. They are consequences of the three gates above, stated explicitly because the LLM's statistical defaults resist them.

[State each discipline rule as a consequence of a gate. Format:

**[Rule name — e.g., "Use the finding, not the researcher."]** [Explanation of the rule, grounded in the publication's conventions. Include the gate it derives from and why the LLM's default would violate it.]

Include 3-6 discipline rules. Each should be specific enough that an LLM can apply it mechanically.]

---

## Revision Backstop

The three process gates handle the architecture. This backstop catches the LLM's strongest statistical defaults — words, phrases, and structures so deeply embedded in the training distribution that they slip through even with good gate framing.

**When you find one of these, don't just swap the word or restructure the sentence.** Return to the relevant process gate and rewrite from the generative instruction. The flagged item is a symptom; the slipped gate is the problem.

### Banned Language

[Words and phrases that no writer in this publication/genre uses. These are immediate signals of AI-generated prose in this genre's context. List them plainly.]

### Flagged Language

[Words and phrases that writers in this genre use occasionally but LLMs use constantly. Flag and reconsider — the word itself isn't wrong, but its appearance usually means a gate has slipped. List with brief notes where helpful.]

### Structural Flags

[Sentence-level or paragraph-level structures that signal genre drift. These are patterns, not individual words. Include 2-4 structural flags.

Two structural flags should always be evaluated during analysis because LLMs produce them even when gates are well-written:

1. **Preview/thesis openings:** A section that opens by stating what it will prove or summarizing what comes next — before the evidence has earned the conclusion. If the publication opens sections through the concrete (a scene, a detail, an event), flag thesis-first openings as genre drift.

2. **Voice stance drift under subject shift:** A passage where the author's established voice stance drops out when the subject changes — describing someone else's experience, reporting on an organization, presenting a case. LLMs default toward journalistic distance whenever the subject shifts. If the publication maintains its voice stance across subject shifts, flag passages where the author becomes an invisible reporter.

Include these only if the analysis confirms the publication follows the non-default convention. If the publication uses thesis-first openings or deliberately shifts register for different subjects, these are not flags — they're the standard.]

---

## Scope

[One paragraph: what this module covers and does not cover. Name the publication or genre. Name what it is NOT — it is not a voice profile, not behavioral guardrails, not a content strategy. State when to load it and when to skip it.]
```

---

## Template Notes

- Every gate must contain concrete process instructions, not trait descriptions or checklists
- The test for each gate: if an LLM followed only this gate's instructions, would it produce prose that moves toward this publication's craft standards?
- The module should be self-contained — an LLM loading this document should not need the original samples to write on-genre
- 3 process gates is the standard count. If analysis reveals that 2 gates capture the craft fully, use 2. Do not pad to 3 with a weak gate. If 4 are genuinely needed, include 4 — but the bar is high; most publications' craft can be captured in 3.
- The Writing Discipline section makes implicit gate consequences explicit. It exists because LLM defaults are strong — stating the consequence directly helps more than relying on the gate alone.
- The Revision Backstop is genre-specific. The S0 natural prose standards already capture universal AI-tell words (delve, foster, etc.). This backstop captures words and structures specific to this genre that would mark prose as off-genre.
- Omit the Contextual Adaptations section unless the genre has genuinely different conventions for different article types (e.g., news vs. features within the same publication)
