# Phase 3: Generate Brand YAML

Translate confirmed Phase 2 decisions into brand YAML. Every value must be traceable to a confirmed decision. Do not invent values.

See [YAML-SPEC-FORMAT.md](YAML-SPEC-FORMAT.md) for the complete format reference.

---

## YAML Structure — Required Order

```yaml
name: "Brand Name"
id_namespace: "brand-slug"
boilerplate: "path/to/boilerplate.json"

overrides:
  # only values that differ from boilerplate defaults

fonts:
  heading: "Font Name"
  body:    "Font Name"

palette_css: "palette.css"  # if palette file provided

system_colors:
  # Divi's 5 fixed slots

colors:
  # all 20 boilerplate semantic slots

presets:
  # role presets from confirmed decisions
```

**The `boilerplate:` key is required.** Path is relative to the YAML file location.

---

## Section: overrides

Only include values that differ from boilerplate defaults. Do not repeat defaults.

All overrideable variables with their defaults:

| Key | Default | What it controls |
|-----|---------|-----------------|
| `type-base` | `1rem` | Root type size |
| `type-scale` | `1.333` | Desktop heading ratio |
| `type-scale-mobile` | `1.200` | Mobile heading ratio |
| `leading-display` | `0.91em` | Line height for display headings |
| `leading-body` | `1.65em` | Line height for body copy |
| `leading-tight` | `1.1em` | Line height for UI labels |
| `tracking-tight` | `-0.04em` | Letter spacing for large display text |
| `tracking-normal` | `0em` | Default letter spacing |
| `tracking-wide` | `0.13em` | Letter spacing for eyebrows, labels |
| `weight-heading` | `800` | Font weight for headings |
| `weight-body` | `400` | Font weight for body copy |
| `weight-emphasis` | `600` | Font weight for buttons, eyebrows |
| `space-base` | `1rem` | Root spacing unit |
| `space-scale` | `1.333` | Spacing ratio |
| `container-max` | `1200px` | Content max-width |

If the designer confirmed different values in Phase 2, put them here. If they confirmed the defaults, omit this section entirely.

```yaml
overrides:
  type-scale:    1.250       # only if different from 1.333
  weight-heading: 700        # only if different from 800
  space-base:    "1.125rem"  # only if different from 1rem
  container-max: "1440px"    # only if different from 1200px
```

---

## Section: colors

All 20 boilerplate semantic slots must be assigned. Use `{ ref: "palette-name" }` when the value exists in palette CSS — never duplicate hex values.

```yaml
colors:
  # Environment
  color-ground:        { ref: "shoreline-800" }
  color-surface:       { ref: "shoreline-700" }
  color-surface-alt:   { ref: "shoreline-600" }
  color-border:        { ref: "shoreline-600" }
  color-surface-scrim: { ref: "shoreline-900" }

  # Text
  color-text-primary:        { ref: "shoreline-100" }
  color-text-secondary:      { ref: "shoreline-300" }
  color-text-dim:            { ref: "shoreline-500" }
  color-text-on-interactive: { ref: "shoreline-800" }

  # Interactive
  color-interactive:              { ref: "neon-carrot-400" }
  color-interactive-hover:        { ref: "neon-carrot-500" }
  color-interactive-text:         { ref: "neon-carrot-400" }
  color-interactive-text-hover:   { ref: "neon-carrot-500" }

  # Functional
  color-error:         { ref: "error-500" }
  color-error-hover:   { ref: "error-600" }
  color-success:       { ref: "success-500" }
  color-success-hover: { ref: "success-600" }
  color-info:          { ref: "info-500" }
  color-info-hover:    { ref: "info-600" }
  color-warning:       { ref: "neon-carrot-400" }
```

---

## Section: presets

### Variable syntax — no exceptions

**Colors:**
```yaml
button.decoration.background.desktop.value.color: "$color(color-interactive)"
```

**Numbers/dimensions:**
```yaml
button.decoration.border.desktop.value.radius.topLeft: "var(--gvid-radius-pill)"
button.decoration.font.font.desktop.value.weight: "var(--gvid-weight-emphasis)"
module.decoration.spacing.desktop.value.padding.top: "var(--gvid-space-sm)"
```

**Never use `$var()` for number variables.** It is broken in the current Divi version.

**Literal values:**
```yaml
button.decoration.button.desktop.value.enable: "on"
button.decoration.border.desktop.value.styles.all.width: "2px"
```

---

### Typography presets (divi/text)

**Preset merge behavior:** the generator merges brand presets with the boilerplate by name. If you define a `divi/text "Body"` preset, your attrs are sparse-merged into the boilerplate's Body preset — your values win on any attr you specify, boilerplate attrs you don't mention are preserved. You only need to write the attrs that differ from the boilerplate.

The boilerplate Body preset sets the full h1–h6 scale wired to `gvid-` variables, with `tracking-tight` on h1. To extend it — for example, adding `tracking-tight` on h2 — just specify that one attr:

```yaml
divi/text:
  - name: "Body"
    attrs:
      # Only the attrs that differ from or add to the boilerplate Body preset.
      # The full h1–h6 scale is already wired by the boilerplate.
      content.decoration.headingFont.h2.font.desktop.value.letterSpacing: "var(--gvid-tracking-tight)"
```

For additional role presets (Eyebrow, Key Statement, Lede, etc.) — these are new names, so the full heading scale is required since there's no boilerplate base to merge into:

```yaml
  - name: "Eyebrow"
    attrs:
      content.decoration.bodyFont.body.font.desktop.value.size: "var(--gvid-type-sm)"
      content.decoration.bodyFont.body.font.desktop.value.weight: "var(--gvid-weight-emphasis)"
      content.decoration.bodyFont.body.font.desktop.value.letterSpacing: "var(--gvid-tracking-wide)"
      content.decoration.headingFont.h1.font.desktop.value.size: "var(--gvid-type-d-h1)"
      content.decoration.headingFont.h1.font.desktop.value.lineHeight: "var(--gvid-leading-display)"
      content.decoration.headingFont.h1.font.desktop.value.weight: "var(--gvid-weight-heading)"
      content.decoration.headingFont.h1.font.desktop.value.letterSpacing: "var(--gvid-tracking-tight)"
      # ... h2–h6 ...
```

The same merge logic applies to `divi/button`, `divi/image`, and `divi/menu`. Empty boilerplate placeholder presets (Button, Image, Menu, etc.) are removed from output automatically — they carry no wiring. If you define a brand preset with the same name, the merge replaces the empty placeholder cleanly.

---

### Button presets (divi/button)

**`button.decoration.button.desktop.value.enable: "on"` is required in every button preset.**

Each button preset is self-contained — no stacking, no group presets. Variables provide shared values.

```yaml
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
```

For Ghost and Text variants — same structure, different color and border treatment. Include `enable: "on"` in each. Example Ghost variant (transparent fill, same structure):

```yaml
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

The pattern: same structure variables (`radius-pill`, `space-sm`, `space-lg`, `weight-emphasis`), different color references. The Text variant uses no fill, bottom border only, `color-interactive-text` instead of `color-interactive`, and minimal padding.

---

### Card presets (divi/group or divi/column)

```yaml
divi/group:
  - name: "Card"
    attrs:
      module.decoration.background.desktop.value.color: "$color(color-surface)"
      module.decoration.border.desktop.value.radius.topLeft: "var(--gvid-radius-lg)"
      module.decoration.border.desktop.value.radius.topRight: "var(--gvid-radius-lg)"
      module.decoration.border.desktop.value.radius.bottomLeft: "var(--gvid-radius-lg)"
      module.decoration.border.desktop.value.radius.bottomRight: "var(--gvid-radius-lg)"
      module.decoration.border.desktop.value.radius.sync: "true"
      module.decoration.spacing.desktop.value.padding.top: "var(--gvid-space-md)"
      module.decoration.spacing.desktop.value.padding.right: "var(--gvid-space-md)"
      module.decoration.spacing.desktop.value.padding.bottom: "var(--gvid-space-md)"
      module.decoration.spacing.desktop.value.padding.left: "var(--gvid-space-md)"
```

---

### Image presets (divi/image)

For rounded images — use `var()` directly, not `$var()`. Include border width `0px` to prevent Divi showing a default border control.

```yaml
divi/image:
  - name: "Rounded"
    attrs:
      image.decoration.border.desktop.value.radius.topLeft: "var(--gvid-radius-lg)"
      image.decoration.border.desktop.value.radius.topRight: "var(--gvid-radius-lg)"
      image.decoration.border.desktop.value.radius.bottomLeft: "var(--gvid-radius-lg)"
      image.decoration.border.desktop.value.radius.bottomRight: "var(--gvid-radius-lg)"
      image.decoration.border.desktop.value.radius.sync: "true"
      image.decoration.border.desktop.value.styles.all.width: "0px"
```

---

## Before Presenting the YAML

Verify:
1. `boilerplate:` key is present with correct relative path
2. All 20 semantic color slots are assigned in `colors:`
3. Every `divi/button` preset has `enable: "on"`
4. No `$var()` references — only `var(--gvid-xxx)` and `$color()`
5. Every `divi/text` preset includes the full h1–h6 heading scale
6. Paths checked against `divi-module-reference.json` for any custom presets

Present the complete YAML to the user. **STOP.** Do not generate JSON until explicitly approved.
