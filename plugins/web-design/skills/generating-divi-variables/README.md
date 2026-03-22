# Generating Divi Variables

Builds a complete Divi 5 design system from brand inputs and generates a Divi-compatible import file — semantic variables, a live math engine, and role presets wired together.

## When to Use

- Setting up a new Divi 5 design system
- Translating a visual design direction into Divi variables and presets
- Generating a Divi import from palette files and reference images
- Regenerating an existing Divi import after brand changes

## How to Invoke

- "Generate a Divi design system from these reference images and palette"
- "Build a Divi variable set for this brand"
- "Create Divi presets based on this page content spec"
- "Regenerate my Divi import from this brand YAML"
- "Set up Divi variables and presets for a dark theme"

## What You'll Need

- **Palette CSS** — color stops from your design tool or existing system (optional but recommended)
- **Reference images** — screenshots of sites or designs showing visual direction (optional)
- **Page content spec** — output from the designing-websites skill (optional)
- Or just describe your design intent directly

## What You'll Get

A Divi 5 import JSON ready to upload via the Portability modal, containing:
- 25+ semantic color variables wired to your palette
- A live type scale using CSS `pow()` — change one variable, all headings update
- A harmonic spacing scale derived from the same ratio as the type scale
- Primitive grid presets (section, row, column, group gap wiring)
- Role presets for typography, buttons, cards, and other patterns

## Requirements

Python 3.9+ and PyYAML:
```bash
pip install pyyaml
```

## Tips

- Reference images produce better results than descriptions alone — the skill reads visual intent from images
- If you have a palette CSS file, provide it — the skill uses it to wire semantic color slots automatically
- The three adjustable variables that have the most impact: `type-scale` (heading drama), `space-base` (overall breathing room), and `color-interactive` (the brand action color)
