# researching-youtube-channels

A Claude Code skill that researches YouTube channels and retrieves video metadata, descriptions, and transcripts.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Researches YouTube channels and retrieves video metadata, descriptions, and transcripts. Use when the user wants to research a YouTube channel, pull video metadata, extract transcripts, search a channel's video library, analyze YouTube playlists, or find videos on specific topics. Activates when YouTube URLs, channel handles, or video research requests are provided.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "research a YouTube channel"
- "pull video metadata"
- "extract transcripts"
- "search a channel's video library"

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `researching-youtube-channels-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/researching-youtube-channels/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip researching-youtube-channels-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/researching-youtube-channels.git ~/.claude/skills/researching-youtube-channels
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
