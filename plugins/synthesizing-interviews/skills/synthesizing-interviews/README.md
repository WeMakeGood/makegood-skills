# Synthesizing Interviews

An Agent Skill that transforms interview transcripts into comprehensive research documents with structured insights, key quotes, and verified references.

## What This Skill Does

This skill extracts the substance of recorded conversations for later research use. Unlike meeting report generators that focus on action items and decisions, this skill captures:

- **Ideas and insights** expressed during the conversation
- **Viewpoints and perspectives** of each speaker
- **Direct quotes** organized by theme
- **References** mentioned (with verified URLs when possible)
- **Speaker information** including roles and background

The output is intentionally comprehensive—designed to preserve the richness of discussion while removing conversational overhead.

## When to Use This Skill

Use this skill when you need to:

- Process interview transcripts for research purposes
- Extract insights from client conversations
- Create reference documents from recorded discussions
- Preserve the substance of important conversations for later use

**Do NOT use this skill for:**

- Meeting notes with action items (use a meeting report skill instead)
- Quick summaries or executive briefs
- Transcripts where you only need a few specific quotes

## How to Trigger the Skill

The skill activates when you provide a transcript and use phrases like:

- "Synthesize this interview"
- "Extract insights from this transcript"
- "Distill this conversation"
- "Process this interview transcript"
- "Analyze this interview"

## Supported Input Formats

The skill handles transcripts in any common format:

| Format | Examples |
|--------|----------|
| Subtitle files | `.srt`, `.vtt` |
| Meeting platform exports | Google Meet, Microsoft Teams |
| Recorder transcripts | Otter.ai, Rev, etc. |
| Word documents | `.docx` |
| Plain text | Pasted or uploaded |

## Providing Context (Optional)

For better results, you can provide additional context files alongside the transcript:

- **Organization dossiers** - Help verify spellings of people, programs, and initiatives
- **Reference materials** - Background on topics discussed
- **Relationship context** - Who the speakers are and their roles

The skill will use these to:
- Verify correct spellings of names and terms
- Add relevant background to the synthesis
- Flag discrepancies between transcript and known information

## Output

The skill saves output to `./tmp/[subject]-interview-synthesis-YYYY-MM-DD.md` with these sections:

1. **Discussion Outline** - High-level flow of the conversation (3 levels max)
2. **Speaker Information** - Names, roles, background, contact info if mentioned
3. **Synthesis** - Detailed distillation of the discussion (the main content)
4. **Key Quotes** - Significant quotes organized by theme
5. **References** - Articles, tools, people, organizations mentioned (with URLs)
6. **Verification Notes** - Spelling uncertainties, unverified items, discrepancies

## Example Usage

### Basic Usage

```
User: Synthesize this interview
[attaches transcript.txt]
```

### With Context

```
User: Synthesize this interview. I've attached our organization dossier for reference.
[attaches transcript.txt]
[attaches acme-corp-dossier.md]
```

### Specific Subject

```
User: Extract insights from this product feedback interview with Sarah Chen
[pastes transcript text]
```

## Tips for Best Results

1. **Provide complete transcripts** - The skill works best with full conversations, not excerpts

2. **Include speaker labels** - Transcripts with speaker identification produce better attribution

3. **Add context files for proper nouns** - If the transcript mentions specific people, products, or organizations, providing reference materials helps verify spellings

4. **Expect comprehensive output** - The synthesis section will be long by design; this is not a summarizer

5. **Check verification notes** - The skill flags uncertain items; review these for accuracy

## Handling Poor Quality Transcripts

The skill gracefully handles degraded transcripts by:

- Flagging quality issues prominently at the start of output
- Extracting what narrative is recoverable
- Marking reconstructed quotes appropriately
- Recommending re-transcription when needed

## Skill Architecture

This skill uses structured patterns to ensure consistent, high-quality output:

- **Purpose statement** - Metacognitive framing that reinforces synthesis over summarization
- **XML phase boundaries** - 7 phases wrapped in tags for hard workflow separation
- **Commitment gates** - Written confirmations required before proceeding at key decision points
- **Failed attempts documentation** - Common mistakes and why they don't work

The workflow phases are:
1. Process transcript and identify speakers
2. Build discussion outline
3. Write main synthesis (with gate confirming topics, viewpoints, tensions)
4. Extract key quotes
5. Compile and verify references
6. Note spelling/verification issues
7. Save output (with gate confirming reference search completion)

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

Upload via the `/v1/skills` endpoint.
