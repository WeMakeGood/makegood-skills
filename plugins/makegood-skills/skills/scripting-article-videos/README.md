# scripting-article-videos

A Claude Code skill that creates short video scripts (primarily 1-minute shorts/reels) from article drafting artifacts.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Creates short video scripts (primarily 1-minute shorts/reels) from article drafting artifacts. Mines comprehension findings, process logs, and article plans for research that was interesting but fell outside the article's structural argument — connections found, surprises, gaps flagged. Use when user says script a video, create video script, make a video from the article, write a short, or references video content for an article. Activates when article drafting artifacts exist (article plan, process log, draft) from the drafting-articles skill.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "script a video"
- "create video script"
- "make a video from the article"
- "write a short"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `scripting-article-videos-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/scripting-article-videos/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip scripting-article-videos-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/scripting-article-videos.git ~/.claude/skills/scripting-article-videos
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
