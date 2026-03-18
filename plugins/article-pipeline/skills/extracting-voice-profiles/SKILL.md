---
name: extracting-voice-profiles
description: Extracts voice and style profiles from writing samples for LLM role adoption. Analyzes emails, transcripts, LLM conversations, and writing samples to produce process-gate voice documents that enable an LLM to write in a specific person's voice. Use when user says extract voice, create voice profile, build writing style guide, capture someone's voice, analyze writing style, or generate voice document. Activates when writing samples are present via pasted text, attached file, or uploaded document, even when accompanied by additional context files.
---

# Extracting Voice Profiles

<purpose>
LLMs default to describing voice ("tone is warm and direct") rather than establishing
generative conditions that produce it. Descriptive voice guides are failure-mode lists —
they name what the voice should be and monitor for compliance. This skill exists because
voice profiles must be structured as process gates that make off-voice writing architecturally
difficult, not as trait descriptions to check against.
</purpose>

## Critical Rules

**SOURCING:** Every pattern claimed in the voice profile must trace to specific evidence in the writing samples. Before stating any voice pattern, locate the passages that demonstrate it. If a pattern appears in only one sample, mark it as provisional. If it cannot be sourced to any sample, do not include it.

**EPISTEMIC CALIBRATION:** The user should always be able to tell whether a voice pattern is directly observed in samples, inferred from structural evidence, or your analytical interpretation — because your language makes the distinction clear.

**PROCESS GATES, NOT FAILURE MODES:** The voice profile must contain upstream process instructions that produce on-voice writing naturally. Never write "don't do X" or "avoid Y." Instead, establish a generative step that makes X architecturally unlikely. If you catch yourself writing a prohibition, convert it to a process gate.

**PROFESSIONAL CHALLENGE:** If writing samples are insufficient to establish a pattern reliably, say so. If the user's stated perception of their voice contradicts what the samples show, surface the discrepancy. Accuracy over agreement.

**PREMATURE COMMITMENT CHECK:** Before finalizing any dimension's analysis, check whether the pattern you identified is the best framing or the first one you noticed. A pattern that looks like "terse writing" might alternatively be "context-dependent compression" — a different framing that produces a different gate. If your analysis would change significantly under an alternative framing, note both and let the evidence determine which holds.

**AUGMENTATION BOUNDARY:** The voice profile augments but does not replace model alignment or guardrails documents. It shapes *how* the LLM expresses things, not *what* it's permitted to express. Never include instructions that would override epistemic calibration, sourcing discipline, or other behavioral standards.

---

## Workflow

```
Voice Profile Extraction:
- [ ] Phase 1: Gather samples and context
- [ ] Phase 2: Analyze samples against framework
- [ ] Phase 3: Draft voice profile
- [ ] Phase 4: Review and refine with user
- [ ] Phase 5: Finalize and deliver
```

<phase_gather>
### Phase 1: Gather Samples and Context

**Ask the user for:**

1. **Writing samples** — At least 3 samples, ideally 5+. More variety produces better profiles. Accept any combination of:
   - Emails or written correspondence
   - Voice or meeting transcripts
   - LLM conversation logs
   - Long-form writing (articles, essays, reports, blog posts)
   - Social media posts or comments

2. **Context for each sample:**
   - Who was the audience?
   - What was the purpose?
   - Is this representative of their typical writing, or an edge case?

3. **Output location** — Where to save the voice profile file.

4. **Name** — Whose voice is being captured (for the profile filename and header).

**Sample quality assessment:**

After receiving samples, evaluate before proceeding:
- **Minimum:** 3 samples across at least 2 contexts (e.g., email + long-form, or transcript + LLM conversation)
- **Ideal:** 5+ samples across 3+ contexts
- **Insufficient:** Fewer than 3 samples, or all from the same context

If samples are insufficient, tell the user what additional material would improve the profile and why. Proceed if they choose to, but note the limitation.

**Transcript handling:** Voice transcripts capture speaking patterns, not writing patterns. They're valuable for cognitive architecture and interpersonal orientation but unreliable for sentence-level DNA. Note this distinction during analysis.

**LLM conversation handling:** These reveal how the person thinks and what they value, but the actual prose is shaped by the conversational format. Extract thinking patterns and domain orientation; treat the prose style as secondary.

**GATE:** Before proceeding, write:
- "Samples received: [count] across [count] contexts"
- "Sample types: [list]"
- "Sufficiency assessment: [sufficient/limited/insufficient — and why]"
</phase_gather>

<phase_analyze>
### Phase 2: Analyze Samples

**Read** [references/ANALYSIS-FRAMEWORK.md](references/ANALYSIS-FRAMEWORK.md) before beginning analysis.

Work through each sample against all five dimensions:

1. **Cognitive Architecture** — How they structure thinking
2. **Sentence-Level DNA** — Mechanical sentence patterns
3. **Interpersonal Orientation** — Relationship to reader
4. **Domain Relationship** — How they engage subject matter
5. **Rhetorical Signature** — Distinctive individual patterns

**For each dimension, across all samples:**

1. Identify candidate patterns with specific evidence (quote or cite the passage)
2. Cross-validate: does this pattern appear in multiple samples?
3. Note contextual variations: does the pattern shift by audience or purpose?
4. Distinguish the person's patterns from LLM defaults — only capture divergences

**Priority:** Focus analytical effort on where the person's voice diverges most from how an LLM would naturally write the same content. Patterns that match LLM defaults add nothing to the profile.

**Present analysis to user** as a structured summary organized by dimension. For each dimension, show:
- The pattern identified
- Evidence from samples (with citations)
- Confidence level (strong/moderate/provisional)
- Any contextual variations

**GATE:** Before proceeding, write:
- "Analysis complete across [N] dimensions"
- "High-confidence patterns: [list key findings]"
- "Provisional patterns (single-sample only): [list or 'none']"
- "Patterns matching LLM defaults (excluded): [list or 'none']"

**STOP.** Present the analysis to the user and get approval before drafting the profile. The user may:
- Confirm patterns
- Correct misidentifications
- Provide additional samples to strengthen provisional patterns
- Note patterns you missed
</phase_analyze>

<phase_draft>
### Phase 3: Draft Voice Profile

**Read** [references/PROFILE-TEMPLATE.md](references/PROFILE-TEMPLATE.md) before drafting.

Transform confirmed patterns into process gates:

| Analysis Finding | Wrong (trait) | Right (process gate) |
|---|---|---|
| Short sentences, direct | "Use short, direct sentences" | "Default to the shortest sentence that holds the complete idea. When you reach for a longer construction, check whether the idea genuinely requires it or whether two shorter sentences would be clearer." |
| Reasons by analogy | "Uses analogies frequently" | "When explaining a concept, find a structural parallel from a different domain before writing the explanation. Build the explanation around what the parallel reveals." |
| Peer stance with reader | "Tone is collegial" | "Write as someone working alongside the reader on the same problem. Assume they have context. State your view directly and expect them to push back if they disagree." |

**For each gate in the profile:**

1. State the generative instruction (what the LLM should do *before* or *while* writing)
2. Ground it in evidence from the analysis
3. Test: if an LLM followed only this instruction, would it move toward this person's voice?

**Write the profile** following the template structure:
- Gate 1: Generative Orientation (from Dimensions 1 + 3)
- Gate 2: Sentence Architecture (from Dimension 2)
- Gate 3: Domain Stance (from Dimension 4)
- Gate 4: Signature Texture (from Dimension 5 + cross-cutting patterns)
- Contextual Adaptations (if applicable)

**Omit gates where the person's patterns match LLM defaults.** A shorter profile with only meaningful divergences is more effective than a comprehensive one that restates what the LLM would do anyway.

**GATE:** Before proceeding, confirm:
- "Profile drafted with [N] gates"
- "All gates are process instructions, not trait descriptions: [yes/no]"
- "Augmentation boundary statement included: [yes/no]"
</phase_draft>

<phase_review>
### Phase 4: Review and Refine

Present the draft profile to the user. Ask them to evaluate:

1. **Recognition test:** "Does this sound like how you think about writing, even if you've never articulated it this way?"
2. **Missing patterns:** "Is there anything distinctive about your writing that this doesn't capture?"
3. **Overclaiming:** "Does anything here feel like a stretch — a pattern attributed to you that's really just the AI's interpretation?"

**If the user provides additional samples or feedback:**

1. Re-analyze against the framework with the new information
2. Update the profile — strengthen confirmed patterns, remove overclaims, add missing elements
3. Present the revised version

**This phase is iterative.** Repeat until the user is satisfied.

**GATE:** Before proceeding, write:
- "User has reviewed and approved the profile: [yes / needs revision]"
- "Revisions made: [list or 'none']"
</phase_review>

<phase_deliver>
### Phase 5: Finalize and Deliver

1. **Remove all analytical scaffolding** — the final profile should contain only the gates and any contextual adaptations. No analysis notes, no evidence citations, no confidence levels.

2. **Save the profile** to the user's specified output location as `voice-profile-[name].md`

3. **Confirm delivery** with a brief summary of what was captured and how to use the file:
   - Load it into an LLM's context window alongside other guardrails
   - It shapes voice, not permissions — behavioral guardrails still apply
   - Revisit and refine as the person's writing evolves or as new samples become available
</phase_deliver>

---

## Output Requirements

**ALWAYS save the voice profile to a file. Do not output the final profile inline in chat.**

1. Generate filename: `voice-profile-[name].md` (lowercase, hyphens for spaces)
2. Write the complete profile to this file
3. After saving, confirm: "Voice profile saved to `[filename]`" with a brief summary of what was captured

---

<failed_attempts>
## What DOESN'T Work

- **Trait lists:** "Tone is warm, style is concise, voice is professional" gives an LLM nothing actionable. Every LLM can produce warm-concise-professional prose — the question is *whose* warm-concise-professional prose.

- **Word frequency analysis:** Counting someone's most-used words produces a vocabulary list, not a voice. Voice lives in structure, not vocabulary. The same person uses different words for different topics but the same structural patterns.

- **Mimicking sample text directly:** Copying sentence patterns from samples produces pastiche, not voice. The profile must capture the *generative logic* behind the patterns — what produces them — not the patterns themselves.

- **Prohibitions as voice guidance:** "Don't use long sentences" and "Avoid passive voice" are failure-mode monitors. They tell the LLM what to watch for, not how to write. Convert every prohibition to a generative instruction.

- **Comprehensive profiles:** Capturing everything about someone's writing produces a document full of patterns the LLM would produce anyway. Only capture divergences from LLM defaults. A 10-line profile that nails three distinctive patterns outperforms a 200-line profile that describes everything.

- **Treating transcripts as writing samples:** Spoken language has different rhythms, fillers, and structures than written language. Transcripts reveal how someone *thinks*, not how they *write*. Extract cognitive patterns; ignore speech artifacts.
</failed_attempts>

---

## Examples

**Example: Transforming analysis into a process gate**

Analysis finding from samples: "The person consistently opens with the most controversial or unexpected claim, then works backward to justify it. They rarely provide context before the point."

Wrong (trait): "Opens with strong, unexpected claims."

Right (process gate): "Before writing any opening, identify the single claim in what follows that the reader is least likely to expect or most likely to disagree with. Start there. The reader's surprise or resistance is the hook — do not cushion it with context. Context comes after, as justification for the opening claim."

**Example: Handling a contextual adaptation**

Analysis finding: "In emails, the person is extremely terse — often single-sentence responses. In long-form writing, they use extended analogies and longer paragraphs."

Profile entry: "When writing short-form communication (emails, messages, quick responses), compress to the minimum viable response — one sentence if possible, never more than three. Drop greetings, sign-offs, and transitional language. When writing long-form content (articles, reports, essays), expand through analogy — find a structural parallel and develop it across multiple paragraphs before returning to the main argument."

---

## Reference Files

- [references/ANALYSIS-FRAMEWORK.md](references/ANALYSIS-FRAMEWORK.md) — Five analytical dimensions for voice extraction
- [references/PROFILE-TEMPLATE.md](references/PROFILE-TEMPLATE.md) — Output structure and gate format
