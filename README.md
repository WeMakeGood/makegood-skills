# Make Good Skills

A single Claude Code plugin bundling all 18 Make Good agent skills — writing, research, client work, web design, and AI development. Built by [Make Good](https://wemakegood.org).

Each skill is also available as a standalone repo at [github.com/WeMakeGood](https://github.com/WeMakeGood) for users who want to install individual skills via ZIP.

## Install

```
/plugin marketplace add WeMakeGood/makegood-skills
/plugin install makegood-skills@makegood-skills
```

That's it — all 18 skills are now available in Claude Code.

## What's included

### Writing

- **`drafting-articles`** — Research-grounded multi-session article drafting
- **`designing-article-series`** — Plan series structure and project manifests
- **`scripting-article-videos`** — Short video scripts from article artifacts
- **`generating-writing-standards`** — Extract publication-level writing standards
- **`extracting-voice-profiles`** — Build voice profiles from writing samples
- **`writing-case-studies`** — Case studies from interview transcripts or notes
- **`processing-docx-edits`** — Process tracked changes and comments in Word docs

### Research

- **`synthesizing-interviews`** — Interview transcripts → structured research documents
- **`researching-youtube-channels`** — Channel research, video metadata, and transcripts
- **`creating-organization-dossiers`** — Org research profiles via 6-phase workflow

### Client Work

- **`writing-project-dossiers`** — Project scope documents via guided conversation
- **`generating-meeting-reports`** — Structured meeting reports from transcripts
- **`planning-social-campaigns`** — Campaign strategy, asset calendars, and content files

### Web Design

- **`designing-websites`** — Interactive phased website content strategy
- **`generating-divi-variables`** — Divi 5-compatible JSON import files (legacy — Make Good no longer uses Divi)

### AI Development

- **`building-context-libraries`** — Transform org documents into agent metaprompt modules
- **`creating-skills`** — Guided workflow for building new agent skills
- **`auditing-skills`** — Audit existing skills against current best practices

## Installing individual skills

If you only want a few skills, install them as standalone packages:

1. Visit the per-skill repo (e.g., [WeMakeGood/drafting-articles](https://github.com/WeMakeGood/drafting-articles))
2. Download the latest release ZIP
3. Unzip into `~/.claude/skills/`

Each per-skill repo has its own README, version history, and release ZIPs.

## How this repo works

This is an **aggregator** — it vendors copies of each skill from its source repo at a pinned version. Skill development happens in the per-skill repos, not here.

See [CLAUDE.md](CLAUDE.md) for the development workflow (bumping skills, adding new skills, syncing vendored content).

## License

MIT — see [LICENSE](LICENSE).
