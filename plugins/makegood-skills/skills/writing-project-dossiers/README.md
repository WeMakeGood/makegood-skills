# writing-project-dossiers

A Claude Code skill that creates comprehensive project dossiers through interactive guided conversation.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Creates comprehensive project dossiers through interactive guided conversation. Produces scope documents covering objectives, deliverables, timeline, budget, team roles, risks, and communication plans suitable for client approval. Accepts multiple input documents (meeting reports, client dossiers, example deliverables, templates) in any format. Use when user says write a project dossier, create a project scope document, build a project plan, draft a project brief, scope a project, or create a campaign dossier. Activates when project planning materials are provided via pasted text, attached file, or uploaded document, even when accompanied by additional context files.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "write a project dossier"
- "create a project scope document"
- "build a project plan"
- "draft a project brief"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `writing-project-dossiers-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/writing-project-dossiers/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip writing-project-dossiers-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/writing-project-dossiers.git ~/.claude/skills/writing-project-dossiers
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
