# Phase 2: Design Decisions

Present each decision with your recommendation and rationale. The designer confirms or overrides. Do not proceed to YAML until all decisions are confirmed.

The decisions made here determine everything downstream. A wrong scale choice is 5 seconds to fix here and 30 minutes to fix after import.

---

## Decision 1: Environment

Dark ground or light ground?

State your read from the Phase 1 analysis and ask for confirmation. If unclear from inputs, ask directly.

The environment determines which end of the palette serves as ground, which semantic color slots get which palette stops, and how the interactive colors behave against the ground.

---

## Decision 2: Type Scale

Which modular scale ratio fits the brand character?

| Scale | Ratio | Character |
|-------|-------|-----------|
| Minor third | 1.200 | Subtle, compact — headings only slightly larger than body |
| Major third | 1.250 | Balanced, editorial — clear hierarchy without drama |
| Perfect fourth | 1.333 | Classic, confident — standard for most sites |
| Augmented fourth | 1.414 | Dramatic, display-forward — strong visual hierarchy |
| Perfect fifth | 1.500 | Very dramatic — large gap between heading levels |

Present your recommendation with rationale drawn from the reference images:
> "The references show a dramatic heading scale with large h1s relative to body text — augmented fourth (1.414) fits this character."

Also consider:
- **`type-base`** — should it stay at 1rem or shift? If the reference images show noticeably larger body text than typical, suggest 1.125rem or 1.25rem.
- **`type-scale-mobile`** — defaults to 2 steps down (minor-third at 1.200 for perfect-fourth desktop). Confirm this is appropriate or adjust.

---

## Decision 3: Spacing Feel

How dense or airy is the layout?

This drives `space-base`. The scale ratio follows from type scale unless there's a reason to decouple them.

| Feel | space-base | Character |
|------|-----------|-----------|
| Tight/compact | 0.875rem | Dense UI, information-forward |
| Standard | 1rem | Balanced — default |
| Airy | 1.125rem | Generous breathing room |
| Very airy | 1.25rem | Gallery-like, minimal |

Present your read from reference images:
> "The references show generous section spacing with comfortable card padding — space-base 1rem with the default 1.333 scale feels right."

---

## Decision 4: Radius

What shape language does the design use?

| Treatment | Radius | Character |
|-----------|--------|-----------|
| Sharp | 0px everywhere | Formal, architectural, editorial |
| Subtle | radius-sm (4px) for inputs, radius-md (0.5rem) for cards | Professional, clean |
| Friendly | radius-lg (1rem) for cards, radius-pill for buttons | Modern, approachable |
| Pill + rounded | radius-pill for buttons, radius-lg for cards | Contemporary, action-forward |

State which radius variables apply to which contexts:
- Buttons → `radius-pill` or `radius-md` or `0px`
- Cards/panels → `radius-lg` or `radius-md` or `0px`
- Inputs → `radius-sm` or `0px`

Consistency matters. Using the same radius family across buttons, cards, and inputs creates visual coherence.

---

## Decision 5: Color Assignments

Propose the mapping from palette stops to semantic slots. Present as a table.

The palette names below are examples from a dark environment implementation — replace with your palette's actual stop names.

| Semantic slot | Palette stop | Hex | Rationale |
|--------------|-------------|-----|-----------|
| color-ground | shoreline-800 | #081e22 | Darkest cool neutral — primary ground |
| color-surface | shoreline-700 | #223f43 | One step lighter — cards float above ground |
| color-interactive | shoreline-100 | #f6f6f1 | Near-white — maximum contrast against dark |
| ... | ... | ... | ... |

All 20 boilerplate semantic slots must be assigned. See [DIVI-SPEC.md](DIVI-SPEC.md) for the full slot list.

Also propose the 5 Divi system slot assignments (`primary`, `secondary`, `heading`, `body`, `link`).

**Color assignment principles from [PRESET-COOKBOOK.md](PRESET-COOKBOOK.md):**
- `color-ground` carries 70–80% of the visual field — get it right first
- `color-interactive` must contrast strongly against `color-ground`
- `color-text-on-interactive` must be readable on `color-interactive` fill
- `color-surface` is one elevation step from ground (lighter in dark env, darker in light env)
- Functional colors (error/success/info) follow established conventions unless brand overrides

---

## Decision 6: Preset Roles Needed

Based on the page content spec and cookbook guidance, which role presets are required?

**Typography roles** (always needed):
- Body — the default text preset with full heading scale
- What additional roles? (Eyebrow, Key Statement, Lede, Meta, Footer, Pullquote)

**Button roles** (always needed):
- Which tiers? (Primary/filled, Ghost/outline, Text/underline)
- Any environment variants? (On light surface, on accent band)

**Card/surface roles** (if page has cards):
- Column as card? Group as card?
- What content pattern — image+text+button, icon+text, stat+label?

**Section roles** (if page has distinct section treatments):
- CTA band with background color?
- Hero section with scrim?
- Accent band?

**Other module roles** (as needed from page spec):
- Navigation treatment
- Image treatments (rounded corners, etc.)
- Divider style

---

## Artifact: Decision Summary

Present all decisions in one block for user confirmation:

```
PHASE 2 DECISIONS — awaiting confirmation
──────────────────────────────────────────
Environment: [dark / light]

Type scale: [scale name] ([ratio])
  type-base: [value]
  type-scale-mobile: [value]

Spacing: space-base [value], space-scale [value]

Radius:
  Buttons: [variable name]
  Cards: [variable name]
  Inputs: [variable name]

Color assignments: [table or "see above"]

Preset roles:
  Typography: [list]
  Buttons: [list]
  Cards: [list]
  Sections: [list]
  Other: [list or none]
```

**STOP.** Do not write any YAML until the user explicitly confirms these decisions.
