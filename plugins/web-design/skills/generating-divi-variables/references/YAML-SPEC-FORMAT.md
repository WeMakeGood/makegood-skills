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

### numbers

Numeric/measurement variables. Values are strings (CSS values).

```yaml
numbers:
  type-body: "1rem"
  leading-body: "1.65em"
  type-d-xl: "clamp(3.157rem, 7vw, 5.61rem)"
  type-d-lg: "clamp(2.369rem, 5.25vw, 4.209rem)"
  type-d-md: "clamp(1.777rem, 4vw, 3.157rem)"
  type-d-sm: "clamp(1.333rem, 3vw, 2.369rem)"
  type-d-xs: "1.777rem"
  leading-display: "0.91em"
  border-radius: "1rem"
  spacing-sm: "0.5rem"
  spacing-md: "1rem"
  spacing-lg: "2rem"
```

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
