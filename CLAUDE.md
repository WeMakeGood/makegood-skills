# Make Good Skills — Aggregator Plugin

This repo is the **aggregator plugin** for Make Good's Claude Code skills. It bundles all 18 per-skill repos into a single installable plugin so users can run `/plugin install makegood-skills@makegood-skills` and get everything at once.

## Source of truth

Skills are developed in their own repos under [github.com/WeMakeGood](https://github.com/WeMakeGood). This repo only **vendors** copies of those skills at pinned tagged releases — it is not a development workspace. To change a skill, change it in its own repo.

| Concern | Where it lives |
|---------|----------------|
| Skill content (SKILL.md, references/, scripts/) | `WeMakeGood/<skill-name>` |
| Skill versioning | Tags on `WeMakeGood/<skill-name>` |
| Aggregator structure (this repo) | `WeMakeGood/makegood-skills` |
| Pinned versions per skill | `skills.yaml` (this repo) |

## Repository structure

```
makegood-skills/
├── .claude-plugin/
│   └── marketplace.json              # Marketplace catalog (one plugin entry)
├── plugins/
│   └── makegood-skills/
│       ├── .claude-plugin/
│       │   └── plugin.json           # Single aggregator plugin manifest
│       └── skills/                   # Vendored from per-skill repos by sync_skills.py
│           ├── auditing-skills/
│           ├── building-context-libraries/
│           └── ... (18 skill folders total)
├── scripts/
│   └── sync_skills.py                # Pulls vendored content from GitHub releases
├── skills.yaml                       # Manifest: name, repo, tag for each skill
├── CLAUDE.md
└── README.md
```

## Workflow: bumping a skill

When a per-skill repo ships a new release and you want it in the aggregator:

1. Edit `skills.yaml` — change that skill's `tag:` to the new version
2. Run `python3 scripts/sync_skills.py` — fetches the new ZIP, replaces the vendored content
3. Bump `version` in `plugins/makegood-skills/.claude-plugin/plugin.json` (calver: `YYYY.MM.DD`)
4. Commit with a message naming which skills changed
5. Tag the aggregator release (e.g., `git tag v2026.06.15 && git push origin v2026.06.15`)

## Workflow: adding a new skill

1. Create the per-skill repo under WeMakeGood using the [ai-skills-template](https://github.com/WeMakeGood/ai-skills-template)
2. Add an entry to `skills.yaml`
3. Follow the bump workflow above

## Workflow: removing a skill

1. Delete the entry from `skills.yaml`
2. Run sync (it will not delete already-vendored skills — manually remove the folder under `plugins/makegood-skills/skills/`)
3. Bump aggregator version and tag

## Critical files

These files control how Claude Code resolves the aggregator. Do not corrupt them:

- `.claude-plugin/marketplace.json` — must list exactly one plugin: `makegood-skills`
- `plugins/makegood-skills/.claude-plugin/plugin.json` — the single plugin manifest
- `skills.yaml` — defines what gets vendored

After editing JSON or YAML, validate before committing.

## What this repo is NOT

- A development workspace for skills. Skills live in their own repos.
- A multi-plugin marketplace. There is only one plugin: the aggregator. (We tried multi-plugin previously; bundling into one matches the user intent of "I want all the Make Good skills.")
- The source of truth for skill content. The vendored copies under `plugins/makegood-skills/skills/` are downstream artifacts — edits made here will be overwritten on the next sync.

## Quality checklist

Before committing:

- [ ] `marketplace.json` is valid JSON
- [ ] `plugins/makegood-skills/.claude-plugin/plugin.json` is valid JSON
- [ ] `skills.yaml` is valid YAML
- [ ] Aggregator `version` bumped if any vendored content changed
- [ ] No skill content edited directly in `plugins/makegood-skills/skills/` (those edits will be lost on next sync)
