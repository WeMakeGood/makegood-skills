# writing-case-studies

A Claude Code skill that guides users through creating comprehensive case studies from interview transcripts, notes, or outlines.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Guides users through creating comprehensive case studies from interview transcripts, notes, or outlines. Produces the case study plus all supporting assets (social posts, platform versions, metadata). Use when user says write a case study, create a case study, build a case study, develop a case study, case study from interview, or case study from transcript. Activates when source content is present via pasted text, attached file, or uploaded document, even when accompanied by context files or style guides.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "write a case study"
- "create a case study"
- "build a case study"
- "develop a case study"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `writing-case-studies-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/writing-case-studies/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip writing-case-studies-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/writing-case-studies.git ~/.claude/skills/writing-case-studies
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
