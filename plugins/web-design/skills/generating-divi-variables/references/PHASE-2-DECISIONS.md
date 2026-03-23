# Phase 2: Design Decisions

The decisions made here determine everything downstream. This phase is not about filling in a form — it's about reading what the inputs are telling you and building a coherent design argument before committing to any values.

Read [PRESET-COOKBOOK.md](PRESET-COOKBOOK.md) before working through this phase. The cookbook teaches the reasoning; this phase applies it.

---

## Work Through the Inputs

Before proposing any decision, read the inputs as evidence of design intent. Each input is a signal; your job is to understand what they're saying together, not just separately.

**From the palette:** What is the emotional temperature? Warm or cool? Wide chroma range or muted? How many stops — does this palette have the vocabulary to express elevation (surface above ground) and contrast (text against ground) simultaneously? Where is the strongest chroma, and what does that color want to do?

**From reference images:** Don't start with individual elements. Start with the visual field as a whole. What ratio of ground to surface to accent? Then ask: what does the heading scale say about the relationship between headings and body — dramatic hierarchy or quiet coherence? What do the buttons say about the brand's character? What does the spacing say about how dense or airy this design wants to be? What surprises you? What would you have expected that isn't there?

**From the page content spec:** What content patterns repeat — cards, editorial columns, feature grids, hero sections? What spatial relationships does the content want to create? A grid of cards wants different rhythm than a page of long-form text.

**From direct design intent:** Listen for underlying values, not just preferences. "I want it to feel premium" is different from "I want pill buttons." The former is a character argument; the latter is a specification. When you hear a specification, ask what character it's trying to express.

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

Present your design argument to the designer — the underlying read, the convergences you found, any tensions that need resolution, and the specific values your argument implies.

Don't present it as a table of decisions awaiting approval. Present it as a design read you've built from the evidence, and ask whether it matches their understanding of what they're building. If it doesn't, what's different? If it does, confirm the specific values together.

The artifact to produce before the GATE:

```
PHASE 2 DESIGN READ
───────────────────
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
