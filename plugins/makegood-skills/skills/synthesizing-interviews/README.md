# synthesizing-interviews

A Claude Code skill that synthesizes interview transcripts into comprehensive research documents with structured insights, key quotes, speaker information, and verified references.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Synthesizes interview transcripts into comprehensive research documents with structured insights, key quotes, speaker information, and verified references. Use when user says synthesize interview, extract insights from transcript, distill conversation, process interview, or analyze interview. Activates when transcript content is present via pasted text, inline content, attached file, or uploaded document, even when accompanied by additional context files or reference materials. NOT for meeting reports with action items.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "synthesize interview"
- "extract insights from transcript"
- "distill conversation"
- "process interview"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `synthesizing-interviews-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/synthesizing-interviews/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip synthesizing-interviews-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/synthesizing-interviews.git ~/.claude/skills/synthesizing-interviews
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
