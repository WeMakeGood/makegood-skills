# building-context-libraries

A Claude Code skill that builds modular context libraries from organizational source documents. The output is metaprompt modules — system prompt components that change how AI agents behave — not fact sheets or documentation.

Maintained by [Make Good](https://wemakegood.org).

---

## What this skill does

When you point Claude Code at a directory of organizational documents (transcripts, strategy docs, process notes, interviews), this skill:

1. Reads the sources in two passes — first for recognition, then for synthesis
2. Designs a module architecture with explicit ownership and use-shape commitments
3. Writes context modules that are tested for behavioral effect on agents, not for prose quality
4. Produces a complete library: foundation modules, shared modules, specialized modules, addenda, and agent definitions

The skill enforces transformation at every phase. Modules that an agent could ignore without behavioral change are treated as failures, not finished work.

## When Claude Code activates this skill

Claude Code will load this skill when you say things like:

- "Build a context library from these source documents"
- "Create agent context from our organizational docs"
- "Transform these documents into a knowledge base for our agents"
- "Build domain context for [agent role]"

The skill activates automatically when organizational source documents are provided via file path or directory.

## What you'll need

- A directory of organizational source documents (the messier and more complete, the better — the skill handles transcripts and raw notes directly)
- An output directory for the context library (default: `./context-library/`)
- Optionally: a list of domain agents that will use the library (the skill can derive these from sources if you don't have them yet)

## Installation

### Option 1: Install via the Make Good aggregator plugin (recommended)

If you're using Claude Code with plugin support, install all Make Good skills at once:

```
/plugin install makegood-skills@makegood-skills
```

### Option 2: Install this skill directly (ZIP)

1. Download the latest `building-context-libraries-<version>.zip` from the [Releases page](https://github.com/WeMakeGood/building-context-libraries/releases).
2. Unzip it into your Claude Code skills directory:
   ```
   unzip building-context-libraries-<version>.zip -d ~/.claude/skills/
   ```
3. Restart Claude Code (or reload skills) so the new skill is registered.

### Option 3: Clone for development

```
git clone https://github.com/WeMakeGood/building-context-libraries.git ~/.claude/skills/building-context-libraries
```

## What you'll get

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

## How the build runs

The build runs in 4 phases across 3 sessions. Phase 2 (Comprehend) splits internally into two passes — recognition and synthesis — with a mandatory session break between them.

| Phase | What happens | You'll review |
|-------|-------------|---------------|
| **Setup** | Source inventory, classification, initial expectations per agent | File list, agent needs, expectations, gaps |
| **Comprehend Pass 1** | Deep reading; observational artifacts written at the moment of reading | Recognition outputs and conflict types |
| *(session break)* | | |
| **Comprehend Pass 2** | Sources mostly out of context; synthesis with cognitive room for lateral moves | Synthesis outputs and refined agent roles |
| *(session break)* | | |
| **Design** | Module architecture, agent definitions, ownership and use-shape table | Complete structural proposal |
| **Build** | Module writing with per-module quality gates | Finished library |

The two-pass structure exists because single-pass synthesis on a large source set produces sector-applicable rather than organization-specific patterns. Recognition needs sources loaded; synthesis needs sources mostly out of context. The break makes both possible.

## What's in this repo

- `SKILL.md` — the skill itself, loaded by Claude Code when activated
- `references/` — architecture documentation and templates the skill consults during a build
  - `ARCHITECTURE.md` — runtime perspective, module design, use-shapes, load discipline
  - `TEMPLATES.md` — module, agent, addendum, and proposal templates
  - `COMPREHENSION_TEMPLATES.md` — Phase 2 artifact templates
  - `phases/` — one self-contained instruction file per build phase, including migration
- `scripts/` — utility scripts the skill runs during builds
  - `analyze_sources.py`, `count_tokens.py`, `create_source_index.py`, `validate_library.py`, `verify_module.py`
- `templates/` — runtime templates the skill copies into a build (e.g., `build-state.md`)
- `examples/` — representative example output from a real build

## Tips

- Provide the messiest, most complete set of source documents you have
- If you know what agents you want, mention them upfront; otherwise the skill derives them from the sources
- Review the proposal carefully in Design — restructuring is much easier before modules are written
- Token budgets are room for useful content, not ceilings — if an agent seems thin, ask for richer modules

## Version history

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT — see [LICENSE](LICENSE).

## About Make Good

[Make Good](https://wemakegood.org) is a consultancy that partners with mission-driven organizations through new terrain — scaling, technology adoption, leadership transitions, strategic evolution. We publish our skills openly because the methodology is meant to be portable.

For other skills in this collection, see the [Make Good skills index](https://github.com/WeMakeGood/makegood-skills).
