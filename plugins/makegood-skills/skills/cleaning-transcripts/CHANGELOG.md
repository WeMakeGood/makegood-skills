# Changelog

All notable changes to this skill are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this skill follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
