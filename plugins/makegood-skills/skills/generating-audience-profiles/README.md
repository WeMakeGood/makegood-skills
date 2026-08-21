# generating-audience-profiles

A Claude Code skill that generates audience profile research artifacts — a matrix of audience dimensions and activatable sub-profile metaprompts — as upstream input for building-context-libraries.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

Marketing and communications agencies typically build audience definitions as personas: a named individual with biographical detail ("Mary, 34, two children, Instagram every night"). That shape helps a human marketer imagine the audience. It actively hurts an LLM, which anchors on the specifics, generalizes them into rules, and loses the organization's actual decision question.

This skill produces a structurally different artifact. The output is a **matrix of audience dimensions** plus **activatable sub-profile modules** — decision-frame metaprompts that shift agent generation when an audience dimension is active. The matrix shape allows RAG-style loading of only the dimensions relevant to the current session, instead of ambient persona context that distorts every output.

The skill is upstream of [building-context-libraries](https://github.com/WeMakeGood/building-context-libraries). Its output becomes a source document the library build then consumes, alongside the organization's other research, to design audience-aware agents.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "Generate audience profiles from this research directory"
- "Build an audience matrix for this context library"
- "Design audience modules for the new context library"
- "Develop audience definitions from this research"
- "Create audience research artifacts from these peer org dossiers"

It activates when research documents, strategy materials, or peer organization dossiers are provided via file path or directory.

## What you'll need

- A directory of source documents (the skill handles mixed source sets):
  - **Direct audience research** (interviews, surveys, ethnographic notes) — increasingly rare
  - **Competitive/sector research** (peer org dossiers, sector synthesis memos)
  - **Internal strategy and program documents** (theory of change, strategic plans, brand guidelines)
- An audience question — what the organization would use these profiles to *decide*
- An output path (default: `./audience-profiles/`)
- *Optional:* a target context library this artifact will feed into

The skill also generates and tests an LLM-modeled-data picture as a fourth source class — required under F0 sourcing discipline whenever the model's audience knowledge is being drawn on.

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `generating-audience-profiles-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/generating-audience-profiles/releases).
2. Unzip into your Claude Code skills directory:
   ```
   unzip generating-audience-profiles-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills).

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/generating-audience-profiles.git ~/.claude/skills/generating-audience-profiles
```

## What you'll get

```
<OUTPUT_PATH>/
├── audience-matrix.md              # Top-level matrix: dimensions, cells, status, triggers
├── modules/                        # One sub-profile module per substantive cell
│   ├── [dimension-coordinate].md
│   └── ...
├── source-index.md                 # Sources classified by class (A direct / B competitive / C internal / D modeled)
├── process-log.md                  # Build agent reasoning, considered-and-rejected, modeled-data tests
├── build-state.md                  # Session resume state
└── comprehension-artifacts/        # Pass 1 per-source notes, signal log, conflicts, modeled-data pictures
    └── ...
```

The matrix is the navigation; the modules are the substance. Each substantive cell becomes a sub-profile module — a short metaprompt (200–600 words) that shifts the downstream agent's generation when that audience dimension is active.

## How it works

| Session | Phases | Function |
|---------|--------|----------|
| A | Setup + Comprehend Pass 1 (Recognition) | Load and classify sources, write initial expectations, per-source notes, signal log, conflicts |
| **MANDATORY BREAK** | | Synthesis needs sources mostly out of context |
| B | Comprehend Pass 2 (Synthesis) + Design | Surface and test modeled-data, propose dimensions, construct matrix |
| **MANDATORY BREAK** | | Build needs per-module gates fresh |
| C | Build | Write sub-profile modules with per-module runtime-frame and source-surface gates |

Both session breaks are mandatory. Single-pass synthesis on a saturated source context collapses toward sector-applicable rather than organization-specific dimensions.

## What's in this repo

- `SKILL.md` — the skill itself, loaded by Claude Code when activated
- `references/ARCHITECTURE.md` — design philosophy, source classes, dimension selection, matrix shape, modeled-data discipline, downstream handoff
- `references/phases/` — per-phase instructions (Setup, Comprehend Pass 1, Comprehend Pass 2, Design, Build)
- `templates/` — scaffolds for build-state, process-log, source-index, matrix, sub-profile module, per-source notes, signal log, modeled-data picture, suggested-default dimensions
- `examples/` — representative example output

## Tips

- **Get the audience question right.** "What would your team use these profiles to *decide*?" — not "describe your audience." Wrong question produces wrong dimensions; wrong dimensions produce profiles that don't shift agent behavior.
- **Don't force every cell substantive.** Empty cells are diagnostic. A matrix where every cell has content usually reflects paper-over, not coverage.
- **Treat modeled-data as a source class with its own discipline.** The skill generates a Class D modeled-data picture in Phase 2 Pass 2, surfaces references where the model can identify them, and tests every claim against client and competitive sources before it appears in a module. Untested modeled-data stays in the process log.
- **The artifact is upstream input, not a finished library module.** building-context-libraries' Phase 2 reads this artifact during its own Comprehend phase. The matrix and modules are inputs to library design — the library skill decides where audience context lives, how it loads, and what shape it takes inside the library.

## Version history

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT — see [LICENSE](LICENSE).

## About Make Good

[Make Good](https://wemakegood.org) is a consultancy that partners with mission-driven organizations through new terrain — scaling, technology adoption, leadership transitions, strategic evolution. We publish our skills openly because the methodology is meant to be portable.

For other skills in this collection, see the [Make Good skills index](https://github.com/WeMakeGood/makegood-skills).
