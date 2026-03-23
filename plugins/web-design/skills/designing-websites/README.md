# Designing Websites

Designs website content strategy and generates all content assets through an interactive, phased workflow. Starts with CTAs and business goals, then builds audience analysis, sitemap, and page content with user review at each stage.

## What It Does

Guides a website project from "what should visitors do?" to a complete content package — sitemap, page outlines, full page content, form specs, and CPT definitions. Works with WordPress and ACF Pro.

## How It Works

7 phases across 3-4 sessions with mandatory breaks between planning and content generation:

| Session | Phases | What Happens |
|---------|--------|-------------|
| A | Gather + Comprehend | Collect requirements, read all source docs, understand how the org thinks |
| B | Strategy + Sitemap | Define CTAs and audience journeys, build conversion-driven sitemap |
| C | Outline + Content | Outline every page section-by-section, then generate full content |
| D | Validation | Structural checks and package delivery |

## Key Features

- **CTA-first** — defines what visitors should do before deciding what pages exist
- **Comprehension phase** — reads and internalizes source material before making strategy decisions
- **Context library integration** — loads agent definitions and modules from the building-context-libraries skill
- **Process logging** — tracks decisions and reasoning across sessions
- **Page outlining** — every section justifies its existence before full content is written
- **Voice/standards loading** — voice profile and writing standards load last in the content session to prevent context compaction

## Usage

```
"Design a website for [organization]"
"Help me plan website content"
"Build a sitemap for [project]"
"Resume designing website"
```

Provide source documents (brand guides, org docs, interview syntheses, context library) for best results. The skill works without them but relies entirely on conversation.

## File Structure

```
designing-websites/
├── SKILL.md                              # Orchestrator — session architecture, critical rules
├── README.md                             # This file
├── scripts/
│   └── create_source_index.py            # Generates/updates source-index.md from file paths
└── references/
    ├── TEMPLATES.md                      # Build state, process log, outline templates
    ├── CONTENT-FORMAT.md                 # Content file format, template syntax
    ├── FORMS-CPTS.md                     # Form and CPT specification formats
    ├── TECHNICAL-CONTEXT.md              # WordPress platform specifics
    └── phases/
        ├── PHASE_1_GATHER.md             # Requirements, source registry, context library discovery
        ├── PHASE_2_COMPREHEND.md         # Organizational reasoning, convergences, tensions
        ├── PHASE_3_STRATEGY.md           # CTAs, audience journeys, conversion paths
        ├── PHASE_4_SITEMAP.md            # Page hierarchy, CTA/template assignments
        ├── PHASE_5_OUTLINE.md            # Per-page section outlines with purpose statements
        ├── PHASE_6_CONTENT.md            # Full page content generation
        └── PHASE_7_VALIDATION.md         # Structural checks, package delivery
```
