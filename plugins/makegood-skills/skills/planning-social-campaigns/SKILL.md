---
name: planning-social-campaigns
description: Plans social media campaigns from source content, producing a campaign strategy, asset calendar, per-asset content files, and optional engagement plan. Use when planning a social campaign, creating social media content calendars, building campaign assets, or developing a multi-channel content strategy. Activates when campaign goals, source content, or planning materials are provided via pasted text, attached file, or uploaded document, even when accompanied by additional context files or brand guidelines.
---

# Planning Social Campaigns

<purpose>
Social campaign planning requires holding a large system in memory — strategy, channel selection,
audience journeys, individual asset specs, and cross-asset consistency. LLMs lose coherence when
this is attempted in a single pass or across loosely connected prompts. This skill exists to
impose structure on that complexity: plan first, confirm the plan, then build assets one at a time
from a verified manifest.
</purpose>

## Critical Rules

**SOURCING:** Base all campaign content ONLY on provided source materials (documents, transcripts, briefs, user input, context libraries). Before stating any claim about the organization, audience, or campaign goals, locate its source. If you cannot locate a source, state what's missing and ask the user.

**EPISTEMIC CALIBRATION:** The user should always be able to tell whether they're receiving content drawn from their source materials, a strategic recommendation you're making based on those materials, or a gap you're flagging. Your language should make this distinction clear without bracket markers.

**PROFESSIONAL CHALLENGE:** When a campaign approach has known pitfalls (wrong channel for the audience, timeline too compressed for the asset volume, messaging that contradicts provided brand guidelines), cite the concern and offer an alternative. Accuracy over agreement.

**NATURAL PROSE — PLANNING DOCUMENTS:** Strategy, calendar, engagement plan, and verification documents are internal working documents. Write these as a campaign strategist would — direct, specific, grounded in audience and channel realities. When a sentence sounds like AI writing about marketing rather than someone planning a campaign, the voice has slipped. Return to the practitioner's perspective.

**NATURAL PROSE — ASSET CONTENT:** Captions, emails, ad copy, and other publishable content are the organization's voice, not the strategist's. Write asset content in the organization's voice as established by their brand guidelines, context library, or tone description from Phase 1 intake. Adapt that voice to the channel per the "Writing by Channel" guidance in CHANNEL-SPECS.md. If no voice guidance was provided, ask before writing assets — do not default to a generic marketing voice.

**REVISION BACKSTOP (applies to both):** These words signal AI drift regardless of context: pivotal, crucial, vital, testament to, underscores, highlights, vibrant, tapestry, delve, foster, garner, leverage, landscape (figurative), holistic, robust, synergy. Structures to avoid: "Not only X but Y," "serves as," "stands as," vague attribution ("experts say"), formulaic balance ("Despite challenges, [positive]"). When you catch one, the fix is returning to the appropriate voice — strategist for planning docs, organization for assets — not just swapping the word.

**EARN EVERY CLAIM:** Before writing any evaluative statement — anything that asserts quality, importance, or impact — find the evidence. What specific outcome, number, or observable result supports this claim? Lead with the evidence. If no evidence exists in the source materials, cut the claim entirely. "Groundbreaking results" fails this test. "Reduced onboarding time from 6 weeks to 10 days" passes it. This applies to strategy documents, asset copy, and engagement plans equally.

**START FROM THE POINT:** Every opening — document, section, paragraph, caption, email, post — must start with the single most useful or interesting thing the reader will get. No preamble, no throat-clearing, no "We're excited to announce..." If you find yourself writing context before the point, delete the context and lead with the point. The reader can absorb context after they know why they're reading.

**ASSET INTEGRITY:** Every asset in the campaign calendar MUST be produced as an individual file/artifact. Every produced asset MUST appear in the calendar. No exceptions. The verification phase enforces this.

## Workflow

Copy this checklist and track progress:

```
Campaign Planning Progress:
- [ ] Phase 1: Intake & Strategy
- [ ] Phase 2: Campaign Calendar
- [ ] Phase 3: Asset Creation
- [ ] Phase 4: Engagement Plan (if requested)
- [ ] Phase 5: Verification & Handoff
```

<phase_intake>
### Phase 1: Intake & Strategy

#### Step 1: Gather Inputs

Collect from the user:

1. **Source content** — What are we campaigning about? (articles, videos, announcements, events, product launches, reports, etc.)
2. **Campaign goals** — What should this campaign accomplish?
3. **Target audience(s)** — Who are we trying to reach?
4. **Channels** — Which platforms will be used? Ask the user to specify their active channels and any channel-specific constraints (e.g., "Instagram but no Reels," "email list is segmented by region").
5. **Campaign dates** — Start date, end date, any fixed dates (event dates, launch dates, holidays).
6. **Campaign code** — Does the organization have an existing campaign ID or code? If not, derive one: first letters of significant words in the campaign name, max 4-5 characters, uppercase. Example: "Summer Product Launch" → `SPL`. Present the derived code for confirmation.
7. **Brand/voice context** — Any loaded context libraries, brand guidelines, or tone preferences? If none provided, ask for a brief description of the organization's voice.
8. **Calendar format preference** — Does the user want the campaign calendar as a Markdown table or CSV file?

#### Step 2: Produce Campaign Strategy

Write and save the campaign strategy document.

**Filename:** `strategy.md` (or artifact titled "[Campaign Name] Strategy")

**Structure:**

```markdown
# [Campaign Name] — Campaign Strategy
Campaign Period: [Start Date] – [End Date]
Campaign Code: [CODE]

## Goals & Objectives
[What the campaign aims to achieve, grounded in user-provided goals]

## Audience
[Target audience(s), what we know about them, what assumptions we're making]

## Strategic Approach
[How the campaign builds toward its goals over time — the narrative arc,
the audience journey, how channels work together]

## Channel Strategy
[For each channel: why it's being used, what role it plays, what content
types it will carry, any constraints]

## Campaign Segments
[If the campaign has distinct phases or thematic segments, define them
here with date ranges and focus areas]
```

#### Step 3: Gap Analysis

After drafting the strategy, explicitly categorize what's missing:

**Blocking gaps** (cannot produce quality assets without these):
- No target audience defined
- No campaign dates
- No source content to build from
- Channel selection unclear

**Informational gaps** (worth flagging, but work can proceed):
- No specific KPI targets
- No brand voice guide provided
- No competitor context
- Budget/resource constraints unknown

Present both lists to the user. For blocking gaps, ask for the information. For informational gaps, note assumptions you'll make if the user doesn't provide more.

**GATE:** Present the strategy document and gap analysis to the user.

Write: "Strategy document complete. [N] blocking gaps identified: [list or 'none']. [N] informational gaps noted: [list or 'none']. Please review the strategy and resolve any blocking gaps before we proceed to the campaign calendar."

Do not proceed until the user confirms.
</phase_intake>

<phase_calendar>
### Phase 2: Campaign Calendar

Build the asset manifest — the single source of truth for what gets produced.

#### Asset ID Format

```
[CAMPAIGN_CODE]-[CHANNEL]-[###]
```

- **CAMPAIGN_CODE**: The code from Phase 1 (e.g., `SPL`)
- **CHANNEL**: Standard abbreviation for the platform:
  - `WEB` — Website page/post
  - `EM` — Email
  - `YT` — YouTube (long-form)
  - `YTS` — YouTube Shorts
  - `FB` — Facebook post
  - `FBR` — Facebook Reel
  - `FBE` — Facebook Event
  - `IG` — Instagram post
  - `IGC` — Instagram Carousel
  - `IGR` — Instagram Reel
  - `IGS` — Instagram Story
  - `LI` — LinkedIn
  - `TT` — TikTok
  - `TH` — Threads
  - `GA` — Google Ads
  - For unlisted channels, derive a 2-3 letter abbreviation and confirm with the user
- **###**: Sequential number within that channel, starting at 001

Example: `SPL-IG-001`, `SPL-EM-003`, `SPL-YT-001`

#### Component IDs

Multi-component assets (carousels, emails with header images, videos with thumbnails) use an alpha suffix on the parent ID for individual production components:

```
[PARENT_ID]-[A-Z]
```

Components are lettered sequentially: `-A`, `-B`, `-C`, etc. The parent asset file contains all component specs; component IDs are for production reference (designer handoff, project management tracking). See the Examples section for common patterns.

#### Calendar Output

Produce the calendar in the user's preferred format (MD table or CSV).

**Filename:** `calendar.md` or `calendar.csv`

Required columns:

| Asset ID | Channel | Asset Type | Title/Description | Publish Date | Campaign Segment |
|----------|---------|------------|-------------------|--------------|-----------------|

Every row represents one discrete publishable asset. Multi-component assets (e.g., a carousel with 5 slides) get one row — the components are detailed in the asset file.

**GATE:** Present the calendar to the user.

Write: "Campaign calendar complete with [N] assets across [N] channels. This calendar is the build list — every asset on it will be produced in Phase 3. Please review and confirm, or request changes."

Do not proceed until the user confirms.
</phase_calendar>

<phase_assets>
### Phase 3: Asset Creation

**REQUIRED:** Read [references/CHANNEL-SPECS.md](references/CHANNEL-SPECS.md) before creating any assets. It contains channel-specific field requirements.

#### File Structure

When filesystem is available (Claude Code, Claude Agent SDK):
```
[campaign-name]/
├── strategy.md
├── calendar.md (or .csv)
├── assets/
│   ├── [CAMPAIGN_CODE]-[CHANNEL]-001.md
│   ├── [CAMPAIGN_CODE]-[CHANNEL]-002.md
│   └── ...
├── engagement-plan.md  (if requested, Phase 4)
└── verification.md     (Phase 5)
```

When no filesystem (Claude.ai): produce each asset as a separate artifact titled with the asset ID.

#### Per-Asset File Structure

Every asset file follows this structure:

```markdown
# [Asset ID]: [Asset Title]

**Campaign:** [Campaign Name]
**Channel:** [Channel Name]
**Asset Type:** [Post / Carousel / Email / Reel / etc.]
**Publish Date:** [YYYY-MM-DD]
**Campaign Segment:** [Segment name if applicable]

---

[Channel-specific content sections per CHANNEL-SPECS.md]
```

#### Creation Process

**Voice shift:** Asset content is the organization's voice, not the strategist's. Use the brand voice/tone from Phase 1 intake, adapted to the channel per CHANNEL-SPECS.md "Writing by Channel" guidance. If no voice guidance was provided, ask before writing assets.

Work through the calendar sequentially. For each asset:

1. Load the channel-specific writing guidance AND field requirements from CHANNEL-SPECS.md — apply both the "Writing by Channel" voice direction and the required fields for that channel type
2. Write the asset content in the organization's voice, grounded in source materials and campaign strategy
3. Include all required fields for that channel type
4. Save/output the file

If the source materials don't contain enough information to write a specific asset well, flag it in the asset file:

```markdown
## Gaps
- [What's missing and what the user needs to provide to complete this asset]
```

**Do not invent content to fill gaps.** Flag them.

#### Early Review Checkpoint

After creating the first 3 assets (or all assets if fewer than 3), pause and present them to the user.

"I've created the first [N] assets. Please review the voice, content direction, and format before I continue with the remaining [N] assets. If adjustments are needed, I'll apply them to all subsequent assets."

Do not proceed until the user confirms direction.

After all assets are created, proceed to Phase 4 (if engagement plan was requested) or Phase 5.
</phase_assets>

<phase_engagement>
### Phase 4: Engagement Plan (Optional)

Before starting this phase, ask the user: "Would you like an engagement plan covering internal team activation, audience response guidelines, and success metrics?"

If no, skip to Phase 5.

**Filename:** `engagement-plan.md` (or artifact titled "[Campaign Name] Engagement Plan")

**Structure:**

```markdown
# [Campaign Name] — Engagement Plan
Campaign Period: [Start Date] – [End Date]

## Overview
[2-3 sentences on campaign goals and engagement focus]

## Campaign Touchpoints & Timeline
### Key Dates & Milestones
- [Date]: [Activity/Milestone]

### Engagement Windows
[Key periods for concentrated engagement efforts]

## Internal Team Activation
### Team Responsibilities
[Roles and their campaign responsibilities]

### Response Guidelines
#### Common Questions & Responses
[Anticipated questions with suggested response frameworks]

#### Engagement Prompts
[Conversation starters for social media or community engagement]

## External Engagement
### Target Audiences
[Primary audience segments with engagement approaches]

### Partnership Opportunities
[Potential collaboration opportunities if relevant]

## Success Metrics
### Engagement Indicators
[Specific metrics to track]

### Growth Milestones
[Key milestones with target dates and success criteria]

## Review & Adaptation
### Check-in Schedule
[Regular review points]

### Capturing Wins
[Framework for documenting campaign successes]

## Next Steps
[Immediate actions to begin implementation]
```

Ground all content in the campaign strategy and source materials. Where organizational specifics are unknown, provide frameworks the user can fill in rather than inventing details.

**GATE:** Present the engagement plan to the user.

Write: "Engagement plan complete. Please review before we proceed to verification."

Do not proceed until the user confirms.
</phase_engagement>

<phase_verify>
### Phase 5: Verification & Handoff

#### Asset Verification

Cross-reference the Phase 2 calendar against all assets produced in Phase 3.

For every asset ID in the calendar, verify:
1. A corresponding file/artifact exists
2. The asset ID in the file matches the calendar
3. The channel matches
4. The publish date matches
5. All required channel-specific fields are present (per CHANNEL-SPECS.md)

**Filename:** `verification.md` (or artifact titled "[Campaign Name] Verification Report")

**Structure:**

```markdown
# [Campaign Name] — Verification Report

## Summary
- Total assets in calendar: [N]
- Assets created: [N]
- Assets with gaps flagged: [N]
- Missing assets: [N]

## Asset Checklist
| Asset ID | Created | ID Match | Channel Match | Date Match | Fields Complete | Notes |
|----------|---------|----------|---------------|------------|-----------------|-------|
[One row per calendar entry]

## Issues
[Any discrepancies found, with specifics]

## Gaps Summary
[Consolidated list of all gaps flagged across asset files]
```

If any assets are missing or have mismatched metadata, fix them before finalizing.

#### Teamwork Handoff

After verification is complete, ask the user:

"Would you like to generate a Teamwork import file for this campaign? If so, you can invoke the `generating-teamwork-imports` skill with the campaign strategy and calendar as input."

**GATE:** Write: "Verification complete. [N]/[N] assets confirmed. [Issues found / No issues found]. Campaign planning is complete."
</phase_verify>

## Output Requirements

**ALWAYS save outputs to files when a filesystem is available. Do not output full documents inline in chat.**

When saving files:
1. Create the campaign directory using a slugified campaign name
2. Save each deliverable to its designated filename
3. After saving, confirm the filename and provide a brief summary in chat

When no filesystem is available (Claude.ai):
1. Produce each deliverable as a separate artifact
2. Title artifacts with the document name and campaign name

<failed_attempts>
## What DOESN'T Work

- **Generating all assets in one pass:** Context degrades. The strategy and calendar get fuzzy by asset 15. The phased approach with a confirmed calendar as the build manifest prevents this.

- **Embedding asset content in the campaign plan:** Putting full email copy, carousel text, and ad specs in a single "detailed plan" document creates a monolith that's hard to use. You can't hand a designer just the Instagram carousel spec. Individual files per asset solve this.

- **Self-verifying without a checklist:** "I made sure everything is correct" is not verification. Cross-referencing every calendar row against every created file catches the assets that silently get dropped.

- **Assuming channels:** Defaulting to "the usual platforms" produces assets for channels the organization doesn't use. Always ask.

- **Inventing campaign content to fill gaps:** A plausible-sounding email subject line that doesn't reflect the actual campaign is worse than a gap flag. Flag what's missing; don't approximate.
</failed_attempts>

## Examples

### Campaign Code Derivation

| Campaign Name | Derived Code |
|---------------|-------------|
| Summer Product Launch | `SPL` |
| Annual Fundraising Gala | `AFG` |
| Q3 Brand Awareness | `Q3BA` |
| Back to School 2026 | `BTS26` |

### Asset & Component ID Examples

| Asset ID | Meaning |
|----------|---------|
| `SPL-IG-001` | Summer Product Launch, Instagram post #1 |
| `SPL-IGC-001` | Summer Product Launch, Instagram Carousel #1 |
| `SPL-IGC-001-A` | ↳ Carousel slide 1 |
| `SPL-IGC-001-B` | ↳ Carousel slide 2 |
| `SPL-EM-001` | Summer Product Launch, Email #1 |
| `SPL-EM-001-A` | ↳ Email header image |
| `SPL-YT-001` | Summer Product Launch, YouTube video #1 |
| `SPL-YT-001-A` | ↳ Video thumbnail |
| `AFG-FB-003` | Annual Fundraising Gala, Facebook post #3 |

### Calendar Row Example

| Asset ID | Channel | Asset Type | Title/Description | Publish Date | Campaign Segment |
|----------|---------|------------|-------------------|--------------|-----------------|
| SPL-IG-001 | Instagram | Post | Product teaser with key feature visual | 2026-06-01 | Teaser Phase |
| SPL-IGC-001 | Instagram | Carousel | 5-slide feature breakdown | 2026-06-03 | Teaser Phase |
| SPL-EM-001 | Email | Newsletter | Launch announcement to subscriber list | 2026-06-05 | Launch Phase |

### Asset File Example (Instagram Post)

```markdown
# SPL-IG-001: Product Teaser

**Campaign:** Summer Product Launch
**Channel:** Instagram
**Asset Type:** Post
**Publish Date:** 2026-06-01
**Campaign Segment:** Teaser Phase

---

## Caption
The part nobody tells you about switching to solar: the first month's bill.
Ours was $4.12.

Full breakdown of what changed (and what didn't) dropping June 5.

## Image Requirements
- Format: Portrait (1080x1350)
- Subject: Close-up of an electricity bill showing a $4.12 total, natural lighting, kitchen counter setting
- Text overlay: "$4.12" in large type, upper third of frame

## Alt Text
Close-up photograph of a monthly electricity bill on a kitchen counter showing a total of $4.12

## Hashtags
#solar #electricbill #homeenergy #solarpanels #energycosts
```

### Asset File Example (Email)

```markdown
# SPL-EM-001: Launch Announcement

**Campaign:** Summer Product Launch
**Channel:** Email
**Asset Type:** Newsletter
**Publish Date:** 2026-06-05
**Campaign Segment:** Launch Phase

---

## Subject Line
Our first month on solar cost $4.12

## Preview Text
Here's exactly what changed — and the one thing that surprised us.

## Body Content
We installed the panels in April. May's bill arrived yesterday.

$4.12. Down from $287.

Here's what that looked like in practice: [continue with specifics from source materials]

## Call to Action
See the full cost breakdown → [landing page URL]
```
