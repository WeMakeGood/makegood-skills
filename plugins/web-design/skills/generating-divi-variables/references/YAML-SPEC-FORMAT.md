# YAML Spec Format

The brand YAML is the design layer that sits on top of the boilerplate. It supplies brand-specific values — colors, fonts, scale choices — and adds role presets on top of the boilerplate's primitive presets.

The generator loads `boilerplate.json` first, then applies the brand YAML as overrides and additions. The output is a complete Divi import JSON.

---

## Required Fields

```yaml
name: "Brand Name"        # Human-readable name, used in generator output
boilerplate: "../path/to/boilerplate.json"  # Path relative to this YAML file
```

## Optional Fields

```yaml
id_namespace: "brand"     # Slug for stable color ID generation. Defaults to slugified name.
```

---

## Sections

### overrides

Patches specific boilerplate variable values by label. Use this to set scale ratios, container width, and any other adjustable variable that differs from the boilerplate default.

```yaml
overrides:
  type-scale:        1.333   # Desktop type ratio (default: 1.333)
  type-scale-mobile: 1.200   # Mobile type ratio (default: 1.200)
  space-scale:       1.333   # Spacing ratio (default: 1.333)
  container-max:     "1440px"
```

Available adjustable variables (see `DIVI-SPEC.md` for full list):

| Label | Default | What it controls |
|-------|---------|-----------------|
| `type-base` | 1rem | Root type size |
| `type-scale` | 1.333 | Desktop heading ratio |
| `type-scale-mobile` | 1.200 | Mobile heading ratio |
| `space-base` | 1rem | Root spacing unit |
| `space-scale` | 1.333 | Spacing step ratio |
| `container-max` | 1200px | Content max-width |
| `weight-heading` | 800 | Heading font weight |
| `weight-body` | 400 | Body font weight |
| `weight-emphasis` | 600 | Button/eyebrow weight |
| `radius-pill` | 999px | Full-round radius |
| `radius-lg` | 1rem | Card/panel radius |
| `radius-md` | 0.5rem | Small element radius |
| `radius-sm` | 4px | Input radius |

---

### fonts

Sets the global heading and body fonts. These map to Divi's fixed system font slots.

```yaml
fonts:
  heading: "Inter Tight"
  body:    "Inter"
```

Custom font variables (for use in presets):
```yaml
fonts:
  heading: "Inter Tight"
  body:    "Inter"
  custom:
    display: "Playfair Display"   # Available as var(--gvid-font-display) in presets
```

---

### palette_css

Path to a CSS file containing custom properties to bulk-import as colors. Path is relative to the YAML file.

```yaml
palette_css: "palette.css"
```

The generator extracts `--name: #hex` patterns. These become available as `$color(name)` references in presets and as `{ ref: "name" }` values in color assignments.

---

### system_colors

Assigns values to Divi's 5 fixed global color slots. These appear in the Divi color palette UI.

```yaml
system_colors:
  primary:   { ref: "neon-carrot-400" }   # ref to palette_css name
  secondary: { ref: "neon-carrot-600" }
  heading:   { ref: "shoreline-100" }
  body:      { ref: "shoreline-300" }
  link:      { ref: "neon-carrot-400" }
  # OR direct hex values:
  # primary: "#4a90d9"
```

Keys must be exactly: `primary`, `secondary`, `heading`, `body`, `link`.

---

### colors

Assigns values to the boilerplate's semantic color slots. This is how palette stops become design decisions.

```yaml
colors:
  color-ground:                 { ref: "shoreline-800" }
  color-surface:                { ref: "shoreline-700" }
  color-surface-alt:            { ref: "shoreline-600" }
  color-border:                 { ref: "shoreline-600" }
  color-text-primary:           { ref: "shoreline-100" }
  color-text-secondary:         { ref: "shoreline-300" }
  color-text-dim:               { ref: "shoreline-500" }
  color-text-on-interactive:    { ref: "shoreline-800" }
  color-interactive:            { ref: "shoreline-100" }
  color-interactive-hover:      { ref: "shoreline-300" }
  color-interactive-text:       { ref: "neon-carrot-400" }
  color-interactive-text-hover: { ref: "neon-carrot-500" }
  color-error:                  { ref: "error-500" }
  color-error-hover:            { ref: "error-600" }
  color-success:                { ref: "success-500" }
  color-success-hover:          { ref: "success-600" }
  color-info:                   { ref: "info-500" }
  color-info-hover:             { ref: "info-600" }
  color-warning:                { ref: "neon-carrot-400" }
  color-surface-scrim:          { ref: "shoreline-900" }
```

Values can be hex strings or `{ ref: "palette-name" }` references to palette CSS names.

Additional brand-specific colors beyond the boilerplate slots can also be added here:
```yaml
colors:
  brand-orange: "#ff9e3d"   # New color not in boilerplate
```

---

### numbers

Brand-specific number variables that extend the boilerplate. Use sparingly — the boilerplate's spacing scale covers most needs automatically.

```yaml
numbers:
  card-gap-tight: "var(--gvid-space-sm)"   # Custom spacing alias
  nav-height:     "64px"
```

The `$ref()` shorthand is available inside number values:
```yaml
numbers:
  sidebar-width: "calc($ref(container-max) * 0.3)"
  # → "calc(var(--gvid-container-max) * 0.3)"
```

---

### strings

Text variables for frequently repeated content.

```yaml
strings:
  tagline: "Building nonprofit capacity"
```

---

### links

URL variables for social media and frequently-used links.

```yaml
links:
  facebook:  "https://www.facebook.com/example"
  instagram: "https://www.instagram.com/example"
```

---

### presets

Role presets that layer on top of the boilerplate's primitive presets. The boilerplate primitives are always preserved — brand presets are added alongside them.

```yaml
presets:
  divi/text:
    - name: "Body"
      default: true
      attrs:
        content.decoration.bodyFont.body.font.desktop.value.size: "var(--gvid-type-body)"
        content.decoration.bodyFont.body.font.desktop.value.lineHeight: "var(--gvid-leading-body)"
        content.decoration.bodyFont.body.font.desktop.value.weight: "var(--gvid-weight-body)"
        content.decoration.headingFont.h1.font.desktop.value.size: "var(--gvid-type-d-h1)"
        content.decoration.headingFont.h1.font.desktop.value.lineHeight: "var(--gvid-leading-display)"
        content.decoration.headingFont.h1.font.desktop.value.weight: "var(--gvid-weight-heading)"
```

#### Variable reference syntax in preset attrs

**Colors** — use `$color(name)`:
```yaml
button.decoration.background.desktop.value.color: "$color(color-interactive)"
```

**Numbers/dimensions** — use `var(--gvid-xxx)` directly:
```yaml
button.decoration.border.desktop.value.radius.topLeft: "var(--gvid-radius-pill)"
button.decoration.font.font.desktop.value.weight: "var(--gvid-weight-emphasis)"
```

**Do not use `$var()`** — this syntax is broken in the current Divi version. Always use direct CSS `var(--gvid-xxx)` for number variables.

**Literal values** — written as-is:
```yaml
button.decoration.border.desktop.value.styles.all.width: "2px"
button.decoration.button.desktop.value.enable: "on"
```

#### Multiple presets per module

```yaml
presets:
  divi/button:
    - name: "Primary"
      default: true
      attrs:
        button.decoration.button.desktop.value.enable: "on"
        # ...

    - name: "Ghost"
      attrs:
        button.decoration.button.desktop.value.enable: "on"
        # ...
```

---

## Complete Example

The palette names below (`brand-blue-500`, `neutral-900`, etc.) are illustrative. Replace with names from your actual `palette.css` file — using names that don't exist in your palette will cause generator errors.

```yaml
name: "Acme Corp"
id_namespace: "acme"
boilerplate: "../../boilerplate.json"

# ── Scale overrides ───────────────────────────────────────────────────────────
overrides:
  type-scale:    1.250   # Major third — balanced hierarchy
  space-scale:   1.250
  container-max: "1280px"

# ── Fonts ─────────────────────────────────────────────────────────────────────
fonts:
  heading: "Playfair Display"
  body:    "Source Sans Pro"

# ── Palette ───────────────────────────────────────────────────────────────────
palette_css: "palette.css"

# ── Divi system slots ─────────────────────────────────────────────────────────
system_colors:
  primary:   { ref: "brand-blue-500" }
  secondary: { ref: "brand-blue-700" }
  heading:   { ref: "neutral-900" }
  body:      { ref: "neutral-700" }
  link:      { ref: "brand-blue-500" }

# ── Semantic color assignments ────────────────────────────────────────────────
colors:
  color-ground:              { ref: "neutral-50" }
  color-surface:             { ref: "neutral-100" }
  color-surface-alt:         { ref: "neutral-200" }
  color-border:              { ref: "neutral-300" }
  color-text-primary:        { ref: "neutral-900" }
  color-text-secondary:      { ref: "neutral-600" }
  color-text-dim:            { ref: "neutral-400" }
  color-text-on-interactive: "#ffffff"
  color-interactive:         { ref: "brand-blue-500" }
  color-interactive-hover:   { ref: "brand-blue-700" }
  color-interactive-text:    { ref: "brand-blue-500" }
  color-interactive-text-hover: { ref: "brand-blue-700" }
  color-error:               { ref: "error-500" }
  color-error-hover:         { ref: "error-600" }
  color-success:             { ref: "success-500" }
  color-success-hover:       { ref: "success-600" }
  color-info:                { ref: "info-500" }
  color-info-hover:          { ref: "info-600" }
  color-warning:             { ref: "warning-500" }
  color-surface-scrim:       "rgba(0,0,0,0.6)"

# ── Role presets ──────────────────────────────────────────────────────────────
presets:

  divi/text:
    - name: "Body"
      default: true
      attrs:
        content.decoration.bodyFont.body.font.desktop.value.size: "var(--gvid-type-body)"
        content.decoration.bodyFont.body.font.desktop.value.lineHeight: "var(--gvid-leading-body)"
        content.decoration.bodyFont.body.font.desktop.value.weight: "var(--gvid-weight-body)"
        content.decoration.headingFont.h1.font.desktop.value.size: "var(--gvid-type-d-h1)"
        content.decoration.headingFont.h1.font.desktop.value.lineHeight: "var(--gvid-leading-display)"
        content.decoration.headingFont.h1.font.desktop.value.weight: "var(--gvid-weight-heading)"
        content.decoration.headingFont.h1.font.desktop.value.letterSpacing: "var(--gvid-tracking-tight)"
        content.decoration.headingFont.h2.font.desktop.value.size: "var(--gvid-type-d-h2)"
        content.decoration.headingFont.h2.font.desktop.value.lineHeight: "var(--gvid-leading-display)"
        content.decoration.headingFont.h2.font.desktop.value.weight: "var(--gvid-weight-heading)"
        content.decoration.headingFont.h3.font.desktop.value.size: "var(--gvid-type-d-h3)"
        content.decoration.headingFont.h3.font.desktop.value.lineHeight: "var(--gvid-leading-display)"
        content.decoration.headingFont.h3.font.desktop.value.weight: "var(--gvid-weight-heading)"
        content.decoration.headingFont.h4.font.desktop.value.size: "var(--gvid-type-d-h4)"
        content.decoration.headingFont.h4.font.desktop.value.lineHeight: "var(--gvid-leading-display)"
        content.decoration.headingFont.h4.font.desktop.value.weight: "var(--gvid-weight-heading)"
        content.decoration.headingFont.h5.font.desktop.value.size: "var(--gvid-type-d-h5)"
        content.decoration.headingFont.h5.font.desktop.value.lineHeight: "var(--gvid-leading-display)"
        content.decoration.headingFont.h5.font.desktop.value.weight: "var(--gvid-weight-heading)"
        content.decoration.headingFont.h6.font.desktop.value.size: "var(--gvid-type-d-h6)"
        content.decoration.headingFont.h6.font.desktop.value.lineHeight: "var(--gvid-leading-display)"
        content.decoration.headingFont.h6.font.desktop.value.weight: "var(--gvid-weight-heading)"

  divi/button:
    - name: "Primary"
      default: true
      attrs:
        button.decoration.button.desktop.value.enable: "on"
        button.decoration.button.desktop.value.icon.enable: "off"
        button.decoration.font.font.desktop.value.size: "var(--gvid-type-sm)"
        button.decoration.font.font.desktop.value.weight: "var(--gvid-weight-emphasis)"
        button.decoration.font.font.desktop.value.letterSpacing: "var(--gvid-tracking-wide)"
        button.decoration.background.desktop.value.color: "$color(color-interactive)"
        button.decoration.font.font.desktop.value.color: "$color(color-text-on-interactive)"
        button.decoration.border.desktop.value.styles.all.color: "$color(color-interactive)"
        button.decoration.border.desktop.value.styles.all.width: "2px"
        button.decoration.border.desktop.value.styles.all.style: "solid"
        button.decoration.border.desktop.value.radius.topLeft: "var(--gvid-radius-pill)"
        button.decoration.border.desktop.value.radius.topRight: "var(--gvid-radius-pill)"
        button.decoration.border.desktop.value.radius.bottomLeft: "var(--gvid-radius-pill)"
        button.decoration.border.desktop.value.radius.bottomRight: "var(--gvid-radius-pill)"
        button.decoration.border.desktop.value.radius.sync: "true"
        module.decoration.spacing.desktop.value.padding.top: "var(--gvid-space-sm)"
        module.decoration.spacing.desktop.value.padding.right: "var(--gvid-space-lg)"
        module.decoration.spacing.desktop.value.padding.bottom: "var(--gvid-space-sm)"
        module.decoration.spacing.desktop.value.padding.left: "var(--gvid-space-lg)"

    - name: "Ghost"
      attrs:
        button.decoration.button.desktop.value.enable: "on"
        button.decoration.button.desktop.value.icon.enable: "off"
        button.decoration.font.font.desktop.value.size: "var(--gvid-type-sm)"
        button.decoration.font.font.desktop.value.weight: "var(--gvid-weight-emphasis)"
        button.decoration.font.font.desktop.value.letterSpacing: "var(--gvid-tracking-wide)"
        button.decoration.background.desktop.value.color: "rgba(0,0,0,0)"
        button.decoration.font.font.desktop.value.color: "$color(color-interactive)"
        button.decoration.border.desktop.value.styles.all.color: "$color(color-interactive)"
        button.decoration.border.desktop.value.styles.all.width: "2px"
        button.decoration.border.desktop.value.styles.all.style: "solid"
        button.decoration.border.desktop.value.radius.topLeft: "var(--gvid-radius-pill)"
        button.decoration.border.desktop.value.radius.topRight: "var(--gvid-radius-pill)"
        button.decoration.border.desktop.value.radius.bottomLeft: "var(--gvid-radius-pill)"
        button.decoration.border.desktop.value.radius.bottomRight: "var(--gvid-radius-pill)"
        button.decoration.border.desktop.value.radius.sync: "true"
        module.decoration.spacing.desktop.value.padding.top: "var(--gvid-space-sm)"
        module.decoration.spacing.desktop.value.padding.right: "var(--gvid-space-lg)"
        module.decoration.spacing.desktop.value.padding.bottom: "var(--gvid-space-sm)"
        module.decoration.spacing.desktop.value.padding.left: "var(--gvid-space-lg)"
```

---

## File Reference

| File | Purpose |
|------|---------|
| `boilerplate.json` | Base variable system and primitive presets — loads before brand YAML |
| `DIVI-SPEC.md` | Technical rules, bugs, exact path patterns, import constraints |
| `PRESET-COOKBOOK.md` | Design recipes — how to compose primitives into design patterns |
| `divi-module-reference.json` | Complete module element and path reference |
| `generate_divi_variables.py` | Generator — brand YAML + boilerplate → Divi import JSON |
