# Make Good Skills — Claude Code Instructions

This is a **plugin marketplace repository** for Claude Code. It distributes agent skills as installable plugins via the Claude Code plugin system.

## Repository Structure

```
makegood-skills/
├── .claude-plugin/
│   └── marketplace.json       # Marketplace catalog — lists all plugins
└── plugins/
    ├── article-pipeline/      # Bundle plugin (5 skills)
    │   ├── .claude-plugin/
    │   │   └── plugin.json    # Plugin manifest
    │   └── skills/
    │       └── skill-name/
    │           └── SKILL.md   # Skill instructions
    ├── web-design/            # Bundle plugin (2 skills)
    └── [skill-name]/          # Standalone plugin (1 skill each)
```

**Bundles** contain multiple related skills under one `plugin.json`. **Standalones** are one plugin per skill.

## Working in This Repo

### What this repo IS

A distribution layer. Skills are developed in `anthropic-skills` (the source repo) and published here in plugin format. Changes here are to the plugin structure, metadata, and marketplace catalog — not to skill content.

### What this repo IS NOT

A development workspace. Do not develop or test new skills here. Do not run validation scripts against the `plugins/` tree — those live in the source repo.

### Critical: Do Not Corrupt These Files

Two files control how Claude Code resolves this marketplace. Corrupting them breaks installation for all users:

- `.claude-plugin/marketplace.json` — the marketplace catalog
- `plugins/*/\.claude-plugin/plugin.json` — each plugin's manifest

Before editing either, read the file first. After editing, verify JSON is valid.

### Plugin Structure Rules

- `plugin.json` goes in `.claude-plugin/` inside the plugin folder — nowhere else
- `SKILL.md` goes in `skills/<skill-name>/` inside the plugin folder — not at the plugin root
- `references/` and `scripts/` live alongside `SKILL.md` inside the skill folder
- Do not create files outside this structure

### Adding a New Plugin

1. Create `plugins/<plugin-name>/.claude-plugin/plugin.json` with `name`, `version`, `description`
2. Create `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`
3. Add the plugin entry to `.claude-plugin/marketplace.json`
4. Verify JSON in both files is valid before committing

### Updating a Skill

1. Update `SKILL.md` (and any `references/` or `scripts/` files) in the skill folder
2. Bump `version` in the plugin's `plugin.json` — users will not receive updates without a version bump
3. Commit with a message that describes what changed and why

### Marketplace Name

The marketplace name is `makegood-skills`. This is the public-facing name users type in `/plugin install <plugin>@makegood-skills`. Do not change it.

## Quality Checklist

Before committing any change:

- [ ] JSON in `plugin.json` and `marketplace.json` is valid
- [ ] `version` bumped in `plugin.json` if skill content changed
- [ ] New plugins are listed in `marketplace.json`
- [ ] `SKILL.md` is in `skills/<skill-name>/` — not at the plugin root
- [ ] No files added outside the documented structure
