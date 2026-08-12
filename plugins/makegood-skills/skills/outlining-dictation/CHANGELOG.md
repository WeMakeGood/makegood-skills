# Changelog

All notable changes to this skill are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this skill follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-08-10

### Added

Initial release. Decomposes a cleaned dictation transcript into a nested outline of the speaker's own words, with a companion log carrying every machine observation by node number.

Every rule in this skill was derived from a failure observed in testing against real dictation — five runs across four samples, including one recorded during a chronic-illness flare. The rules and their origins:

- **Comprehend before decomposing.** A run that decomposed first produced a structurally sound outline the author judged impossible to recompose: the four load-bearing claims were all structurally subordinate to less important material. Re-running the same sample comprehension-first promoted all four to top level and produced 175 nodes against 199 — fewer nodes, more top-level moves.
- **Comprehension shapes depth, never sequence or wording.** Both violations are mechanically detectable, so the boundary is checkable rather than promised.
- **Never fuse.** A spoken list of five services returned as two items removes three nodes the author could have culled or reordered, before they see the outline.
- **Split at the thought boundary.** A subject governing two predicates must become their parent. Split as siblings, each node holds one beat — a naive check passes — and the claims still cannot move against each other.
- **Never rank or select takes.** One sample delivered the same four-move arc twice, the second pass compressed with a different ending. A summarizing pass keeps one.
- **Takes stay unmarked.** A `[take]` label was tested and rejected: it is an assertion sitting among the author's words, and it has to be stripped by hand later — a keystroke added to the artifact whose purpose is removing them.
- **The legibility test.** Replaces asking whether something is voice or disfluency, which is unanswerable in the moment and produces hedging. Ask instead whether the edit makes an illegible node legible.
- **Report every drop.** Culling restatement is correct; doing it silently is not. Only the author knows whether an abandoned thought was going somewhere.
- **The argument trace, as node references only.** An outline whose argument is invisible cannot be recomposed. But a machine-written thesis anchors the author on its framing — so the trace points at nodes and never paraphrases them.
- **Report scene groupings, never apply them.** Tested against a sample chosen to justify grouping, and rejected: across five runs spoken order was never arbitrary, and relocating a node moves it out of the argument that earned it.
- **Dates are not repairable from context.** A correct date was removed because surrounding references seemed not to corroborate it; file metadata resolved it. Dates carry no internal redundancy.
- **Check whether a gap is distributed before requesting a pickup.** An argument spread across three nodes was reported as missing.
