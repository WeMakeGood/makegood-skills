# Divi 5 Technical Specification

Hard rules, confirmed bugs, and structural requirements for generating correct Divi 5 import files. These are empirically verified — not guesses or inferences from documentation.

The cookbook references this document for technical constraints. The generator enforces most of these automatically, but the skill must understand them to write correct YAML and diagnose import failures.

---

## Boilerplate Structure

`boilerplate.json` is the static base file that ships with the skill. It contains the complete variable system and primitive preset wiring. A brand YAML loads it and patches brand-specific values on top.

### How the boilerplate is loaded

In the brand YAML:
```yaml
boilerplate: "../boilerplate.json"  # path relative to the YAML file
```

The generator loads the boilerplate first, then applies brand YAML values as overrides and additions. Boilerplate defaults are used for anything not specified in the brand YAML.

### Global colors

The boilerplate defines 25 semantic color slots with empty values. All must be populated by the brand YAML.

**Divi system slots** (5) — fixed IDs, wired to Divi's global palette:
```
gcid-primary-color       → accent color for links and site-wide UI accents
gcid-secondary-color     → secondary accent (hover states, active elements)
gcid-heading-color       → default heading text color
gcid-body-color          → default body text color
gcid-link-color          → inline link color (often matches primary)
```

**Critical constraint:** System slots are stored in WordPress theme customizer options, not Divi's variable system. They must be **literal hex values** — `$variable()` refs and CSS var() expressions are silently ignored. The generator resolves `ref:` values to hex automatically.

**What primary/secondary mean — and don't mean:**
`primary` and `secondary` are site-wide accent colors for links and UI elements. They are NOT button fill colors. Buttons have their own semantic slots (`color-interactive`, `color-interactive-hover`, `color-text-on-interactive`) which may or may not use the same color as primary.

Example: a dark-environment site might set `primary` to a warm accent for links, while `color-interactive` uses a light neutral for button fills (inverted treatment). These are independent decisions. Do not assume buttons should use the primary color.

**Environment slots** (4) — surface hierarchy:
```
gcid-color-ground        → page background (70-80% of visual field)
gcid-color-surface       → raised surface (cards, panels)
gcid-color-surface-alt   → secondary surface (footer, dividers)
gcid-color-border        → borders and dividers
gcid-color-surface-scrim → dark overlay for image backgrounds
```

**Text slots** (4):
```
gcid-color-text-primary        → primary text (high contrast on ground)
gcid-color-text-secondary      → secondary text (reduced contrast)
gcid-color-text-dim            → placeholder, disabled, captions
gcid-color-text-on-interactive → text on filled interactive elements
```

**Interactive slots** (4):
```
gcid-color-interactive              → primary button fill, links
gcid-color-interactive-hover        → hover state for interactive
gcid-color-interactive-text         → text-only interactive (tertiary buttons)
gcid-color-interactive-text-hover   → hover for text-only interactive
```

**Functional slots** (7):
```
gcid-color-error         → error solid fill
gcid-color-error-hover   → error hover
gcid-color-success       → success solid fill
gcid-color-success-hover → success hover
gcid-color-info          → info solid fill
gcid-color-info-hover    → info hover
gcid-color-warning       → warning (typically same as interactive)
```

### Global variables

**Adjustable variables** — brand YAML should set these (or use boilerplate defaults):

| ID | Default | What it controls |
|----|---------|-----------------|
| `gvid-type-base` | 1rem | Root type size — all heading sizes multiply from this |
| `gvid-type-scale` | 1.333 | Desktop type ratio — determines heading hierarchy spread |
| `gvid-type-scale-mobile` | 1.200 | Mobile type ratio — controls heading compression on small screens |
| `gvid-leading-display` | 0.91em | Line height for display headings |
| `gvid-leading-body` | 1.65em | Line height for body copy |
| `gvid-leading-tight` | 1.1em | Line height for UI labels, subheadings |
| `gvid-tracking-tight` | -0.04em | Letter spacing for large display text |
| `gvid-tracking-normal` | 0em | Default letter spacing |
| `gvid-tracking-wide` | 0.13em | Letter spacing for eyebrows, labels |
| `gvid-weight-heading` | 800 | Font weight for headings |
| `gvid-weight-body` | 400 | Font weight for body copy |
| `gvid-weight-emphasis` | 600 | Font weight for buttons, eyebrows, key statements |
| `gvid-radius-pill` | 999px | Full round — buttons |
| `gvid-radius-lg` | 1rem | Cards, panels, sections |
| `gvid-radius-md` | 0.5rem | Chips, tags, smaller elements |
| `gvid-radius-sm` | 4px | Inputs, tight UI |
| `gvid-space-base` | 1rem | Root spacing unit |
| `gvid-space-scale` | 1.333 | Spacing ratio — matches type scale by default |
| `gvid-container-max` | 1200px | Content max-width |

**Derived variables** — computed automatically, do not set in brand YAML:

| ID | Expression | What it computes |
|----|-----------|-----------------|
| `gvid-type-d-h1` | `clamp(base*scale-mobile^6, vw, base*scale^6)` | H1 fluid size |
| `gvid-type-d-h2` through `h6` | Same pattern, exponents 5 through 1 | H2–H6 fluid sizes |
| `gvid-type-body-lg` | `base * scale` | Large body / lede |
| `gvid-type-body` | `base` | Standard body |
| `gvid-type-sm` | `base * 0.875` | Small UI text |
| `gvid-type-caption` | `base * 0.75` | Caption / fine print |
| `gvid-space-xs` | `base / scale` | Tight spacing |
| `gvid-space-sm` | `base` | Base spacing |
| `gvid-space-md` | `base * scale` | Standard spacing |
| `gvid-space-lg` | `base * scale²` | Generous spacing |
| `gvid-space-xl` | `base * scale³` | Large spacing |
| `gvid-space-2xl` | `base * scale⁴` | Section-scale spacing |
| `gvid-container-padding` | `clamp(space-md, 2vw, space-xl)` | Fluid horizontal padding |

### Primitive presets

The boilerplate ships 11 primitive presets — infrastructure wiring only, no design decisions:

**Grid system** (gap wiring):
- `divi/section` — `columnGap: space-2xl`, `rowGap: space-2xl`
- `divi/row` — `flexWrap: wrap`, `columnGap: space-xl`, `rowGap: space-lg`
- `divi/column` — `columnGap: space-md`, `rowGap: space-md`
- `divi/group` — `columnGap: space-md`, `rowGap: space-md`

**Typography** (scale wiring):
- `divi/text` Body — full h1–h6 scale + body font wired to boilerplate variables
- `divi/post-content` Body — same scale on `module` element

**Empty placeholders** (registered for brand presets to build on):
- `divi/button` Button
- `divi/image` Image
- `divi/icon` Icon
- `divi/divider` Divider
- `divi/menu` Menu

### How brand YAML patches the boilerplate

**`overrides:`** — patches specific variable values by label:
```yaml
overrides:
  type-scale: 1.250       # changes gvid-type-scale value
  space-scale: 1.250      # changes gvid-space-scale value
  container-max: "1440px" # changes gvid-container-max value
```

**`system_colors:`** — patches the 5 fixed Divi color slots:
```yaml
system_colors:
  primary: { ref: "brand-blue-500" }
  heading: { ref: "neutral-900" }
```

**`colors:`** — patches semantic boilerplate color slots by label:
```yaml
colors:
  color-interactive: { ref: "brand-blue-500" }
  color-ground:      { ref: "neutral-900" }
```

**`presets:`** — adds role presets on top of boilerplate primitives. Boilerplate presets are preserved; brand presets are added alongside them.

---

## Import Format

### Colors must go in `global_colors`, not `global_variables`

Divi's `import_global_variables()` silently drops entries with `type: "colors"`. Colors must be in the `global_colors` tuple array. The generator handles this correctly — never put colors in `global_variables` in YAML.

```json
// Correct — global_colors tuple format
["gcid-color-interactive", {"color": "#4a90d9", "status": "active", "label": "color-interactive"}]

// Wrong — silently dropped on import
{"id": "gcid-color-interactive", "type": "colors", "value": "#4a90d9"}
```

### System color slot IDs are fixed

These five IDs are hardcoded in Divi. They cannot be renamed.

| Slot | Fixed ID |
|------|----------|
| Primary | `gcid-primary-color` |
| Secondary | `gcid-secondary-color` |
| Heading text | `gcid-heading-color` |
| Body text | `gcid-body-color` |
| Link | `gcid-link-color` |

### System font IDs are fixed

| Slot | Fixed ID |
|------|----------|
| Heading font | `--et_global_heading_font` |
| Body font | `--et_global_body_font` |

### Semantic variable IDs use `gvid-` prefix

- Colors: `gcid-{semantic-name}` (e.g. `gcid-color-interactive`)
- All other variables: `gvid-{semantic-name}` (e.g. `gvid-type-base`)
- IDs must be lowercase alphanumeric with single hyphens: `[a-z0-9-]`
- No double hyphens, no underscores

### Preset structure requires both `attrs` and `styleAttrs`

Both fields must be present with identical content. Missing `styleAttrs` causes preset styles to not render. The generator duplicates `attrs` into `styleAttrs` automatically.

### `global_colors` uses tuple format

```json
["gcid-xxx", {"color": "#hex", "status": "active", "label": "name"}]
```

`global_variables` uses flat objects. The formats are different — don't mix them.

---

## Variable Reference Syntax

### Two syntaxes — never mix them up

**`$color(name)`** — for colors only.

Used in YAML preset attrs. Resolves to Divi's `$variable({"type":"color",...})$` syntax. Divi's color resolution system handles this correctly.

```yaml
button.decoration.background.desktop.value.color: "$color(color-interactive)"
```

**`var(--gvid-xxx)`** — for all number/dimension variables.

Used in YAML preset attrs. Written as a direct CSS custom property. Divi outputs the variable value verbatim, so the browser resolves the chain at render time.

```yaml
button.decoration.border.desktop.value.radius.topLeft: "var(--gvid-radius-pill)"
button.decoration.font.font.desktop.value.weight: "var(--gvid-weight-emphasis)"
module.decoration.spacing.desktop.value.padding.top: "var(--gvid-space-md)"
```

**`$var(name)` is broken — do not use.**

`$var()` in YAML resolves to Divi's `$variable({"type":"content",...})$` syntax. This system is currently bugged for number variables in preset attrs — values render incorrectly or show as icons/controls in the builder UI instead of resolved values. Always use `var(--gvid-xxx)` directly.

### CSS calc chains in variable values

Number variables can contain CSS calc expressions that reference other variables:

```json
"value": "calc(var(--gvid-space-base) * pow(var(--gvid-space-scale), 2))"
```

The Divi UI shows a spurious "Invalid unit" warning for these. This is a false positive — the expressions resolve correctly in the browser and editor preview. Do not remove `gvid-` prefixes or simplify expressions to silence the warning.

### `$ref()` in YAML numbers section

Inside `numbers:` values in the brand YAML, `$ref(name)` expands to `var(--gvid-xxx)`:

```yaml
numbers:
  card-gap: "calc($ref(space-md) * 0.75)"
  # → "calc(var(--gvid-space-md) * 0.75)"
```

Valid only in the `numbers:` section. Not valid in preset attrs.

---

## Preset Attr Path Structure

All preset attribute paths follow this pattern:

```
{element}.decoration.{group}.{subgroup}.{device}.value.{property}
```

- `element` — the module element (module, content, button, title, image, etc.)
- `decoration` — always present
- `group` — decoration group (font, background, border, spacing, layout, etc.)
- `subgroup` — depends on group (e.g. `font` → `font`, `bodyFont` → `body`, `headingFont` → `h1`)
- `device` — always `desktop` in boilerplate presets (tablet/phone are overrides)
- `value` — always present before property keys
- `property` — the specific CSS property

### Font group variants

| Group | Subgroup path | Used in |
|-------|--------------|---------|
| `font` | `font.font.desktop.value.{prop}` | Most modules — single font control |
| `bodyFont` | `bodyFont.body.font.desktop.value.{prop}` | divi/text, divi/post-content |
| `headingFont` | `headingFont.h1.font.desktop.value.{prop}` | divi/text, divi/post-content only |

Only `divi/text` and `divi/post-content` use `headingFont` with h1–h6 breakdown. Everything else uses `font` as a single control.

### Common path patterns

**Background color:**
```
{element}.decoration.background.desktop.value.color
```

**Border radius (all corners):**
```
{element}.decoration.border.desktop.value.radius.topLeft
{element}.decoration.border.desktop.value.radius.topRight
{element}.decoration.border.desktop.value.radius.bottomLeft
{element}.decoration.border.desktop.value.radius.bottomRight
{element}.decoration.border.desktop.value.radius.sync  → "true"
```

**Border styles:**
```
{element}.decoration.border.desktop.value.styles.all.color
{element}.decoration.border.desktop.value.styles.all.width
{element}.decoration.border.desktop.value.styles.all.style
{element}.decoration.border.desktop.value.styles.bottom.width  (side-specific)
```

**Padding (module element only for buttons):**
```
module.decoration.spacing.desktop.value.padding.top
module.decoration.spacing.desktop.value.padding.right
module.decoration.spacing.desktop.value.padding.bottom
module.decoration.spacing.desktop.value.padding.left
```

**Layout gap:**
```
module.decoration.layout.desktop.value.columnGap
module.decoration.layout.desktop.value.rowGap
```

---

## divi/button — Required Rules

### Enable flag is required in every preset

```yaml
button.decoration.button.desktop.value.enable: "on"
```

Without this, none of the button decoration attrs apply — not background, border, or font color. This must be in every `divi/button` preset individually. It is not inherited from stacked presets.

### Padding goes on `module`, not `button` element

```yaml
# Correct
module.decoration.spacing.desktop.value.padding.top: "var(--gvid-space-sm)"

# Wrong — hidden from UI, locks value, cannot be overridden
button.decoration.spacing.desktop.value.padding.top: "0.5em"
```

`button.decoration.spacing` is hidden from the builder UI. Any value set there is locked with no way for the designer to see or override it.

### Stacking is broken for buttons

Divi's stacked preset system produces CSS cascade conflicts for buttons — padding and decoration from one preset gets overridden by Divi's default hover styles from another. Use self-contained presets where each button preset has all required attrs. Variables provide shared values across presets.

### Group presets are broken for buttons

Same CSS cascade issue as stacking. Avoid group presets for `divi/button` modules entirely.

---

## Divi 5 Layout Defaults

Only set values that differ from these defaults. Setting defaults adds noise and can cause issues if Divi changes default behavior.

| Module | Element | Default values |
|--------|---------|---------------|
| divi/section | module | flexDirection: column, alignItems: center |
| divi/row | module | flexDirection: row, alignItems: stretch |
| divi/column | module | flexDirection: column, alignItems: stretch |
| divi/group | module | flexDirection: column, alignItems: stretch |

The boilerplate only sets `columnGap`, `rowGap`, and `flexWrap` (on row) — all other layout properties inherit Divi's defaults.

---

## Module Element Reference

The authoritative source is `module-reference-v2.json`. This table covers the most commonly preset modules.

### Font group per element

| Module | Element | Font group | Notes |
|--------|---------|-----------|-------|
| divi/text | content | headingFont (h1–h6), bodyFont | Document typography |
| divi/post-content | module | headingFont (h1–h6), bodyFont | Same capability, different element — not compatible with divi/text presets |
| divi/heading | title | font | Single control |
| divi/button | button | font | Single control |
| divi/blurb | title | font | Single control |
| divi/blurb | content | bodyFont | |
| divi/cta | title, button | font | |
| divi/cta | content | bodyFont | |
| divi/menu | menu | font | Nav links |
| divi/menu | menuDropdown | background, font | Dropdown |
| divi/menu | menuMobile | background, font | Mobile nav |
| divi/testimonial | author, position | font | |
| divi/testimonial | body | bodyFont | |

### Image element

`divi/image` styling goes on the `image` element, not `module`:
```
image.decoration.border.desktop.value.radius.topLeft
image.decoration.border.desktop.value.styles.all.width
```

Setting border width to `0px` is required when setting radius — otherwise Divi shows a default border control state.

---

## Import Safety

### Always close the Visual Builder before importing

The Visual Builder's save operation overwrites imports. Every time. Close it completely before using the Portability modal.

### Re-import is safe

The generator produces stable IDs — same input always produces the same `gcid-`/`gvid-` IDs. Re-importing an updated spec overwrites existing variables rather than creating duplicates.

### Inactive color zombie bug

When colors are deleted in the Divi UI, they persist in the database with `"status":"inactive"`. Re-importing should overwrite them to `"active"`, but may fail if the Visual Builder is open during import. If colors appear missing after import, check for inactive duplicates.

### Variable display order

The boilerplate uses 100-span order ranges to keep the Divi variables UI organized:

| Range | Category |
|-------|----------|
| 100–199 | Fonts |
| 200–299 | Type base, scale, mobile scale |
| 300–399 | Leading, tracking |
| 400–499 | Weights |
| 500–599 | Radii |
| 600–699 | Space base, scale, container-max |
| 700–799 | Heading sizes (derived) |
| 800–899 | Body/utility sizes (derived) |
| 900–999 | Spacing steps (derived) |
| 1000+ | Layout derived values |

Brand-added variables should use open slots within the appropriate range. Adjustable variables at the top (100–699), derived calc values at the bottom (700+).
