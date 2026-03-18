---
name: generating-writing-standards
description: Generates structured writing standards modules from writing samples of a target publication, genre, or editorial tradition. Analyzes craft-level patterns and produces process-gate writing rules that shape how an LLM writes at the publication level. Use when user says generate writing standards, create prose standards, analyze publication style, build writing rules, extract editorial standards, or when writing samples from a publication or genre are provided for standards extraction. Activates when writing samples are present via pasted text, attached file, or uploaded document, even when accompanied by additional context files.
---

# Generating Writing Standards

<purpose>
LLMs default to a generic "good writing" mode — competent, clear, and recognizably AI. Writing
standards modules counter this by establishing publication-specific craft rules as process gates.
The result: prose that reads like it belongs in a specific publication or genre, not like it was
produced by a language model writing generically well.

This skill is structurally parallel to extracting-voice-profiles. Voice profiles capture a person's
voice — how an individual thinks and writes. Writing standards capture a publication or genre's
craft-level rules — how prose should work regardless of whose voice leads. They are complementary:
loaded together at the point of generation, the voice profile determines *whose* voice, the writing
standards determine *what publication-level craft rules govern the writing*.
</purpose>

## Critical Rules

**SOURCING:** Every pattern claimed in the writing standards must trace to specific evidence in the samples. Before stating any craft pattern, locate the passages that demonstrate it. If a pattern appears in only one sample, mark it as provisional. If it cannot be sourced to any sample, do not include it.

**EPISTEMIC CALIBRATION:** The user should always be able to tell whether a craft pattern is directly observed in samples, inferred from structural evidence, or your analytical interpretation — because your language makes the distinction clear.

**PROCESS GATES, NOT CHECKLISTS:** The writing standards must contain upstream process instructions that produce on-genre writing naturally. Never write "don't do X" or "avoid Y." Instead, establish a generative step that makes X architecturally unlikely. If you catch yourself writing a prohibition, convert it to a process gate.

**DIVERGENCES FROM LLM DEFAULTS:** Only capture patterns where the publication's prose diverges from how an LLM would naturally write the same content. Patterns that match LLM defaults add nothing to the module. The highest-value standards are the ones the LLM would get wrong without explicit guidance.

**PROFESSIONAL CHALLENGE:** If samples are insufficient to establish a pattern reliably, say so. If the samples show inconsistent craft patterns that resist standardization, surface this rather than forcing coherence. Not all writing traditions produce clean standards — name the limitation.

**AUGMENTATION BOUNDARY:** Writing standards shape craft-level rules for a publication or genre. They do not replace behavioral guardrails, sourcing discipline, or epistemic calibration loaded elsewhere in context. A writing standard that says "assert directly" does not override a guardrail requiring epistemic calibration.

**DISTINCTION FROM VOICE PROFILES:** Writing standards capture the publication. Voice profiles capture the person. If the analysis starts identifying individual authorial patterns (how one writer thinks, their personal rhetorical signature), that belongs in a voice profile, not a writing standards module. The test: would this standard apply to a different writer publishing in the same venue? If yes, it's a writing standard. If no, it's a voice pattern.

---

## Workflow

```
Writing Standards Generation:
- [ ] Phase 1: Gather samples and context
- [ ] Phase 2: Analyze samples against framework
- [ ] Phase 3: Draft writing standards module
- [ ] Phase 4: Review and refine with user
- [ ] Phase 5: Finalize and deliver
```

<phase_gather>
### Phase 1: Gather Samples and Context

**Ask the user for:**

1. **Writing samples** — At least 5 samples, ideally 10+. Samples should represent the target publication or genre, not a single author. Accept any combination of:
   - Published articles, essays, or features
   - Markdown files, text files, or URLs
   - Pasted text

2. **Context for the samples:**
   - What publication, genre, or editorial tradition do these represent?
   - Are these exemplary of the standard, or do they include range?
   - Is there a specific section or type within the publication (e.g., "Atlantic features" vs. "Atlantic opinion")?

3. **Output location** — Where to save the writing standards file.

4. **Name** — A short identifier for the standards (e.g., "longform", "practitioner-essay", "investigative-feature").

**Sample quality assessment:**

After receiving samples, evaluate before proceeding:
- **Minimum:** 5 samples, ideally from multiple authors within the same publication/genre
- **Ideal:** 10+ samples spanning the genre's range (different topics, lengths, publication dates)
- **Insufficient:** Fewer than 5 samples, or all from a single author (which produces voice patterns, not publication standards)

If samples are from a single author, inform the user that the result will blend voice and standards — and suggest using extracting-voice-profiles instead if the goal is to capture that author's voice.

If samples are insufficient, tell the user what additional material would improve the standards and why. Proceed if they choose to, but note the limitation.

**GATE:** Before proceeding, write:
- "Samples received: [count] from [publication/genre]"
- "Author diversity: [single author / multiple authors]"
- "Sufficiency assessment: [sufficient/limited/insufficient — and why]"
</phase_gather>

<phase_analyze>
### Phase 2: Analyze Samples

**Read** [references/ANALYSIS-FRAMEWORK.md](references/ANALYSIS-FRAMEWORK.md) before beginning analysis.

Work through each sample against all three dimensions:

1. **Structural Discipline** — How the publication builds arguments and structures prose
2. **Evidence Handling** — How claims are supported, sources cited, data presented
3. **Prose Mechanics** — Sentence-level patterns characteristic of the genre

**For each dimension, across all samples:**

1. Identify candidate patterns with specific evidence (quote or cite the passage and sample)
2. Cross-validate: does this pattern appear across multiple samples and authors?
3. Note variations: do patterns shift by article type, topic, or section within the article?
4. Distinguish the publication's patterns from LLM defaults — only capture divergences

**Priority:** Focus analytical effort on where the publication's prose diverges most from how an LLM would naturally write the same content. Patterns that match LLM defaults add nothing to the standards module.

**Present analysis to user** as a structured summary organized by dimension. For each dimension, show:
- The pattern identified
- Evidence from samples (with citations)
- Confidence level (strong/moderate/provisional)
- Whether this is a publication standard (appears across authors) or a possible individual voice pattern

**GATE:** Before proceeding, write:
- "Analysis complete across [N] dimensions"
- "Publication-level patterns (cross-author): [list key findings]"
- "Provisional patterns (limited evidence): [list or 'none']"
- "Possible voice patterns (single-author): [list or 'none' — flag for exclusion]"
- "Patterns matching LLM defaults (excluded): [list or 'none']"

**STOP.** Present the analysis to the user and get approval before drafting the module. The user may:
- Confirm patterns
- Correct misidentifications
- Provide additional samples to strengthen provisional patterns
- Flag patterns to include or exclude
- Note aspects of the publication's craft the analysis missed
</phase_analyze>

<phase_draft>
### Phase 3: Draft Writing Standards Module

**Read** [references/MODULE-TEMPLATE.md](references/MODULE-TEMPLATE.md) before drafting.

Transform confirmed patterns into process gates:

| Analysis Finding | Wrong (checklist) | Right (process gate) |
|---|---|---|
| Sections connected by implicit questions, not bridge phrases | "Use smooth transitions between sections" | "Before closing any section, identify what the reader now needs to understand that this section hasn't provided. Close by creating that need — through an unanswered tension, a consequence not yet explored, or a new frame on what was just established. The next section opens where this need lives." |
| Evidence woven into narrative | "Integrate evidence naturally" | "Before introducing any research finding, establish the narrative moment or reader experience it speaks to. The finding enters through a door the narrative has opened — never through its own door. If the finding doesn't connect to what the reader just experienced in the article, it belongs in a hyperlink, not in prose." |
| Consistent use of short declarative sentences after dense evidence passages | "Vary sentence length for readability" | "After any passage presenting data or research findings, resolve to a short declarative sentence — one that names what the evidence means for the reader. The short sentence is the landing. If it doesn't change how the reader sees what came before, it's a summary, not a resolution." |

**For each gate in the module:**

1. State the generative instruction (what the LLM should do *before* or *while* writing)
2. Ground it in evidence from the analysis
3. Test: if an LLM followed only this instruction, would it move toward this publication's craft standards?

**Write the module** following the template structure:
- 3 process gates (synthesized from the three analytical dimensions)
- Writing Discipline section (consequences of the gates, stated explicitly)
- Revision Backstop (banned language, flagged language, structural flags)
- Scope statement

**Gate synthesis:** Each analytical dimension does not need to produce exactly one gate. The three dimensions are analytical entry points — synthesize their findings into the 3 most important process gates for this publication's craft. A gate may draw from multiple dimensions if that's where the pattern lives.

**Revision backstop construction:** Identify words and phrases that:
- No writer in this genre uses (banned) — LLM defaults that would immediately mark the prose as AI-generated in this publication's context
- Writers in this genre use occasionally but LLMs overuse (flagged) — the symptom of a slipped gate
- Structural patterns that signal genre drift (structural flags) — always evaluate preview/thesis section openings and voice stance drift under subject shift. Include as flags only if the analysis confirms the publication follows the non-default convention. See the MODULE-TEMPLATE for details.

**GATE:** Before proceeding, confirm:
- "Module drafted with [N] process gates"
- "All gates are process instructions, not trait descriptions or checklists: [yes/no]"
- "Augmentation boundary statement included: [yes/no]"
- "Revision backstop includes banned, flagged, and structural flags: [yes/no]"
</phase_draft>

<phase_review>
### Phase 4: Review and Refine

Present the draft module to the user. Ask them to evaluate:

1. **Recognition test:** "Does this capture what makes this publication's prose work — the craft rules a skilled editor at this publication would enforce?"
2. **Missing standards:** "Are there craft-level rules this publication follows that the module doesn't capture?"
3. **Overclaiming:** "Does anything here feel like a stretch — a pattern attributed to the publication that's really just good writing in general?"
4. **Compatibility test:** "If this module were loaded alongside a voice profile for a specific author, would the standards complement the voice or conflict with it?"

**If the user provides additional samples or feedback:**

1. Re-analyze against the framework with the new information
2. Update the module — strengthen confirmed patterns, remove overclaims, add missing elements
3. Present the revised version

**This phase is iterative.** Repeat until the user is satisfied.

**GATE:** Before proceeding, write:
- "User has reviewed and approved the module: [yes / needs revision]"
- "Revisions made: [list or 'none']"
</phase_review>

<phase_deliver>
### Phase 5: Finalize and Deliver

1. **Remove all analytical scaffolding** — the final module should contain only the gates, writing discipline, revision backstop, and scope. No analysis notes, no evidence citations, no confidence levels.

2. **Save the module** to the user's specified output location as `writing-standards-[name].md`

3. **Confirm delivery** with a brief summary of what was captured and how to use the file:
   - Load it alongside a voice profile at the point of generation (not at session bootstrap)
   - It shapes publication-level craft rules — the voice profile shapes whose voice
   - Compatible with the drafting-articles skill: specify the path in a project manifest, or reference a baseline
   - Revisit and refine as additional samples become available or as the publication's standards evolve
</phase_deliver>

---

## Output Requirements

**ALWAYS save the writing standards module to a file. Do not output the final module inline in chat.**

1. Generate filename: `writing-standards-[name].md` (lowercase, hyphens for spaces)
2. Write the complete module to this file
3. After saving, confirm: "Writing standards saved to `[filename]`" with a brief summary of what was captured

---

<failed_attempts>
## What DOESN'T Work

- **Feature checklists:** "Uses short paragraphs, evidence-based claims, and narrative openings" gives an LLM a list to execute rather than a craft to inhabit. The result reads like compliance, not like the publication.

- **Capturing everything the publication does well.** Every good publication uses clear sentences and supports its claims. Capturing that produces generic "good writing" standards indistinguishable from what the LLM would produce anyway. Only capture divergences from LLM defaults.

- **Confusing voice with standards.** If the analysis keeps identifying how one author thinks, structures arguments, or uses humor — that's a voice profile, not a writing standard. The test: would a different author publishing in the same venue follow this rule? If not, it's voice.

- **Prohibition-based standards.** "Don't use passive voice" and "Avoid long paragraphs" are monitoring rules. They tell the LLM what to watch for, not how to write. Convert every prohibition to a generative step that makes the prohibited pattern unlikely.

- **Ignoring the revision backstop.** Process gates handle architecture, but LLM statistical defaults are strong. Without a backstop listing specific words and structures to flag, the LLM's training distribution pulls prose toward generic competence even when the gates are well-written.

- **Producing standards from too few samples or a single author.** Five samples from one Atlantic writer produces that writer's patterns, not Atlantic craft standards. The minimum for publication-level standards is 5 samples across multiple authors. Single-author analysis belongs in a voice profile.

- **Over-specifying structural rules.** "Every article must open with a scene, move through three evidence sections, and close with a question" is a template, not a standard. Standards describe craft principles (how evidence enters prose, how openings earn attention) — not structural formulas that make every article identical.
</failed_attempts>

---

## Examples

**Example: Transforming analysis into a process gate**

Analysis finding from samples: "The publication consistently presents research findings by describing what was found before naming who found it. Author names and institutional affiliations appear in hyperlinks, not in the prose. The reader encounters the finding as a fact about the world, not as a report about a study."

Wrong (checklist): "Cite by finding, not by author name."

Right (process gate): "When presenting a research finding, lead with the finding itself — what was discovered, measured, or demonstrated. The finding is a fact the reader encounters in the flow of the article's argument. Link to the source inline. Do not name the researchers or their institution in the prose unless the researcher's identity is itself part of the story. The reader cares about what was found, not who found it."

**Example: Building a revision backstop entry**

Analysis finding: "Across all samples, no article uses 'it is important to note that,' 'significantly,' or 'it should be noted that.' Evidence is presented without framing its importance — the placement within the argument signals importance structurally."

Backstop entry: "Structural flag: any sentence that frames the importance of what follows ('it is important to note,' 'significantly,' 'notably,' 'crucially') signals that the evidence hasn't been placed where its importance is structural. If you need to tell the reader something is important, it isn't in the right position. Move it."

---

## Reference Files

- [references/ANALYSIS-FRAMEWORK.md](references/ANALYSIS-FRAMEWORK.md) — Three analytical dimensions for writing standards extraction
- [references/MODULE-TEMPLATE.md](references/MODULE-TEMPLATE.md) — Output structure and gate format
