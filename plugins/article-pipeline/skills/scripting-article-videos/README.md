# Scripting Article Videos

Creates short video scripts (primarily 1-minute shorts/reels) from article drafting artifacts — highlighting research that was interesting but fell outside the article's structural argument.

## When to Use

Use this skill when you need to:
- Create a companion video for a drafted article
- Script a short/reel from research that didn't make the article
- Produce teleprompter-ready scripts for on-camera delivery

## How to Invoke

Say things like:
- "Script a video for Article 3"
- "Create a short from the healthcare article"
- "What video could we make from the article we just drafted?"

## What You'll Need

- A **project manifest** (`project-manifest.md`) — the same one used by the drafting-articles skill
- **Article drafting artifacts** — article plan (with comprehension findings), process log, and draft (the article must be past Phase 2 at minimum)
- A **voice profile** — referenced in the manifest

## Related Skills

| Skill | Relationship |
|-------|-------------|
| **drafting-articles** | Produces the article artifacts this skill mines |
| **designing-article-series** | Produces the project manifest |
| **extracting-voice-profiles** | Produces voice profiles loaded for on-camera delivery |

## What You'll Get

A teleprompter-ready video script saved to `Drafts/article-[N]-video-script-[date].md`, including:
- Script text written for spoken delivery
- B-roll suggestions as margin notes for the editor
- Source list tracing every claim to research documents
- Word count and estimated duration

## How It Works

Three phases in a single session:

| Phase | What Happens |
|-------|-------------|
| Setup + Comprehend | Load article artifacts, mine comprehension findings and process log for excluded material, propose 1-3 video topics (STOP 1) |
| Script | Load voice profile, build evidence inventory, write teleprompter script with b-roll notes |
| Review + Present | Self-review against quality checks, present to user for feedback (STOP 2) |

## Tips

- The skill deliberately does NOT load writing standards — video has different conventions than longform prose
- Videos are supplemental to the article, not summaries — they tell an adjacent story
- Default target is ~150-180 words (~1 minute). Can go longer with your approval.
- The voice profile's conversational/teaching mode leads, not its analytical writing mode
- B-roll suggestions are for your editor — the script itself is what you read on the teleprompter
