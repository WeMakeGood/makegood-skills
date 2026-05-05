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

### Ownership and Use-Shape Table

**CRITICAL:** Naming an owner is necessary but not sufficient. The build agent will reach for content as it writes a section and restate by default. The proposal must commit to *both* the owner *and* the shape every using module takes when it incorporates the content. See ARCHITECTURE.md, "Single Source of Truth" for the four use-shapes.

Build the table in two passes:

**Pass 1 — identify shared content areas.** A content area is *shared* if more than one module's source set contains it. Examples: organizational identity claims, methodology descriptions, anchor figures, named credentials, cross-cultural constants. Walk through the proposed module set and identify every content area that more than one module would otherwise want to describe.

**Pass 2 — assign owner and use-shape.** For each shared content area:

1. Pick the single owner — the module whose primary purpose is that content area
2. List every other module that needs the content
3. Commit each using module to one of four shapes (see ARCHITECTURE.md):
   - **cross-reference** — pointer only, no restatement
   - **subset (X)** — restate the named subset (one phrase or short sentence) and cross-reference; X names the subset
   - **invocation by name** — name the thing without describing it
   - **reach-beyond** — module instructs agent to load addendum/invoke skill when needed

| Content Area | Owner | Used By | Use-Shape | Rationale |
|--------------|-------|---------|-----------|-----------|
| [Topic] | [Module] | [Modules] | [shape per using module] | [Why this owner, why this shape] |

**Restatement is not a use-shape.** If the table contains an entry where a using module describes the content in its own prose, the table is incomplete. Use one of the four shapes — or move the content to its proper owner.

**Owner-user pairs to think about explicitly:**
- A module that owns rules and another module that needs to apply them (rule owner / rule user)
- A module that owns a constant and adaptations of it (constant owner / regional or contextual users)
- An addendum that owns data and modules that need to invoke or reach for it (data owner / data users)
- A module that owns identity claims and modules that need to operate from those claims (identity owner / operating users)

For each of these pairs in the proposed structure, specify the use-shape explicitly. Do not leave it for Build to decide.

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

### Ownership and Use-Shape Table
(From Step 1 — every shared content area with owner, users, and committed use-shape per using module)

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
PHASE 4 RULES — Read ARCHITECTURE.md before writing any module, including:
- "The Runtime Agent's Perspective" — what the runtime agent does and doesn't know
- "Shape Reference: F0 as a Worked Example" — what mixed-shape content looks like
- "Single Source of Truth" — the four use-shapes

Per-module protocol (PHASE_4_BUILD.md) has 7 steps:
  1. Runtime Frame Set
  2. Commitment Gate
  3. Re-Read Sources
  4. Substantive Source Surface
  5. Section Plan
  6. Write the Module
  7. Self-Check

Steps 4 and 5 are planning artifacts the agent commits to BEFORE writing prose. Skipping them produces narrative-prose modules, build-perspective contamination, and restated canonical content.

- Modules are read by a runtime agent that has no awareness of sources, the build, or the library.
- Use the Ownership and Use-Shape table above. The table commits using modules to specific shapes; do not restate at write-time.
- Quotes and named individuals from sources do not appear in modules. Extract reasoning before generating, in the Section Plan.
- [PROPOSED] marks inferences. [HIGH-STAKES] marks exact-copy content. Both removed before delivery.
- Token budget is room for useful content, not a ceiling. Under-budget modules need more depth.
- When a module fails self-check or user review, follow the failure-recovery protocol. Diagnose the upstream planning gap; do not regenerate prose from scratch.
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
- "Ownership and use-shape table complete: [yes/no — every using module has a use-shape, none rely on restatement]"
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
- Is the Ownership and Use-Shape table correct? Specifically: any content assigned to the wrong owner, any using module that should take a different shape, any shared content area missing from the table?
- Any modules missing, or modules proposed that aren't needed?
- Ready to proceed to Build?

**Generalization check (per F0_agent_behavioral_standards):**

Before approval, work through these questions with the user:

1. **What features of this organization is the proposed architecture depending on?** Name them. (e.g., "the organization has two operational arms with shared infrastructure," "the organization's reasoning is heavily transcript-evidenced rather than codified in strategy docs," "audience reasoning matters in 4 of 6 modules.")

2. **Would the same architecture serve an organization with substantially different features?** If yes, the architecture is generic and may be missing organization-specific reasoning. If no, the dependency on those features is correctly load-bearing.

3. **The shapes the Section Plan will use** (reasoning context, decision framework, prescriptive rule, cross-reference, reach-beyond signal) — are these the right shape categories for this organization's modules? Is there a genuine module need that doesn't fit these five shapes? If so, name it now rather than at write-time, and decide with the user whether to add a shape, recategorize the content, or restructure the module.

4. **The use-shapes** (cross-reference, subset, invocation by name, reach-beyond) — do these cover every owner-user relationship in the table? Is any using module's relationship to its owner being forced into the wrong shape because the right shape isn't on the list?

If any of (3) or (4) surfaces a genuine gap, the framework expands or the architecture changes — do not force the content into an ill-fitting shape. The output of this check is either confirmed framework adequacy or a documented framework adjustment.

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
