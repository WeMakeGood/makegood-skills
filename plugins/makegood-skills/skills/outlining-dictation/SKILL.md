---
name: outlining-dictation
description: Turns a cleaned dictation transcript into a manipulable nested outline of the speaker's own words, so the author can cut, reorder, and reparent their thinking without retyping it. Comprehends the argument first, then decomposes to the smallest movable unit — preserving spoken lists, alternate takes, and self-corrections rather than fusing or deduplicating them. Reports every repair, drop, and observation in a companion log addressed by node number. Use when the user says outline this transcript, turn my dictation into an outline, decompose this voice note, or build an outline I can edit. NOT for summarizing, restructuring into a deliverable, or drafting prose from the outline — this skill produces a working surface, not finished writing.
---

# Outlining Dictation

<purpose>
Claude's default when handed a transcript is to improve it — smooth the phrasing,
tighten the rambling, deduplicate the repetitions, and pick the clearest version of
a point made three ways. Every one of those operations is defensible in isolation,
and together they destroy the thing an outline is for: a surface the author can
manipulate, made of words the author actually said.

The damage is worse than lost phrasing. When the model joins what the speaker kept
separate, the author permanently loses the ability to reorder their own argument —
five spoken items returned as two means three nodes that can no longer be culled,
promoted, or moved. The manipulation surface is gone before the author touches it.

This skill produces an outline whose every token traces to the speaker, structured
so that any node can be moved, reparented, or deleted in one operation without
retyping. The author does the editorial work. Claude makes it cheap.
</purpose>

Produces a nested outline the author can open in an editor and reflow with a pointing device — plus a companion log carrying every machine observation, addressed by node number.

## Critical Rules

**AUTHOR TOKENS ONLY:** Every word in the outline traces to something the speaker said. No bridges, no connectives, no summaries, no labels — not even helpful ones. A marker Claude adds is a keystroke the author spends stripping it later. Every machine observation belongs in the log.

**COMPREHEND BEFORE DECOMPOSING:** Read the whole transcript and identify the argument before building any structure. Granularity follows load — a load-bearing claim is decomposed finely because the author will manipulate it; a passing aside is not. Structure built before understanding anchors on whatever came first, and produces an outline that cannot be recomposed because nothing marks which nodes carry weight.

**COMPREHENSION SHAPES DEPTH, NEVER SEQUENCE OR WORDING:** Claude may decide what nests under what and how deep the tree runs. Claude may not reorder the speaker's material or alter their words. Both violations are mechanically detectable; both are disqualifying.

**NEVER FUSE:** Items the speaker delivered separately stay separate. A spoken list of eleven becomes eleven nodes. This is the primary failure mode and the most destructive — see `<failed_attempts>`.

**NEVER RANK OR SELECT:** When the speaker makes the same point more than once, those are alternate takes, not redundancy. Present all of them in spoken order. Choosing among them is authorship and belongs to the author. A ranked list looks like helpful ordering, and a tired reader takes the top one.

**REPORT EVERY DROP:** Culling restatement and disfluency is correct work. Doing it silently is not — only the author knows whether an abandoned thought was going somewhere.

## Quick Start

1. Confirm the input is a **cleaned** transcript. If it is raw, run `cleaning-transcripts` first.
2. Read the whole thing and write the comprehension pass (Phase 1).
3. Decompose from that comprehension (Phase 2).
4. Write the log — trace first, then repairs, drops, and observations (Phase 3).
5. Verify, and report what the check found (Phase 4).

## Output

Two files, named after the source:

| File | Contents | Provenance |
|---|---|---|
| `<name>_outline.md` | The outline. Nothing but the author's words. | author-origin |
| `<name>_log.md` | Every machine observation, by node number. | machine-origin |

Optionally `<name>_trims.md` when material is cut — same nested format, retaining each node's original parent path so it can be restored.

## Workflow

```
Progress:
- [ ] Phase 1: Comprehend
- [ ] Phase 2: Decompose
- [ ] Phase 3: Log
- [ ] Phase 4: Verify
```

<phase_comprehend>
### Phase 1: Comprehend

**REQUIRED:** Read the entire transcript before building any structure.

Establish, in your thinking or in a short working note:

1. **What this is.** A meeting prep, an argument being worked out, a status report, a piece of positioning. The kind of artifact determines what the author will do with it.
2. **The argument.** What is the speaker actually claiming, and what depends on what? Arguments in dictation are frequently distributed — stated in pieces across the whole recording and never gathered. Trace the dependencies.
3. **What is load-bearing.** The claims the argument rests on. These get decomposed finely.
4. **What is supporting detail.** Mechanics, walkthroughs, asides, context. These get decomposed coarsely — nobody reorders a UI description.
5. **Restatement.** Where the speaker says the same thing twice for emphasis rather than as a genuine alternate take. Knowing which claim is load-bearing is what makes a second statement of it recognizable as reinforcement.
6. **Explicit content to surface.** Asks, deadlines, commitments, decisions — things the author will need to find without re-reading.
7. **What is genuinely missing.** A claim the argument needs that the speaker never made anywhere. Check first whether it is *distributed rather than absent*: asking for something the author already said spends their attention on work already done.

**GATE:** Before decomposing, write this line in your thinking — not in your response: "I have read the full transcript, identified the argument and its load-bearing claims, and know which material is supporting detail." Do not build structure until you have written it.
</phase_comprehend>

<phase_decompose>
### Phase 2: Decompose

Plain nested markdown ordered lists. `1.` at every level — markdown handles the numbering, so inserting a node never requires renumbering. No headers, no frontmatter, no metadata, no annotation.

**Every node must be:**

1. **Writable** — text that could appear in the finished piece. Not an instruction, not a label naming an argumentative move.
2. **One beat** — one idea. Tells that it holds more: a comma series, two clauses joined by *and*, a colon followed by a list.
3. **Mobile** — movable, reparentable, or deletable **without rewording**. A node that would need rewriting to work in a new position is not a real node.
4. **Cullable in one operation** — deleting it is a single selection.
5. **Legible** — it reads.

Mobility is the operative structural test. A node can hold exactly one beat and still be immobile because its meaning depends on the sibling above it.

**Granularity:** decompose to the smallest unit the author would want to move, cut, or reparent on its own — and no finer. Four hundred fragments destroys shape as thoroughly as fusion destroys granularity.

Depth follows the material. Four to five levels is normal. **Uniform depth across a piece is a defect** — it means the rate was set by sentence structure rather than by what matters. A good outline has visible relief.

**Split at the thought boundary, not the sentence boundary.** When a node holds a subject governing two predicates, the subject becomes the parent and the predicates become children:

```markdown
2. All of these things
   1. End up building up a larger campaign
   2. That allows them to address the needs they're really looking to address
```

Splitting those into siblings passes a naive one-beat check and still destroys reflow, because the claims cannot move against each other while staying attached to their subject. **Find the node that owns the parts, then break out what it owns.**

**The legibility test governs what to repair:**

- The edit makes an illegible node legible → **make it**
- The node already reads → **leave it**
- The edit would not make it legible → **flag it as a gap**, do not attempt a repair

Do not ask whether something is a disfluency or the speaker's voice. That question is unanswerable in the moment and produces hedging. A mid-sentence self-correction usually reads and stays; an abandoned sentence-start usually does not and goes.

**Takes stay unmarked.** The same point made twice becomes separate nodes in spoken order, with no annotation. The geometry already carries the signal — contiguous nodes in parallel construction covering ground the outline has covered. The log records the mapping.

**GATE:** Before writing the log, write this line in your thinking — not in your response: "Every node is the speaker's words, spoken order is unchanged, and no list the speaker delivered separately has been fused." Do not proceed until you have written it.
</phase_decompose>

<phase_log>
### Phase 3: Write the log

Machine-origin. This is where everything Claude noticed goes, addressed by node number so the author can check any claim in one glance.

**Use tables.** Scanning a table costs less than reading prose — the same reason the outline works. Length is not the cost driver; form is. Do not compress the log to save the author reading; structure it so reading is cheap.

Sections, in this order:

**1. The argument trace.** The load-bearing chain, stated as **node references only**:

> Node 17.2 says enrichment consumes the context library. Node 24 says the library is contaminated. Node 25.2 says the lookup is therefore running on wrong data.

That is a trace, not a thesis. **Every element must be a node reference.** A trace containing prose that is not in a node is Claude authoring the conclusion — and an author who reads a machine-written thesis will edit against its framing instead of finding their own.

Name what is genuinely missing separately, and only after checking that it is not merely distributed.

**2. Explicit content.** Asks, deadlines, commitments — by node number, in spoken order, unranked.

**3. Scene observations.** Which nodes share a subject. **Reported, never applied.** Spoken order is the order the thinking happened; relocating material by subject moves it out of the argument that earned it. Grouping is the author's cut to make.

**4. Takes.** A move-by-move mapping table by node number, where the speaker covered the same ground more than once.

**5. Repairs.** Every token changed, in a table, meaning-affecting ones first, each with what the guess rests on.

**6. Drops.** Everything culled, with a reason. Mandatory.

**7. Structural notes.** Where granularity was a judgment call, and why.

**8. Pickups.** Genuine gaps, phrased as a request: *"You went from X to Y with nothing between; give me the line that joins them."*
</phase_log>

<phase_verify>
### Phase 4: Verify

Run `check-custody.py` against the **cleaned transcript** (not the raw one — against raw, every removed filler registers as a drop and buries the real ones):

```
check-custody.py CLEANED OUTLINE [--trims FILE] [--repairs w1,w2,...]
```

It reports two things, and they fail differently:

- **Invention** — outline tokens absent from the source and not declared as repairs. **Always a defect.** Every one must appear in the log's repair table.
- **Coverage** — source material in neither outline nor trims. **Not a defect by itself.** Culling restatement is correct; the requirement is that every drop is reported.

If the script is unavailable, do the same check by reading: confirm every outline token traces to the transcript, and that spoken order is unchanged.

**GATE:** Before delivering, write this line in your thinking — not in your response: "Verified: no invented tokens, spoken order preserved, and every drop is reported in the log." Do not deliver until you have written it.
</phase_verify>

## Distinction From Adjacent Skills

This skill **decomposes** a transcript into a manipulable structure. It does not clean, summarize, or draft.

- **Raw transcript with transcription errors and fillers** → `cleaning-transcripts` first. This skill expects cleaned input.
- **A summary, minutes, or action items** → `generating-meeting-reports`.
- **Research synthesis with structured insights and quotes** → `synthesizing-interviews`.
- **Prose drafted from research and a voice profile** → `drafting-articles`.

If the user asks for something the Critical Rules forbid — tighten it, cut the repetition, pick the best version, write it up — do not silently comply and do not simply refuse. Name what falls outside a decomposition, deliver the outline, and offer the other work as a separate pass on top of it. The preserved version still exists, and the tradeoff stays visible.

<failed_attempts>
What DOESN'T work — every one of these happened in testing against real dictation:

- **Fusing a spoken list.** Five items delivered separately, returned as "CRM integrations including social media and website development." The author loses three nodes they could have culled, promoted, or reordered — before they ever see the outline. This is the most destructive single operation in the skill.
- **Splitting at the transcription's sentence boundary.** "All of these things end up building a larger campaign" and "that allows them to address the needs" as siblings, when the first phrase is a subject governing both predicates. Each node holds one beat, so a naive check passes, and the claims still cannot move against each other.
- **Deduplicating a story the speaker replaced.** In one sample the speaker told a story, rejected it mid-telling, and told a better one. A summarizing pass keeps the vivid first story and deletes the correction — which is the actual thinking.
- **Marking takes in the outline.** A `[take]` label seems helpful and has to be stripped by hand later, adding a keystroke to the artifact whose purpose is to remove them.
- **Repairing a date from context.** A correct date was removed because surrounding references seemed not to corroborate it. File metadata resolved it. Dates carry no internal redundancy — check the file's timestamp, then flag rather than alter.
- **Asking for a pickup on material the author already supplied.** An argument distributed across three nodes was reported as a missing bridge. Check whether it is distributed before asking.
- **Deciding whether something is voice or disfluency.** Unanswerable in the moment; it produces hedging and hands the author a decision Claude should have made. Ask whether the edit makes an illegible node legible.
- **Grouping by subject.** Moving material together by topic assumes spoken order is arbitrary. Across five samples it never was — it is the order the thinking happened, and relocating a node moves it out of what earned it.
</failed_attempts>

## Example

Decomposition is a judgment task with wide valid variation, so this shows the *shape* of the work rather than a template.

### Cleaned transcript fragment

> For example, if they're doing a capital campaign, they're going to need CRM integrations, which includes social media development, email strategy, website design and development, tracking, Google add-ons possibly. All of these things end up building up a larger campaign that allows them to address the needs that they're really looking to address.

### Outline

```markdown
1. For example, if they're doing a capital campaign
   1. They're going to need CRM integrations, which includes
      1. social media development
      2. email strategy
      3. website design and development
      4. tracking
      5. Google add-ons possibly
   2. All of these things
      1. End up building up a larger campaign
      2. That allows them to address the needs that they're really looking to address
```

### What happened

- **The five services stayed five nodes.** Each can be reordered for rhetorical punch or cut individually.
- **"All of these things" became a parent, not a sibling.** It is a subject governing two predicates. As siblings, those two claims could not move against each other while staying attached to their subject.
- **Nothing was reworded.** Every token is the speaker's, including "possibly" and the loose "end up building up."
