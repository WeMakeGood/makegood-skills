# Phase 2: Design Decisions

The decisions made here determine everything downstream. This phase is not about filling in a form — it's about reading what the inputs are telling you and building a coherent design argument before committing to any values.

Read [PRESET-COOKBOOK.md](PRESET-COOKBOOK.md) before working through this phase. The cookbook teaches the reasoning; this phase applies it.

---

## Name What You Expected First

Before reading anything, you already have a prediction. A travel site, a fintech startup, a nonprofit consultancy — each category carries assumptions about what the design will do. Name those assumptions explicitly before engaging with the inputs.

Write one sentence: "A design like this typically..." Then read the inputs. Then write one sentence about where what you found departs from what you expected.

That gap is where the organizing principle lives. Organizing principles are almost always the thing a design is doing that its category doesn't require it to do. Photography-as-ground in a travel site is invisible if you expect it — it's just what travel sites do. It becomes visible when you articulate "I expected photography to sit inside content sections, but here it's the actual environment everything else lives on." That surprise is the principle. Every other decision follows from it.

This is not a rhetorical step. If nothing surprised you, either the design is entirely conventional (possible) or you pattern-completed rather than actually looked (more likely). Push until you find at least one place where the design made a choice it didn't have to make.

---

## Find the Organizing Principle

Before analyzing any specific element, name what this design is organized around. Not a list of what you see — one sentence about what holds it all together.

Some designs are organized around photography as environment. Some around typography carrying all the visual weight. Some around color doing the structural work — bold surface blocking that creates rhythm without imagery. Some around content density as the aesthetic itself. The organizing principle is the logic that makes all the individual decisions coherent.

You cannot find the organizing principle by cataloging elements. You find it by asking: if you removed one thing and the whole design collapsed, what would that thing be? Whatever it is — that's what the design is organized around.

Only after naming the principle should you read the individual elements. Because now you're reading them as expressions of that principle, which means you'll notice when an element is doing structural work (and must be preserved in the design system) versus decorative work (and can be varied).

---

## Work Through the Inputs

With the organizing principle in view, read the inputs as evidence — not to confirm the principle, but to test and refine it.

**From the palette:** What is the emotional temperature? Warm or cool? Wide chroma range or muted? Does this palette have the vocabulary to express elevation (surface above ground) and contrast (text against ground) simultaneously? Where is the strongest chroma, and what does that color want to do? Does the palette support the organizing principle, or create tension with it?

**From reference images:** What ratio of ground to surface to accent across the visual field? What does the heading scale say about the relationship between headings and body? What do buttons say about the brand's character? What does spacing say about density? And critically: are any elements doing double duty — serving both structural and decorative roles simultaneously? Photography that functions as ground, type that functions as a layout grid, color that functions as both accent and surface — these are places where the organizing principle is doing its most interesting work.

**From the page content spec:** What content patterns repeat? What spatial relationships does the content want to create? Does the content structure reinforce or complicate the organizing principle?

**From direct design intent:** Listen for underlying values, not just preferences. "I want it to feel premium" is a character argument. "I want pill buttons" is a specification. When you hear a specification, ask what character it's trying to express, and whether that character is consistent with the organizing principle you've identified.

---

## Find Convergence

When multiple inputs point toward the same character, that convergence is your strongest signal. Name it explicitly.

If the palette is cool and muted, the references show generous spacing, and the page spec is editorial-forward — those three signals converge on a precise, restrained character. Decisions that respect that character will feel right. Decisions that fight it will create friction somewhere.

When inputs conflict — warm palette but minimal references, dramatic references but a page spec full of dense UI — name the tension and surface it to the designer. Some tensions are real conflicts requiring a choice. Others are complementary: the palette provides warmth while the layout provides precision, and both can coexist. Know which kind you're looking at before deciding.

---

## Reframe Before Committing

For any major design direction, name the alternative framing before committing.

If your read is "this is a dark, editorial design with tight type," ask: what if the tight type is a font-family artifact rather than a character choice? What if the designer actually wants generous heading sizes and the references are just showing one narrow treatment? Testing the alternative doesn't mean abandoning the first read — it means the first read has been challenged and survived.

For color environment specifically: before committing to dark vs. light, ask whether the palette supports both and whether the page content has sections that might need the opposite treatment (a dark-ground site with a light-ground CTA band, for example).

---

## Build the Design Argument

Once you've worked through the inputs and tested alternatives, build a coherent design argument — not a list of decisions, but a single statement of what this design is trying to be and how the specific variable choices express that.

Something like: "This is a confident, architecture-forward design — the palette's cool neutrals and the references' precise spacing call for a perfect-fourth scale with generous `type-base`, a matching spacing scale, and squared-off radius. The button treatment inverts against the dark ground, so `color-interactive` uses the light end of the neutral spine rather than the accent color, which is reserved for links and eyebrows."

That argument generates the specific values. The values don't generate the argument.

---

## Present for Confirmation

Present your design argument to the designer — the organizing principle you found, the surprise that revealed it, the convergences you found, any tensions that need resolution, and the specific values your argument implies.

Don't present it as a table of decisions awaiting approval. Present it as a design read you've built from the evidence, and ask whether it matches their understanding of what they're building. If it doesn't, what's different? If it does, confirm the specific values together.

The artifact to produce before the GATE:

```
PHASE 2 DESIGN READ
───────────────────
What I expected: [one sentence — what a design like this typically does]
What surprised me: [one sentence — where this design departed from expectation]

Organizing principle: [one sentence — what this design is organized around]

Character: [2–3 sentences — what this design is trying to be and why]

Convergences: [where inputs point the same direction]
Tensions: [where inputs conflict and how you've resolved or flagged them]

Values this argument implies:
  type-scale: [value] — [why this ratio fits the character]
  space-base: [value] — [why this base fits the density]
  radius: [buttons / cards / inputs] — [what character this expresses]
  color environment: [dark / light] — [what in the inputs led to this]

Color argument:
  primary (links): [palette stop] — [why]
  color-interactive (buttons): [palette stop] — [why, and whether it differs from primary]
  color-ground: [palette stop] — [why this stop]
  [other notable assignments with brief rationale]

Preset roles needed:
  [List drawn from page spec and design character — not exhaustive, just the ones
  the character clearly calls for]
```

**STOP.** Do not write any YAML until the designer explicitly confirms this design read. A confirmed design read produces correct YAML quickly. Unconfirmed assumptions produce YAML that needs to be rebuilt.
