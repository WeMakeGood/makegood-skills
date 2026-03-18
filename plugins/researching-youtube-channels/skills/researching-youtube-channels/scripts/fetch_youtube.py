#!/usr/bin/env python3
"""
YouTube channel research tool using yt-dlp.

Extracts video metadata, channel information, and transcripts from YouTube
channels, videos, and playlists. Does NOT download video files.

Usage:
    python fetch_youtube.py channel "https://www.youtube.com/@channel" --output ./output
    python fetch_youtube.py video "https://www.youtube.com/watch?v=xxxxx" --output ./output
    python fetch_youtube.py playlist "https://www.youtube.com/playlist?list=xxxxx" --output ./output
    python fetch_youtube.py filter manifest.json --keyword "term" --output filtered.json
    python fetch_youtube.py transcripts manifest.json --output ./transcripts

Requirements:
    pip install yt-dlp
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional


def check_yt_dlp():
    """Check if yt-dlp is installed, install if missing."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print(f"yt-dlp version: {result.stdout.strip()}")
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    print("yt-dlp not found. Installing...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "yt-dlp"],
            check=True,
            timeout=120
        )
        print("yt-dlp installed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install yt-dlp: {e}")
        return False


def extract_channel_id(url: str) -> Optional[str]:
    """Extract channel identifier from various YouTube URL formats."""
    # Handle @username format
    match = re.search(r"youtube\.com/@([\w-]+)", url)
    if match:
        return f"@{match.group(1)}"

    # Handle /channel/UCxxxx format
    match = re.search(r"youtube\.com/channel/(UC[\w-]+)", url)
    if match:
        return match.group(1)

    # Handle /c/channelname format
    match = re.search(r"youtube\.com/c/([\w-]+)", url)
    if match:
        return match.group(1)

    # Handle /user/username format
    match = re.search(r"youtube\.com/user/([\w-]+)", url)
    if match:
        return match.group(1)

    return None


def extract_video_id(url: str) -> Optional[str]:
    """Extract video ID from YouTube URL."""
    patterns = [
        r"youtube\.com/watch\?v=([\w-]+)",
        r"youtu\.be/([\w-]+)",
        r"youtube\.com/embed/([\w-]+)",
        r"youtube\.com/v/([\w-]+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def extract_playlist_id(url: str) -> Optional[str]:
    """Extract playlist ID from YouTube URL."""
    match = re.search(r"[?&]list=([\w-]+)", url)
    if match:
        return match.group(1)
    return None


def format_duration(seconds: Optional[int]) -> str:
    """Format duration in seconds to human-readable string."""
    if seconds is None:
        return "Unknown"
    seconds = int(seconds)  # Convert float to int
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def format_views(count: Optional[int]) -> str:
    """Format view count to human-readable string."""
    if count is None:
        return "Unknown"
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}M"
    if count >= 1_000:
        return f"{count / 1_000:.1f}K"
    return str(count)


def fetch_channel_videos(channel_url: str, output_dir: Path) -> Dict:
    """Fetch all video metadata from a channel."""
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching channel videos from: {channel_url}")
    print("This may take a moment for channels with many videos...")

    # Use yt-dlp to get channel video list with metadata
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-json",
        "--no-warnings",
        "--extractor-args", "youtube:skip=hls,dash",
        channel_url + "/videos"
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )

        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return {"error": result.stderr, "videos": []}

    except subprocess.TimeoutExpired:
        return {"error": "Timeout fetching channel videos", "videos": []}

    # Parse JSON lines output
    videos = []
    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            video_data = json.loads(line)
            videos.append({
                "id": video_data.get("id"),
                "title": video_data.get("title"),
                "url": f"https://www.youtube.com/watch?v={video_data.get('id')}",
                "duration": video_data.get("duration"),
                "duration_string": format_duration(video_data.get("duration")),
                "view_count": video_data.get("view_count"),
                "view_count_string": format_views(video_data.get("view_count")),
                "upload_date": video_data.get("upload_date"),
                "description": video_data.get("description", ""),
            })
            # Rate limiting
            time.sleep(0.1)
        except json.JSONDecodeError:
            continue

    # Get channel metadata
    channel_info = fetch_channel_info(channel_url)

    manifest = {
        "source_url": channel_url,
        "fetched_at": datetime.now().isoformat(),
        "channel": channel_info,
        "video_count": len(videos),
        "videos": videos
    }

    # Save manifest
    manifest_path = output_dir / "channel-manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"Saved manifest: {manifest_path}")

    # Generate overview markdown
    overview_path = output_dir / "channel-overview.md"
    with open(overview_path, "w") as f:
        f.write(f"# {channel_info.get('name', 'Channel')} Overview\n\n")
        f.write(f"**URL:** {channel_url}\n")
        f.write(f"**Subscribers:** {format_views(channel_info.get('subscriber_count'))}\n")
        f.write(f"**Total Videos:** {len(videos)}\n")
        f.write(f"**Fetched:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")

        if channel_info.get("description"):
            f.write(f"## Description\n\n{channel_info.get('description')}\n\n")

        f.write("## Videos\n\n")
        f.write("| Title | Date | Duration | Views |\n")
        f.write("|-------|------|----------|-------|\n")

        for video in videos[:100]:  # Limit table to 100 rows
            title = video["title"][:60] + "..." if len(video.get("title", "")) > 60 else video.get("title", "")
            date = video.get("upload_date", "")
            if date and len(date) == 8:
                date = f"{date[:4]}-{date[4:6]}-{date[6:8]}"
            f.write(f"| [{title}]({video['url']}) | {date} | {video['duration_string']} | {video['view_count_string']} |\n")

        if len(videos) > 100:
            f.write(f"\n*...and {len(videos) - 100} more videos (see manifest for full list)*\n")

    print(f"Saved overview: {overview_path}")
    print(f"Found {len(videos)} videos")

    return manifest


def fetch_channel_info(channel_url: str) -> Dict:
    """Fetch channel metadata."""
    cmd = [
        "yt-dlp",
        "--dump-json",
        "--playlist-items", "0",
        "--no-warnings",
        channel_url
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0 and result.stdout.strip():
            data = json.loads(result.stdout.strip().split("\n")[0])
            return {
                "name": data.get("channel") or data.get("uploader"),
                "id": data.get("channel_id") or data.get("uploader_id"),
                "subscriber_count": data.get("channel_follower_count"),
                "description": data.get("description", ""),
            }
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        pass

    return {"name": "Unknown", "id": None, "subscriber_count": None, "description": ""}


def fetch_video_metadata(video_url: str, output_dir: Path, include_transcript: bool = False) -> Dict:
    """Fetch metadata for a single video."""
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching video metadata: {video_url}")

    cmd = [
        "yt-dlp",
        "--dump-json",
        "--no-warnings",
        video_url
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0:
            return {"error": result.stderr}

        data = json.loads(result.stdout.strip())

        video = {
            "id": data.get("id"),
            "title": data.get("title"),
            "url": video_url,
            "channel": data.get("channel") or data.get("uploader"),
            "channel_url": data.get("channel_url") or data.get("uploader_url"),
            "duration": data.get("duration"),
            "duration_string": format_duration(data.get("duration")),
            "view_count": data.get("view_count"),
            "view_count_string": format_views(data.get("view_count")),
            "upload_date": data.get("upload_date"),
            "description": data.get("description", ""),
            "tags": data.get("tags", []),
            "categories": data.get("categories", []),
        }

        manifest = {
            "source_url": video_url,
            "fetched_at": datetime.now().isoformat(),
            "video_count": 1,
            "videos": [video]
        }

        # Save manifest
        manifest_path = output_dir / "channel-manifest.json"
        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        print(f"Saved manifest: {manifest_path}")

        # Generate overview
        overview_path = output_dir / "channel-overview.md"
        with open(overview_path, "w") as f:
            f.write(f"# {video['title']}\n\n")
            f.write(f"**URL:** {video_url}\n")
            f.write(f"**Channel:** {video['channel']}\n")
            f.write(f"**Duration:** {video['duration_string']}\n")
            f.write(f"**Views:** {video['view_count_string']}\n")
            date = video.get("upload_date", "")
            if date and len(date) == 8:
                date = f"{date[:4]}-{date[4:6]}-{date[6:8]}"
            f.write(f"**Uploaded:** {date}\n\n")

            if video.get("description"):
                f.write(f"## Description\n\n{video['description']}\n\n")

            if video.get("tags"):
                f.write(f"## Tags\n\n{', '.join(video['tags'][:20])}\n")

        print(f"Saved overview: {overview_path}")

        if include_transcript:
            fetch_transcripts_for_videos([video], output_dir / "transcripts")

        return manifest

    except (subprocess.TimeoutExpired, json.JSONDecodeError) as e:
        return {"error": str(e)}


def fetch_playlist_videos(playlist_url: str, output_dir: Path) -> Dict:
    """Fetch all video metadata from a playlist."""
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching playlist videos: {playlist_url}")

    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-json",
        "--no-warnings",
        playlist_url
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode != 0:
            return {"error": result.stderr, "videos": []}

    except subprocess.TimeoutExpired:
        return {"error": "Timeout fetching playlist", "videos": []}

    videos = []
    playlist_title = "Playlist"

    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            data = json.loads(line)
            if data.get("_type") == "playlist":
                playlist_title = data.get("title", "Playlist")
                continue

            videos.append({
                "id": data.get("id"),
                "title": data.get("title"),
                "url": f"https://www.youtube.com/watch?v={data.get('id')}",
                "duration": data.get("duration"),
                "duration_string": format_duration(data.get("duration")),
                "view_count": data.get("view_count"),
                "view_count_string": format_views(data.get("view_count")),
                "upload_date": data.get("upload_date"),
                "description": data.get("description", ""),
            })
        except json.JSONDecodeError:
            continue

    manifest = {
        "source_url": playlist_url,
        "fetched_at": datetime.now().isoformat(),
        "playlist_title": playlist_title,
        "video_count": len(videos),
        "videos": videos
    }

    manifest_path = output_dir / "channel-manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"Saved manifest: {manifest_path}")

    # Generate overview
    overview_path = output_dir / "channel-overview.md"
    with open(overview_path, "w") as f:
        f.write(f"# {playlist_title}\n\n")
        f.write(f"**URL:** {playlist_url}\n")
        f.write(f"**Total Videos:** {len(videos)}\n")
        f.write(f"**Fetched:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")

        f.write("## Videos\n\n")
        f.write("| # | Title | Duration | Views |\n")
        f.write("|---|-------|----------|-------|\n")

        for i, video in enumerate(videos, 1):
            title = video["title"][:50] + "..." if len(video.get("title", "")) > 50 else video.get("title", "")
            f.write(f"| {i} | [{title}]({video['url']}) | {video['duration_string']} | {video['view_count_string']} |\n")

    print(f"Saved overview: {overview_path}")
    print(f"Found {len(videos)} videos in playlist")

    return manifest


def filter_videos(manifest_path: Path, output_path: Optional[Path] = None, **filters) -> Dict:
    """Filter videos from a manifest based on criteria."""
    with open(manifest_path) as f:
        manifest = json.load(f)

    videos = manifest.get("videos", [])
    original_count = len(videos)

    # Keyword filter (searches title and description)
    keywords = filters.get("keywords", [])
    if keywords:
        filtered = []
        for video in videos:
            text = f"{video.get('title', '')} {video.get('description', '')}".lower()
            if any(kw.lower() in text for kw in keywords):
                filtered.append(video)
        videos = filtered
        print(f"Keyword filter: {len(videos)} videos match {keywords}")

    # Date filters
    after_date = filters.get("after")
    if after_date:
        filtered = []
        for video in videos:
            upload = video.get("upload_date", "")
            if upload and upload >= after_date.replace("-", ""):
                filtered.append(video)
        videos = filtered
        print(f"After {after_date}: {len(videos)} videos")

    before_date = filters.get("before")
    if before_date:
        filtered = []
        for video in videos:
            upload = video.get("upload_date", "")
            if upload and upload <= before_date.replace("-", ""):
                filtered.append(video)
        videos = filtered
        print(f"Before {before_date}: {len(videos)} videos")

    # Duration filters (in seconds)
    min_duration = filters.get("min_duration")
    if min_duration:
        videos = [v for v in videos if (v.get("duration") or 0) >= min_duration]
        print(f"Min duration {min_duration}s: {len(videos)} videos")

    max_duration = filters.get("max_duration")
    if max_duration:
        videos = [v for v in videos if (v.get("duration") or 0) <= max_duration]
        print(f"Max duration {max_duration}s: {len(videos)} videos")

    # View count filter
    min_views = filters.get("min_views")
    if min_views:
        videos = [v for v in videos if (v.get("view_count") or 0) >= min_views]
        print(f"Min views {min_views}: {len(videos)} videos")

    filtered_manifest = {
        "source_url": manifest.get("source_url"),
        "fetched_at": manifest.get("fetched_at"),
        "filtered_at": datetime.now().isoformat(),
        "filters_applied": {k: v for k, v in filters.items() if v},
        "original_count": original_count,
        "video_count": len(videos),
        "videos": videos
    }

    if output_path:
        with open(output_path, "w") as f:
            json.dump(filtered_manifest, f, indent=2, ensure_ascii=False)
        print(f"Saved filtered manifest: {output_path}")

    print(f"\nFiltered: {original_count} -> {len(videos)} videos")
    return filtered_manifest


def fetch_transcripts_for_videos(videos: List[Dict], output_dir: Path) -> Dict:
    """Fetch transcripts for a list of videos."""
    output_dir.mkdir(parents=True, exist_ok=True)

    results = {
        "fetched": [],
        "unavailable": [],
        "errors": []
    }

    for i, video in enumerate(videos):
        video_id = video.get("id")
        if not video_id:
            continue

        print(f"Fetching transcript ({i+1}/{len(videos)}): {video.get('title', video_id)[:50]}...")

        url = f"https://www.youtube.com/watch?v={video_id}"

        # Try to get subtitles
        cmd = [
            "yt-dlp",
            "--write-auto-sub",
            "--write-sub",
            "--sub-lang", "en",
            "--sub-format", "vtt",
            "--skip-download",
            "--output", str(output_dir / f"{video_id}"),
            "--no-warnings",
            url
        ]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )

            # Check for subtitle file
            vtt_files = list(output_dir.glob(f"{video_id}*.vtt"))
            if vtt_files:
                # Convert VTT to plain text markdown
                vtt_path = vtt_files[0]
                md_path = output_dir / f"{video_id}.md"

                transcript_text = convert_vtt_to_text(vtt_path)

                with open(md_path, "w") as f:
                    f.write(f"# Transcript: {video.get('title', video_id)}\n\n")
                    f.write(f"**Video:** {url}\n")
                    f.write(f"**Duration:** {video.get('duration_string', 'Unknown')}\n\n")
                    f.write("---\n\n")
                    f.write(transcript_text)

                # Clean up VTT file
                vtt_path.unlink()

                results["fetched"].append({
                    "id": video_id,
                    "title": video.get("title"),
                    "file": str(md_path)
                })
                print(f"  Saved: {md_path.name}")
            else:
                results["unavailable"].append({
                    "id": video_id,
                    "title": video.get("title")
                })
                print(f"  No transcript available")

        except subprocess.TimeoutExpired:
            results["errors"].append({
                "id": video_id,
                "error": "Timeout"
            })
            print(f"  Timeout")

        # Rate limiting
        time.sleep(1)

    print(f"\nTranscripts: {len(results['fetched'])} fetched, {len(results['unavailable'])} unavailable, {len(results['errors'])} errors")
    return results


def convert_vtt_to_text(vtt_path: Path) -> str:
    """Convert VTT subtitle file to plain text, removing timestamps and deduplicating."""
    with open(vtt_path) as f:
        content = f.read()

    lines = []
    seen = set()

    for line in content.split("\n"):
        # Skip VTT header
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        # Skip timestamps
        if re.match(r"^\d{2}:\d{2}:\d{2}", line):
            continue
        # Skip blank lines and position markers
        if not line.strip() or line.startswith("align:") or line.startswith("position:"):
            continue
        # Skip numeric cue identifiers
        if re.match(r"^\d+$", line.strip()):
            continue

        # Clean HTML tags
        text = re.sub(r"<[^>]+>", "", line).strip()
        if text and text not in seen:
            lines.append(text)
            seen.add(text)

    return "\n".join(lines)


def fetch_transcripts_command(args):
    """Handle transcript fetching from command line."""
    output_dir = Path(args.output)

    if args.videos:
        # Fetch specific video IDs
        video_ids = [v.strip() for v in args.videos.split(",")]
        videos = [{"id": vid} for vid in video_ids]
    else:
        # Load from manifest
        with open(args.source) as f:
            manifest = json.load(f)
        videos = manifest.get("videos", [])

    if not videos:
        print("No videos to fetch transcripts for")
        return

    results = fetch_transcripts_for_videos(videos, output_dir)

    # Save results summary
    summary_path = output_dir / "transcript-summary.json"
    with open(summary_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved summary: {summary_path}")


def main():
    parser = argparse.ArgumentParser(
        description="YouTube channel research tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Fetch channel videos:
    python fetch_youtube.py channel "https://www.youtube.com/@anthropic-ai" --output ./output

  Fetch single video:
    python fetch_youtube.py video "https://www.youtube.com/watch?v=xxxxx" --output ./output

  Fetch playlist:
    python fetch_youtube.py playlist "https://www.youtube.com/playlist?list=xxxxx" --output ./output

  Filter videos:
    python fetch_youtube.py filter manifest.json --keyword "AI safety" --after 2024-01-01 --output filtered.json

  Fetch transcripts:
    python fetch_youtube.py transcripts manifest.json --output ./transcripts
"""
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Channel command
    channel_parser = subparsers.add_parser("channel", help="Fetch videos from a channel")
    channel_parser.add_argument("url", help="Channel URL (e.g., https://www.youtube.com/@handle)")
    channel_parser.add_argument("--output", "-o", default="./output", help="Output directory")

    # Video command
    video_parser = subparsers.add_parser("video", help="Fetch single video metadata")
    video_parser.add_argument("url", help="Video URL")
    video_parser.add_argument("--output", "-o", default="./output", help="Output directory")
    video_parser.add_argument("--transcript", action="store_true", help="Also fetch transcript")

    # Playlist command
    playlist_parser = subparsers.add_parser("playlist", help="Fetch videos from a playlist")
    playlist_parser.add_argument("url", help="Playlist URL")
    playlist_parser.add_argument("--output", "-o", default="./output", help="Output directory")

    # Filter command
    filter_parser = subparsers.add_parser("filter", help="Filter videos from manifest")
    filter_parser.add_argument("manifest", help="Path to channel-manifest.json")
    filter_parser.add_argument("--keyword", action="append", dest="keywords", help="Filter by keyword (can use multiple)")
    filter_parser.add_argument("--after", help="Videos after date (YYYY-MM-DD)")
    filter_parser.add_argument("--before", help="Videos before date (YYYY-MM-DD)")
    filter_parser.add_argument("--min-duration", type=int, help="Minimum duration in seconds")
    filter_parser.add_argument("--max-duration", type=int, help="Maximum duration in seconds")
    filter_parser.add_argument("--min-views", type=int, help="Minimum view count")
    filter_parser.add_argument("--output", "-o", help="Output path for filtered manifest")

    # Transcripts command
    transcripts_parser = subparsers.add_parser("transcripts", help="Fetch transcripts")
    transcripts_parser.add_argument("source", help="Manifest file path")
    transcripts_parser.add_argument("--videos", help="Comma-separated video IDs (optional)")
    transcripts_parser.add_argument("--output", "-o", default="./transcripts", help="Output directory")

    args = parser.parse_args()

    # Check yt-dlp
    if not check_yt_dlp():
        sys.exit(1)

    # Execute command
    if args.command == "channel":
        fetch_channel_videos(args.url, Path(args.output))
    elif args.command == "video":
        fetch_video_metadata(args.url, Path(args.output), include_transcript=args.transcript)
    elif args.command == "playlist":
        fetch_playlist_videos(args.url, Path(args.output))
    elif args.command == "filter":
        filter_videos(
            Path(args.manifest),
            output_path=Path(args.output) if args.output else None,
            keywords=args.keywords or [],
            after=args.after,
            before=args.before,
            min_duration=args.min_duration,
            max_duration=args.max_duration,
            min_views=args.min_views
        )
    elif args.command == "transcripts":
        fetch_transcripts_command(args)


if __name__ == "__main__":
    main()
