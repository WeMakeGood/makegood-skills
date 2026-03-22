---
name: generating-divi-variables
description: Builds a complete Divi 5 design system from brand inputs — palette CSS, reference images, page content spec, and design intent. Generates a brand YAML layered on top of the boilerplate, then produces an import-ready JSON with semantic variables, a live math engine (type and spacing scales via CSS pow()), and role presets wired to those variables. Use when setting up a Divi 5 design system, generating Divi variables and presets, translating visual design direction into a Divi import file, or when a user provides palette files, reference site images, or page content specs for Divi.
compatibility: Requires Python 3.9+ and PyYAML (pip install pyyaml)
---

# Generating Divi Variables

<purpose>
The default tendency when building a design system is to treat it as a data entry problem — collect values, write them into fields. This skill exists because a design system is a set of decisions about visual relationships, and those decisions must be made before any values are written. The skill enforces a design-first sequence: analyze visual intent from inputs, make and confirm design decisions, then generate the YAML that encodes those decisions. The boilerplate handles the math; the skill handles the thinking.
</purpose>

## Critical Rules

**DESIGN FIRST:** Do not write YAML until design decisions are confirmed. Visual intent → decisions → YAML is the only valid sequence. Skipping the decisions phase produces a technically correct but visually incoherent output.

**BOILERPLATE REQUIRED:** Every brand YAML must include `boilerplate: "path/to/boilerplate.json"`. Without it the semantic variable system is not in place and the output is incomplete.

**VARIABLE SYNTAX — no exceptions:**
- Colors in preset attrs: `$color(semantic-slot-name)` only
- Numbers in preset attrs: `var(--gvid-variable-name)` directly — never `$var()`
- `$var()` is broken in the current Divi version and produces incorrect output

**COOKBOOK BEFORE PRESETS:** Before suggesting any preset structure, consult [PRESET-COOKBOOK.md](references/PRESET-COOKBOOK.md). Design decisions come from the cookbook — module selection, composition patterns, dark vs. light treatment.

**GENERATOR AUTHORITY:** All JSON output MUST be produced by running `scripts/generate_divi_variables.py`. Never generate Divi JSON directly.

**PROFESSIONAL CHALLENGE:** When a design decision contradicts established visual principles, when a path doesn't exist in the module reference, or when the cookbook identifies a better approach — cite the concern and offer an alternative. Accuracy over agreement.

---

## Quick Start

If the user has an existing brand YAML:

```bash
python3 scripts/generate_divi_variables.py <spec.yaml> -o <output.json>
```

Otherwise, follow the full workflow below.

---

## Workflow

<phase_gather>
### Phase 1: Gather Inputs and Analyze

Read [references/PHASE-1-GATHER.md](references/PHASE-1-GATHER.md) for full instructions.

Accept any combination of: palette CSS, reference images, page content spec, direct design intent.

**GATE:** Before proceeding, write:
- "Inputs received: [list — palette/images/page spec/direct intent]"
- "Environment read: [dark / light / unclear — one sentence rationale]"
- "Visual character: [2–3 sentences from reference images]"
- "Modules needed: [list from page spec, or 'not provided']"
</phase_gather>

<phase_decisions>
### Phase 2: Design Decisions

Read [references/PHASE-2-DECISIONS.md](references/PHASE-2-DECISIONS.md) for full instructions.

Present your read of the design direction and get explicit confirmation before writing any YAML. Every decision has downstream consequences.

**GATE:** Before proceeding, write:
- "Type scale: [ratio name and value] — [one sentence rationale]"
- "Spacing feel: [space-base value] — [one sentence rationale]"
- "Radius: [which stop for buttons/cards] — [one sentence rationale]"
- "Color assignments: confirmed by user [yes/no]"
- "Preset roles needed: [list]"

**STOP.** Do not proceed to Phase 3 until the user has explicitly confirmed the design decisions.
</phase_decisions>

<phase_yaml>
### Phase 3: Generate Brand YAML

Read [references/PHASE-3-YAML.md](references/PHASE-3-YAML.md) for full instructions.

Translate confirmed decisions into brand YAML. Start with the boilerplate key, then overrides, fonts, palette, colors, system_colors, presets — in that order.

**GATE:** Before proceeding, write:
- "YAML sections included: [list]"
- "All 20 semantic color slots assigned: [yes/no]"
- "Preset paths verified against module reference: [yes/no]"

**STOP.** Present the complete YAML. Do not generate JSON until the user approves.
</phase_yaml>

<phase_generate>
### Phase 4: Generate and Validate

Run the generator:

```bash
python3 scripts/generate_divi_variables.py <spec.yaml> -o <output.json>
```

**GATE:** Before delivering the output, confirm:
- "Generator completed without errors: [yes/no]"
- "Output counts: [N colors, N variables, N presets]"
- "Boilerplate primitives present: [yes/no]"
- "Brand role presets present: [list]"
</phase_generate>

<phase_import>
### Phase 5: Import

Remind the user: **close the Visual Builder completely before importing.** The VB save overwrites imports.

Import path: any page → Divi builder → Portability modal → upload JSON.

After importing, verify variables appear in the correct order (adjustable at top, derived at bottom) and all presets are present.
</phase_import>

---

## Iterative Refinement

When changes are needed after import, identify the minimal change:
- **Scale/spacing feel** → `overrides:` values
- **Color adjustments** → `colors:` assignments
- **New preset role** → `presets:` section
- **Specific variable** → `overrides:` or `numbers:`

Present the minimal YAML delta for approval. Re-run the generator. Semantic IDs are stable — re-import overwrites cleanly without duplicates.

---

<failed_attempts>
## What DOESN'T Work

- **Using `$var()` in preset attrs:** Broken in current Divi. Use `var(--gvid-xxx)` directly.
- **Stacked module presets for buttons:** CSS cascade conflicts. Each button preset must be self-contained. Variables provide shared values.
- **Group presets for buttons:** Same cascade issue. Avoid entirely for `divi/button`.
- **Omitting `button.decoration.button.desktop.value.enable: "on"`:** Required in every `divi/button` preset individually. Not inherited. No exceptions.
- **Setting button padding on `button.decoration.spacing`:** Hidden from UI, locks value permanently. Always use `module.decoration.spacing`.
- **Skipping Phase 2:** YAML written without confirmed design decisions produces technically valid but visually incoherent output. The phase boundary exists for this reason.
- **Writing YAML without `boilerplate:` key:** The semantic variable system is not in place. The output will be incomplete.
- **Generating JSON without the script:** Too many format requirements. Always use the generator.
- **Importing with Visual Builder open:** The VB save overwrites the import. Every time.
- **Putting colors in `global_variables`:** Silently dropped on import. Colors go through `global_colors` only.
- **`calc(var(--gvid-xxx))` "Invalid unit" warning:** False positive. Works correctly in browser and editor preview.
</failed_attempts>

---

## File Reference

| File | Purpose |
|------|---------|
| [references/boilerplate.json](references/boilerplate.json) | Static base — variable system + primitive presets |
| [references/PHASE-1-GATHER.md](references/PHASE-1-GATHER.md) | Phase 1 detailed instructions |
| [references/PHASE-2-DECISIONS.md](references/PHASE-2-DECISIONS.md) | Phase 2 detailed instructions |
| [references/PHASE-3-YAML.md](references/PHASE-3-YAML.md) | Phase 3 detailed instructions |
| [references/PRESET-COOKBOOK.md](references/PRESET-COOKBOOK.md) | Design recipes — colors, variables, composition |
| [references/DIVI-SPEC.md](references/DIVI-SPEC.md) | Technical rules, bugs, paths, import constraints |
| [references/YAML-SPEC-FORMAT.md](references/YAML-SPEC-FORMAT.md) | Complete brand YAML format reference |
| [references/divi-module-reference.json](references/divi-module-reference.json) | Module element and path reference |
| [references/spec-test.yaml](references/spec-test.yaml) | Working example brand YAML |
| [scripts/generate_divi_variables.py](scripts/generate_divi_variables.py) | Generator — boilerplate + brand YAML → Divi JSON |
| [scripts/extract_module_reference.py](scripts/extract_module_reference.py) | Extracts module reference from Divi source |
