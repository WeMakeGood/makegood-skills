# Skill Conversion Examples

This document shows before/after examples of converting prompts to skills.

## Example 1: Style Guide Builder

### Before (Prompt)

```markdown
# Content Analysis and Voice Guidelines Generator

## Purpose
Analyze the provided content to extract and codify the authentic voice, tone,
and writing patterns while explicitly avoiding artificial or overly corporate
language patterns.

## Input Requirements
Please provide:
1. Email communications (both internal and external)
2. Published blog posts and articles
3. Meeting and interview transcripts
4. Additional written materials that represent the desired voice

## Analysis Instructions

### Phase 1: Content Mining
- Extract recurring vocabulary, phrases, and sentence structures
- Identify consistent tone patterns across different content types
- Note variations in formality between different communication contexts
- Document specific examples of effective communication
- Flag instances of natural, conversational language

### Phase 2: Pattern Recognition
- Catalog sentence length patterns and paragraph structure
- Document common transitions and connecting phrases
- Identify distinctive word choices that appear genuine
...
[continues for 100+ more lines]
```

### After (Skill)

**skills/building-style-guides/SKILL.md:**

```yaml
---
name: building-style-guides
description: Analyzes content samples to extract voice, tone, and writing patterns into comprehensive style guidelines. Use when asked to create a style guide, analyze brand voice, or codify writing patterns from examples.
---
```

```markdown
# Building Style Guides

Extracts authentic voice patterns from content samples and produces comprehensive style guidelines.

## Quick Start

Provide content samples (emails, articles, transcripts). Output is a structured style guide covering voice, vocabulary, tone by context, and writing mechanics.

## Workflow

```
Progress:
- [ ] Collect content samples
- [ ] Phase 1: Mine content for patterns
- [ ] Phase 2: Recognize structural patterns
- [ ] Phase 3: Characterize voice
- [ ] Generate style guide
```

### Phase 1: Content Mining

From provided samples, extract:
- Recurring vocabulary and phrases
- Tone patterns across content types
- Formality variations by context
- Examples of effective communication

### Phase 2: Pattern Recognition

Catalog:
- Sentence length and paragraph structure
- Transition phrases
- Distinctive word choices
- How technical concepts are explained

### Phase 3: Voice Characterization

Document:
- Formality levels by context
- Personality expression patterns
- Emotional resonance techniques
- Audience addressing patterns

## Output Format

Generate style guide with these sections:

1. Voice Characteristics (3-5 core traits)
2. Language Patterns (structure, length, punctuation)
3. Vocabulary Framework (preferred terms, terms to avoid)
4. Tone by Context (email, blog, social, etc.)
5. Writing Mechanics (contractions, abbreviations, numbers)
6. Examples (model sentences, before/after)
7. Editing Checklist

## Example

**Input:** 3 blog posts, 5 emails, 1 interview transcript

**Output excerpt:**
```
VOICE CHARACTERISTICS
- Warm but professional
- Direct without being blunt
- Uses "we" to build partnership

VOCABULARY FRAMEWORK
Priority phrases: "partner with", "build together", "sustainable impact"
Avoid: "leverage", "synergy", "circle back"
```
```

### What Changed

| Aspect | Prompt | Skill |
|--------|--------|-------|
| Length | 112 lines | 80 lines |
| Structure | Flat instructions | Workflow with checklist |
| Examples | None | Concrete input/output |
| Discovery | N/A | Description with triggers |
| Reusability | Single use | Any brand/voice project |

**Removed:**
- Verbose explanations of what content analysis means
- Detailed anti-pattern list (Claude knows these)
- Repetitive instruction formatting

**Added:**
- Quick Start for immediate use
- Workflow checklist for tracking
- Concrete example with actual output

---

## Example 2: Article Draft Generator

### Before (Prompt)

```markdown
# AI Article Generation Prompt

You are tasked with writing a complete article package for Make Good. Using the
provided interview content and brand guidelines, generate a complete draft
following this structure:

## Primary Deliverable: Article Draft

Write a complete article draft that includes:
1. Title: Create 3 potential headlines
2. Subheading: Write a compelling subheading that hooks readers
3. Article Body: Write a complete 800-1200 word article that:
   - Opens with a compelling hook
   - Uses clear section headers
   - Integrates provided quotes naturally
   - Builds a clear argument
   - Includes specific examples
   - Ends with a clear call to action

## Supporting Package

After the main article, provide:
1. Metadata:
   - Target audience
   - Key SEO keywords used
   - Recommended tags
   - Reading time

2. Distribution Elements:
   - 3 LinkedIn posts
   - 3 Tweets
   - 1 Email newsletter blurb (200 words)
   - 3 Pull quotes for graphics

3. Campaign Notes:
   - Related Make Good services to link
   - Suggested imagery/graphics
   - Potential follow-up content ideas

Using the interview transcript provided and focusing on [SPECIFIC STORY ANGLE],
write this complete package while maintaining Make Good's warm, thoughtful,
and professional voice.
```

### After (Skill)

**skills/drafting-articles/SKILL.md:**

```yaml
---
name: drafting-articles
description: Generates complete article packages from interview transcripts including draft, metadata, social posts, and distribution materials. Use when creating articles from interviews, generating content packages, or preparing blog posts with supporting materials.
---
```

```markdown
# Drafting Articles

Creates complete article packages from source material (interviews, research, notes).

## Quick Start

Provide:
1. Interview transcript or source content
2. Story angle or focus
3. Brand voice guidelines (or use defaults)

Output: Article draft + metadata + social posts + campaign notes

## Article Structure

### Headlines (provide 3 options)

Format: [Action/Impact] + [Subject] + [Benefit/Hook]

Example:
- "How One Nonprofit Doubled Donor Retention in 6 Months"
- "The Retention Strategy That's Changing Nonprofit Fundraising"
- "Inside the Campaign That Turned One-Time Donors Into Lifelong Supporters"

### Article Body (800-1200 words)

```
1. Hook (50-100 words)
   - Compelling opening stat, question, or scenario

2. Context (100-150 words)
   - Set up the problem or opportunity

3. Core Content (500-700 words)
   - 3-4 sections with clear headers
   - Integrate quotes naturally
   - Specific examples and data

4. Call to Action (50-100 words)
   - Clear next step for reader
```

## Supporting Package

### Metadata
- Target audience: [specific segment]
- SEO keywords: [3-5 terms used in article]
- Tags: [category tags]
- Reading time: [X minutes]

### Social Distribution

**LinkedIn (3 posts):**
- Post 1: Key insight + question
- Post 2: Quote highlight + context
- Post 3: Data point + takeaway

**Twitter/X (3 posts):**
- Tweet 1: Hook + link
- Tweet 2: Quote + emoji + link
- Tweet 3: Stat + CTA

**Email blurb (200 words):**
- Teaser that drives clicks without giving everything away

### Campaign Notes
- Related services to link
- Imagery suggestions
- Follow-up content ideas

## Example

**Input:**
- Transcript: 30-minute interview with nonprofit ED
- Angle: Donor retention success story
- Voice: Warm, professional

**Output excerpt:**

```markdown
# How Community First Doubled Their Donor Retention Rate

## A data-driven approach to building lasting relationships

When Sarah Chen took over as Executive Director of Community First...

[Article body with integrated quotes]

---

METADATA
Target: Nonprofit development directors
Keywords: donor retention, nonprofit fundraising, relationship building
Reading time: 5 minutes

LINKEDIN POST 1
"We stopped thinking about donations and started thinking about relationships."

Sarah Chen's nonprofit doubled their retention rate in one year. Here's what changed: [link]
```
```

### What Changed

| Aspect | Prompt | Skill |
|--------|--------|-------|
| Specificity | `[SPECIFIC STORY ANGLE]` placeholder | Concrete structure and examples |
| Organization | Numbered lists | Clear sections with templates |
| Examples | None | Full input/output demonstration |
| Reusability | Make Good specific | Any organization (voice configurable) |

**Removed:**
- Organization-specific references (moved to input)
- Vague placeholders like `[SPECIFIC STORY ANGLE]`

**Added:**
- Headline formula with examples
- Article structure template with word counts
- Concrete example showing actual output format

---

## Conversion Checklist

When converting a prompt to a skill:

- [ ] Remove organization-specific details (make them inputs)
- [ ] Replace `[PLACEHOLDER]` with concrete examples
- [ ] Add Quick Start section
- [ ] Add workflow checklist if multi-step
- [ ] Write third-person description with triggers
- [ ] Include at least one full input→output example
- [ ] Keep under 500 lines (split if needed)
- [ ] Remove explanations Claude already knows
