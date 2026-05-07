# Divi 5 Design System Cookbook

This cookbook teaches the skill how to think about design problems. Technical rules live in `DIVI-SPEC.md`. This document is about design reasoning and composition.

---

## Part 1: Reading a Design

Before assigning any values, you need to understand what the design is trying to do. This is not a checklist — it's an act of comprehension. The inputs (reference images, palette, page spec) are evidence. Your job is to read what they're telling you before you decide anything.

### Name what you expected first

Before reading the inputs, you already have a prediction. Name it. "A design like this typically..." Then read. Then name where what you found departs from what you expected.

That gap is where the organizing principle lives. Organizing principles are the things a design is doing that its category doesn't require it to do. They're invisible if you expect them and visible the moment you articulate the surprise.

If nothing surprised you, you probably pattern-completed rather than actually read. Push until you find at least one choice the design made that it didn't have to make.

### Find the organizing principle before analyzing elements

One sentence: what is this design organized around? Not a list of what you see — one sentence about what holds it all together.

Some possibilities: photography as environment (layout sits on top of imagery rather than containing it). Typography as the structural element (type weight and scale carry the visual hierarchy, color is secondary). Color as architecture (surface blocking creates rhythm, imagery is decorative). Density as the aesthetic (information richness is itself the design statement).

Find the principle before reading individual elements. Once you have it, element analysis becomes confirmation and refinement rather than cataloging. And you'll notice when an element is doing structural work — which is where the most important design system decisions live.

### Work through the inputs as evidence

When you look at reference images, you're not measuring values. You're reading visual arguments. A tight type scale isn't a number — it's a statement about the relationship between headings and body copy. A pill-radius button isn't a specification — it's a character claim about the brand.

For each input, ask: what is this telling me about how the design thinks? Not what does it contain, but what does it reveal?

**On palette:** What is the emotional temperature of this palette? Cool palettes create distance and professionalism. Warm palettes create approachability and energy. A palette with a wide chroma range gives you expressive options; a muted palette constrains you toward subtlety. What does this palette want to be?

**On reference images:** Look at the visual field as a whole before examining individual elements. What percentage of the screen is ground? What percentage is surface? What percentage is accent? That ratio tells you more about the design than any individual color choice. Then notice what the interactive elements do to your eye — do they demand attention or invite it?

**On page content spec:** What spatial relationships does the content create? A page heavy in cards wants a grid system that breathes differently than a page heavy in editorial columns. What rhythm does the content naturally suggest?

### Reframe before committing

The first read of a design is usually the most obvious read. Before committing to any decision, name the alternative framing.

If your first read is "this is a dark, editorial design," ask: what if it's actually a dark design that wants to feel warm? What changes? If your first read on buttons is "pill radius, contemporary," ask: what if the overall character is more architectural and the pill radius is fighting the palette? These aren't necessarily better readings — but making them forces you to defend the first one.

Design decisions that can't survive one alternative framing are fragile. They'll produce a system that feels slightly wrong without anyone being able to say why.

### Find convergence

When multiple inputs point toward the same character, that convergence is your strongest signal. A cool neutral palette + generous spacing + restrained heading scale + squared-off references = an architectural, precision-forward design. Each signal alone is a suggestion. Three signals pointing the same way is a design argument.

When inputs conflict — warm palette but tight spacing, dramatic type scale but minimal references — you're looking at a real design tension. Name it. Either one input is misleading (reference images from a different context) or the designer is trying to hold two characters in tension intentionally. Surface that before making decisions.

### The second-order check

After forming a design read, ask what that read forecloses. A choice toward "dramatic scale" forecloses certain body copy sizes. A choice toward "pill radius everywhere" forecloses certain editorial treatments. A "dark environment" forecloses certain palette assignments. Decisions are not independent — each one narrows the design space. Make sure what you're foreclosing is actually worth foreclosing.

---

## Part 2: Color Decisions

Color decisions follow from the design read, not from the palette. The palette provides vocabulary; the design read determines what each word in that vocabulary is doing.

### Ground is the first decision

Ground is what 70–80% of the visual field sits on. Get it wrong and every other color decision is built on an unstable foundation. Ground isn't the "background color" — it's the environmental premise the entire design operates inside.

In a dark environment, the ground draws from the cool/dark end of the palette. In a light environment, from the warm/light end. The specific stop determines how the rest of the palette behaves against it. A very dark ground needs high-contrast text and bright interactive accents. A mid-dark ground has more latitude.

The elevation principle: surfaces float above the ground. In a dark environment, cards are lighter than the ground. In a light environment, cards are darker. This is opposite to what feels intuitive from print design — digital elevation goes toward light, not shadow.

### Interactive color is not the same as primary

This distinction matters and is easy to collapse incorrectly.

**`primary` (Divi system slot)** is a site-wide accent color for links and legacy UI elements. It goes into the WordPress theme customizer and must be a literal hex value. It's what Divi applies automatically across modules where no specific color is set.

**`color-interactive` (boilerplate slot)** fills buttons and primary interactive elements in your design system. It may use the same palette stop as `primary`, but it doesn't have to.

On a dark-environment site with an inverted button treatment — light buttons against a dark ground — `primary` might be a warm accent for links while `color-interactive` is near-white. These are different decisions answering different questions. Do not conflate them.

The question to ask: does your button fill need to match your link accent? Sometimes yes (simple light environment, brand color works for both). Often no (dark environment, different surfaces, different contrast requirements).

### The color chord

A color system is a chord, not a collection. Individual colors have properties, but those properties only matter in relationship to each other. The question isn't "is this a good interactive color" — it's "does this interactive color work against this ground, with this text hierarchy, next to this surface?"

Before finalizing any color assignment, run the chord mentally: ground → surface → text → interactive → text-on-interactive. Does each transition feel intentional? Does the interactive color have enough contrast against the ground to read as interactive without screaming? Does text-on-interactive actually read against the interactive fill?

### Dark environment pattern

Ground draws from the dark/cool end. Surfaces are lighter than ground — not darker. Text is near the lightest end. Interactive should have high contrast against ground — warm colors work well against cool darks. Interactive hover is slightly lighter or more saturated, not a completely different color.

### Light environment pattern

Ground draws from the warm/light end. Surfaces are slightly darker than ground. Text is near the darkest end. Interactive should have AA contrast against ground — mid-tone brand colors typically work. Interactive hover is one step darker/stronger.

### Functional colors

Functional colors (error, success, info, warning) communicate system state. Use established conventions — red for error, green for success, blue for info — unless the brand has a strong reason to fight them. Users bring these associations; overriding them requires real justification. Warning often doesn't need its own palette stop; the interactive accent family usually works.

### Two-brand systems

When two brands share a palette but operate in different environments, write the presets once against the semantic slots. The environment is entirely a color assignment decision — `color-ground` points to one end of the palette for one brand and the other end for the other. The presets reference `color-ground`, `color-interactive`, etc., and render correctly in both environments automatically.

---

## Part 3: Variable Decisions

### Type scale

Three variables control the entire heading system: `type-base` (the root size), `type-scale` (the desktop ratio), and `type-scale-mobile` (mobile ratio). The boilerplate handles the math — change these values and all heading sizes update live.

The scale ratio determines the visual drama of the heading hierarchy. Minor third (1.200) produces subtle, compact headings — good for UI-forward designs. Perfect fourth (1.333) is the classic readable hierarchy. Augmented fourth (1.414) produces dramatic display-forward headings. The choice follows from the design read, not from convention.

`type-base` is the most powerful single adjustment. Shifting it from 1rem to 1.25rem opens up the entire spatial relationship between type and layout without changing the scale's proportional structure. If a design feels cramped but the scale ratio feels right, `type-base` is usually the lever.

Matching `space-scale` to `type-scale` creates harmonic relationships between type and spacing — they feel related because they're mathematically related. Decoupling them is valid but requires intention.

### Spacing scale

The spacing scale works the same way as the type scale — `space-base` and `space-scale` drive everything. The step names communicate their design intent:

`space-xs` and `space-sm` are component-level — icon gaps, inline elements, tight internal padding. `space-md` is the standard working spacing — card padding, component gaps. `space-lg` and `space-xl` are layout-level — row gaps, section internal spacing. `space-2xl` is hero-scale — major section separation.

The gap hierarchy is structural: section gaps wider than row gaps, row gaps wider than column/group internal gaps. This hierarchy communicates content relationships without explicit dividers.

### Radius

Radius is a character decision before it's a specification. Sharp corners (0px) read as formal, architectural, precise. Large radius (`radius-lg`) reads as friendly, modern, approachable. Pill radius (`radius-pill`) reads as playful, contemporary, action-forward.

Consistency across the system matters more than any individual choice. Buttons, cards, and inputs using the same radius family create visual coherence. Mixing radii creates tension — which can be intentional (square cards, pill buttons for contrast) or accidental (just inconsistency). Know which one you're doing.

### Font weights

`weight-heading`, `weight-body`, and `weight-emphasis` are relative to the chosen font family. 800 is correct for Inter Tight; a different face might read as heavy at 700 or need 900 for equivalent impact. When the font family changes, reconsider the weights — they're not absolute, they're relational.

---

## Part 4: Composition Patterns

These are reference patterns, not prescriptions. Use them when the page spec suggests them, adapt when it doesn't.

### Typography roles

The Body preset establishes the full type scale. Every additional text role is built on top — same heading scale, different body treatment. A text module might contain headings at any level; always include the full h1–h6 scale in every text role preset so Divi doesn't fall back to its defaults.

Common roles and their character: **Body** — standard reading weight and size. **Lede** — introductory paragraph, slightly larger, same weight. **Key Statement** — emphasized callout, larger, heavier. **Eyebrow** — small label, wide tracking, emphasis weight, accent color. **Meta** — caption size, dim color, wide tracking. **Footer** — small, secondary color, link hover treatment, list reset. **Pullquote** — large, emphasis weight, left border treatment.

### Button roles

Three tiers with distinct visual weight. **Filled**: solid background, high contrast, maximum visual weight — use once per visual area for the primary action. **Ghost**: transparent fill, visible border, same radius and padding as filled — subordinate action. **Text**: no fill, bottom border only, minimal padding — lowest weight, used inline where visual noise must stay low.

Environment variants matter: a button on a filled accent-colored surface needs color assignments that work against that surface, not against the ground. Create separate environment presets rather than trying to make one preset work everywhere.

### Cards

A card is a group or column preset carrying surface color, radius, and padding. Inner modules (image, text, button) each use their own presets — the card preset styles the shell only. The group's internal gap spaces inner modules; the row's column gap separates cards from each other. Card gap (between cards) should be wider than card padding (internal) — typically one scale step up.

### Section compositions

A CTA band is a section preset with a background color + row + column + text + button. The section handles the environment; the content modules handle the message. No special CTA module — composition carries the design.

A hero is section + row + column + text (Hero role) + button. With a background image, the section gets the image directly through the builder (not through a preset) and uses `color-surface-scrim` for text contrast.

Feature grids are section + row + group per feature. Feature groups often don't need a surface color — the icon anchors each item visually. Let the row gap do the work.

### Core composition principles

Presets style; content is separate. A preset sets decoration. It never sets text, images, or structural choices — those live in the builder.

Inner elements need their own presets. A card preset styles the shell. The text inside needs a text preset. The button inside needs a button preset. Presets don't cascade into children.

Variables are the real design system. Presets are wiring. The decisions that matter most are `type-base`, `type-scale`, `space-base`, `space-scale`, and the color slot assignments. Change those and the entire system shifts without touching a single preset.
