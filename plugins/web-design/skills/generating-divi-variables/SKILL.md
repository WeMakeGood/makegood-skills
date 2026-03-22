---
name: generating-divi-variables
description: Generates Divi 5-compatible JSON import files from natural language design specifications. Translates brand colors, typography, spacing, and module presets into a YAML spec, then runs a Python generator to produce import-ready JSON with global colors, variables, and presets wired with $variable() references. Use when creating Divi design tokens, building Divi variable systems, generating Divi presets, or setting up a Divi 5 design system. Activates when user mentions Divi variables, Divi presets, Divi design tokens, or Divi import files.
compatibility: Requires Python 3.9+ and PyYAML (pip install pyyaml)
---

# Generating Divi Variables

<purpose>
Divi 5's variable and preset system uses a specific JSON import format with undocumented
constraints (colors must go through global_colors, not global_variables; system IDs are fixed;
presets need both attrs and styleAttrs). This skill exists because getting the format wrong
produces silent failures — variables appear to import but don't work. The skill wraps a
validated Python generator and provides the module reference needed to build correct preset
attribute paths.
</purpose>

## Critical Rules

**GENERATOR AUTHORITY:** All JSON output MUST be produced by running `scripts/generate_divi_variables.py`. Do not generate Divi JSON directly — the generator handles ID generation, `$variable()` syntax, the `global_colors` tuple format, and the `attrs`/`styleAttrs` duplication that Divi requires.

**VALIDATION BEFORE OUTPUT:** Before presenting generated JSON to the user, verify:
1. The generator exited without errors
2. All `$var()` and `$color()` references in the YAML resolve to defined variables
3. The summary counts match expectations

**PROFESSIONAL CHALLENGE:** If the user requests a preset attribute path that doesn't exist in the module reference, flag it rather than guessing. Offer the closest valid path. If they request a color in `global_variables` instead of `global_colors`, explain why it won't work (see [DIVI-SPEC.md](references/DIVI-SPEC.md)).

**IMPORT SAFETY:** Always warn users to close the Visual Builder before importing. Divi's Visual Builder save overwrites imports if both happen simultaneously.

## Quick Start

If the user already has a YAML spec file:

```bash
python3 scripts/generate_divi_variables.py <spec.yaml> -o <output.json>
```

Otherwise, follow the full workflow below.

## Workflow

```
Progress:
- [ ] Phase 1: Gather design intent
- [ ] Phase 2: Generate YAML spec
- [ ] Phase 3: Define presets (optional)
- [ ] Phase 4: Generate and validate
- [ ] Phase 5: Import instructions
```

<phase_gather>
### Phase 1: Gather Design Intent

Ask the user about their design system. Gather what's available — not every category is required.

1. **Brand name** — Used for the spec name and ID namespace
2. **Colors** — Primary, secondary, heading, body, link (system slots). Additional custom colors. Full palette CSS file if available.
3. **Typography** — Heading and body fonts. Type scale approach:
   - **Modular scale (preferred):** Ask for a scale name or ratio. The `type_scale` section generates all heading sizes as fluid `clamp()` values automatically — desktop from the named ratio, mobile from two steps down the scale list. Scales: minor-second (1.067), major-second (1.125), minor-third (1.200), major-third (1.250), perfect-fourth (1.333), augmented-fourth (1.414), perfect-fifth (1.500), golden-ratio (1.618).
   - **Explicit sizes:** specific values for each heading level — use only when values are non-negotiable and cannot be derived
   - **Fluid typography:** `clamp()` values — can combine with derived base tokens via `$ref()`
4. **Spacing** — Base spacing unit and scale multipliers (preferred over hardcoded stops), border radii
5. **Links/Social** — Social media URLs, frequently-used links
6. **Strings** — Taglines, repeated text snippets
7. **CSS source** — Existing `palette.css` or design tokens file to bulk-import colors
8. **Presets** — Which modules need presets? (text, button, section, etc.)

For type scales, prefer the base token + derived calc approach over hardcoding:
- **Modular scale (preferred):** Store `base-size` and derive each step with `calc($ref(base-size) * {multiplier})`. Multipliers for 1.333 (Perfect Fourth): h5=1.333, h4=1.777, h3=2.369, h2=3.157, h1=4.209. Changing `base-size` updates the whole scale.
- **Fluid clamp:** Can reference derived stops: `clamp($ref(type-h5), 3vw, $ref(type-h3))`. If the clamp max doesn't map to an existing step, use a literal: `calc($ref(base-size) * 5.61)`.
- **Spacing:** Store a `section-unit` base and derive stops with integer multipliers. Same principle — one value to tune, everything follows.

**GATE (self-check — document and proceed, no user approval needed):**
- "Brand: [name]"
- "Design tokens gathered: [list categories with counts]"
- "Presets requested: [list modules or 'none yet']"
</phase_gather>

<phase_yaml>
### Phase 2: Generate YAML Spec

Translate gathered information into a YAML spec file. See [YAML-SPEC-FORMAT.md](references/YAML-SPEC-FORMAT.md) for the complete format reference.

### Color architecture

When `palette_css` provides the raw color stops, build a three-layer reference chain instead of hardcoding hex values:

1. **palette_css** — bulk-imports raw stops (shoreline-800, neon-carrot-500, etc.)
2. **colors** — semantic role aliases using `ref:` to palette names (mg-ground → shoreline-800, mg-interactive → neon-carrot-500)
3. **system_colors** — Divi's 5 slots using `ref:` to palette or semantic names

This means changing one palette stop updates every semantic alias and system slot that references it. Never duplicate hex values that exist in the palette — always use `ref:`.

Without `palette_css`, use direct hex values in `system_colors` and `colors`.

### Key structure

```yaml
name: "Brand Name"
id_namespace: "brand-slug"

palette_css: "palette.css"  # optional — bulk import CSS custom properties

system_colors:
  primary:
    ref: "neon-carrot-500"   # ref to palette_css name
  heading:
    ref: "shoreline-100"
  # ... or direct hex when no palette_css:
  # primary: "#ff9e3d"

colors:
  brand-interactive:
    ref: "neon-carrot-500"   # semantic alias → palette stop
  brand-ground:
    ref: "shoreline-800"

fonts:
  heading: "Font Name"
  body: "Font Name"
  custom:
    display: "Font Name"

type_scale:
  scale: "perfect-fourth"   # generates type-d-h1 through type-d-h6 as fluid clamp() values
  base: "1rem"              # mobile ratio auto-derived 2 steps down (minor-third)

numbers:
  # Base tokens — tune these, derived values follow automatically
  section-unit: "32px"

  # Derived spacing
  section-sm: "calc($ref(section-unit) * 1.75)"
  section-md: "calc($ref(section-unit) * 3)"

  border-radius: "1rem"

strings:
  tagline: "Brand Tagline"

links:
  facebook: "https://..."
```

Present the YAML to the user for review.

**STOP.** Get user approval on the YAML spec before proceeding. This is the source of truth — changes here propagate to everything downstream.

If the user provided complete design inputs and presets are clearly needed, present the YAML with presets included for combined Phase 2+3 review rather than forcing two separate approval rounds.
</phase_yaml>

<phase_presets>
### Phase 3: Define Presets (Optional)

Read [PRESET-COOKBOOK.md](references/PRESET-COOKBOOK.md) for complete preset templates organized by design role, with verified attribute paths and token dependency mappings.

**REQUIRED:** Before adding any preset attribute path, verify it exists in [divi-module-reference.json](references/divi-module-reference.json). The cookbook paths are verified, but custom paths need checking.

**Suggest presets proactively** based on tokens gathered in Phase 1. The cookbook includes a suggestion matrix:
- Type scale + line heights → text, post-content, heading, post-title
- Colors → heading, post-title, blurb, blog, button, cta
- Spacing + radii → button, cta, blurb (card variant), section, contact-form
- Full token set → suggest the complete suite

**Priority order:** text → post-content → heading → button → blurb → cta → section → others.

Reference shortcuts in preset `attrs` values:
- `$var(name)` — References a number, string, font, or link variable by its YAML key
- `$color(name)` — References a color by its YAML key (system or custom)

Reference shortcuts in `numbers` values:
- `$ref(name)` — References another number variable by key. Expands to `var(--gvid-xxx)`. Use inside `calc()` or `clamp()` to build derived tokens from base values.

The generator resolves these to full `$variable()` syntax with correct `gvid-`/`gcid-` prefixes.

Add presets to the YAML spec and present updated spec for review.

**STOP.** Get user approval on presets before generating.
</phase_presets>

<phase_generate>
### Phase 4: Generate and Validate

1. Write the approved YAML spec to a `generator/` folder in the user's project (or the location they specify)
2. Run the generator:

```bash
python3 scripts/generate_divi_variables.py <spec.yaml> -o <output.json>
```

3. Review the generator's summary output (color count, variable count, preset count)
4. Verify all `$var()` and `$color()` references resolved
5. Present the summary to the user

**GATE:** Before delivering the JSON, confirm:
- "Generator completed without errors: [yes/no]"
- "Output: [N] colors, [N] fonts, [N] numbers, [N] strings, [N] links, [N] presets"
- "All variable references resolved: [yes/no]"
</phase_generate>

<phase_import>
### Phase 5: Import Instructions

Provide these instructions to the user:

1. **Close the Visual Builder completely** — if open, its save will overwrite the import
2. Navigate to any page with the Divi builder
3. Open the Portability modal (import/export icon)
4. Upload the generated JSON file
5. Open the Visual Builder — variables and presets should appear

**Warning about inactive color zombies:** If they've previously deleted colors with the same IDs in the Divi UI, the colors persist in the database with `"status":"inactive"`. Re-importing should overwrite them to `"active"`, but if the Visual Builder is open during import this can fail. If colors appear missing after import, check for inactive duplicates.

**Re-import safety:** The generator uses stable IDs (same input produces same gcid/gvid). Re-importing an updated spec overwrites existing variables rather than creating duplicates.
</phase_import>

## Iterative Refinement

The skill supports iterating on an existing spec. When the user requests changes:

1. Load the existing YAML spec
2. Apply the requested modification
3. Present the updated YAML for approval
4. Regenerate the JSON

Stable ID generation ensures re-importing doesn't create duplicates.

<failed_attempts>
## What DOESN'T Work

- **Putting colors in global_variables:** Divi's `import_global_variables()` silently drops type `"colors"`. Colors MUST go through `global_colors`. The generator handles this correctly.
- **Generating JSON without the script:** The format has too many undocumented requirements (tuple format for colors, both attrs and styleAttrs, stable ID hashing). Always use the generator.
- **Guessing preset attribute paths:** Divi 5 module schemas are not intuitive. A path like `content.decoration.font` looks plausible but doesn't exist. Always verify against the module reference.
- **Importing with Visual Builder open:** The VB's save operation overwrites the import. Every time.
- **Hardcoding a full type scale:** If all size values are literal `rem` values, changing the base size requires recalculating every step manually. Use `type_scale` instead — one scale name, all steps generated automatically.
- **Hardcoding clamp() min values without a scale:** A common mistake is setting the mobile min too large (e.g. clamp min = one step below desktop max on the same scale). The correct mobile minimum comes from a different, smaller ratio applied to the same step. Two scale positions down is the standard — `perfect-fourth` desktop → `minor-third` mobile. The `type_scale` section handles this automatically.
- **Setting button padding on `button.decoration.spacing`:** This path is hidden from the builder UI. Any value set there is locked — the user has no way to see or override it. Button padding must go on `module.decoration.spacing`, which is what the builder exposes.
- **Omitting `button.decoration.button.desktop.value.enable: "on"` from any button preset:** Without this flag, none of the button decoration attrs apply. This must be in **every** `divi/button` preset — base presets, color variants, environment overrides. A stacked color variant without it will not render even if the base preset has it.
- **`calc(var(--gvid-xxx))` showing "Invalid unit" in the Divi UI:** This is a false positive in the UI validator. The expression works correctly in the browser and in the editor preview. Divi's variable system outputs `--gvid-xxx` as the CSS custom property name, and `calc(var(--gvid-xxx) * N)` resolves correctly at runtime. Do not remove the `gvid-` prefix — `calc(var(--xxx))` without it does not resolve.
</failed_attempts>

## File Reference

| File | Purpose |
|------|---------|
| [references/boilerplate.json](references/boilerplate.json) | Static base — variable system + primitive presets. Load with `boilerplate:` key in brand YAML. |
| [references/YAML-SPEC-FORMAT.md](references/YAML-SPEC-FORMAT.md) | Brand YAML format — how to write a brand spec |
| [references/PRESET-COOKBOOK.md](references/PRESET-COOKBOOK.md) | Design recipes — colors, variables, composition patterns |
| [references/DIVI-SPEC.md](references/DIVI-SPEC.md) | Technical rules — bugs, constraints, exact paths, import requirements |
| [references/divi-module-reference.json](references/divi-module-reference.json) | Complete module element and path reference |
| [references/spec-test.yaml](references/spec-test.yaml) | Working example brand YAML spec |
| [references/spec-test.json](references/spec-test.json) | Generated JSON from the example spec |
| [scripts/generate_divi_variables.py](scripts/generate_divi_variables.py) | Generator — boilerplate + brand YAML → Divi import JSON |
| [scripts/extract_module_reference.py](scripts/extract_module_reference.py) | Extracts module reference from Divi source |
