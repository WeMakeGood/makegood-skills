# Voice Analysis Framework

This document defines the analytical dimensions used to extract voice profiles from writing samples. Each dimension produces process gates — upstream requirements for the writing LLM — not descriptive traits.

## Why Dimensions, Not Traits

A trait-based voice guide says: "Tone is warm but direct." This names a target and hopes the LLM hits it — a monitoring-based approach.

A dimension-based voice profile says: "Before writing any sentence, generate it from the perspective of someone who treats every interaction as a peer conversation where both parties are working toward the same outcome." This establishes a generative orientation that produces warmth and directness as natural consequences.

Every dimension below should yield a process gate, not a description.

---

## Dimension 1: Cognitive Architecture

How the person structures their thinking. This shapes paragraph-level and document-level organization.

**What to extract:**

- **Entry point pattern:** Do they start from concrete examples and build to principles? From principles and illustrate with examples? From questions that frame the territory? From assertions they then defend?
- **Reasoning sequence:** Do they build arguments linearly (A→B→C), dialectically (thesis→antithesis→synthesis), by accretion (layer upon layer of evidence), or by elimination (ruling out alternatives)?
- **Abstraction comfort:** Do they stay close to specifics, or do they move freely between concrete and abstract? When they go abstract, how quickly do they return to ground?
- **Complexity handling:** Do they simplify before explaining? Hold complexity and expect the reader to follow? Break complex ideas into sequential parts? Use analogy to make complexity tangible?

**What this becomes in the profile:**

A process gate that requires the writing LLM to organize its thinking in the same structural pattern before generating prose. If the person reasons by elimination, the LLM must consider and discard alternatives in the same sequence, not just state the conclusion.

---

## Dimension 2: Sentence-Level DNA

The mechanical patterns of how the person constructs sentences. This is the most immediately recognizable aspect of voice.

**What to extract:**

- **Sentence length distribution:** Not an average, but a rhythm. Short-long-short? Consistently medium? Long sentences with embedded clauses? How do they use sentence length for emphasis?
- **Clause architecture:** Do they front-load the main point (right-branching) or build to it (left-branching)? Do they use parenthetical asides? Dashes for interjection? Semicolons for parallel structure?
- **Verb orientation:** Active vs. passive isn't sufficient. Look at verb energy: do they use state verbs ("is," "has") or action verbs ("builds," "drives")? Do they nominalize actions ("the implementation of" vs. "implementing")?
- **Punctuation as voice:** Dash users think differently than semicolon users. Em-dash interruptions signal a mind that pivots mid-thought. Semicolons signal parallel thinking. Colons signal setup-delivery. Ellipses signal trailing thought.

**What this becomes in the profile:**

Structural parameters the writing LLM adopts as defaults for sentence construction. Not rules to check against, but a generative baseline — the sentence architecture the LLM starts from before the content shapes it further.

---

## Dimension 3: Interpersonal Orientation

How the person positions themselves relative to their reader. This determines register, formality, and relational dynamics.

**What to extract:**

- **Authority stance:** Do they write as a peer, a guide, a challenger, an observer? Does this shift by topic or audience?
- **Reader model:** Do they assume the reader is an expert, a learner, a collaborator, a decision-maker? How does this show in what they explain vs. assume?
- **Directness gradient:** Do they state conclusions then support them, or build evidence then conclude? Do they qualify ("I think," "it seems") or assert?
- **Engagement mode:** Do they address the reader directly ("you"), use inclusive language ("we"), maintain third-person distance, or mix these?

**What this becomes in the profile:**

A relational frame the writing LLM adopts before generating any reader-facing content. The LLM writes from a specific stance toward the reader, which naturally produces the right register without style rules.

---

## Dimension 4: Domain Relationship

How the person relates to their subject matter. This shapes vocabulary, metaphor, and the depth at which ideas are engaged.

**What to extract:**

- **Insider/outsider position:** Do they write from inside the domain (using its native vocabulary naturally) or about it from the outside (translating for a broader audience)?
- **Vocabulary signature:** Not a word list, but vocabulary *behavior* — do they use technical terms without definition? Define them inline? Avoid them in favor of plain language? Coin their own terms?
- **Metaphor patterns:** Do they use metaphor heavily or rarely? When they do, what source domains do they draw from? (Mechanical, organic, spatial, athletic, musical, etc.) Do they extend metaphors or use them briefly?
- **Engagement depth:** Do they skim across many ideas or go deep into fewer? When they go deep, what does that look like — more examples? More qualifications? More connections to other ideas?

**What this becomes in the profile:**

An orientation to subject matter that shapes how the writing LLM engages with any topic. If the person is a practitioner who uses domain language naturally without explanation, the LLM writes from that same position rather than defaulting to its own explanatory tendencies.

---

## Dimension 5: Rhetorical Signature

The distinctive moves the person makes that are uniquely theirs — not captured by the structural dimensions above.

**What to extract:**

- **Characteristic transitions:** How do they move between ideas? Explicit connectives ("however," "moreover")? Juxtaposition without connective? Questions as transitions? White space?
- **Emphasis patterns:** How do they signal importance? Repetition? Short sentences after long ones? Direct address? Sentence fragments?
- **Humor and texture:** If present, what kind? Dry understatement? Self-deprecation? Absurdist asides? Wry observation? Sarcasm?
- **Distinctive moves:** Any patterns that don't fit the categories above — things that make their writing recognizably theirs. These are often the most valuable elements to capture because they're the hardest for an LLM to produce without explicit guidance.

**What this becomes in the profile:**

Specific generative instructions that produce the person's distinctive texture. These are the elements most likely to be lost if not explicitly captured, because the LLM's training distribution will smooth them out.

---

## Analysis Process

For each sample, work through the dimensions in order. The first three dimensions (Cognitive Architecture, Sentence-Level DNA, Interpersonal Orientation) are usually stable across samples. Dimensions 4 and 5 may vary by context — note when they do.

**Cross-sample validation:** A pattern that appears in one sample is a hypothesis. A pattern that appears across multiple samples and contexts is a finding. A pattern that appears in one context but not another is a contextual adaptation — note the conditions under which it appears.

**What to prioritize:** The highest-value patterns are those where the person's natural voice diverges most from LLM defaults. An LLM already writes in complete sentences with reasonable grammar — capturing that adds nothing. Patterns where the person's writing would feel wrong if the LLM wrote it its own way are the ones that matter.

**Conflict resolution:** When samples show contradictory patterns, this usually indicates contextual adaptation, not inconsistency. Note both patterns and the contexts that produce each. The voice profile should capture the adaptation, not force consistency.
