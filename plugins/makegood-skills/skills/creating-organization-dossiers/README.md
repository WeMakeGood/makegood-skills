# creating-organization-dossiers

A Claude Code skill that creates structured organizational dossiers following a 6-phase research workflow.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Creates structured organizational dossiers following a 6-phase research workflow. Produces comprehensive profiles with executive summary, mission, leadership, financials, programs, partnerships, and strategic analysis sections. Use when user says create a dossier, build an org profile, generate an organization report, compile background on a company, or produce a prospect brief. Also triggers on client research, prospect research, due diligence report, partnership evaluation, or org analysis.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "create a dossier"
- "build an org profile"
- "generate an organization report"
- "compile background on a company"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `creating-organization-dossiers-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/creating-organization-dossiers/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip creating-organization-dossiers-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/creating-organization-dossiers.git ~/.claude/skills/creating-organization-dossiers
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
