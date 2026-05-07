# Phase 1: Gather Inputs and Analyze

Accept all available brand inputs. The quality of Phase 2 decisions depends entirely on how well you read the inputs here. Take time to analyze before proceeding.

Before loading anything, write one sentence about what you expect based on the brand name, category, or any context already provided. This expectation becomes the baseline you'll compare against. The gap between what you expected and what you find is where the most important design decisions live.

---

## Accept Any Combination

**Palette CSS** (`palette.css` or similar)
Read the file and understand: how many color families, their temperature (warm/cool/neutral), how many stops per family, which stops have strong chroma vs. are muted. Don't assign roles yet — just understand the vocabulary available.

**Reference images** (JPGs, PNGs, design screenshots)
Look at each image and extract design intent. You're not copying values — you're reading the visual language. See analysis guidance below.

**Page content spec** (from designing-websites skill or similar)
Understand what sections, modules, and content patterns exist. What repeats? Cards, hero sections, CTA bands, feature lists, navigation? This determines which preset roles are needed.

**Direct design intent** (the designer describes what they want)
Listen for: environment preference (dark/light), typography character (bold/subtle), spacing feel (tight/airy), specific treatments mentioned (pill buttons, sharp corners, etc.).

---

## Reading Reference Images

When reference images are provided, analyze each one for design intent — not literal values. Ask:

**Environment:**
- Is the ground dark or light?
- What percentage of the visual field is the ground color vs. lighter surfaces?
- Does content float on surfaces, or does it live directly on the ground?

**Typography:**
- How dramatic is the heading scale? (Subtle difference between h1 and body = tight scale. Large jump = dramatic scale.)
- How heavy are the headings? (Thin/light vs. bold/black)
- Is there tight or loose letter spacing on headings and labels?
- How dense is the body copy? (Tight leading = compact. Generous leading = airy.)

**Spacing:**
- How much breathing room exists between sections?
- Are cards tightly packed or generously spaced?
- Does the layout feel dense or airy overall?

**Shape language:**
- What radius do buttons use? (Pill, rounded, square)
- Do cards have radius or sharp corners?
- Is the radius consistent across buttons and cards?

**Interactive elements:**
- What do buttons look like? Filled, ghost, or text?
- Is there a clear visual hierarchy between button tiers?
- What color are the primary actions?

**Overall character** — summarize in 2–3 sentences:
> "These images show a dark, editorial environment with tight typography, generous section spacing, and warm accent colors against a cool dark ground. Buttons use pill radius with a high-contrast fill treatment. Cards are subtle surface elevations with generous internal padding."

---

## Artifact: Analysis Summary

Before leaving Phase 1, produce this summary for the user to confirm:

```
PHASE 1 ANALYSIS
────────────────
Inputs received: [palette CSS / N reference images / page content spec / direct intent]

Environment: [dark / light / unclear]
Rationale: [one sentence — what in the inputs led to this read]

Visual character:
[2–3 sentences describing the design intent extracted from reference images.
If no images: "No reference images provided — visual direction from direct intent only."]

Color vocabulary available:
[Brief summary of palette: "3 color families — cool neutral spine (9 stops),
warm accent (11 stops), functional colors (error/success/info)"]

Modules needed from page spec:
[List, or "Page spec not provided"]

Initial observations:
[Anything notable — unusual color temperature, strong radius preference seen
in images, very tight or very generous spacing, specific typography style, etc.]
```

Present this summary and ask the user to confirm or correct before proceeding to Phase 2.

**GATE:** Before presenting the analysis summary, confirm:
- "I have analyzed all provided inputs: [list]"
- "My environment read is based on: [specific input reference — which image or statement]"
