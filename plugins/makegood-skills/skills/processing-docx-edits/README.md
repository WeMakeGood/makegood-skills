# processing-docx-edits

A Claude Code skill that processes DOCX files containing tracked changes and comments, synthesizes all edits, and produces clean final documents.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Processes DOCX files containing tracked changes and comments, synthesizes all edits, and produces clean final documents. Use when processing Word documents with track changes, reviewer comments, collaborative edits, or markup. Activates when DOCX file with edits is provided via attached file, uploaded document, or file path.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "processing Word documents with track changes"
- "reviewer comments"
- "collaborative edits"
- "or markup"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `processing-docx-edits-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/processing-docx-edits/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip processing-docx-edits-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/processing-docx-edits.git ~/.claude/skills/processing-docx-edits
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
