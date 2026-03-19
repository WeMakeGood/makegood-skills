# YAML Spec Format

The YAML spec is the source of truth for a Divi design system. The generator reads this file and produces the Divi-compatible JSON import.

## Required Fields

```yaml
name: "Brand Name"        # Human-readable name, used in generator output
```

## Optional Fields

```yaml
id_namespace: "brand"      # Slug for stable ID generation. Defaults to slugified name.
```

## Sections

### system_colors

The 5 built-in Divi color slots. Keys must be exactly: `primary`, `secondary`, `heading`, `body`, `link`.

```yaml
system_colors:
  primary: "#ff9e3d"
  secondary: "#d47b10"
  heading: "#f6f6f1"
  body: "#d5d4c1"
  link: "#ff9e3d"
```

### colors

Custom colors beyond the 5 system slots. Can be hex values or references to other colors.

```yaml
colors:
  accent: "#e74c3c"
  accent-ref:
    ref: "primary"    # Creates a $variable() reference to the primary color
```

### fonts

System fonts (heading/body) and custom fonts.

```yaml
fonts:
  heading: "Inter Tight"   # Sets --et_global_heading_font
  body: "Inter"             # Sets --et_global_body_font
  custom:
    display: "Playfair Display"   # Creates a gvid- font variable
```

### type_scale

Optional. Generates fluid heading size variables from a modular scale — no hardcoded rem values needed. The generator computes desktop sizes, derives mobile sizes from a smaller ratio, and produces `clamp()` values with a vw midpoint calibrated to hit the desktop max at `viewport_max`.

```yaml
type_scale:
  scale: "perfect-fourth"   # scale name or ratio (e.g. 1.333)
  base: "1rem"              # base size — default: "1rem"
  steps: 6                  # heading levels to generate (h1–h6) — default: 6
  mobile_steps_down: 2      # positions down the scale list for mobile ratio — default: 2
  viewport_max: 1200        # px — desktop breakpoint where max size is reached — default: 1200
  prefix: "type-d"          # variable name prefix — default: "type-d"
```

Available scale names (ordered smallest to largest):

| Name | Ratio |
|------|-------|
| `minor-second` | 1.067 |
| `major-second` | 1.125 |
| `minor-third` | 1.200 |
| `major-third` | 1.250 |
| `perfect-fourth` | 1.333 |
| `augmented-fourth` | 1.414 |
| `perfect-fifth` | 1.500 |
| `golden-ratio` | 1.618 |

`mobile_steps_down: 2` with `perfect-fourth` (position 4) uses `minor-third` (position 2) for mobile — two steps smaller, same harmonic system.

**Generated variables** (with `prefix: "type-d"`, `steps: 6`):

```
type-scale-base: "1rem"
type-d-h1: "clamp(2.986rem, 7.48vw, 5.61rem)"
type-d-h2: "clamp(2.488rem, 5.61vw, 4.209rem)"
type-d-h3: "clamp(2.074rem, 4.21vw, 3.157rem)"
type-d-h4: "clamp(1.728rem, 3.16vw, 2.369rem)"
type-d-h5: "clamp(1.44rem, 2.37vw, 1.777rem)"
type-d-h6: "clamp(1.2rem, 1.78vw, 1.333rem)"
```

These become available as `$var(type-d-h1)` etc. in preset attrs. Any generated token can be overridden by defining the same key in `numbers`.

### numbers

Numeric/measurement variables. Values are strings (CSS values).

```yaml
numbers:
  type-body: "1rem"
  leading-body: "1.65em"
  type-d-xl: "clamp(3.157rem, 7vw, 5.61rem)"
  border-radius: "1rem"
  spacing-sm: "0.5rem"
  spacing-md: "1rem"
```

#### $ref() — derived variables

Inside any number value, `$ref(name)` expands to `var(--gvid-xxx)`, where `name` is another key in the `numbers` section. This lets you define base tokens once and derive everything else with `calc()`.

```yaml
numbers:
  # Base tokens — the only values you hand-tune
  base-size:    "1rem"
  section-unit: "32px"

  # Type scale derived from base-size (Perfect Fourth, ratio 1.333)
  type-h5: "calc($ref(base-size) * 1.333)"
  type-h4: "calc($ref(base-size) * 1.777)"
  type-h3: "calc($ref(base-size) * 2.369)"
  type-h2: "calc($ref(base-size) * 3.157)"
  type-h1: "calc($ref(base-size) * 4.209)"

  # Fluid display sizes — clamp between two derived stops
  type-d-sm: "clamp($ref(type-h5), 3vw, $ref(type-h3))"
  type-d-xl: "clamp($ref(type-h2), 7vw, calc($ref(base-size) * 5.61))"

  # Spacing derived from section-unit
  section-xs: "$ref(section-unit)"
  section-sm: "calc($ref(section-unit) * 1.75)"
  section-md: "calc($ref(section-unit) * 3)"
  section-xl: "calc($ref(section-unit) * 4)"
```

The generator resolves each `$ref()` to the corresponding `var(--gvid-xxx)` CSS custom property before writing the variable value. Divi resolves the chain at render time — changing `base-size` updates every derived token automatically.

`$ref()` names must exist in the `numbers` section. The generator validates this and exits with an error if any reference is undefined.

### strings

Text variables.

```yaml
strings:
  tagline: "We Make Good"
```

### links

URL variables.

```yaml
links:
  facebook: "https://www.facebook.com/example"
  instagram: "https://www.instagram.com/example"
```

### palette_css

Optional path to a CSS file containing custom properties to bulk-import as colors. Path is relative to the YAML spec file.

```yaml
palette_css: "../Design/palette.css"
```

The generator extracts `--name: #hex` patterns from the CSS file. Colors defined in the `colors` section take precedence over palette CSS entries with the same name.

### presets

Module presets using dot-path attribute notation. Each key under `presets` is a Divi module name (e.g., `divi/text`).

```yaml
presets:
  divi/text:
    name: "Brand Text"
    default: true          # Mark as the default preset for this module
    attrs:
      content.decoration.bodyFont.body.font.desktop.value.size: "$var(type-body)"
      content.decoration.bodyFont.body.font.desktop.value.lineHeight: "$var(leading-body)"
      content.decoration.headingFont.h1.font.desktop.value.size: "$var(type-d-xl)"
      content.decoration.headingFont.h1.font.desktop.value.lineHeight: "$var(leading-display)"
```

#### Variable Reference Shorthand

In preset `attrs` values:

- `$var(name)` — References a number, string, font, or link variable. Resolves to `$variable({"type":"content","value":{"name":"gvid-xxx",...}})$`
- `$color(name)` — References a color (system or custom). Resolves to `$variable({"type":"color","value":{"name":"gcid-xxx",...}})$`

The `name` in `$var()` or `$color()` must match a key defined in the corresponding section of the spec.

#### Multiple Presets Per Module

Use a list instead of a single dict:

```yaml
presets:
  divi/text:
    - name: "Body Text"
      default: true
      attrs:
        content.decoration.bodyFont.body.font.desktop.value.size: "$var(type-body)"
    - name: "Display Text"
      attrs:
        content.decoration.bodyFont.body.font.desktop.value.size: "$var(type-d-md)"
```

## Complete Example

See [spec-test.yaml](spec-test.yaml) for a working example with system colors, fonts, a type scale, and a text module preset.
