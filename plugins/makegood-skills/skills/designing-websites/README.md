# designing-websites

A Claude Code skill that designs website content strategy and generates all content assets through interactive phased workflow.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Designs website content strategy and generates all content assets through interactive phased workflow. Starts with CTAs and business goals, then builds audience analysis, sitemap, and page content with user review at each stage. Use when planning a new website, creating website content strategy, building site architecture, or generating website copy. Triggers on website design, content strategy, sitemap creation, or website planning requests.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "planning a new website"
- "creating website content strategy"
- "building site architecture"
- "or generating website copy"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `designing-websites-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/designing-websites/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip designing-websites-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/designing-websites.git ~/.claude/skills/designing-websites
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
