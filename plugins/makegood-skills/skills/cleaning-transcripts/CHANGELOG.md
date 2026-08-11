# Changelog

All notable changes to this skill are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this skill follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] — 2026-08-10

### Added
- Mode determination in Phase 1: every transcript is classified single-speaker or multi-speaker before editing — by explicit user statement first, inference second, and a question only when genuinely ambiguous. The gate line now records the mode and the evidence for it.
- Single-speaker cleaning rules. Dictation recorders segment on pauses rather than turns, so a solo recording arrives labeled like a conversation with breaks falling mid-sentence and sometimes mid-word. In single-speaker mode those breaks carry no information: severed sentences are rejoined as a mechanical edit, and a stray second label whose content continues the previous sentence is treated as a diarization artifact rather than a turn.
- Two anti-patterns: treating a solo dictation's block breaks as turns, and smoothing a rejoined sentence instead of flagging a gap where two halves do not meet.
- A `single-speaker` / `multi-speaker` hint is honored when the user supplies one, and is named in the description so it can be passed.

### Changed
- The v1.1.0 speaker-attribution rules are now scoped to multi-speaker mode. They still govern every real multi-speaker transcript unchanged — the protection against attributing one person's words to another was correct and is untouched. Applied to solo dictation, however, they left sentences severed at arbitrary recorder breaks and handed the user a transcript to repair by hand. The rules exist to protect real turns, not recorder artifacts.
- Phase 3 verification is mode-specific: attribution intact for multi-speaker, sentences whole for single-speaker.

### Why
Found while testing a voice-authoring pipeline against real dictation. Two independent samples showed the failure: a solo recording split a sentence across a block break so the thought never completed, and another mislabeled one solo block as a second speaker. In both cases the cleaner preserved the artifact, because the no-merge rule read it as a turn boundary.

## [1.1.0] — 2026-08-08

### Added
- Speaker attribution rules for multi-speaker transcripts. Merging is now confined to a single speaker's turn, speaker labels and turn boundaries (including short interjections) are preserved as transcribed, and apparent misattribution is treated as an uncertain repair to be flagged rather than silently reassigned. The skill's description claimed meeting transcripts, but every rule and example had been written against single-speaker dictation — merging across a speaker change would have put one person's words in another's mouth with nothing in the output to reveal it.
- Verification check and anti-pattern entry covering the same failure.
- A defined path for requests that conflict with the skill's premise (tighten, condense, cut repetition): name what falls outside a cleanup, deliver the preserved version, and offer the condensing as a separate pass — leaving the tradeoff visible and the decision with the user.

### Changed
- Phase gates are now written unconditionally rather than only on file and artifact delivery. Previously the default inline path let all three gates degrade to silent self-attestation; the commitment lines are now written in thinking on every path, which keeps the chat response uncluttered without giving up the commitment.

## [1.0.0] — 2026-08-08

### Added
- Initial release. Cleans raw dictation and meeting transcripts into readable paragraph form while preserving the speaker's wording, order, and meaning. Removes fillers, merges fragmented speaker blocks, and repairs transcription errors — classifying each edit as mechanical, a confident lexical repair, or an uncertain repair. Uncertain repairs (proper nouns, ambiguous words, meaning-affecting corrections) are made as best guesses and flagged in the chat response for user review, never silently. Supports inline, file, and artifact delivery.

---

[1.1.0]: https://github.com/WeMakeGood/cleaning-transcripts/releases/tag/v1.1.0
[1.0.0]: https://github.com/WeMakeGood/cleaning-transcripts/releases/tag/v1.0.0
