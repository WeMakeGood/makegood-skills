# extracting-voice-profiles

A Claude Code skill that extracts voice and style profiles from writing samples for LLM role adoption.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Extracts voice and style profiles from writing samples for LLM role adoption. Analyzes emails, transcripts, LLM conversations, and writing samples to produce process-gate voice documents that enable an LLM to write in a specific person's voice. Use when user says extract voice, create voice profile, build writing style guide, capture someone's voice, analyze writing style, or generate voice document. Activates when writing samples are present via pasted text, attached file, or uploaded document, even when accompanied by additional context files.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "extract voice"
- "create voice profile"
- "build writing style guide"
- "capture someone's voice"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `extracting-voice-profiles-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/extracting-voice-profiles/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip extracting-voice-profiles-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/extracting-voice-profiles.git ~/.claude/skills/extracting-voice-profiles
```

## What's in this repo

- `SKILL.md` — the skill itself, loaded by Claude Code when activated
- `references/` — supporting documentation the skill consults at runtime *(if applicable)*
- `scripts/` — utility scripts the skill runs *(if applicable)*
- `templates/` — runtime templates the skill copies into output *(if applicable)*
- `examples/` — representative example output

## Version history

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT — see [LICENSE](LICENSE).

## About Make Good

[Make Good](https://wemakegood.org) is a consultancy that partners with mission-driven organizations through new terrain — scaling, technology adoption, leadership transitions, strategic evolution. We publish our skills openly because the methodology is meant to be portable.

For other skills in this collection, see the [Make Good skills index](https://github.com/WeMakeGood/makegood-skills).
