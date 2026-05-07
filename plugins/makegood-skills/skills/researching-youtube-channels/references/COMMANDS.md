# Command Reference

Complete reference for the `fetch_youtube.py` script commands and options.

## Prerequisites

The script requires `yt-dlp`. It will auto-install if missing:

```bash
pip install yt-dlp
```

## Commands

### channel

Fetch all video metadata from a YouTube channel.

```bash
python3 scripts/fetch_youtube.py channel "<channel-url>" --output <dir>
```

**Arguments:**
- `url` — Channel URL in any format:
  - `https://www.youtube.com/@handle`
  - `https://www.youtube.com/channel/UCxxxxxx`
  - `https://www.youtube.com/c/channelname`
  - `https://www.youtube.com/user/username`

**Options:**
- `--output`, `-o` — Output directory (default: `./output`)

**Output:**
- `channel-manifest.json` — JSON with all video metadata
- `channel-overview.md` — Human-readable summary with video table

### video

Fetch metadata for a single video.

```bash
python3 scripts/fetch_youtube.py video "<video-url>" --output <dir> [--transcript]
```

**Arguments:**
- `url` — Video URL:
  - `https://www.youtube.com/watch?v=xxxxx`
  - `https://youtu.be/xxxxx`

**Options:**
- `--output`, `-o` — Output directory (default: `./output`)
- `--transcript` — Also fetch transcript (if available)

**Output:**
- `channel-manifest.json` — JSON with video metadata
- `channel-overview.md` — Video details in markdown
- `transcripts/<video-id>.md` — Transcript (if `--transcript` used)

### playlist

Fetch all videos from a playlist.

```bash
python3 scripts/fetch_youtube.py playlist "<playlist-url>" --output <dir>
```

**Arguments:**
- `url` — Playlist URL:
  - `https://www.youtube.com/playlist?list=PLxxxxxx`

**Options:**
- `--output`, `-o` — Output directory (default: `./output`)

**Output:**
- `channel-manifest.json` — JSON with all video metadata
- `channel-overview.md` — Playlist overview with video table

### filter

Filter videos from an existing manifest.

```bash
python3 scripts/fetch_youtube.py filter <manifest.json> [options]
```

**Arguments:**
- `manifest` — Path to `channel-manifest.json`

**Options:**
- `--keyword "<term>"` — Filter by keyword in title/description (can use multiple)
- `--after "YYYY-MM-DD"` — Videos uploaded after date
- `--before "YYYY-MM-DD"` — Videos uploaded before date
- `--min-duration <seconds>` — Minimum video length
- `--max-duration <seconds>` — Maximum video length
- `--min-views <count>` — Minimum view count
- `--output`, `-o` — Save filtered results to new file

**Examples:**

```bash
# Videos about "AI safety" uploaded in 2024
python3 scripts/fetch_youtube.py filter manifest.json \
  --keyword "AI safety" \
  --after "2024-01-01" \
  --output filtered.json

# Short videos (under 10 minutes) with high view counts
python3 scripts/fetch_youtube.py filter manifest.json \
  --max-duration 600 \
  --min-views 10000 \
  --output popular-shorts.json

# Multiple keyword search
python3 scripts/fetch_youtube.py filter manifest.json \
  --keyword "Claude" \
  --keyword "personality" \
  --keyword "behavior" \
  --output claude-videos.json
```

### transcripts

Fetch transcripts for videos.

```bash
python3 scripts/fetch_youtube.py transcripts <manifest-or-url> --output <dir>
```

**Arguments:**
- `source` — Path to manifest file

**Options:**
- `--videos "id1,id2,id3"` — Fetch only specific video IDs
- `--output`, `-o` — Output directory (default: `./transcripts`)

**Output:**
- `<video-id>.md` — Individual transcript files
- `transcript-summary.json` — Summary of what was fetched/unavailable

**Examples:**

```bash
# All videos in manifest
python3 scripts/fetch_youtube.py transcripts channel-manifest.json --output ./transcripts

# Specific videos only
python3 scripts/fetch_youtube.py transcripts channel-manifest.json \
  --videos "dQw4w9WgXcQ,jNQXAC9IVRw" \
  --output ./transcripts
```

## Manifest Schema

The `channel-manifest.json` file structure:

```json
{
  "source_url": "https://www.youtube.com/@example",
  "fetched_at": "2024-01-15T10:30:00",
  "channel": {
    "name": "Channel Name",
    "id": "UCxxxxxx",
    "subscriber_count": 100000,
    "description": "Channel description..."
  },
  "video_count": 42,
  "videos": [
    {
      "id": "xxxxx",
      "title": "Video Title",
      "url": "https://www.youtube.com/watch?v=xxxxx",
      "duration": 600,
      "duration_string": "10:00",
      "view_count": 50000,
      "view_count_string": "50.0K",
      "upload_date": "20240115",
      "description": "Video description..."
    }
  ]
}
```

## Troubleshooting

**"yt-dlp not found"**
→ Install manually: `pip install yt-dlp`

**"Unable to extract" or "Video unavailable"**
→ Video may be private, age-restricted, or region-locked

**Timeout errors**
→ Large channels may take several minutes. The script has a 5-minute timeout.

**No transcripts available**
→ Not all videos have auto-generated or manual subtitles

**"PO token" errors for transcripts**
→ YouTube now requires Proof of Origin tokens for subtitle access on some videos. Workarounds:
  - Use video descriptions which often contain chapter markers
  - Fetch individual video metadata for detailed info
  - Provide direct YouTube links for manual viewing

**Rate limiting**
→ The script includes 1-second delays. If still rate-limited, wait and retry.

**Wrong channel content**
→ YouTube handles can be misleading. Example: `@Anthropic` is a gaming channel, while `@anthropic-ai` is Anthropic the AI company. Always verify the fetched content matches expectations.

**upload_date is null**
→ The `channel` command uses `--flat-playlist` for speed, which doesn't fetch upload dates. To get dates:
  1. Use keyword filtering first to narrow down videos
  2. Fetch individual video metadata using the `video` command
  3. Individual video fetches include full metadata with dates

## URL Format Examples

| Type | URL Format |
|------|------------|
| Channel (handle) | `https://www.youtube.com/@anthropic-ai` |
| Channel (ID) | `https://www.youtube.com/channel/UCxxxxxx` |
| Channel (custom) | `https://www.youtube.com/c/channelname` |
| Video | `https://www.youtube.com/watch?v=xxxxx` |
| Video (short) | `https://youtu.be/xxxxx` |
| Playlist | `https://www.youtube.com/playlist?list=PLxxxxxx` |
