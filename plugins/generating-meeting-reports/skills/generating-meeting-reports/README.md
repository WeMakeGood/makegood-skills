# Generating Meeting Reports

An Agent Skill that transforms meeting transcripts into structured, actionable reports with attendees, decisions, action items, and follow-ups.

## What This Skill Does

This skill extracts actionable information from meeting transcripts and organizes it into a standardized report format. Unlike interview synthesis that preserves conversational richness, this skill focuses on:

- **Decisions made** during the meeting
- **Action items** with owners, due dates, and dependencies
- **Discussion topics** organized by subject
- **Resources mentioned** (tools, documents, links)
- **Follow-ups and open questions**

The output is designed for quick scanning and action tracking—executives should grasp essentials in 30 seconds.

## When to Use This Skill

Use this skill when you need to:

- Document meeting outcomes for stakeholders
- Track action items and their owners
- Create records of decisions made
- Produce standardized meeting minutes

**Do NOT use this skill for:**

- Interview transcripts for research (use synthesizing-interviews instead)
- Casual conversations without action items
- Transcripts where you only need a summary paragraph

## How to Trigger the Skill

The skill activates when you provide a transcript and use phrases like:

- "Create a meeting report"
- "Generate meeting minutes"
- "Summarize this meeting"
- "Turn this transcript into a report"
- "Document this meeting"

## Supported Input Formats

The skill handles transcripts in any common format:

| Format | Examples |
|--------|----------|
| Meeting platform exports | Zoom, Google Meet, Microsoft Teams |
| Subtitle files | `.srt`, `.vtt` |
| Recorder transcripts | Otter.ai, Rev, Fireflies, etc. |
| Word documents | `.docx` |
| Plain text | Pasted or uploaded |

## Output

By default, the skill returns the report inline in the conversation. You can change this with a keyword in your request:

| Request | Output |
|---------|--------|
| "Create a meeting report" | Returns report inline |
| "Create a meeting report **as a file**" | Writes `meeting-report-YYYY-MM-DD.md` to disk |
| "Create a meeting report **as an artifact**" | Creates a Claude artifact |

When outputting as a file or artifact, the skill shows progress checkpoints as it works. When outputting inline, it runs silently and returns only the final report.

The report includes these sections:

1. **Executive Summary** - 2-3 paragraphs covering purpose, key decisions, and critical next steps
2. **Meeting Details** - Date, time, duration, type, and attendees
3. **Key Discussion Topics** - Background, points discussed, decisions, and implementation details
4. **Action Items** - Checkboxes with owner, due date, priority, and dependencies
5. **Resources Discussed** - Tools, documents, and systems mentioned
6. **Notes** - Follow-up meetings, open questions, and future considerations

## Example Usage

### Inline (default)

```
User: Create a meeting report from this transcript
[attaches zoom-transcript.txt]
```

### Save to File

```
User: Create a meeting report as a file
[attaches zoom-transcript.txt]
```

### As an Artifact

```
User: Generate meeting minutes as an artifact

[Sarah Chen]
Let's discuss the Q2 roadmap...
[pastes rest of transcript]
```

## Tips for Best Results

1. **Provide complete transcripts** - Partial transcripts may miss key decisions or action items

2. **Include speaker labels** - Transcripts with speaker identification enable proper action item attribution

3. **Mention the meeting date** - If not in the transcript, tell the skill when the meeting occurred

4. **Review action item ownership** - The skill extracts "I'll do X" as commitments; verify the assignments are correct

5. **Check the Notes section** - Open questions and follow-ups are captured here

## How the Skill Handles Uncertainty

The skill explicitly marks uncertain information rather than guessing:

| Situation | How It's Marked |
|-----------|-----------------|
| Unknown meeting date | "[Not specified]" |
| Unclear speaker role | "[Role unknown]" or "[Role inferred from context]" |
| Implicit commitment | "[Implicit commitment]" |
| Ambiguous attribution | "Speaker attribution uncertain between [Name A] and [Name B]" |

## Skill Architecture

This skill uses structured patterns to ensure consistent output:

- **Purpose statement** - Reinforces extraction over compression
- **XML phase boundaries** - 4 phases with hard workflow separation
- **Commitment gates** - Written confirmations required before proceeding
- **Failed attempts documentation** - Common mistakes to avoid

The workflow phases are:
1. Analyze transcript (identify speakers, topics, date)
2. Extract structured data (action items, decisions, topics)
3. Generate report (using standardized template)
4. Review and deliver (verify completeness)

## Installation

### Claude Code

Place the skill folder in:
- `~/.claude/skills/` (personal)
- `.claude/skills/` (project)

### Claude.ai

1. Zip the skill folder
2. Go to Settings > Features > Skills
3. Upload the zip file
4. Start a new conversation to load the skill

### Claude API

Upload via the `/v1/skills` endpoint. By default, the skill returns the report inline — ideal for API consumers. Include "as a file" in the prompt if you want file output instead.
