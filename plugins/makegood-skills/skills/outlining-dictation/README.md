# outlining-dictation

A Claude Code skill that turns a cleaned dictation transcript into a nested outline you can actually edit — made entirely of your own words.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Takes a cleaned transcript and decomposes it into a nested markdown outline where every node is a movable piece of your own speech. You open it in an editor and reflow it — cut, reorder, reparent — without retyping anything.

It reads the whole transcript and identifies the argument *before* building structure, so depth follows what matters rather than following sentence boundaries. Load-bearing claims get decomposed finely because you will manipulate them; a walkthrough or an aside gets collapsed because nobody reorders a UI description.

Everything the skill noticed goes in a companion log, addressed by node number: the argument's dependency chain, asks and deadlines buried mid-narrative, alternate takes, every repair, and every drop.

It does **not** summarize, restructure, or draft. The output is a working surface, not finished writing.

## Why it exists

Hand a voice note to an LLM and it improves it — smooths the phrasing, tightens the rambling, deduplicates repetition, picks the clearest version of a point made three ways. Each operation is defensible; together they destroy what an outline is for.

The damage runs deeper than lost phrasing. When the model joins what you kept separate, you lose the ability to reorder your own argument. Five spoken items returned as two is three nodes you can no longer cull, promote, or move — gone before you ever see the outline.

This skill treats your recording as source material and your words as fixed points. The editorial work stays yours. The skill makes it cheap.

## When Claude Code activates this skill

Say things like:

- "outline this transcript"
- "turn my dictation into an outline"
- "decompose this voice note"
- "build me an outline I can edit"

Input should be a **cleaned** transcript. For raw dictation with transcription errors and fillers, run `cleaning-transcripts` first.

## What you get

| File | Contents |
|---|---|
| `<name>_outline.md` | The outline — nothing but your words |
| `<name>_log.md` | Every machine observation, by node number |
| `<name>_trims.md` | Cut material, retained with its original parent path (when anything is cut) |

## The rules it holds itself to

- **Your tokens only.** Every word traces to something you said. No bridges, no connectives, no markers.
- **Never fuses.** Items you delivered separately stay separate.
- **Never ranks.** When you make the same point three ways, all three survive. Choosing is authorship.
- **Never reorders.** Spoken order is preserved; relocating material is your cut to make.
- **Reports every drop.** Culling restatement is correct work; doing it silently is not.

## Verification

`check-custody.py` compares the outline against the cleaned transcript and reports two things:

- **Invention** — outline words absent from your transcript. Always a defect.
- **Coverage** — material dropped and not in the trims bin. Reported, not forbidden, because culling restatement is legitimate and the requirement is only that you can see it.

## License

MIT
