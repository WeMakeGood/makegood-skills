---
name: researching-youtube-channels
description: Researches YouTube channels and retrieves video metadata, descriptions, and transcripts. Use when the user wants to research a YouTube channel, pull video metadata, extract transcripts, search a channel's video library, analyze YouTube playlists, or find videos on specific topics. Activates when YouTube URLs, channel handles, or video research requests are provided.
---

# Researching YouTube Channels

<purpose>
When researching YouTube content, Claude's default is to use WebFetch (unreliable for YouTube) or ask the user to copy/paste information manually. This skill exists because systematic YouTube research requires reliable data extraction—metadata, transcripts, and channel information—that scripts handle better than web scraping. The skill separates data fetching (scripts with yt-dlp) from analysis (Claude), producing structured output for research, curriculum design, or content curation.
</purpose>

## Critical Rules

**GROUNDING:** Base all output ONLY on data returned by the fetch scripts. Before stating any video title, URL, view count, upload date, or transcript content, verify it exists in the fetched data. If a video or transcript cannot be fetched, name what's missing and why. Your language should make clear whether information comes from fetched metadata, transcript content, or your inference from titles and descriptions.

**PROFESSIONAL OBJECTIVITY:** If a channel doesn't have relevant content for the user's research goals, say so. If search criteria are too narrow or too broad, suggest adjustments. The user needs accurate curation, not validation that their search was productive.

**SOURCE ATTRIBUTION:** Every video reference must include a direct YouTube URL. Every transcript quote must include the video title and timestamp (if available).

**NO VIDEO DOWNLOADS:** This skill extracts metadata and subtitles only. Never download actual video files.

**SCRIPT-FIRST:** Always run the fetch script before attempting manual approaches. The script produces structured, reliable data; WebFetch does not work reliably with YouTube.

## Quick Start

For a simple channel scan:

```bash
python3 scripts/fetch_youtube.py channel "https://www.youtube.com/@channel-handle" --output ./output
```

This produces:
- `channel-manifest.json` — All video metadata as JSON
- `channel-overview.md` — Human-readable channel summary with video listing

## Workflow

Copy this checklist and track progress:

```
YouTube Research Progress:
- [ ] Phase 1: Gather requirements
- [ ] Phase 2: Fetch channel/video data
- [ ] Phase 3: Filter and organize
- [ ] Phase 4: Fetch transcripts (if needed)
- [ ] Phase 5: Analyze and curate
- [ ] Phase 6: Present results
```

<phase_gather>
### Phase 1: Gather Requirements

Ask the user:

1. **Target(s):** What channel(s), video(s), or playlist(s) to research?
   - Channel URL or handle (e.g., `@anthropic-ai`)
   - Specific video URL(s)
   - Playlist URL

2. **Research goal:** What are they looking for?
   - Full channel scan
   - Videos on a specific topic
   - Content for curriculum/training
   - Competitive analysis
   - Specific information search

3. **Filters:** Any constraints?
   - Date range (e.g., "last 6 months")
   - Duration limits (e.g., "under 20 minutes")
   - Keyword requirements
   - Minimum view count

4. **Transcripts:** Do they need transcript content?
   - Full transcripts (for analysis)
   - No transcripts (metadata only)
   - Selective transcripts (for filtered videos)

5. **Output location:** Where to save results?
   - Default: scratchpad directory
   - User-specified directory

**GATE:** Before proceeding, confirm:
- "Target: [channel/video/playlist URL or description]"
- "Research goal: [what they're looking for]"
- "Filters: [any constraints, or 'none']"
- "Transcripts needed: [yes/no/selective]"
- "Output directory: [path]"
</phase_gather>

<phase_fetch>
### Phase 2: Fetch Channel/Video Data

**REQUIRED:** Run the fetch script. Do not skip this step or attempt WebFetch instead.

Determine the fetch type and run the appropriate command:

**For a channel:**
```bash
python3 scripts/fetch_youtube.py channel "<channel-url>" --output <output-dir>
```

**For a specific video:**
```bash
python3 scripts/fetch_youtube.py video "<video-url>" --output <output-dir>
```

**For a playlist:**
```bash
python3 scripts/fetch_youtube.py playlist "<playlist-url>" --output <output-dir>
```

The script will:
1. Check for yt-dlp (install if missing)
2. Fetch metadata with rate limiting (1-second delays)
3. Write `channel-manifest.json` with all video data
4. Write `channel-overview.md` with human-readable summary

**Known limitation:** Channel fetches use `--flat-playlist` which does NOT include upload dates. If the user needs date filtering, fetch individual video metadata for relevant videos using the `video` command.

**If the script fails:**
- Check the error message for troubleshooting hints
- Common issues: invalid URL, private channel/video, rate limiting
- **Verify the channel handle** — handles can be confusing (e.g., `@anthropic-ai` is Anthropic the AI company, but `@Anthropic` is a gaming channel)
- Report the error to the user; do not invent data

**GATE:** Before proceeding, confirm:
- "Fetched [N] videos from [channel/playlist name]"
- "Data saved to: [manifest path]"
</phase_fetch>

<phase_filter>
### Phase 3: Filter and Organize

Read the manifest file and apply user-specified filters:

```bash
python3 scripts/fetch_youtube.py filter <manifest-path> [options]
```

Filter options:
- `--keyword "<term>"` — Videos with keyword in title/description
- `--after "YYYY-MM-DD"` — Videos uploaded after date
- `--before "YYYY-MM-DD"` — Videos uploaded before date
- `--min-duration <seconds>` — Minimum video length
- `--max-duration <seconds>` — Maximum video length
- `--min-views <count>` — Minimum view count
- `--output <path>` — Save filtered results

If the user wants thematic grouping:
1. Review filtered video titles and descriptions
2. Identify themes/categories
3. Group videos by theme in your analysis

**GATE:** Before proceeding, confirm:
- "Filtered to [N] videos matching criteria"
- "Themes identified: [list themes, or 'not requested']"
</phase_filter>

<phase_transcripts>
### Phase 4: Fetch Transcripts (If Requested)

**Only fetch transcripts for filtered/selected videos.** Do not fetch transcripts for all videos in a large channel.

```bash
python3 scripts/fetch_youtube.py transcripts <manifest-or-url> --output <output-dir>/transcripts
```

For selective fetching (specific video IDs):
```bash
python3 scripts/fetch_youtube.py transcripts --videos "id1,id2,id3" --output <output-dir>/transcripts
```

Transcripts are saved as individual markdown files: `<video-id>.md`

**Transcript availability notes:**
- Not all videos have transcripts (auto-generated or manual)
- The script will note which videos lack transcripts
- Do not invent transcript content for videos without transcripts

**Known limitation:** YouTube may require a PO (Proof of Origin) token for subtitle access. If transcripts fail with "PO token" errors, use these workarounds:
1. Fetch full video metadata (`video` command) — descriptions often contain chapter markers
2. Note chapter timestamps in your curated report as navigation aids
3. Provide direct YouTube links for manual viewing

**GATE:** Before proceeding, confirm:
- "Fetched transcripts for [N] videos"
- "Videos without transcripts: [list or 'none']"
</phase_transcripts>

<phase_analyze>
### Phase 5: Analyze and Curate

Read the manifest, overview, and transcripts. Produce the user's requested output.

**For raw data requests:** Simply summarize what was found and point to the output files.

**For curated research:** Analyze the content and produce a curated report:

1. **Channel/Source Overview**
   - Channel name, subscriber count, total videos
   - Content themes and typical video format
   - Publishing frequency

2. **Relevant Videos** (organized by theme if applicable)
   - Title and URL
   - Upload date, duration, view count
   - Brief description of content
   - Relevance to research goal

3. **Key Insights from Transcripts** (if transcripts were fetched)
   - Notable quotes with timestamps and video attribution
   - Recurring themes or concepts
   - Gaps or areas not covered

4. **Recommendations**
   - Which videos to prioritize
   - What's missing or needs supplementation
   - Related channels or content (if discovered)

**GROUNDING REMINDER:** Base all analysis ONLY on fetched data. Your language should make clear what comes from metadata, what comes from transcripts, and what is your inference. Cite sources for every claim.

Write the curated report to: `<output-dir>/curated-report.md`

**GATE:** Before proceeding, confirm:
- "Curated report written to: [path]"
- "All citations verified against source data"
</phase_analyze>

<phase_present>
### Phase 6: Present Results

Summarize what was produced:

1. **Files created:**
   - `channel-manifest.json` — Raw metadata (N videos)
   - `channel-overview.md` — Channel summary
   - `transcripts/` — Transcript files (if fetched)
   - `curated-report.md` — Analysis (if requested)

2. **Key findings:** 2-3 sentence summary of what was found

3. **Next steps:** What the user might want to do with the data

**Output location:** Confirm the full path to the output directory.

**GATE:** Research complete. Confirm:
- "Output directory: [full path]"
- "Files created: [list]"
</phase_present>

## Output Structure

```
<output-dir>/
├── channel-manifest.json      # All video metadata as JSON
├── channel-overview.md        # Channel info + video listing
├── transcripts/               # Individual transcript files (if fetched)
│   ├── <video-id-1>.md
│   ├── <video-id-2>.md
│   └── ...
└── curated-report.md          # Analysis/curation (if requested)
```

## Script Reference

See [references/COMMANDS.md](references/COMMANDS.md) for detailed command options and troubleshooting.

<failed_attempts>
## What DOESN'T Work

- **WebFetch for YouTube:** YouTube pages are JavaScript-heavy and don't render properly with simple HTTP fetches. Always use the script.

- **Fetching all transcripts upfront:** For channels with hundreds of videos, this wastes time and tokens. Filter first, then fetch transcripts for relevant videos only.

- **Inventing timestamps:** If a transcript doesn't include timestamps, don't make them up. Cite "from transcript" without specific timing.

- **Guessing view counts or dates:** If the script couldn't fetch metadata, say so. Don't estimate or infer numbers.

- **Downloading videos:** The skill is for metadata and transcripts only. Video files are not downloaded.

- **Assuming channel handles:** YouTube handles can be misleading. `@Anthropic` is NOT Anthropic the AI company — that's `@anthropic-ai`. Always verify the channel content matches expectations after fetching.

- **Date filtering on channel fetches:** The `channel` command uses `--flat-playlist` which doesn't include upload dates. For date filtering, either use keyword filtering first, then fetch individual video metadata for date verification.
</failed_attempts>

## Examples

**Example 1: Channel Research**

User: "Research Anthropic's YouTube channel and find videos about Claude's personality or behavior"

1. Fetch channel data: `python3 scripts/fetch_youtube.py channel "https://www.youtube.com/@anthropic-ai" --output ./output`
2. Filter by keywords: `python3 scripts/fetch_youtube.py filter ./output/channel-manifest.json --keyword "personality" --keyword "behavior" --keyword "Claude" --output ./output/filtered.json`
3. Fetch transcripts for filtered videos
4. Analyze and produce curated report

**Example 2: Specific Video Transcript**

User: "Pull the transcript from this video: https://www.youtube.com/watch?v=xxxxx"

1. Fetch video with transcript: `python3 scripts/fetch_youtube.py video "https://www.youtube.com/watch?v=xxxxx" --transcript --output ./output`
2. Present transcript file location

**Example 3: Playlist Analysis**

User: "Get all videos from this playlist and tell me what topics they cover: [playlist URL]"

1. Fetch playlist: `python3 scripts/fetch_youtube.py playlist "<playlist-url>" --output ./output`
2. Read manifest, identify themes from titles/descriptions
3. Present thematic summary (no transcripts needed for topic overview)
