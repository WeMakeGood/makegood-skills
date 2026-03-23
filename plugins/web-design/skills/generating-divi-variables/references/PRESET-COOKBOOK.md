# Divi 5 Design System Cookbook

Recipes for building color systems, variable sets, and presets. This cookbook teaches the skill how to think about design problems and translate them into a correct boilerplate + brand YAML output.

The technical rules (exact paths, bugs, constraints) live in `DIVI-SPEC.md`. This document is about design thinking and composition.

---

## Part 1: Colors

### Recipe: Building a color system

A color system starts with roles, not values. Before assigning any hex, answer: what does each color need to do?

The boilerplate defines semantic slots — `color-ground`, `color-surface`, `color-interactive`, etc. The designer's job is to assign palette stops to those slots. The system then propagates those assignments everywhere automatically.

**The assignment questions to ask:**
1. What is the ground color? (The color 70–80% of the visual field sits on)
2. What color works as a site-wide accent for links and UI elements? (This becomes `primary`)
3. What fills buttons? (May or may not be the same as `primary` — see below)
4. What contrasts with the button fill for text on top of it?
5. What is the surface color? (Cards, panels — one step away from ground)
6. What is the text hierarchy? (Primary, secondary, dim)

Don't start with "what colors do I like." Start with "what does each position in the system need to accomplish."

### Divi system slots vs. button colors — these are separate decisions

**`primary` and `secondary`** (Divi system slots) are accent colors for links and site-wide UI elements. Divi applies them automatically across the theme — to link underlines, module accents, and legacy UI elements. They go into the WordPress theme customizer and must be hex values.

**`color-interactive`** (boilerplate semantic slot) fills buttons and primary interactive elements. It may use the same color as `primary`, or a completely different one.

**Why they're separate:** On a dark environment with an inverted button treatment (light fill on dark ground), `primary` might be a warm accent for links while `color-interactive` is a near-white for button fills. Forcing buttons to use `primary` would make buttons the wrong color.

**The design question:** Does your button treatment match your link accent color? If yes, assign the same palette stop to both. If no — which is common in dark environments — assign them independently.

Example: dark site with warm accent links and inverted buttons:
```yaml
system_colors:
  primary: { ref: "neon-carrot-400" }    # warm accent for links
  secondary: { ref: "neon-carrot-600" }  # hover state for links

colors:
  color-interactive: { ref: "shoreline-100" }      # near-white button fill
  color-interactive-hover: { ref: "shoreline-300" } # slightly dimmer on hover
  color-text-on-interactive: { ref: "shoreline-800" } # dark text on light button
```

---

### Recipe: Dark environment

A dark environment uses the cool/dark end of the palette as ground and needs high-contrast text and warm or bright interactive colors to pop against it.

**Pattern:**
- `color-ground` → darkest neutral
- `color-surface` → one step lighter (cards visible against ground)
- `color-surface-alt` → two steps lighter (borders, dividers)
- `color-text-primary` → lightest neutral (near-white)
- `color-text-secondary` → mid-light neutral
- `color-text-dim` → mid neutral
- `color-interactive` → warm or bright accent (high contrast against dark)
- `color-interactive-hover` → slightly lighter or more saturated version
- `color-text-on-interactive` → dark (readable on the interactive fill)

**Dark environment tip:** Elevation goes lighter, not darker. A card that floats above the ground should be lighter than the ground, not darker. This is opposite to what feels intuitive from print design.

---

### Recipe: Light environment

A light environment uses the warm/light end of the palette as ground. Interactive colors tend to be mid-tone — not too bright (washes out) and not too dark (disappears).

**Pattern:**
- `color-ground` → lightest neutral (barely warm or cool)
- `color-surface` → one step darker (raised surface)
- `color-surface-alt` → two steps darker (footer, dividers)
- `color-text-primary` → darkest neutral
- `color-text-secondary` → mid-dark neutral
- `color-text-dim` → mid neutral
- `color-interactive` → mid-tone brand color (AA contrast on light ground)
- `color-interactive-hover` → one step darker/stronger
- `color-text-on-interactive` → white or lightest neutral

---

### Recipe: Two-brand system (same palette, two environments)

When two brands share a palette but operate in different environments (one dark, one light), the same neutral spine serves both — one brand uses the dark end as ground, the other uses the light end.

The palette CSS is shared. The brand YAML assigns different stops to the same semantic slots. The presets are identical — they reference `color-ground`, `color-interactive`, etc. — but render completely differently because the slot assignments differ.

**This is the entire point of semantic color slots.** Same preset, two completely different environments, zero duplication.

---

### Recipe: Functional colors (error, success, info, warning)

Functional colors communicate system state. They follow a consistent pattern regardless of brand:

- `color-error` → 500-level stop (AA on white, solid fills and badges)
- `color-error-hover` → 600-level stop (hover state for error fills)
- Same pattern for success and info
- Warning typically references the interactive/accent family — no separate palette needed unless brand has strong associations

Don't invent functional colors. Use established conventions (red = error, green = success, blue = info). Users bring these associations — fight them only with strong reason.

---

## Part 2: Variables

### Recipe: Tuning the type scale

The type scale is controlled by three variables:
- `type-base` — the root size everything multiplies from (default: 1rem = 16px)
- `type-scale` — the desktop ratio (default: 1.333 = perfect fourth)
- `type-scale-mobile` — the mobile ratio (default: 1.200 = minor third, 2 steps down)

**How to tune:**
- Scale feels too tight → increase `type-base` (1.125rem, 1.25rem)
- Heading hierarchy feels too dramatic → reduce `type-scale` (try 1.250 = major third)
- Mobile headings still too large → increase `mobile_steps_down` or reduce `type-scale-mobile`
- All headings need to shift up/down → change `type-base` only

**Common scales:**
| Scale | Ratio | Character |
|-------|-------|-----------|
| Minor third | 1.200 | Subtle, compact |
| Major third | 1.250 | Balanced, editorial |
| Perfect fourth | 1.333 | Classic, clear hierarchy |
| Augmented fourth | 1.414 | Dramatic, display-forward |
| Perfect fifth | 1.500 | Very dramatic |

---

### Recipe: Tuning the spacing scale

The spacing scale is controlled by two variables:
- `space-base` — the root spacing unit (default: 1rem)
- `space-scale` — the ratio between steps (default: 1.333, matches type scale)

**Using the same ratio for type and spacing creates harmonic relationships** — spacing and type feel related because they're mathematically related.

**The steps and their typical uses:**
| Variable | Approx at 1rem/1.333 | Typical use |
|----------|---------------------|-------------|
| `space-xs` | ~0.75rem | Tight internal padding (icon gaps, inline spacing) |
| `space-sm` | 1rem | Standard internal padding, base unit |
| `space-md` | ~1.33rem | Column/group internal gaps, component padding |
| `space-lg` | ~1.78rem | Row wrap gap, generous component spacing |
| `space-xl` | ~2.37rem | Row column gap, section internal spacing |
| `space-2xl` | ~3.16rem | Section gap between rows, hero-scale spacing |

**How to tune:**
- Everything feels cramped → increase `space-base`
- Spacing feels unrelated to type → set `space-scale` to match `type-scale`
- Need tighter card layouts → use `space-sm` instead of `space-md` for card padding

---

### Recipe: Radii

Four stops for different contexts:
- `radius-pill` (999px) — full round, used for buttons. Creates a pill/capsule shape.
- `radius-lg` (1rem) — cards, panels, CTA bands. Friendly, modern.
- `radius-md` (0.5rem) — chips, tags, smaller UI elements.
- `radius-sm` (4px) — inputs, tight UI. Barely rounded.

**Design direction:**
- Sharp corners (0px) → formal, architectural, editorial
- Small radius (radius-sm/md) → professional, clean
- Large radius (radius-lg) → friendly, modern, approachable
- Full pill (radius-pill) → playful, contemporary, action-forward

Using the same radius family across buttons, cards, and inputs creates visual coherence. Mixing radius sizes creates tension — use intentionally or avoid.

---

### Recipe: Font weights

Three weight variables:
- `weight-heading` — display sizes, h1–h6 (default: 800 for Inter Tight, bold impact)
- `weight-body` — body copy (default: 400, comfortable reading)
- `weight-emphasis` — buttons, eyebrows, key statements (default: 600, semi-bold)

**When to adjust:**
- Font family changed → weights may need tuning (some fonts read heavier/lighter)
- Design feels too heavy → drop `weight-heading` from 800 to 700
- Buttons feel weak → increase `weight-emphasis` to 700

---

## Part 3: Presets

### Recipe: Typography roles for divi/text

The default Body preset establishes the full type scale. Every additional text role is built on top — same heading scale, different body treatment.

**How to think about text roles:**
- What size is the body copy in this context?
- What color? (Default inherits, override only when meaningful)
- What tracking? (Wide for eyebrows/labels, tight for display, normal for body)
- What weight? (Emphasis for key statements/eyebrows, body for reading)

**Common roles:**
- **Body** — standard reading. `type-body`, `leading-body`, `weight-body`
- **Lede** — introductory paragraph, slightly larger. `type-body-lg`, `leading-body`
- **Key Statement** — emphasized callout. `type-body-lg`, `weight-emphasis`, `color-text-primary`
- **Eyebrow** — small label above headlines. `type-sm`, `tracking-wide`, `weight-emphasis`, `color-interactive-text`
- **Meta** — dates, categories, attribution. `type-caption`, `color-text-dim`, `tracking-wide`
- **Footer** — small, secondary, with link hover treatment. `type-sm`, `color-text-secondary`
- **Pullquote** — large emphasized quote. `type-body-lg`, `weight-emphasis`, left border treatment

**Every text role preset must include the full h1–h6 heading scale.** A text module might contain headings — if the preset omits them, Divi falls back to its defaults for those levels.

---

### Recipe: Button hierarchy

Three tiers, each with a distinct visual weight:

**Filled (Primary)**
Solid background, high contrast. The most important action on the page or section. Use once per visual area. Draws the eye immediately.
- Fill: `color-interactive`
- Text: `color-text-on-interactive`
- Border: matches fill (creates unified pill shape)

**Ghost (Secondary)**
Transparent fill, visible border. Subordinate to a primary action. "Learn more" next to "Get started." Same radius and padding as filled — clearly related, clearly secondary.
- Fill: transparent
- Text: `color-interactive`
- Border: `color-interactive`

**Text (Tertiary)**
No fill, no full border — just a bottom underline. Lowest visual weight. Used inline in content, footers, lists. Reads like a link but behaves like a button and maintains a proper hit area.
- Fill: transparent
- Text: `color-interactive-text`
- Border: bottom only, `color-interactive-text`
- Padding: minimal vertical, no horizontal

**Environment variants:**
When a button appears on a surface where the standard colors don't contrast (e.g. a filled interactive-colored band), create environment variant presets that flip the color assignments. Same structure, different color slot references.

---

### Recipe: Cards

A card is a contained content unit with a surface color, padding, and rounded corners. Two approaches depending on content needs:

**Group as card** (preferred for Divi 5)
Use `divi/group` with a Card role preset. Drop inner modules (image, text, button) inside. The group handles the card shell; each inner module uses its own preset.

```
divi/group (Card preset — surface color, radius, padding)
  └── divi/image (optional — full-bleed, no padding)
  └── divi/text (title + body)
  └── divi/button (CTA)
```

The group's internal gap (`space-md`) spaces the inner modules. If the image should bleed to card edges, use negative margin or set image padding to 0 separately.

**Column as card**
Use `divi/column` with a Card role preset. Same approach — column is the shell, inner modules are independent. Better for loop-based content where Divi iterates over columns.

**Card design decisions:**
- Surface color: `color-surface` (one step from ground, visible but not jarring)
- Radius: `radius-lg` (consistent with panels and CTA bands)
- Padding: `space-md` (internal breathing room)
- Card gap (between cards): `space-xl` on the parent row (wider than card padding)

---

### Recipe: Hero section

A hero is a full-width section with a large headline, supporting body copy, and usually a CTA. The visual treatment depends on whether there's a background image.

**Text-only hero:**
```
divi/section (full-width, generous vertical padding — space-2xl)
  └── divi/row
        └── divi/column
              └── divi/text (Hero role — large body, tight leading)
              └── divi/button (Primary)
```

**Image-background hero:**
The section gets a background image set directly (not through a preset — through the builder). A scrim color (`color-surface-scrim`) provides contrast for text. All text uses the light/inverted color treatment regardless of environment.

---

### Recipe: CTA band

A full-width section with a distinct background color, centered content, and a prominent button. The section background IS the design statement.

```
divi/section (Surface or interactive color background, space-xl padding)
  └── divi/row
        └── divi/column
              └── divi/text (Key Statement role)
              └── divi/button (environment-appropriate variant)
```

The section preset handles the background. The text and button presets handle the content. No special CTA-specific module needed — composition carries the design.

---

### Recipe: Feature section (icon + title + body)

A grid of feature items, each with an icon, headline, and description. Use `divi/group` per feature item.

```
divi/section
  └── divi/row (3 or 4 column grid)
        └── divi/group (Feature Card — minimal padding, no background)
              └── divi/icon
              └── divi/text (title h3/h4 + body)
```

Feature cards often don't need a surface color — the icon provides the visual anchor. Padding creates breathing room. The row gap creates separation between features.

---

### Recipe: Dark vs. light — same layout, different environment

The power of semantic color slots: the exact same preset YAML renders correctly in both environments because the variable values differ, not the preset paths.

**What changes between environments:**
- Semantic color slot assignments in the brand YAML
- Nothing in the presets

**What stays the same:**
- All preset paths
- All `$color()` references
- All `var(--gvid-*)` references
- The boilerplate

When building a two-brand or two-environment system, write presets once against the semantic slots. The environment is a color decision, not a preset decision.

---

### Recipe: Composition principles

**Presets style; content is separate.** A preset sets decoration (color, size, spacing, radius). It never sets text content, image sources, or structural choices. Those live in the builder.

**Inner elements need their own presets.** A card preset styles the card shell. The text module inside still needs a text preset. The button inside still needs a button preset. Presets don't cascade into children.

**The gap hierarchy creates rhythm.** Section gaps are wider than row gaps, which are wider than column/group internal gaps. This spatial hierarchy communicates content structure without explicit dividers.

**Variables are the real design system.** Presets are just wiring. Changing `space-base` from 1rem to 1.25rem resets the entire spatial rhythm. Changing `type-scale` changes the heading hierarchy. The presets don't change — the math does.
