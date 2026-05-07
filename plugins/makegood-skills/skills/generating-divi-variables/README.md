# generating-divi-variables

A Claude Code skill that builds a complete Divi 5 design system from brand inputs — palette CSS, reference images, page content spec, and design intent.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Builds a complete Divi 5 design system from brand inputs — palette CSS, reference images, page content spec, and design intent. Generates a brand YAML layered on top of the boilerplate, then produces an import-ready JSON with semantic variables, a live math engine (type and spacing scales via CSS pow()), and role presets wired to those variables. Use when setting up a Divi 5 design system, generating Divi variables and presets, translating visual design direction into a Divi import file, regenerating an existing Divi import from a brand YAML spec, or when a user provides palette files, reference site images, or page content specs for Divi.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "setting up a Divi 5 design system"
- "generating Divi variables and presets"
- "translating visual design direction into a Divi import file"
- "regenerating an existing Divi import from a brand YAML spec"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `generating-divi-variables-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/generating-divi-variables/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip generating-divi-variables-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/generating-divi-variables.git ~/.claude/skills/generating-divi-variables
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
