# Preset Cookbook

Strategy guide for suggesting and building Divi 5 module presets. Use during Phase 3 to recommend presets based on gathered design tokens.

**This document tells you *what* to preset and *why*. For actual attribute paths, look up the module in `divi-module-reference.json`.**

## How to Build a Preset

1. Look up the module in `divi-module-reference.json`
2. Find the element you want to style (e.g., `title`, `content`, `button`)
3. Check its `decoration_groups` list to see what's available
4. Construct the path using the pattern formula below
5. Wire it to a `$var()` or `$color()` reference from the YAML spec

## Path Pattern Formula

All preset attribute paths follow this structure:

```
{element}.decoration.{group}.{subgroup}.{device}.value.{property}
```

### Three font group types

This is the #1 source of preset errors. Which pattern to use depends on the element's `decoration_groups` in the module reference:

| If decoration_groups contains... | Path pattern | Controls |
|----------------------------------|-------------|----------|
| `headingFont` | `{element}.decoration.headingFont.{h1-h6}.font.desktop.value.{prop}` | Individual heading levels |
| `bodyFont` | `{element}.decoration.bodyFont.body.font.desktop.value.{prop}` | Body copy |
| `font` | `{element}.decoration.font.font.desktop.value.{prop}` | Single font control (no h1-h6 breakdown) |

Font properties: `size`, `lineHeight`, `color`, `letterSpacing`, `weight`

### Other decoration groups

| Group | Path pattern | Properties |
|-------|-------------|------------|
| `background` | `{element}.decoration.background.desktop.value.color` | `color` |
| `spacing` | `{element}.decoration.spacing.desktop.value.{padding\|margin}.{top\|right\|bottom\|left}` | Individual sides |
| `border` radius | `{element}.decoration.border.desktop.value.radius.{topLeft\|topRight\|bottomLeft\|bottomRight}` | Individual corners |
| `border` radius sync | `{element}.decoration.border.desktop.value.radius.sync` | `true` to sync all corners |
| `border` style | `{element}.decoration.border.desktop.value.styles.all.{color\|width\|style}` | Border line properties |

---

## Suggesting Presets from Gathered Tokens

Use this matrix to recommend presets based on what Phase 1 gathered:

| If Phase 1 gathered... | Suggest these presets |
|------------------------|---------------------|
| Type scale + line heights | text, post-content, heading, post-title |
| Colors (system slots filled) | heading, post-title, blurb, blog, button, cta |
| Spacing variables | section, button, cta, blurb (card variant) |
| Border radius | button, cta, blurb (card variant), contact-form |
| Full token set (all above) | Full suite: text, post-content, heading, button, blurb, cta, section |

**Priority order:** text → post-content → heading → button → blurb → cta → section → others.

Text and post-content first because they affect the most content with the least effort. Button next because it defines the interaction pattern. Blurb and CTA follow because they're the most common composite modules.

---

## Composition Patterns

These are architectural decisions that affect which modules to reach for and how to combine presets. Get these wrong and you end up with the right visual but the wrong structure — harder to maintain and harder to extend.

### divi/text over divi/cta for content blocks

`divi/cta` is purpose-built for heading + body + button, but that specificity makes it inflexible. `divi/text` covers more ground with a single UI — use it for body content, callout blocks, key statements, and eyebrows by creating named presets for each treatment. The module stays generic; the preset defines the role. Reserve `divi/cta` for cases where the three-part structure (heading, body, button) is truly fixed.

### Post content on CPTs

On custom post types, a `divi/text` module pointed at the post content variable picks up text presets automatically — the same type scale and body styles apply without extra configuration. `divi/post-content` is still worth setting up for theme builder templates (it renders the post body directly), but `divi/text` is the right tool when you need preset inheritance on CPT content fields.

### Card architecture — two valid approaches

Choose based on what the card needs:

**Blurb as card** — the blurb module has a built-in structure (icon/image, title, body) and supports stacking sub-elements including buttons. Use when the card has a fixed structure and you want a single self-contained module. The blurb preset styles the card shell; a button preset applied to the embedded button styles the CTA.

**Column as card** — a column preset carries the card's visual treatment (background, border-radius, padding) while modules dropped inside (text, button, heading) each use their own presets. The column IS the card; its contents style independently. Use when card content varies or when the layout needs flexibility. Especially powerful with loop columns — define the card treatment once on the column preset and it propagates across every loop item.

The choice is structural, not stylistic. Both can look identical. The difference is in how content is managed and how much flexibility interior modules need.

### CTA bands are compositions, not single presets

A full-width CTA band is a section + columns + modules, each with its own preset:
- `divi/section` preset: background color and vertical padding
- Column layout: typically image left, text + button right
- `divi/text` preset: handles the heading and body copy
- `divi/button` preset: handles the CTA

No CTA-specific module preset is needed. The composition carries the design. Keep section presets minimal — most builds vary sections heavily, and aggressive section defaults create more overrides than they save.

### What presets control — and what they don't

Presets set decoration-level styling: backgrounds, borders, radius, spacing, font size, color, weight, line-height, letter-spacing. They do not control content (text, images), layout grid choices, heading level, or icon selection.

Interior elements of a composed module still need their own presets. A blurb card preset styles the card shell — the button embedded in the blurb needs a button preset applied separately. A column card preset styles the container — the text and button modules inside need their own presets.

---

## Module Catalog

### Tier 1: Typography Modules

Highest-value presets. A single default preset propagates the type scale site-wide.

#### divi/text
**Role:** Primary content module. Every page uses it.
**Tokens:** T
**Key element:** `content` — has `bodyFont` + `headingFont` (h1–h6)
**Gotcha:** Fonts nest under `content`, not `module`.

#### divi/post-content
**Role:** Renders post/page body in theme builder templates. Without this preset, blog posts ignore your type scale.
**Tokens:** T
**Key element:** `module` — has `bodyFont` + `headingFont` directly
**Gotcha:** Opposite of divi/text — fonts are on `module`, not `content`.

#### divi/heading
**Role:** Standalone headlines, section headers, hero text.
**Tokens:** T, C
**Key element:** `title` — has `font` (single control, no h1–h6 breakdown)
**Gotcha:** Uses `font`, not `headingFont`. The heading level is a content option, not a decoration group.

#### divi/post-title
**Role:** Post/page title in theme builder templates.
**Tokens:** T, C
**Key elements:** `title` has `font`, `meta` has `font`

---

### Tier 2: Interactive Modules

Define how actions look site-wide.

#### divi/button
**Role:** Primary interactive element. Also embedded in CTA, contact form, slider.
**Tokens:** T, C, R
**Key element:** `button` — has `font`, `background`, `border`, `boxShadow`
**Required attr:** `button.decoration.button.desktop.value.enable: "on"` — activates custom styles. Without this, none of the decoration attrs apply.
**Padding gotcha:** Button padding goes on `module.decoration.spacing`, NOT `button.decoration.spacing`. The `module` spacing is what the builder exposes. `button.decoration.spacing` is hidden from the UI — setting it there locks the value silently with no way for the user to override it. Never set `button.decoration.spacing` in a preset.
**Note:** Buttons commonly need variants (primary, secondary, tertiary). Use the list syntax for multiple presets per module. Tertiary (text-only) buttons still need padding on `module.decoration.spacing` to maintain an adequate hit area.

#### divi/cta
**Role:** Call-to-action block — heading + body + button. Conversion-focused sections.
**Tokens:** T, C, S, R
**Key elements:** `module` (background, border, spacing), `title` (font), `content` (bodyFont), `button` (font, background, border, spacing)
**Note:** Most visually complex preset — spans typography + interactive + layout tokens.

---

### Tier 3: Card-Pattern Modules

Power card grids, feature lists, content previews.

#### divi/blurb
**Role:** Workhorse card module — feature grids, icon+text blocks, service listings.
**Tokens:** T, C, S, R
**Key elements:** `title` (font), `content` (bodyFont), `module` (background, border, spacing), `imageIcon` (background, border, spacing)
**Gotcha:** Title uses `font`, not `headingFont`.
**Note:** Two common patterns — typography-only preset (just title + body fonts) vs. full card preset (adds background, border-radius, padding).

#### divi/blog
**Role:** Post listing — grid or fullwidth. Controls how post cards appear.
**Tokens:** T, C
**Key elements:** `title` (font), `meta` (font), `content` (bodyFont), `readMore` (font), `pagination` (font), `overlay` (background), `image` (border, boxShadow)

#### divi/testimonial
**Role:** Client quotes with author info. Social proof sections.
**Tokens:** T, C
**Key elements:** `body` (bodyFont), `author` (font), `position` (font)

---

### Tier 4: Layout Modules

Page skeleton — spacing and backgrounds.

#### divi/section
**Role:** Top-level container. Controls vertical rhythm.
**Tokens:** C, S
**Key elements:** `module` (background, border, spacing, sizing), `innerSizing` (sizing — content max-width), `column1`/`column2`/`column3` (background, spacing)
**Note:** Keep section presets minimal. Most builds vary sections heavily. Aggressive defaults create more overrides than they save.

#### divi/row
**Role:** Column container within sections.
**Tokens:** S
**Key element:** `module` (background, border, spacing, sizing)
**Note:** Rarely preset beyond max-width. Skip unless the design system has specific row-level requirements.

---

### Tier 5: Compound Modules

Multiple sub-elements. Lower priority for defaults but useful for specific patterns.

#### divi/accordion
**Role:** FAQ sections, expandable panels.
**Tokens:** T, C
**Key elements:** `title` (font), `content` (bodyFont), `openToggle` (background, font), `closedToggle` (background, font)

#### divi/tabs
**Role:** Tabbed content panels, feature comparisons.
**Tokens:** T, C
**Key elements:** `tab` (background, font), `activeTab` (font), `content` (background, bodyFont)

#### divi/slider
**Role:** Hero slides, carousels, feature showcases.
**Tokens:** T, C
**Key elements:** `title` (font), `content` (bodyFont, sizing), `button` (button group), `children` (background, border)

#### divi/contact-form
**Role:** Lead capture, contact pages.
**Tokens:** T, C, R
**Key elements:** `title` (font), `field` (background, font, spacing), `button` (background, border, boxShadow, font, spacing)

---

## Element-to-Font-Group Map

The critical lookup for avoiding silent preset failures. **Always verify against `divi-module-reference.json`** — this table covers the most commonly preset modules but the reference is authoritative.

| Module | Element | Font group |
|--------|---------|-----------|
| divi/text | content | headingFont (h1–h6), bodyFont |
| divi/post-content | module | headingFont (h1–h6), bodyFont |
| divi/heading | title | font |
| divi/post-title | title, meta | font |
| divi/blurb | title | font |
| divi/blurb | content | bodyFont |
| divi/button | button | font |
| divi/cta | title, button | font |
| divi/cta | content | bodyFont |
| divi/blog | title, meta, readMore | font |
| divi/blog | content | bodyFont |
| divi/accordion | title | font |
| divi/accordion | content | bodyFont |
| divi/tabs | tab, activeTab | font |
| divi/tabs | content | bodyFont |
| divi/slider | title | font |
| divi/slider | content | bodyFont |
| divi/contact-form | title, field, button | font |
| divi/testimonial | author, position | font |
| divi/testimonial | body | bodyFont |

Only two modules use `headingFont` (with h1–h6 breakdown): **divi/text** and **divi/post-content**. Everything else uses `font` (single control).
