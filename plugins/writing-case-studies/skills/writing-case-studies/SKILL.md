---
name: writing-case-studies
description: Guides users through creating comprehensive case studies from interview transcripts, notes, or outlines. Produces the case study plus all supporting assets (social posts, platform versions, metadata). Use when user says write a case study, create a case study, build a case study, develop a case study, case study from interview, or case study from transcript. Activates when source content is present via pasted text, attached file, or uploaded document, even when accompanied by context files or style guides.
---

# Writing Case Studies

<purpose>
Claude's default when given a project story is to report what happened—a narrative
summary of events. Case studies require the opposite: teaching transferable techniques
using the project as proof. This skill exists to enforce the "teach, don't report"
mindset and ensure every section provides actionable knowledge readers can apply.
</purpose>

Case studies are **teaching documents** that show readers how to solve problems. The subject is a running illustration, not the protagonist.

## Critical Rules

**GROUNDING:** Every claim, technique, and quote MUST come from source materials. Never invent success stories, metrics, or testimonials.

**QUOTE INTEGRITY:** Quotes are verbatim from source materials. Never alter, combine, or enhance quotes. Use "[...]" for omissions.

**PROFESSIONAL OBJECTIVITY:** If the source material doesn't support a strong case study, say so. Do not manufacture impact where evidence is thin. If techniques described are questionable, note limitations.

**SECOND-ORDER THINKING:** When presenting a technique, push past the first-order benefit. What does this approach also constrain? What does it depend on? What happens when it's applied in a different context? A teaching document that only shows the upside teaches incomplete lessons.

**CONTEXTUAL SOURCING:** When referencing a methodology or framework used in the case, note the conditions under which it was applied. Readers need to judge whether their situation is similar enough to transfer the technique — help them make that judgment.

**PREMATURE COMMITMENT CHECK:** Before committing to the case study's central teaching angle, check whether the source material supports alternative framings that might be more useful to readers. The most obvious takeaway is not always the most transferable one.

**PROTECT THE SUBJECT:** Default to anonymization. Never expose financial difficulties, organizational dysfunction, or unflattering details without explicit permission.

**NATURAL PROSE:** Write as a senior practitioner in the field would — someone who teaches by describing what they did and what happened, not by calling their work transformative. When your prose sounds like AI writing about the field rather than someone in it, the voice has slipped. Return to the practitioner's perspective. Revision backstop — these words signal the voice has drifted: pivotal, crucial, vital, testament to, underscores, highlights, vibrant, tapestry, delve, foster, garner, leverage, landscape (figurative), holistic, robust, synergy, cutting-edge, groundbreaking, nestled, showcases, boasts, elevate. Also avoid: "Not only X but Y," "serves as," "stands as," vague attribution ("experts say"), formulaic balance ("Despite challenges, [positive]").

<failed_attempts>
What DOESN'T work:

- **Starting with the subject:** "Company X faced a challenge..." puts the subject as protagonist. Start with the reader's problem instead.
- **Reporting chronologically:** "First they did A, then B, then C" is a report. Organize by technique, not timeline.
- **Generic "Get Started" sections:** "Define your goals and understand your audience" wastes the reader's time. Reference specific tools from the case study.
- **Inventing supporting details:** If the source doesn't mention a metric, you can't include it. Plausible-sounding stats are still hallucinations.
- **Enhancing quotes:** Even "cleaning up" a quote changes what the person said. Use verbatim or paraphrase without quotation marks.
- **Skipping source files:** If you haven't read every provided file, you will miss context and contradict information the user gave you.
</failed_attempts>

## Output Rules

**Claude Code:** Write files to the confirmed output directory.

**Claude AI (desktop/web):** Create artifacts for each document. Do not use MCP filesystem tools—artifacts are your output mechanism.

**Claude API:** Return content in your response, clearly labeled by filename.

## The Fundamental Shift

**Wrong mindset:** "What happened in this project that we can report?"
**Right mindset:** "What techniques can we teach readers, using this project as proof?"

A case study is not a report of what happened. It's a teaching document that happens to use a real example.

<phase_setup>
## Before You Start

### 1. Confirm Output Directory

Ask: "Where should I save case study files? Default is `./tmp/` in your current directory."

**STOP.** Wait for confirmation before proceeding.

### 2. Read EVERY Provided File

**REQUIRED:** Read ALL files the user provides. No skipping. No assumptions.

- Context library → Read index AND every referenced module
- Style guide → Read completely
- Background files → Read each one
- Transcript → Read entirely

**If you skip files, you will hallucinate. You will miss critical context. You will write content that contradicts provided information.**

**GATE:** Before proceeding, write:
- "Output directory confirmed: [path]"
- "Files read: [list every file]"
- "Source content type: [transcript/notes/outline]"

Do not proceed until you have written these statements.
</phase_setup>

<phase_identify>
## Phase 1: Identify Reader Questions

**Do not start by analyzing what happened. Start by identifying what readers need to learn.**

Ask yourself:

1. Who will read this case study?
2. What problem keeps them up at night?
3. What questions do they have about solving that problem?
4. What techniques would help them if they knew about them?

Write 3-5 specific questions readers have. These become the backbone of the case study.

**Example:** If the reader is a marketing manager, their questions might be "How do I get consistent results with limited budget?" or "What do I do when something isn't working?" Derive questions from the source content and target audience.

**Ask the user:** "Here are the reader questions I identified: [list]. Are these the right questions? What's missing?"

**GATE:** Before proceeding, write:
- "Target reader: [description]"
- "Reader questions: [list 3-5 questions]"
- "User confirmed questions: [yes/no]"

**STOP.** Wait for user confirmation of reader questions.
</phase_identify>

<phase_extract>
## Phase 2: Extract Techniques from Source

Now read the source content looking for **techniques you can teach** that answer the reader questions.

For each reader question, find:
- **The technique** — What specific method/approach solves this?
- **The proof** — What evidence shows it works? (MUST be from source material)
- **The quote** — What captures the insight? (MUST be verbatim from source)

**CRITICAL:** If you cannot find proof or quotes in the source material, do not invent them. Note the gap and ask the user for additional information.

### Teaching vs. Reporting

**Reporting (wrong):** "The team implemented a new system and saw improved results."

**Teaching (right):** "Here's how to structure this type of system—and here's one team's experience applying it..."

The difference: Teaching tells readers **how to do it themselves**. Reporting just describes what someone else did.

### Critical Judgment Calls

**Before including ANY information, ask:**

1. **Does this teach a technique the reader can use?** If no, cut it.
2. **Would this embarrass the subject?** If yes, anonymize or cut it.
3. **Is this internal/operational?** Processing fees, platform migrations, org restructuring → cut it.
4. **Can the reader act on this?** If no, cut it.

### Protecting the Subject

The case study subject trusted you with their story. Do not:
- Expose financial difficulties
- Reveal organizational dysfunction
- Include metrics that make them look bad
- Name them if anonymity serves them better
- Include dollar amounts without permission (use percentages instead)

**Default to anonymization** unless there's a clear reason to name them AND they benefit from being named.

**GATE:** Before proceeding, write:
- "Techniques identified: [list techniques with supporting evidence]"
- "Gaps in source material: [list any missing proof/quotes, or 'None']"
</phase_extract>

<phase_plan>
## Phase 3: Plan the Structure

Structure the case study as a **teaching document with a through-line**.

### The Through-Line

Identify the reader's transformation:
- **From:** [Starting state - overwhelmed, stuck, skeptical]
- **To:** [Ending state - confident, equipped, enabled]

Each section should move the reader along this journey.

### The Pattern for Each Section

Each section teaches a technique, with the subject as illustration:

```
## [Technique as Header - what reader will learn]

[Speak directly to reader's problem - "You face X..."]

[Teach the technique - "Here's how to approach this..."]

[Illustrate with the example - "One team applied this by..."]

[Quote that captures the insight]
```

### What NOT to Do

Do not write:
- "The Challenge: [Subject] faced..."
- "Background: [Subject] is a..."
- "[Subject] needed to..."

The subject appears only as illustration after you've taught the technique.

### Planning the Structure

Propose a structure based on:
- The reader questions identified in Phase 1
- The techniques extracted in Phase 2
- What the source material supports

Each section should teach a technique. The structure emerges from the content—do not force a template.

**Sections must connect.** A case study is one continuous narrative, not disconnected text blocks. Each section should build on the previous one. If you removed the section headers, it should still read as a coherent piece.

### Planning Questions

Before finalizing the plan, verify:
- Does every section teach a specific technique?
- Does every section open with the reader's problem?
- Does the subject appear only as illustration (not protagonist)?
- Is there a clear through-line (reader transformation)?
- Does "Get Started" give readers something new and actionable?
- **Can every planned section be supported by actual source material?**

**If the source material doesn't support a planned section, either remove it or ask the user for additional information. Do not proceed with gaps you plan to fill with assumptions.**

**GATE:** Before proceeding, write:
- "Through-line: From [starting state] to [ending state]"
- "Planned sections: [list section titles]"
- "Each section has source support: [yes/no]"

**STOP.** Get explicit user approval of the structure before drafting.
</phase_plan>

<phase_draft>
## Phase 4: Write the Draft

Write to `case-study-draft.md` in the output directory.

### Rule 1: Teach, Don't Report

Every section must teach something the reader can do. If you're just describing what happened, rewrite.

**Test:** Could the reader implement this technique based on what you wrote?

### Rule 2: Follow the Approved Plan

The plan was approved. Execute it. Do not:
- Invent a different structure
- Add sections not in the plan
- Skip sections that are in the plan
- Change the techniques you committed to teaching

### Rule 3: Quotes Are Verbatim

**Never alter quotes.** This is an integrity issue.

- Copy quotes exactly from source material
- Use [...] for omissions
- If you must paraphrase, clearly mark it: "The team lead explained that..." (not in quotation marks)
- Attribute quotes to named speakers when possible

### Rule 4: Follow Provided Style Guidelines

If the user provided a context library with writing guidelines—**follow them exactly.** Your instincts about "good writing" do not override explicit instructions.

Watch for:
- Banned words or phrases
- Voice and tone requirements
- Attribution requirements
- Confidentiality rules (e.g., no dollar amounts)

### Rule 5: Substantive Paragraphs

Case studies are documentation, not social media content.

- No single-sentence paragraphs for dramatic effect
- Each paragraph should contain multiple related points
- Information density over style
- Professional tone, not punchy engagement-bait

### What to NEVER Include

- Platform migrations, tool changes
- Processing fees, administrative costs
- Attribution tracking implementation
- Organizational politics or restructuring
- Metrics that don't prove the techniques work
- Details that could embarrass the subject
- Generic advice readers could figure out themselves

### The "Get Started" Section

This section must give readers something **new and actionable**—not platitudes.

**Bad:** "Start by defining your goals and understanding your audience."
**Good:** Specific tools, resources, or next steps the reader can take immediately.

The "Get Started" content comes from the source material—reference specific tools, resources, or techniques mentioned in the case study.

**GATE:** Before proceeding, write:
- "Draft saved to: [file path]"
- "Sections written: [list]"
- "All quotes verbatim from source: [yes/no]"
</phase_draft>

<phase_review>
## Phase 5: Review

Present the draft summary and ask:

1. Does each section teach a technique (not just report what happened)?
2. Is the subject protected?
3. Does "Get Started" give readers something new?
4. Would you share this with the audience?

**Make edits until approved.**

**GATE:** Before proceeding, write:
- "User approved draft: [yes/no]"
- "Edits made: [list changes, or 'None']"

**STOP.** Do not proceed to asset generation until user explicitly approves the draft.
</phase_review>

<phase_assets>
## Phase 6: Generate Assets

Only after draft approval.

**Create assets in this order:**

1. `metadata.md` — Audience, keywords, imagery, distribution
2. `versions/blog-post.md` — Full version
3. `versions/linkedin-article.md` — Condensed, ends with engagement question
4. `versions/email-version.md` — Subject line options + 200-300 word teaser
5. `social/linkedin-posts.md` — 3 posts (one per technique taught)
6. `social/twitter-posts.md` — 3-5 posts
7. `social/pull-quotes.md` — 3-5 quotes with attribution + key statistics
8. `index.md` — **Create last.** Catalog what was actually produced.

**GATE:** Before completing, write:
- "Assets created: [list files]"
- "All assets saved to: [directory path]"
</phase_assets>

## Quick Reference: The Questions

**Phase 1 - Reader Questions:**
- Who reads this?
- What problem do they have?
- What techniques would help them?

**Phase 2 - Extraction Filters:**
- Does this teach a technique the reader can use?
- Would this embarrass the subject?
- Is this internal/operational?
- Can the reader act on this?

**Phase 3 - Structure Check:**
- Does every section teach a specific technique?
- Does every section open with the reader's problem?
- Is there a through-line (reader transformation)?
- Does the subject appear only as illustration?

**Phase 4 - Drafting Rules:**
- Am I teaching or just reporting?
- Are quotes verbatim and attributed?
- Am I following provided style guidelines?
- Does "Get Started" give something new and actionable?

**Phase 5 - Final Check:**
- Would you share this with the target audience?
- Does this teach readers something they didn't know?
