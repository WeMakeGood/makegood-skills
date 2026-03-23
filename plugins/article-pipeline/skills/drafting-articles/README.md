# Drafting Articles

Drafts research-grounded long-form articles using a multi-session workflow that survives context window limits. Works for both series articles and standalone pieces.

## When to Use

Use this skill when you need to:
- Draft an article from research documents
- Resume work on an in-progress article draft
- Write long-form content that requires deep comprehension of research evidence
- Draft a specific article within a multi-article series

## How to Invoke

Say things like:
- "Draft Article 3"
- "Draft an article from this research"
- "Let's work on the healthcare article"
- "Resume drafting where we left off"

## What You'll Need

- A **project manifest** (`project-manifest.md`) pointing to: voice profile, writing standards, audience document, research documents, and drafts directory. The manifest is produced by the `designing-article-series` skill, or can be created manually.
- If no manifest exists, the skill asks for the minimum: research files, voice profile path, audience description, and output directory.

## Related Skills

| Skill | Relationship |
|-------|-------------|
| **designing-article-series** | Produces the project manifest and series architecture this skill reads |
| **extracting-voice-profiles** | Produces voice profiles this skill loads at Draft time |
| **generating-writing-standards** | Produces writing standards modules this skill loads at Draft time |

## What You'll Get

Across multiple sessions, the skill produces:
- **Article plan** (`Drafts/article-[N]-plan.md`) — comprehension findings, metaprompt structural plan, phase tracking
- **Draft** (`Drafts/[number]-[title]-draft-[date].md`) — the article with YAML metadata
- **Process log** (`Drafts/article-[N]-process-log.md`) — reasoning trace, editorial notes, self-corrections

## How It Works

The skill runs in three sessions with five phases:

| Session | Phases | What Happens |
|---------|--------|-------------|
| A | Setup + Comprehend + Design | Load materials, understand the evidence (STOP 1), find the story and build metaprompt plan (STOP 2) |
| B | Draft | Load voice + writing standards LAST, write the article section by section |
| C | Editorial + Quality + Present | Multi-round revision, quality checks, presentation |

Each session produces durable artifacts that the next session reads cold. The boundary between Session A and Session B is mandatory — drafting needs voice profile and writing standards fresh in context.

**Key design decisions:**
- **Comprehend before Design:** Understand the evidence before finding the story. Premature structural commitment creates inertia that resists reframing.
- **Two user STOPs in Session A:** After Comprehend (validate the reading) and after Design (validate the plan). The user confirms understanding before structure, and structure before drafting.
- **Metaprompt structural plans:** Section plans tell the drafting agent how to *think about* each section — what stance to take, what to look for — not what the prose should contain. The agent writes from research + voice + metaprompt orientation, not by paraphrasing the plan.
- **Voice and standards load LAST at Draft time:** Everything analytical loads first; voice profile is the last document loaded before calibration, so it's fresh when generation begins.

## Tips

- The skill stops for user input after every phase — confirm or redirect before it proceeds
- The break before Session B is mandatory; Sessions B and C can combine if context permits
- The process log is a first-class deliverable, not a debugging artifact — review it alongside the draft
- Plans and logs compete with voice profile and writing standards for Draft session context — keep them tight (metaprompts, not pre-drafts; reasoning, not restated sources)
- Writing standards baselines are available in `references/baselines/`
