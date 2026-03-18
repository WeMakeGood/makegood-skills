# Make Good Skills

A Claude Code plugin marketplace with agent skills for writing, research, client work, and web design — built by [Make Good](https://wemakegood.org).

## Install

```
/plugin marketplace add WeMakeGood/makegood-skills
```

Then install individual plugins:

```
/plugin install article-pipeline@makegood-skills
/plugin install web-design@makegood-skills
/plugin install writing-case-studies@makegood-skills
```

Or browse everything with `/plugin` → **Discover** tab.

## Plugins

### Bundles

**`article-pipeline`** — Complete pipeline for long-form article work
- `designing-article-series` — Plan series structure and project manifest
- `drafting-articles` — Research-grounded multi-session article drafting
- `scripting-article-videos` — Short video scripts from article artifacts
- `generating-writing-standards` — Extract publication-level writing standards
- `extracting-voice-profiles` — Build voice profiles from writing samples

**`web-design`** — Website content strategy and Divi 5 design tokens
- `designing-websites` — Interactive phased website content strategy
- `generating-divi-variables` — Generate Divi 5-compatible JSON import files

### Standalone Skills

| Plugin | What it does |
|---|---|
| `writing-case-studies` | Case studies from interview transcripts or notes |
| `writing-project-dossiers` | Project scope documents via guided conversation |
| `creating-organization-dossiers` | Org research profiles via 6-phase workflow |
| `planning-social-campaigns` | Campaign strategy, asset calendars, and content files |
| `synthesizing-interviews` | Interview transcripts → structured research documents |
| `researching-youtube-channels` | Channel research, video metadata, and transcripts |
| `processing-docx-edits` | Process tracked changes and comments in Word docs |
| `generating-meeting-reports` | Structured meeting reports from transcripts |
| `building-context-libraries` | Transform org documents into agent metaprompt modules |
| `creating-skills` | Guided workflow for building new agent skills |
| `auditing-skills` | Audit existing skills against current best practices |

## Repository Structure

```
makegood-skills/
├── .claude-plugin/
│   └── marketplace.json       # Marketplace catalog
└── plugins/
    ├── article-pipeline/      # Bundle: 5 skills
    │   ├── .claude-plugin/
    │   │   └── plugin.json
    │   └── skills/
    │       ├── designing-article-series/
    │       ├── drafting-articles/
    │       ├── scripting-article-videos/
    │       ├── generating-writing-standards/
    │       └── extracting-voice-profiles/
    ├── web-design/            # Bundle: 2 skills
    └── [standalone plugins]/  # One plugin per skill
```

Each plugin contains a `plugin.json` manifest and one or more skills under `skills/`, each with a `SKILL.md` plus optional `references/` and `scripts/`.

## License

MIT — see [LICENSE](LICENSE) for details.
