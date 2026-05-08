# [Library Name]

Context library for [organization]. Each agent file in `agents/` is a system-prompt preamble that loads the modules and addenda the agent needs to do its work.

## Library Structure

```
.
├── agents/                      Source agent files (with @-include directives)
├── modules/                     Reasoning context — how the organization thinks
│   ├── foundation/              Universal organizational context (F-prefix)
│   ├── shared/                  Cross-functional content (S-prefix)
│   └── specialized/             Per-agent domain content (D-prefix)
├── addenda/                     Reference data (volatile facts, lookup tables)
├── scripts/
│   └── build-deploy-bundles.py  Resolves @-includes into self-contained bundles
└── deploy/                      (gitignored — generated bundles)
    └── agents/
        ├── <name>.md            Standard bundle: required-reading inlined
        └── <name>.all-inclusive.md  Optional: required-reading + conditional addenda
```

## Agent File Shape

Each agent file in `agents/` has four sections:

- **`## Required Reading`** — `@`-include directives, one per line. Content the agent needs from turn one. Always-load.
- **`## Conditional Loads`** — table of files the agent loads when their trigger applies to the work in front of it. Conditional.
- **`## Ask the [Role]`** — escalation triggers. Situations where the agent defers to a human rather than answers.
- **`## Domain Guidelines`** — Do/Don't behavioral guidance specific to the agent's domain.

## Deploying to a Runtime

The library supports two deployment patterns based on the runtime's capabilities.

### Claude Code (or other `@`-aware runtimes)

Load the source agent file directly from `agents/<name>.md`. Claude Code expands `@`-include directives natively at load time — the included content is in the system prompt before the model's first turn. Conditional addenda are loaded by the agent when their triggers fire (the runtime has file-tree access).

No bundle build required. Edit agent files and modules directly; changes take effect on next session.

### Claude.ai project upload, Cowork, generic API integrations

These runtimes don't process `@` directives. Use the generated bundles in `deploy/agents/` instead.

**Build the bundles:**

```bash
scripts/build-deploy-bundles.py
```

This produces `deploy/agents/<name>.md` for each agent — a self-contained file with all required-reading content inlined. Upload the standard bundle as the system prompt for the agent.

**Conditional addenda** still live in their original locations (`addenda/...`). Upload them to the runtime's project files alongside the bundle. The agent reads the Conditional Loads table at runtime and pulls the right addendum when a trigger fires (the runtime's retrieval mechanism surfaces the relevant file).

**If the runtime's conditional fetch is unreliable** — the agent recognizes a trigger fires but can't load the addendum — use the all-inclusive variant:

```bash
scripts/build-deploy-bundles.py --all-inclusive
```

This produces `deploy/agents/<name>.all-inclusive.md` for each agent. The variant inlines every conditional addendum's content alongside required-reading content. The Conditional Loads table is preserved so the agent retains per-work selectivity over already-loaded content.

The trade-off: the all-inclusive bundle is significantly larger (every conditional carried whether the work needs it or not) and pays the token cost on every turn. The standard bundle is the default; the all-inclusive variant is the documented fallback for runtimes where conditional fetch reliability is a production problem.

## Editing the Library

Edit source files in `agents/`, `modules/`, and `addenda/`. After edits:

```bash
scripts/build-deploy-bundles.py --check
```

Reports DRIFT if bundles are out of sync with sources. Rebuild with:

```bash
scripts/build-deploy-bundles.py                  # standard bundles
scripts/build-deploy-bundles.py --all-inclusive  # all-inclusive variants
```

Build a single agent's bundle: `scripts/build-deploy-bundles.py --agent <name>`.

## Why the Architecture Looks This Way

Always-load content (everything in `## Required Reading`) governs every output the agent produces. The agent's runtime judgment about whether to load it is unreliable — the failure mode that originated the architecture was an agent skipping a critical load and producing output that violated the loaded item's standards. The `@`-include + bundle approach removes the agent from the load decision entirely. Required Reading content is in the system prompt from turn one in every supported runtime.

Conditional addenda stay separate because they're work-specific. Inlining all of them by default would force every output through every funder profile, every cultural context, every project — defeating the conditional structure. The Conditional Loads table tells the agent *which* addendum applies to the work in front of it, not whether to attend to all of them.

The all-inclusive bundle exists for runtimes where the conditional approach's runtime dependency (work-time file fetch or retrieval) is unreliable. It trades token weight for runtime independence. Most deployments don't need it.

For the full architectural reasoning, see the skill's [ARCHITECTURE.md](https://github.com/WeMakeGood/skill-building-context-libraries) — specifically "Load Discipline," "Always-Load Delivery," and "Trigger Discipline."
