# designing-article-series

A Claude Code skill that designs article series or single-article projects from existing research.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Designs article series or single-article projects from existing research. Through interactive series-level comprehension, produces series maps, research indexes, audience documents, and project manifests that the drafting-articles skill reads. Use when planning a series, setting up an article project, organizing research for articles, or when the user says design series, plan articles, set up article project, or prepare research for drafting. Also activates for single article setup when user provides research and wants to scaffold before drafting.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "planning a series"
- "setting up an article project"
- "organizing research for articles"
- "or when the user says design series"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `designing-article-series-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/designing-article-series/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip designing-article-series-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/designing-article-series.git ~/.claude/skills/designing-article-series
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
