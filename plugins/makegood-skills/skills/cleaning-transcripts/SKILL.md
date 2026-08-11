---
name: cleaning-transcripts
description: Cleans raw dictation and meeting transcripts into readable paragraph form while preserving the speaker's original wording, order, and meaning. Fixes transcription errors, removes fillers (um, ah, you know), and merges fragmented speaker blocks — rejoining sentences the recorder severed mid-thought in solo dictation, while protecting speaker turns in multi-speaker recordings. Flags uncertain corrections for review rather than guessing silently. Use when user says clean up this transcript, fix transcription errors, remove ums and ahs, tidy up this dictation, clean up my voice notes, or format this transcript into paragraphs. Accepts a single-speaker or multi-speaker hint when the user gives one. Activates when transcript content is present via pasted text, inline content, attached file, or uploaded document, even when accompanied by additional context files. NOT for extracting summaries, meeting minutes, action items, or restructuring into a new format — this skill preserves the original text.
---

# Cleaning Transcripts

<purpose>
Claude's default when handed a transcript is to summarize, restructure, or "improve" it —
compressing rambling passages, dropping specifics it judges unimportant, and rewriting the
speaker's phrasing into cleaner prose. That destroys the thing a cleanup is supposed to
preserve: the speaker's own words, in their own order. This skill exists to hold Claude to
repair rather than rewrite. It fixes what the transcription got wrong and strips disfluencies,
but treats the speaker's wording, sequence, and meaning as fixed points that may not be
altered.
</purpose>

Produces a clean, readable version of a raw transcript that the speaker would recognize as their own words — just correctly transcribed and free of filler.

## Critical Rules

**PRESERVE, DON'T REWRITE:** The speaker's wording, the order of their points, and their meaning are fixed. You may fix transcription errors, remove disfluencies, and merge fragments into paragraphs. You may NOT paraphrase, condense, reorder, summarize, or "improve" phrasing. If you find yourself writing a sentence the speaker did not say, stop — that is rewriting, not cleaning.

**SOURCING (every correction traces to the transcript):** Every change must be justified by the transcript itself — a filler to remove, a garbled word whose intended form is recoverable from context, or a fragmented block to join. Before changing a word, locate what in the surrounding text tells you the intended word. If nothing does, do not invent one.

**CLASSIFY BEFORE CHANGING:** Every edit is one of three kinds, and they are handled differently (see Phase 2). Mechanical edits (fillers, block merges) are made silently. Confident lexical repairs (clearly garbled words with an unambiguous intended form) are made and noted if non-obvious. Uncertain repairs (proper nouns, unclear words, anything that changes meaning) are made as a best guess AND flagged for the user's review. Never let an uncertain repair pass silently.

**EPISTEMIC CALIBRATION:** When you flag an uncertain correction, your language must show how confident you are and what the guess rests on — "almost certainly X, from context" reads differently from "possibly X; the transcription is garbled here." Do not present a guess as if it were certain.

**WHEN THE INTENT IS UNRECOVERABLE:** If a passage is too garbled to repair confidently and context doesn't resolve it, do not smooth it into plausible prose. Preserve it as closely as the transcription allows and flag it as unclear. A fabricated-but-fluent sentence is worse than a rough-but-honest one.

## Quick Start

Given a raw transcript:

1. Read the entire transcript before changing anything, and determine whether it is single-speaker or multi-speaker (Phase 1).
2. Clean it: remove fillers, join fragmented blocks into paragraphs, repair transcription errors — classifying each repair as you go (Phase 2). In single-speaker mode, also rejoin sentences the recorder severed at block breaks.
3. Deliver the cleaned transcript (see Output Rules).
4. Report uncertain corrections in your response for the user to confirm.

## Output Rules

The user controls how the cleaned transcript is delivered by including a keyword in their request:

- **"as a file"** (or the source was an attached/uploaded file) → Write to a file named after the source (e.g., `<original-name>_cleaned.md`). After saving, confirm the filename in one line.
- **"as an artifact"** → Create an artifact containing the cleaned transcript.
- **No keyword (default)** → Return the cleaned transcript inline in your response.

**REQUIRED regardless of delivery method:** The uncertain-corrections summary (Phase 4) goes in your chat response, never inside the cleaned file. The file stays clean; the flags travel in the conversation. This is deliberate — the deliverable should be usable as-is, and the flags are for the user's review, not for the reader of the transcript.

## Workflow

```
Progress:
- [ ] Phase 1: Read the whole transcript
- [ ] Phase 2: Clean and classify edits
- [ ] Phase 3: Verify against the original
- [ ] Phase 4: Deliver + report uncertain corrections
```

<phase_read>
### Phase 1: Read the Whole Transcript

**REQUIRED:** Read the entire transcript start to finish before making a single edit. Garbled words are often resolved by context that appears later — a tool named clearly in paragraph ten tells you what the mangled version in paragraph two was. You cannot repair reliably from a partial read.

While reading, note:
- Recurring proper nouns, tool names, product names, and organization names — these are the most common transcription casualties and the most important to get right.
- The speaker's structure: where each point begins and ends, so paragraph breaks follow the speaker's thought, not an arbitrary rhythm.
- Who is speaking, and where the turns change — so merges stay inside a single speaker's turn.
- Passages that are garbled beyond confident repair, so you can flag rather than fabricate.

**Determine the mode before editing: single-speaker or multi-speaker.** This decides whether block breaks carry information, and it changes what you are allowed to merge.

The two modes exist because dictation recorders segment on pauses, not on turns. A solo recording arrives labeled as though it were a conversation, and its labels mark where the speaker drew breath — frequently mid-sentence, sometimes mid-word.

1. **If the user said which it is, or passed `single-speaker`, use that.** An explicit statement always wins over your reading of the file.
2. **Otherwise infer it.** Single-speaker indicators: one label across the whole transcript; or one dominant label with a small number of orphan blocks that continue the previous sentence rather than responding to it. Multi-speaker indicators: turns that answer each other, interjections, questions followed by replies, distinct vocabularies or subject matter by label.
3. **If it is genuinely ambiguous, ask before editing.** Ambiguity means real back-and-forth under two or more labels, or a solo dictation where another voice appears to speak briefly. Do not guess — a wrong call in either direction damages the transcript. Asking is the rare path; detection resolves most transcripts.

**A stray second label is not proof of a second speaker.** One or two blocks under a different label, carrying content that continues the dominant speaker's sentence, is a diarization artifact. Weigh what the content does, not what the label asserts.

**GATE:** Before proceeding, write this line in your thinking — not in your response to the user: "I have read the full transcript, determined this is a [single-speaker / multi-speaker] recording on the basis of [evidence], and noted the recurring proper nouns and any unrecoverable passages." Do not begin editing until you have written it.
</phase_read>

<phase_clean>
### Phase 2: Clean and Classify Edits

Work through the transcript making three kinds of edits. **Classify each edit before you make it** — the class determines whether it needs flagging.

**Mechanical edits — make silently:**
- Remove fillers and disfluencies: um, uh, ah, er, "you know," "sort of," "kind of," "I mean," false starts, and stutter-repetitions ("the the," "we we"). Remove them where they are noise; keep a word like "sort of" if the speaker used it to genuinely hedge a claim.
- Merge fragmented speaker blocks into coherent paragraphs. Raw dictation is often split into many small blocks mid-sentence; join them so sentences are whole and paragraphs follow the speaker's thoughts.
- Fix obvious punctuation, capitalization, and sentence boundaries created by the transcription.

**Confident lexical repairs — make, and note if non-obvious:**
- Repair clearly garbled words where context makes the intended word unambiguous. Transcription engines mishear technical terms, tool names, and homophones.
- If the repair is obvious (a clear mis-hearing anyone would resolve the same way), just make it. If it's confident but not obvious — a reader might not spot that the original was wrong — note it in Phase 4 so the user can confirm.

**Uncertain repairs — make a best guess AND flag every one:**
- Proper nouns you cannot verify (people, organizations, products, places), where you're inferring the intended name.
- Words where more than one plausible intended form exists.
- Anything where the repair changes the meaning of the sentence — for example, a mis-transcribed word that, corrected one way vs. another, says something different about what the speaker meant.
- For these: insert your best-guess correction into the cleaned text so it reads naturally, and record each one for the Phase 4 report with your confidence and what the guess rests on.

**Single-speaker mode — block breaks carry no information:**
- Rejoin sentences across block breaks. The recorder segments on pauses, so a break can fall anywhere, including mid-sentence and mid-word. A sentence severed at a break is a transcription artifact, and repairing it is a mechanical edit.
- Treat labels as artifacts rather than turns. A stray second label whose content continues the previous sentence gets absorbed; note it in Phase 4 if the absorption was non-obvious.
- Everything else still holds: the speaker's wording, order, and meaning remain fixed. Rejoining a severed sentence restores what they said. It never licenses merging two separate thoughts into one, and it never licenses smoothing the join — if the two halves do not meet cleanly, that is a gap to flag, not a seam to write across.

**Speaker attribution — multi-speaker mode only:**
- Merge blocks only within a single speaker's turn. Never join text across a speaker change: attributing one person's words to another is the most serious form of rewriting this skill can commit, and unlike a garbled word it leaves no trace for the reader to catch.
- Preserve every speaker label and turn boundary as the transcription gives them, including short interjections ("Right." "Mm-hm.") — a turn that looks like noise is still evidence of who was in the room and when they spoke.
- If a turn appears misattributed — the content clearly belongs to the previous speaker, or one person's sentence is split across two labels — treat it as an uncertain repair. Leave the labels as transcribed and flag it in Phase 4. Do not reassign the turn yourself; you are inferring from content what the diarization asserts directly.

**Do not:**
- Do not merge, drop, reorder, or reassign speaker turns in multi-speaker mode.
- Do not delete content because it seems repetitive or tangential. Repetition the speaker chose stays.
- Do not reorder points to "flow better."
- Do not add transitions, framing, or connective sentences the speaker didn't say.
- Do not upgrade vocabulary or tighten phrasing for style.

**GATE:** Before proceeding, write this line in your thinking — not in your response to the user: "Every uncertain repair I made is recorded for the Phase 4 report, and — in multi-speaker mode — no text was merged across a speaker change." Do not proceed until you have written it.
</phase_clean>

<phase_verify>
### Phase 3: Verify Against the Original

**REQUIRED:** Compare the cleaned version against the original, section by section, before delivering. This catches the failure mode this skill exists to prevent — silent rewriting.

Check:
- **Order preserved:** Every point appears in the same sequence as the original.
- **Nothing dropped:** No substantive content was removed under the guise of filler removal. (Filler words gone — yes. Whole thoughts gone — no.)
- **Nothing added:** No sentence exists in the clean version that the speaker did not say in some form.
- **Attribution intact (multi-speaker):** Every speaker turn belongs to the speaker the transcription assigned it to, and no paragraph spans a speaker change.
- **Sentences whole (single-speaker):** No sentence is still severed at a block break, and no two separate thoughts were joined into one while repairing them.
- **Meaning intact:** Each repaired sentence still means what the original meant (or, for meaning-affecting uncertain repairs, is flagged).
- **All uncertain repairs captured:** Every guess is in your Phase 4 list.

**GATE:** Before delivering, write this line in your thinking — not in your response to the user: "Verified: order preserved, nothing substantive dropped or added, all uncertain repairs flagged, and the mode-specific check (attribution intact, or sentences whole) passes." Do not deliver until you have written it.
</phase_verify>

<phase_deliver>
### Phase 4: Deliver and Report Uncertain Corrections

Deliver the cleaned transcript per the Output Rules.

Then, in your chat response (not in the file), report the uncertain corrections so the user can confirm them. For each, give: the original garbled text, your correction, and a short note on what the guess rests on and how confident you are. Group obvious mechanical cleanup into a single line — the user does not need every removed "um" itemized. Reserve the detail for the repairs they actually need to check.

If a passage was too garbled to repair, name it here as unclear rather than presenting your smoothing as fact.

If there were no uncertain repairs, say so briefly rather than padding the response.
</phase_deliver>

## Distinction From Adjacent Skills

This skill **preserves and repairs** the original text. If the user wants the transcript *turned into something else* — a summary, meeting minutes with action items, an interview synthesis, a report — that is a different skill (e.g., generating-meeting-reports, synthesizing-interviews). Cleaning produces the speaker's own words, corrected; those skills produce a new document derived from the transcript. If a request is ambiguous between the two ("can you clean this up and pull out the key points?"), do the cleanup this skill covers and ask before restructuring.

If the user asks for something the Critical Rules forbid — tightening the rambling parts, cutting repetition, making it flow better — do not silently comply and do not simply refuse. Name which part of the request falls outside a cleanup, deliver the cleaned transcript, and offer the condensing as a separate pass on top of it. That way the preserved version still exists, and the user can compare it against whatever they asked for. If they confirm they want the tightened version instead, that is their call to make with the tradeoff visible.

<failed_attempts>
What DOESN'T work:

- **"This rambles; I'll tighten it":** Tightening is rewriting. A cleanup keeps the speaker's phrasing even when it's loose. Remove fillers, not the speaker's style.
- **Smoothing a garbled passage into fluent prose:** A confident-sounding sentence you invented to cover a transcription gap is a fabrication. Preserve and flag instead.
- **Fixing proper nouns silently:** A wrong-but-plausible organization or tool name that slips through unflagged is worse than an obvious garble, because no one catches it. Every unverifiable proper-noun repair gets flagged.
- **Dropping "unimportant" specifics:** The specifics are usually the point. Named tools, numbers, and examples stay exactly as the speaker gave them (corrected for transcription, not removed).
- **Reordering for flow:** The speaker's order is data. Keep it.
- **Tidying up speaker turns:** Merging a short "Right." into the previous speaker's paragraph, or joining a sentence that spans a turn change, reads as harmless formatting. It puts words in someone's mouth, and the cleaned version gives no sign it happened.
- **Treating a solo dictation's block breaks as turns:** Recorders segment on pauses, so a solo recording arrives labeled like a conversation with breaks falling mid-sentence. Applying the multi-speaker no-merge rule there leaves sentences severed at arbitrary points and hands the user a transcript they have to repair by hand. Determine the mode in Phase 1; the attribution rules exist to protect real turns, not recorder artifacts.
- **Smoothing a rejoined sentence:** When two halves of a severed sentence do not meet cleanly, the fix is to flag the gap — not to write a connective that makes the seam disappear. A smoothed join is invented text wearing the speaker's voice.
- **Putting correction flags inside the file:** The deliverable should read cleanly. Flags go in the chat response.
</failed_attempts>

## Example

Cleanup is a language task with wide valid variation, so this example shows the *shape* of the work — how the three edit classes and the flagging behavior look — not a template to copy.

### Raw transcript fragment

```
[Speaker 1]
So, um, the the main thing we, you know, we set up was the.

[Speaker 1]
Was the Redis cash for. For session storage, and it, it dropped our.
Our latency by, like, I want to say 40. 40 milliseconds.
```

### Cleaned

> The main thing we set up was the Redis cache for session storage, and it dropped our latency by, I want to say, 40 milliseconds.

### What happened, by edit class

- **Mechanical (silent):** removed "So," "um," "you know," the "the the" / "we, we" / "it, it" / "For. For" / "Our. Our" stutters; merged the two fragmented blocks into one sentence; fixed the mid-sentence period breaks.
- **Confident lexical repair (noted):** "Redis cash" → "Redis cache" — an unambiguous homophone mis-hearing given "session storage."
- **Preserved deliberately:** "by, I want to say, 40 milliseconds" — the speaker's hedge and exact figure are kept, not tightened to "by 40 milliseconds."

### What the Phase 4 report would say

> One correction to confirm: "Redis cash" → **"Redis cache"** (homophone; unambiguous from the session-storage context). Everything else was filler removal and joining fragmented lines into paragraphs.
