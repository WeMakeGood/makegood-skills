# Extracting Voice Profiles

Analyzes writing samples to produce LLM-consumable voice profiles that enable an AI to write in a specific person's voice.

## When to Use

Use this skill when you need to:
- Capture someone's writing voice for AI-assisted content creation
- Create a voice profile from emails, transcripts, or writing samples
- Enable an LLM to write in a way that matches a specific person's style and thinking patterns

## How to Invoke

Say things like:
- "Extract a voice profile from these writing samples"
- "Create a voice guide from my emails and articles"
- "Capture my writing voice for AI use"
- "Analyze my writing style and build a voice profile"

## What You'll Need

- At least 3 writing samples (5+ recommended) across 2+ contexts, such as:
  - Emails or written correspondence
  - Voice or meeting transcripts
  - LLM conversation logs
  - Articles, essays, or reports
- Context about each sample (audience, purpose, representativeness)

## What You'll Get

A single markdown file (`voice-profile-[name].md`) structured as process gates — upstream instructions that produce on-voice writing naturally. The file is designed to be loaded into an LLM's context window alongside behavioral guardrails.

The profile typically contains four core gates, with additional gates when the analysis warrants them:
1. **Generative Orientation** — How to think before writing
2. **Sentence Architecture** — Structural defaults for sentence construction
3. **Domain Stance** — How to engage with subject matter
4. **Signature Texture** — Distinctive patterns unique to this person

## How It Works

The skill uses an iterative workflow:
1. Gather and assess writing samples
2. Analyze samples across five dimensions (cognitive architecture, sentence DNA, interpersonal orientation, domain relationship, rhetorical signature)
3. Draft a voice profile transforming patterns into process gates
4. Review with you and refine based on feedback
5. Deliver the final profile

## Key Design Principle

The profile uses **process gates, not trait descriptions**. Instead of "tone is warm and direct" (which describes a target and hopes the LLM hits it), it establishes generative conditions like "write as someone working alongside the reader on the same problem" (which produces warmth and directness as natural consequences).

## Tips

- More variety in samples produces better profiles — an email and an article reveal more than five emails
- The skill only captures patterns that diverge from LLM defaults — patterns the LLM would produce anyway are omitted
- Transcripts reveal thinking patterns, not writing patterns — both are valuable but serve different dimensions
- The profile augments guardrails documents, it doesn't replace them
