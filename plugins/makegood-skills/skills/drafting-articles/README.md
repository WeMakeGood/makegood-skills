# drafting-articles

A Claude Code skill that drafts research-grounded long-form articles across multiple sessions.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Drafts research-grounded long-form articles across multiple sessions. Reads a project manifest to find voice profile, writing standards, audience document, and research, then runs Setup, Comprehend, Design, Draft, and Editorial phases with process gates. Use when drafting, writing, resuming, or working on an article, or when the user says draft article, resume drafting, write article, draft standalone article, or references an article by number or title. Works for both series articles and standalone pieces.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "drafting"
- "writing"
- "resuming"
- "or working on an article"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `drafting-articles-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/drafting-articles/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip drafting-articles-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/drafting-articles.git ~/.claude/skills/drafting-articles
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
