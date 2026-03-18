# Phase 3: Design

> **CRITICAL RULES — Read these first:**
> - **Read [references/ARCHITECTURE.md](../ARCHITECTURE.md) now.** Design decisions depend on understanding module hierarchy, single source of truth, content transformation, and token budgets.
> - The proposal describes STRUCTURE — module names, purposes, source mappings, agent assignments. It contains ZERO organizational content.
> - Agent definitions belong HERE, not after modules are built. Who needs what context is a structural question.
> - Before committing to a structure, generate at least one alternative. The first framing is rarely the best.
> - Apply the Source Before Statement gate — don't invent organizational details for the proposal.

---

## What This Phase Does

Transform comprehension findings into a complete structural proposal: what modules to build, what each one does, which sources feed each module, which agents load which modules, and how the token budget allocates. The output is a proposal document the user approves before any module is written.

---

## Session Loading Gate

**This phase starts a new session.** You have nothing in context from the previous session except what you load now.

**GATE:** Before any design work, load in this order:
1. Read [references/ARCHITECTURE.md](../ARCHITECTURE.md) — module design philosophy, transformation rules, token budgets
2. Read `<OUTPUT_PATH>/build-state.md` — comprehension findings, agent roles, gaps
3. Read `<OUTPUT_PATH>/process-log.md` — decisions and corrections from earlier phases
4. Read `<OUTPUT_PATH>/source-index.md` — the complete source inventory
5. Read every source file in the index. Not key sources — every source. Module architecture determines which organizational reasoning goes where. You cannot make that determination without the full source set in context.

Write to the build state: "Design session loaded: ARCHITECTURE.md, build-state, source-index, and [count] source files re-read"

**Do not proceed to Step 1 until all sources are loaded.** Design decisions made without source files in context produce structures based on memory, not evidence. The agent that skips sources during Design will assign content to the wrong modules — or miss modules entirely.

---

<phase_design_structure>
## Step 1: Design Module Architecture

Working from your comprehension findings (reasoning patterns, convergences, agent roles), propose the module structure.

**For each proposed module:**
- **Name and tier** (Foundation/Shared/Specialized)
- **Purpose** — one sentence: what organizational reasoning does this module provide? Not what procedures it encodes — what it equips the agent to *think about*.
- **Source files** that feed this module
- **Key reasoning patterns** from comprehension that this module captures
- **Estimated tokens** (2,000-4,000 per module is typical)

**Design principles (from ARCHITECTURE.md):**
- Organize for USE, not taxonomy. "What reasoning does this equip?" not "What category does this fit?"
- Each module serves a coherent domain of organizational thinking
- Modules under 1,000 tokens are too thin — they lack the reasoning context to be useful
- Guide, don't catalog — principles and tradeoffs over inventories and procedures

### Addenda

Identify volatile data that should be addenda rather than module content:
- **A0: Organizational Reference** (default — always include): Legal entity name, EIN, entity type, addresses, website URLs, key contact information. Every library needs this.
- Pricing, rates, fee structures
- Biographical details
- Service catalogs, team rosters
- Counts of things that change

For each addendum: name, what data it contains, which modules reference it.

### Shared Source Ownership Table

**CRITICAL:** Create a table assigning each content area from shared sources to exactly ONE module. This prevents duplication during the Build phase.

| Content Area | Source File(s) | Assigned Module | Rationale |
|-------------|---------------|-----------------|-----------|
| [Topic] | [File] | [Module] | [Why here and not elsewhere] |

### Audience Reasoning Check

**Which modules govern how the agent interacts with people or produces content for them?** Those modules need audience needs reasoning — a framework for how the agent thinks about the humans on the other end.

- **Modules governing engagement, qualification, or relationship management** need reasoning about what the people/organizations the org serves actually need. Frame as interacting needs on spectrums, not persona types.
- **Modules governing content production or communication** need reasoning about what readers need from specific pieces of content. Frame as active needs that combine and shift by context, not fixed audience profiles.

Audience reasoning belongs *inside* existing modules as sections, not as a separate "audience" module. It's a behavioral extension of existing reasoning domains.

**Anti-patterns to flag in the proposal:**
- Persona profiles ("the skeptic," "the executive director") — these create boxes and force classification
- Sector-based audience models ("faith-based audiences need X") — sector correlates with needs but doesn't determine them
- Static audience definitions — needs shift by context; the same person has different active needs reading a case study vs. a thought leadership piece

### Standard Guardrails

Copy these from `templates/guardrails/` into the library:
- `F0_agent_behavioral_standards.md` → loaded by ALL agents
- `S0_natural_prose_standards.md` → loaded by external-facing agents

---

## Step 2: Design Agent Definitions

For each agent role (refined in Comprehend):

- **Agent name and domain**
- **Role** — focused on actions and decisions, not knowledge areas. "Handles [what] and recommends [what]" not "Knows about [topic]"
- **Modules to load** — Foundation + relevant Shared + Specialized
- **Addenda available** — reference data the agent can consult on demand
- **Estimated total tokens** — sum of all loaded modules (excluding addenda)
- **Budget assessment** — is this agent well-served by its module set? An agent at 60% of budget may need richer modules or additional context

**Budget check:** Each agent's module total should use the budget well — neither cramped over 100% nor starved under 50%. If agents are consistently under-budget, the modules are likely too thin or there's missing content. If over-budget, look for duplication or modules the agent doesn't actually need.

---

## Step 3: Alternative Structure Check

**Before committing:** Generate at least one alternative module architecture. Compare:
- What does each structure gain?
- What does each structure lose?
- Which better serves the agent roles?

Choose — and document why. This is required, not optional.
</phase_design_structure>

---

<phase_design_proposal>
## Step 4: Write the Proposal

Create `<OUTPUT_PATH>/proposal.md` with:

### Library Overview
- Source document count and types
- Target model and context window
- Agent count and roles

### Module Architecture
For each module (Foundation → Shared → Specialized):
- Module ID and name
- Tier
- Purpose (one sentence — what organizational reasoning it provides)
- Source files feeding this module
- Estimated tokens

### Addenda
For each addendum:
- Name
- Data contents
- Source files
- Which modules reference it

### Shared Source Ownership Table
(From Step 1 — the complete assignment of content areas to modules)

### Agent Definitions
For each agent:
- Name and role
- Modules loaded (with token estimates)
- Addenda available
- Total estimated tokens
- Budget utilization (% of 10% context window)

### Gaps and Limitations
- BLOCKING gaps resolved (how)
- LIMITING gaps accepted (impact)
- ENHANCING gaps noted (low priority)

### Conflicts Resolved
- What conflicted, how it was resolved, user's decision

### Build Plan
- Recommended build order for modules
- Which modules share sources (highest duplication risk — build these with extra cross-reference checking)

**EMBEDDED RULES FOR PHASE 4 (survives context compaction):**
```
PHASE 4 RULES — Read ARCHITECTURE.md before writing any module.
- Modules provide reasoning context — how the organization thinks. Not procedures. Not "If X, do Y" rules.
- Re-read sources in the same turn you write each module.
- Check the Shared Source Ownership table before writing — if content is assigned elsewhere, cross-reference.
- Every module should tell the agent when to reach beyond itself — load addenda, invoke skills, or ask the user.
- [PROPOSED] marks inferences. [HIGH-STAKES] marks exact-copy content. Both removed before delivery.
- Token budget is room for useful content, not a ceiling. Under-budget modules need more depth.
```
</phase_design_proposal>

---

## GATE

Write to the build state:
- "Module count: [N] (Foundation: [n], Shared: [n], Specialized: [n])"
- "Addenda count: [N]"
- "Agent count: [N]"
- "All agents within budget: [yes/list exceptions]"
- "Under-budget agents flagged: [list or 'none']"
- "Alternative structure considered: [what, why rejected]"
- "Shared source ownership table complete: [yes/no]"
- "Guardrail modules copied: [yes/no]"
- "BLOCKING gaps resolved: [yes/list remaining]"

---

## STOP

**Present to the user:**
- The complete module architecture — names, tiers, purposes, source mappings
- Agent definitions — who loads what, token budgets, budget utilization
- The shared source ownership table — how shared content is assigned to prevent duplication
- Addenda — what volatile data is separated and where
- The alternative structure you considered, with tradeoffs
- Any gaps or limitations and their expected impact
- The recommended build order

**Ask:**
- Does this module structure serve what your agents need to do?
- Are the agent definitions right — roles, module assignments, budget utilization?
- Is the shared source ownership correct — any content assigned to the wrong module?
- Any modules missing, or modules proposed that aren't needed?
- Ready to proceed to Build?

**Do not proceed until the user approves the proposal.**

**After the user responds, log to `process-log.md`:**
- Why this module structure was chosen over the alternative
- User feedback on the proposal — what changed, what was confirmed
- Any scope decisions or tradeoffs that shaped the final structure
- Agent role decisions and their rationale

---

## After This Phase

Update build state:
- **Current phase:** Phase 4 (Build)
- **Next phase file:** `references/phases/PHASE_4_BUILD.md`

Proceed to Build in the same session if context allows. If the Design session was long, start a new session — the Build phase needs ARCHITECTURE.md and the metaprompt transformation rules fresh in context.
