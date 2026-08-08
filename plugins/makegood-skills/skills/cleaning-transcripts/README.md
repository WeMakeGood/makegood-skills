# cleaning-transcripts

A Claude Code skill that cleans raw dictation and meeting transcripts into readable paragraph form — while keeping the speaker's own words.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Cleans raw dictation and meeting transcripts into readable paragraph form while preserving the speaker's original wording, order, and meaning. It fixes transcription errors, removes fillers (um, ah, "you know"), and merges fragmented speaker blocks into paragraphs. Uncertain corrections — mishearing of proper nouns, ambiguous words, anything that changes meaning — are flagged for your review rather than guessed at silently.

For multi-speaker transcripts, speaker labels and turn boundaries are preserved exactly as transcribed — text is never merged across a speaker change, and an apparently misattributed turn is flagged for you rather than reassigned.

It does **not** summarize, restructure, or extract from the transcript. The output is the speaker's own words, corrected — not a new document derived from them. For summaries, minutes, or action items, use `generating-meeting-reports`; for research synthesis, use `synthesizing-interviews`.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "clean up this transcript"
- "fix the transcription errors in this"
- "remove the ums and ahs and format this into paragraphs"
- "tidy up this dictation"

## What you'll need

- A transcript — pasted inline, or as an attached/uploaded file (any plain-text format).

## What you'll get

- A cleaned version of the transcript (inline by default; as a file if you say "as a file" or attach one; as an artifact if you say "as an artifact").
- A short list, in the chat response, of any uncertain corrections to confirm — with the original text, the correction, and how confident the guess is.

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `cleaning-transcripts-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/cleaning-transcripts/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip cleaning-transcripts-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/cleaning-transcripts.git ~/.claude/skills/cleaning-transcripts
```

## What's in this repo

- `SKILL.md` — the skill itself, loaded by Claude Code when activated
- `examples/` — representative example output

## Version history

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT — see [LICENSE](LICENSE).

## About Make Good

[Make Good](https://wemakegood.org) is a consultancy that partners with mission-driven organizations through new terrain — scaling, technology adoption, leadership transitions, strategic evolution. We publish our skills openly because the methodology is meant to be portable.

For other skills in this collection, see the [Make Good skills index](https://github.com/WeMakeGood/makegood-skills).
