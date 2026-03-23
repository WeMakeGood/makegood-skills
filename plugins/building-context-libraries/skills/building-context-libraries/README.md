# Building Context Libraries

Transforms organizational source documents into modular context libraries that change how AI agents behave. Modules are metaprompts — system prompt components that shape agent decision-making — not fact sheets.

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

The build runs in 4 phases across 2-3 sessions:

| Phase | What Happens | You'll Review |
|-------|-------------|---------------|
| **Setup** | Source inventory and classification | File list, agent needs, gaps |
| **Comprehend** | Deep reading for behavioral patterns | Patterns, convergences, tensions |
| **Design** | Module architecture and agent definitions | Complete structural proposal |
| **Build** | Module writing with per-module quality gates | Finished library |

There's a mandatory session break between Comprehend and Design to keep critical instructions fresh in context.

## Tips

- Provide the messiest, most complete set of source documents you have — the skill handles transcripts and raw notes directly
- If you know what agents you want, mention them upfront; otherwise the skill derives them from the sources
- Review the proposal carefully in Design — it's much easier to restructure before modules are written
- Token budgets are room for useful content, not ceilings — if an agent seems thin, ask for richer modules
