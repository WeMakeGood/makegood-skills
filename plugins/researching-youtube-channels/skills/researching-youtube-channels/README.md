# Researching YouTube Channels

Research YouTube channels, videos, and playlists to extract metadata, transcripts, and structured data for analysis.

## When to Use

Use this skill when you need to:
- Research a YouTube channel's video library
- Extract metadata (titles, dates, views, durations) from multiple videos
- Pull transcripts for analysis or content creation
- Filter videos by date, duration, keywords, or view count
- Analyze playlists or compare content across channels

## How to Invoke

Say things like:
- "Research Anthropic's YouTube channel and find videos about AI safety"
- "Pull the transcript from this video: [URL]"
- "List all videos from @channel-handle uploaded in the last 6 months"
- "Get the metadata for this playlist: [URL]"
- "Find videos about Constitutional AI on Anthropic's channel"

## What You'll Need

- A YouTube channel URL, handle, video URL, or playlist URL
- A research goal (what you're looking for)
- Optional: Filtering criteria (date range, duration, keywords)

## What You'll Get

The skill produces structured output files:

- `channel-manifest.json` — Complete metadata for all videos (JSON)
- `channel-overview.md` — Human-readable summary with video table
- `transcripts/` — Individual transcript files for selected videos
- `curated-report.md` — Analysis and recommendations (if requested)

## Example

**Input:** "Research Anthropic's YouTube channel and find videos relevant to Claude's personality"

**Output:**
1. Fetches all video metadata from the channel
2. Filters by keywords (personality, behavior, Claude)
3. Pulls transcripts for matching videos
4. Produces a curated report with video summaries, key quotes, and recommendations

## Tips

- Filter before fetching transcripts — for large channels, this saves significant time
- The skill uses `yt-dlp` for reliable data extraction (auto-installs if needed)
- Not all videos have transcripts available; the skill will report which ones are missing
- Output goes to the scratchpad directory by default; specify a custom path if needed
