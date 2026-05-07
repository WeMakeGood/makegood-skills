# generating-writing-standards

A Claude Code skill that generates structured writing standards modules from writing samples of a target publication, genre, or editorial tradition.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Generates structured writing standards modules from writing samples of a target publication, genre, or editorial tradition. Analyzes craft-level patterns and produces process-gate writing rules that shape how an LLM writes at the publication level. Use when user says generate writing standards, create prose standards, analyze publication style, build writing rules, extract editorial standards, or when writing samples from a publication or genre are provided for standards extraction. Activates when writing samples are present via pasted text, attached file, or uploaded document, even when accompanied by additional context files.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "generate writing standards"
- "create prose standards"
- "analyze publication style"
- "build writing rules"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `generating-writing-standards-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/generating-writing-standards/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip generating-writing-standards-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/generating-writing-standards.git ~/.claude/skills/generating-writing-standards
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
