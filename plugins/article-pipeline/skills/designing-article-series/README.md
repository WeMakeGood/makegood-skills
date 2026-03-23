# Designing Article Series

Designs article series or single-article projects from existing research. Produces series maps, research indexes, audience documents, and project manifests through interactive series-level comprehension.

## When to Use

Use this skill when you need to:
- Plan a multi-article series from a body of research
- Set up a single-article project with proper scaffolding
- Organize research documents for the drafting-articles skill
- Create the project manifest that connects research to drafting

This skill enters **after research is done** (or done enough). Origin conversations, domain research sessions, and exploratory analysis happen naturally in Claude Code sessions. This skill formalizes what that exploration produced.

## How to Invoke

Say things like:
- "Plan a series of articles from this research"
- "Set up an article project"
- "Design a series architecture"
- "I have research and want to prepare for drafting"
- "Set up a single article project from this research document"

## What You'll Need

- Research documents (a directory, file list, or documents to provide)
- A sense of author intent — what the series or article should do, who it's for
- Optionally: an existing voice profile and/or writing standards preference

## Related Skills

| Skill | Relationship |
|-------|-------------|
| **drafting-articles** | Consumer — reads the project manifest this skill produces. The handoff: "To draft Article [N], start a new session and say 'Draft Article [N].'" |
| **extracting-voice-profiles** | Upstream — produces voice profiles referenced in the manifest |
| **generating-writing-standards** | Upstream — produces writing standards modules referenced in the manifest |

## What You'll Get

All saved as files in the output location:
- **Project manifest** (`project-manifest.md`) — the contract the drafting skill reads
- **Series map** (or article brief for single articles) — per-article structural payloads and research assignments
- **Research index** — inventory of research documents with tags
- **Audience document** — who the reader is, editorial rules, prose address

## How It Works

| Phase | What Happens |
|-------|-------------|
| 1: Gather | Locate research, capture author intent, identify voice/standards preferences |
| 2: Comprehend | Read research as a body, find the series arc, propose article boundaries |
| 3: Design | Build series map entries, audience document, research index |
| 4: Produce | Write all artifacts to files, verify manifest paths |
| 5: Review | Present architecture to user, iterate until confirmed |

## Key Discipline

The series map provides **broad strokes** per article — thesis, structural role, misconception, research-to-load. It does NOT provide argument sequences, section structures, or evidence-to-section mappings. Article-level comprehension belongs in the drafting skill.

## Tips

- The skill stops for user input after Phase 2 (comprehension) and Phase 5 (review) — the two highest-value interaction points
- For single articles, the output is lighter: an article brief instead of a series map, but the same manifest format
- The necessity test applies at the series level: if an article can be removed without breaking the build, it doesn't earn its place
