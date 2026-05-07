# Building Context Libraries

Transforms organizational source documents into modular context libraries that change how AI agents behave. Modules are metaprompts — system prompt components that shape agent decision-making — not fact sheets.

The skill is built around four architectural commitments that prevent recurring build failures:

- **The runtime agent's perspective is the writing frame.** Modules are read by an agent that has only its loaded modules and a user message — no source files, no proposal, no awareness of the build. Sentences that only make sense inside the build are contamination.
- **Planning precedes prose.** Each module gets a Substantive Source Surface and a Section Plan that commit to shape, source patterns, and use-shape *before* writing. When prose drifts from the plan, the failure-recovery protocol fixes the upstream plan rather than regenerating the prose.
- **Single source of truth is a use-shape commitment.** The proposal's Ownership and Use-Shape table commits every using module to one of four shapes (cross-reference, subset, invocation by name, reach-beyond). Restatement is not a shape.
- **Load discipline is a classification.** Each loadable item in an agent's manifest is `always_load` (governs every output, agent's runtime judgment about loading is unreliable) or `conditional` (applies only in specific contexts, with a `load_when:` trigger written in plain language). F0 (behavioral standards) and S0 (natural prose standards) are hard-rule `always_load` whenever they appear. The classification is decided in Design, not at agent-write time.

## When to Use

Use this skill when you need to:
- Build a context library from organizational documents for AI agents
- Create modular agent context from transcripts, strategy docs, or process documents
- Transform organizational knowledge into behavioral instructions for domain agents

## How to Invoke

Say things like:
- "Build a context library from these source documents"
- "Create agent context from our organizational docs"
- "Transform these documents into a knowledge base for our agents"

## What You'll Need

- A directory of organizational source documents (strategy docs, transcripts, interviews, process docs, notes)
- An output directory for the context library (default: `./context-library/`)
- Optionally: a list of domain agents that will use the library

## What You'll Get

A complete context library:
```
context-library/
├── source-index.md           # Manifest of all sources
├── build-state.md            # Progress tracker
├── process-log.md            # Reasoning history and decision record
├── proposal.md               # Approved structure
├── modules/
│   ├── foundation/           # Universal context (all agents)
│   ├── shared/               # Cross-functional (multiple agents)
│   └── specialized/          # Domain-specific (single agents)
├── addenda/                  # Volatile reference data (on-demand)
└── agents/                   # Agent definitions with module assignments
```

## Process

The build runs in 4 phases across 3 sessions. Phase 2 (Comprehend) is internally split into two passes — recognition and synthesis — with a mandatory session break between them.

| Phase | What Happens | You'll Review |
|-------|-------------|---------------|
| **Setup** | Source inventory, classification, initial expectations per agent | File list, agent needs, expectations, gaps |
| **Comprehend Pass 1 (recognition)** | Deep reading; observational artifacts written at the moment of reading (per-source notes, signal log, expectations-vs-findings, conflicts) | Recognition outputs and conflict types |
| *(mandatory session break)* | | |
| **Comprehend Pass 2 (synthesis)** | Sources mostly out of context; synthesis with cognitive room for lateral moves (pattern-pointers, convergences, cross-domain parallels, agent-needs) | Synthesis outputs and refined agent roles |
| *(mandatory session break)* | | |
| **Design** | Module architecture, agent definitions, ownership and use-shape table | Complete structural proposal |
| **Build** | Module writing with per-module quality gates and a planning artifact per module | Finished library |

The two-pass structure for Comprehend exists because single-pass synthesis on a large source set produces sector-applicable rather than organization-specific patterns. Recognition needs sources loaded; synthesis needs sources mostly out of context. The break makes both possible.

## Tips

- Provide the messiest, most complete set of source documents you have — the skill handles transcripts and raw notes directly
- If you know what agents you want, mention them upfront; otherwise the skill derives them from the sources
- Review the proposal carefully in Design — it's much easier to restructure before modules are written, and the Ownership and Use-Shape table is much harder to revise once Build has started
- Token budgets are room for useful content, not ceilings — if an agent seems thin, ask for richer modules

## Redoing a Build After a Rollback

If a build attempt produced a library you needed to roll back, tell the skill at the start of the next session that this is a redo. The redo-session protocol moves retrospective documents and prior-attempt module files to an archive (so they cannot anchor the new attempt) and gathers from you a list of *named failure patterns* to avoid. The build agent regenerates from the proposal and sources, not from retrospective examples.

## Migrating a Library to a Newer Skill Version

If you maintain a library built with an earlier skill version and the manifest format has changed, the bootstrap will detect the format mismatch and offer to run the migration phase. Migrations are versioned and applied in order — each migration brings artifacts from one specific format version to the next. The 1.4 → 1.5 migration converts agent manifests from tier-grouped to `always_load`/`conditional` classification; future migrations will be added as further format changes ship.
