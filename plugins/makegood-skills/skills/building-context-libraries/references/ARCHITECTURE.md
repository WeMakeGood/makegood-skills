# Context Library Architecture

## The Runtime Agent's Perspective

Modules are system prompt components for a runtime agent. The runtime agent reads its system prompt (the modules loaded for it) and a user message — nothing else. It has no awareness of:

- Source files, source documents, or anything called "the source set"
- The build process, the build agent, or that there was a "library being constructed"
- The proposal, the build-state file, or any document outside its loaded modules
- Dates of source documents, document authors, or anything about when or how a module came to exist
- Other modules' contents except by explicit cross-reference

Anything in a module that only makes sense to a reader who knows about the build is contamination, not context. A runtime agent encountering "the library doesn't carry the underlying detail" or "in some 2025-era sources" reads instructions about a library it has no access to and information it cannot consult.

The test for runtime-frame contamination is not whether the sentence contains specific build-perspective phrases. It is whether **the sentence makes sense to a reader who knows nothing about how this module came to exist**. Phrases that almost always indicate contamination:

- "the source set" / "source documents" / "the sources"
- "the library" / "this library" / "the build" / "the build agent"
- Any reference to a specific source file by name or path
- Dates attached to document provenance ("in 2025-era sources," "the late-2024 strategy doc")
- "as documented in" / "per the [document type]" — when "the document" is a source file
- Any sentence that explains why something is or isn't in the module

The runtime agent reads modules as instruction. It is not interested in why one piece of information is here and another is elsewhere; it cannot consult what is elsewhere.

---

## Modules Instantiate Organizational Thinking, Not Procedures

Context libraries exist so agents can do meaningful work on behalf of an organization. Modules are not fact sheets or procedure manuals — they are system prompt components that give the agent the organization's reasoning patterns, principles, and contextual knowledge. An agent with well-built modules can handle situations the module author never anticipated, because it understands *how the organization thinks*, not just what it does in specific scenarios.

### Content vs. Context vs. Metaprompting

Source documents contain **content** (raw facts). The agent building this library defaults to copying content into modules because it's easier than transformation. This produces modules that are useless — fact sheets an agent reads but doesn't act on.

| Level | What It Is | What It Sounds Like |
|-------|-----------|---------------------|
| **Content** (source material) | Raw facts from documents | A list of what the organization offers, how many people it employs, where it operates |
| **Context** (minimum bar) | Processed knowledge that shapes reasoning | The relationship between those facts — why one offering fits one situation and not another, what constrains capacity, what the numbers actually mean for decision-making |
| **Metaprompting** (target) | Reasoning context that equips the agent to think well | The principles behind the organization's choices — what it prioritizes when values are in tension, how it evaluates opportunities, what "success" means in its terms. An agent grounded in this can handle situations the module author never anticipated. |

**The transformation pattern:** Content states what exists. Context explains why it matters. Metaprompting gives the agent the organization's way of thinking so it can reason about new situations — not just the ones you enumerated.

**Every module section should be context or metaprompting.** The transformation test:

1. **Does this give the agent the reasoning it needs to handle novel situations?** Content doesn't. Context/metaprompting does.
2. **Could the agent apply this to a situation the module author didn't anticipate?** If the module only works for pre-specified scenarios, it's too prescriptive.
3. **Does this read like organizational wisdom or like a procedure manual?** Modules should read like the former.

### What Metaprompting Is and Isn't

Metaprompting equips the agent to think like someone from the organization. It is NOT a list of "If X, do Y" rules. The hierarchy of module content, from most to least valuable:

1. **Reasoning context** (primary) — The organization's principles, values, tradeoffs, and ways of thinking. An agent grounded in these can handle situations no one anticipated.

2. **Decision frameworks** (when needed) — Not "If X, do Y" but "When you encounter X, consider these factors. The organization weighs B most heavily because [reason]." The agent makes the decision; the module equips it to weigh correctly.

3. **Prescriptive rules** (rare — only for genuine constraints) — Hard rules that exist because violating them causes real organizational harm. Most module content should NOT be prescriptive rules.

4. **Reaching beyond modules** — The agent should recognize when it needs something modules don't provide: specific data (load an addendum), a capability (invoke a skill), or human judgment (ask the user). Modules that try to contain everything produce agents that never ask for help.

**The prescriptive-rule trap:** The default when writing modules is to convert every organizational pattern into "If X, do Y" rules. This feels like transformation because it's no longer raw content — but it produces agents that can only handle situations you enumerated. The better transformation is to capture *why* the organization does what it does, so the agent can reason about new situations the same way the organization would.

### Writing for LLM Consumption

**LLMs process context differently than humans:**
- LLMs read the entire context; humans scan and skip
- LLMs don't need explanations of concepts they already know
- LLMs benefit from explicit decision criteria and conditional logic
- LLMs can't follow external links or reference other documents not in context
- LLMs work best with direct, declarative statements

**Write reasoning context, not summaries:**

| Instead of... | Write... |
|---------------|----------|
| A fact about headcount or team size | The principle that defines capacity — what actually constrains the organization's ability to take on work, and why the obvious metric is misleading |
| A list of service offerings or programs | The reasoning behind how offerings map to situations — what the organization is actually trying to achieve with each one, and what determines which fits |
| "It's important to understand that..." | State the principle directly |
| "See [external document] for details" | Encode the reasoning in the module; reference addenda for volatile data |
| Varied synonyms for style | Consistent terminology throughout |

**Token efficiency matters:**
- Every token costs money and consumes context window
- Cut preambles, transitions, and hedging language
- Front-load reasoning context and principles, then supporting specifics
- Don't explain what Claude already knows (general concepts, industry basics)

**Effective module patterns:**

The examples below show the *shape* of each pattern, not content to reproduce. The actual content comes from your organization's sources.

*Reasoning context (primary — equips the agent to think):*
Captures the organization's principles and way of evaluating situations. Includes a reach-beyond signal.
```markdown
## [Domain] Philosophy

[The organization's core principle for this domain — what it prioritizes
when values are in tension. Written as organizational identity, not as
rules for the agent.]

[How this principle applies to the agent's work — what it means for the
decisions the agent will face.]

[Reach-beyond signal: when the agent should load an addendum, invoke a
skill, or ask the user instead of acting from module content alone.]
```

*Decision framework (secondary — when the agent needs to weigh factors):*
Names the factors and their relative weight. The agent makes the decision.
```markdown
## [Decision Area]

When [situation the agent will face], weigh these factors:
- [Factor A] (most important — [why])
- [Factor B] ([what it determines])
- [Factor C] ([what it determines])

[The tradeoff the organization has already resolved — when it accepts
a suboptimal outcome on one factor because another matters more.]

[Signal for when to escalate to the user rather than decide.]
```

*Prescriptive rule (rare — only for genuine constraints):*
Exists because violation causes real organizational harm, not because it's a common situation.
```markdown
[Hard constraint — a single sentence stating what must or must not happen,
with no flexibility. Reserve for situations where the organization has
determined that violating this rule causes irreversible damage.]
```

The first two patterns equip the agent to handle situations the author didn't anticipate. The third is a hard constraint. Most module content should look like the first two.

---

## Shape Reference: F0 as a Worked Example

`templates/guardrails/F0_agent_behavioral_standards.md` is a working module — every library copies it verbatim into Foundation. It is also a worked example of mixed-shape content for a reasoning-context-primary module. Reference it when uncertain what shape a section should take.

F0 illustrates three shapes coexisting in one module:

**Process gates as upstream-operation prescriptive rules.** F0's five process gates ("Source Before Statement," "Mark the Move," "Reframe Before Committing," "Second-Order Check," "Generalization Check") are prescriptive — they tell the agent what to do in a defined sequence. They earn the prescriptive shape because violation produces specific, recognizable failures (unsourced claims, conflated epistemic statuses, unconsidered framings). When a module has genuine constraints whose violation causes real harm, prescriptive shape is correct. Note that even the gates are not "if X, do Y" rules for runtime decisions — they are upstream operations the agent performs *before* generating substantive output.

**HIGH-STAKES Content section as decision framework.** F0's HIGH-STAKES section names two conditions that must both be true ("an error would cause significant harm that is difficult or impossible to undo, and accuracy depends on organizational specifics that require verified sourcing"), and three things required when both are met (cite source, reproduce exact details, flag for verification). The agent makes the determination of whether content is HIGH-STAKES; the module gives it the factors to weigh. This is decision-framework shape — naming factors rather than enumerating cases.

**Uncertainty section as pure reasoning context.** F0's Uncertainty section reads: "Confidence calibration is not a formatting requirement — it's an epistemic one. The language used to convey a claim should accurately reflect how much the agent actually knows about it..." There are no rules and no factors. It is the reasoning the organization wants the agent to internalize, written as instruction to the agent ("the practical discipline is to notice the actual epistemic status of each claim before stating it"). This is reasoning-context shape — the most common shape for identity, philosophy, and values modules.

**What F0 is not:** F0 is not third-person prose about the organization. It does not say "the organization values accurate sourcing." It says "Before generating any substantive claim, complete this sequence." Reasoning-context shape is *instruction* — second-person or imperative — that gives the agent the organization's way of thinking.

When writing a module whose primary content is values, identity, or philosophy, the default shape is reasoning context. Decision frameworks appear when the agent will face a recurring choice the organization has thought through. Prescriptive rules appear rarely, only for genuine constraints. The mix in F0 is roughly: 40% prescriptive (the process gates, which are upstream operations not runtime rules), 20% decision framework (HIGH-STAKES), 40% reasoning context (Uncertainty, Error Correction, Professional Challenge, Analytical Depth Requirements).

---

## Content Transformation

Modules contain synthesized organizational knowledge — not source material. Transform content for LLM consumption.

### What Goes In vs. Stays Out

**Include in modules:**
- Organizational principles, values, and reasoning patterns (the *why* behind decisions)
- Positioning and identity (how the organization sees itself and wants to be understood)
- Decision frameworks (what factors to weigh, not what to decide)
- Tradeoffs the organization has already resolved (and why)
- Team structure and roles as context for how the organization operates
- Verified facts (names, dates, figures) that ground the reasoning
- Signals for when to reach beyond modules — load addenda, invoke skills, or ask the user

**Do NOT include:**
- Verbatim quotes (synthesize the meaning instead)
- Client names or specific testimonials
- Step-by-step procedures (capture the reasoning and principles; the agent or a skill handles execution)
- Historical context unless it explains current reasoning
- Competitive details that may become outdated
- Personal anecdotes or stories
- Exhaustive "If X, do Y" rules for every scenario (capture the reasoning; the agent applies it)

### Transforming Transcripts and Interviews

Transcripts are the messiest source type. Machine transcription adds errors. Conversational speech includes filler words, false starts, tangents, and incomplete thoughts. Your job is to extract the *meaning* and discard the mess.

**What transcripts contain (discard or transform all of this):**
- Filler words: "um," "uh," "you know," "like," "I mean"
- False starts: "We usually — well, actually we sometimes —"
- Tangents and digressions
- Conversational hedging: "I think maybe," "sort of," "kind of"
- Repetition and restarts
- Transcription errors and artifacts
- Speaker attributions for routine statements
- **Time spans** — Convert to dates (see below)

**What to extract (keep only this):**
- Facts and decisions stated
- Principles and values expressed
- Processes and approaches described
- Organizational positions and stances

**Example transformation:**

**Source (transcript):**
```
Yeah so we, um, we really try to — I mean, it's something we've always believed in —
meeting clients where they are, you know? Like if they're just starting out with AI
stuff, we don't want to, like, overwhelm them with all the technical, you know,
jargon and complexity. We focus on quick wins first. That's been our approach.
```

**Module content:**
```
Client engagement principle: adapt approach to client's current AI maturity level.
- Early-stage clients: prioritize quick wins, minimize technical complexity
- Never open with jargon or comprehensive architecture — meet them where they are
```

**NOT this (wrong — preserves conversational structure):**
```
The team mentioned that they "really try to meet clients where they are" and
believe in not "overwhelming them with technical jargon." They noted that
"quick wins" are prioritized for clients "just starting out with AI."
```

The wrong example is useless to an LLM agent — it's just transcription with quotation marks. The correct example provides actionable guidance.

### Converting Time Spans to Dates

Time spans become outdated the moment the calendar changes. Always convert relative time references to absolute dates or years.

**Wrong:** "25 years of experience" / "Founded over two decades ago"
**Right:** "Founded in 1999" / "Operating since 2009"

When you can't determine the exact date, calculate from the source document's date and mark it: "Founded approximately 1999 [calculated from '25 years' in 2024 source]"

### Volatile Specifics vs. Durable Process Parameters

**Volatile (move to addenda):** Values that change as the business evolves — counts of things, prices, named lists of tools or team members, enrollment numbers.

**Durable (keep in modules):** Process parameters that only change if processes are redesigned — escalation timelines, contract thresholds, review cadences.

**The test:** Would this change because the business *grew* (volatile) or only if processes were *redesigned* (durable)?

**Wrong (volatile in module):** "Retainers at $3,500/mo and $6,000/mo"
**Right (module references addendum):** "For current retainer pricing, see addenda/pricing-and-rates.md"

### Transforming Quotes, Case Studies, and Process Documents

**Quotes** are evidence — they inform what goes in modules, but aren't copied directly. Extract the practice the quote proves exists.

**Case studies** contain methodology patterns. Extract the pattern ("We used X approach for Y situation"), leave out client names, specific metrics, testimonials, and timeline details.

**Process documents** contain step-by-step procedures. Agents don't need procedures — they need decision criteria. Extract the decision logic, not the steps.

---

## Module Design Philosophy

**Organize modules for USE, not for taxonomy.**

**Wrong (taxonomy-based):** Separate modules for "Identity," "Voice," "Services" — many small modules agents must combine, losing coherence.

**Right (use-based):** Fewer, richer modules organized around coherent domains of organizational thinking. Each module gives an agent the reasoning it needs for a type of work.

**The test:** For each proposed module, ask: "What organizational reasoning does this equip?" If the answer is unclear, the module may be too abstract or taxonomic.

### Focused, Not Monolithic

Use-based doesn't mean "put everything in one module." Each module should serve a **single, coherent domain of organizational thinking.**

**Signals a module needs splitting:**
- Covers multiple distinct reasoning domains
- Exceeds ~4,000 tokens and growing
- Content from shared sources duplicated because it "fits"
- Purpose statement requires "and" to describe what it does

### Guiding, Not Cataloging

Modules should provide creation and decision guidance, not inventory existing content.

**Wrong (catalog):** List of all programs with session counts and descriptions.
**Right (guide):** Principles for designing programs — progressive complexity, practical exercises, reusability.

**The test:** If the organization added a new program tomorrow, would this module need updating? If yes, you've cataloged instead of guided.

**Exception:** Response patterns can be valuable when they encode the organization's reasoning about *why* to respond that way — not just scripted replies. If a pattern captures organizational thinking ("We respond this way because we prioritize X over Y"), keep it. If it's just a script without reasoning, it's a procedure, not context.

### Respecting Scope Boundaries

The proposal defines what content belongs in each module. When writing a module, the proposal's scope boundary is authoritative. Content assigned to addenda or other modules should be cross-referenced, not included.

### Principles Over Prescriptions

Capture decision criteria and principles, not specific tool choices or current-state descriptions. "Our criteria for selecting tools" outlasts "We use Tool X."

### Audience Reasoning in Modules

Agents interact with people — they serve organizations, write for readers, engage with stakeholders. Without audience reasoning, agents default to writing for a generic reader and evaluating situations by surface categories. Every module that governs engagement or content production needs a framework for thinking about the humans on the other end.

**The pattern: Needs, not personas.**

Persona profiles ("the skeptic," "the internal champion") create boxes that force the agent to classify people into one type. Real people hold multiple orientations simultaneously — skeptical AND curious AND championing. The better model is interacting needs on spectrums:

- Each need exists on a continuum
- A single person or organization presents multiple needs simultaneously
- The combination of active needs — not any single category — determines how the agent should adapt
- Needs shift by context: the same person reading a case study has different active needs than when reading a policy brief

**Where it belongs:** Inside modules that govern engagement or content production, as sections within those modules. Not as a separate "audience" module — audience reasoning is a behavioral extension of existing reasoning domains, not a new domain.

**Anti-patterns:**
- Persona profiles that force classification into one type
- Sector-based models ("faith-based audiences need X") — sector correlates with needs but doesn't determine them
- Character archetypes ("the skeptic") — same problem as personas
- Static audience definitions that don't shift by context

---

## Module Hierarchy

### Foundation Modules
Universal organizational context loaded by all or most agents. Substantial — 2,000-4,000 tokens each.

Typical: Organizational Identity, Brand & Communication, Ethical Framework.

### Shared Modules
Cross-functional knowledge used by multiple (not all) agents.

Typical: Client engagement approach, service methodology, content standards.

### Specialized Modules
Domain-specific knowledge for particular agent roles.

### Addenda (Reference Data)

**Container** (modules vs. addenda) and **load discipline** (always_load vs. conditional) are orthogonal. Confusing them is a documented failure mode — see "Load Discipline" below.

| Component | Contains | Changes When |
|-----------|----------|-------------|
| **Modules** | Reasoning context, decision frameworks, organizational principles | Processes redesigned |
| **Addenda** | Data — pricing, bios, catalogs, inventories | Business evolves |

Modules reference addenda; addenda don't reference modules.

---

## Load Discipline

Each item an agent might load is classified as **`always_load`** (loaded into the agent's system prompt every time) or **`conditional`** (loaded only when a specific runtime trigger applies). Container and load discipline are independent dimensions:

| | Module | Addendum |
|---|---|---|
| **`always_load`** | Foundation modules in most agents (F0, F1, F2, F3); shared modules whose content governs every output (e.g., S0 for any external-facing agent); specialized modules whose content governs every output for that agent's role (e.g., D2 for an external-communications agent) | Reference addenda containing universal organizational data the agent's judgment about needing is unreliable (e.g., A0 organizational reference for any agent that names the organization) |
| **`conditional`** | Shared modules that apply only in specific task or audience contexts | Most addenda — funder-specific, region-specific, project-specific, peer-specific, sector-specific |

### The Classification Rule

An item is **`always_load`** when its content governs the quality, accuracy, or compliance of the agent's output universally — meaning the agent's judgment about whether to load it is unreliable.

An item is **`conditional`** when its content applies only in specific task or audience contexts, with a load-time trigger expressible as a plain-language sentence.

**The classification is per-agent.** The same module may be `always_load` for one agent and `conditional` for another. Methodology content is `always_load` for an agent that writes proposals (every proposal is methodology-anchored); the same content is `conditional` for an agent doing prospect research (only some prospects need methodology depth). The question to ask, per agent: *does this govern every output this specific agent produces?*

### F0 and S0 Are a Hard Rule

`F0_agent_behavioral_standards` is `always_load` whenever it appears in an agent's set. No exceptions.

`S0_natural_prose_standards` is `always_load` whenever it appears in an agent's set (i.e., for any agent that writes anything for any audience). No exceptions.

Both rules exist because the failure mode they prevent (agent's runtime judgment about whether to apply behavioral guardrails or prose discipline) was the originating failure that produced this classification system. The hard rule is enforced at three layers: Phase 3 GATE (Design refuses to advance), Phase 4 self-check (Build flags violations), and `scripts/count_tokens.py` (script refuses to compute a budget).

### Why This Classification Replaces Tiered Manifests

Earlier versions of the agent-definition template grouped modules by tier (foundation/shared/specialized) and listed addenda separately as reach-beyond. The visual structure suggested two categories of load decision: modules were the agent's context, addenda were things to reach for. In runtime behavior, this distinction collapsed. Agents made their own load-time judgments — sometimes deciding S0 didn't apply for "quick" tasks, then producing output that violated S0's prose standards. Sometimes deciding A0's legal-entity data wasn't needed, then generating from inference instead of from the loaded reference.

The pattern: when the manifest leaves to the agent's judgment whether a piece of context governs output, the agent will sometimes get that judgment wrong — confidently. Items that govern output universally must be loaded universally; items that apply only in specific situations are loaded with explicit triggers.

The tier structure (foundation/shared/specialized) still describes where module *files* live in the library directory, and what scope of agents typically use each tier. It does not describe load discipline. The two are independent.

### Trigger Discipline (`load_when:`)

A `load_when:` trigger is a plain-language sentence the runtime agent reads and applies to the work in front of it. Triggers must be diagnostic — concrete enough that two reasonable readers would agree on whether the trigger fires for a given piece of work.

**Three components:**

1. **The diagnostic axis.** Audience type ("when work is anchored in climate-focused foundations as the funder type"), task type ("when contract analysis crosses jurisdictions"), content type ("when work names anchor figures from the project portfolio"), or domain ("when work touches MRV architecture or FPIC depth"). One axis per trigger; if a trigger combines audience + task ("when writing proposals to climate funders"), it should be split — that's two triggers on two items, not one trigger on one.

2. **The condition phrasing.** Plain "when X" or "if X." Names the situation, not the agent's judgment about the situation. Wrong: "when you think the audience needs X" — that reintroduces the runtime judgment the classification was designed to remove. Right: "when work crosses into Germany / Germanic cultural context" — names the situation, not the agent's reading of it.

3. **Right-side specificity.** Concrete enough that two reasonable readers would agree on whether it applies. "When work touches methodology" is too thin. "When work touches project methodology, MRV architecture, FPIC depth, or community-ownership claims" gives the runtime agent a checklist.

**Discipline rules:**

- One axis per trigger. Split combined triggers across multiple items.
- Triggers reference the work, not the agent's judgment ("when work involves X," not "when you need X").
- Ambiguous-sounding triggers should err toward loading: "When in doubt, load it." The cost of loading an unneeded item is small compared to the cost of skipping a needed one.

**Worked examples** (drawn from the classification's first deployment):

```
- addendum: cultural/A_cultural_germany
  load_when: "Work crosses into Germany / Germanic cultural context"

- module: S2_methodology
  load_when: "Work touches project methodology, MRV architecture, FPIC depth, or community-ownership-as-constraint claims"

- addendum: sector/A_sector_carbon_controversies
  load_when: "Work involves adversarial sector questions or audience-specific scripts for carbon-market-credibility engagement"
```

Each names a diagnostic axis, uses plain "when X" phrasing, and is specific enough to be checkable.

---

## Always-Load Delivery

Classification decides *whether* an item is always-load. Delivery is the separate question: how does an always-load item actually reach the agent's system prompt? The two questions are independent, and getting delivery wrong undoes the classification.

### The Delivery Principle

Always-load items must be in the agent's system prompt from turn one. Not loaded on instruction. Not fetched when the agent decides to read them. Not retrieved by the runtime when the agent's request matches a file. **In the system prompt, before the first turn.**

This rule exists because the failure mode the classification was designed to remove — the agent's runtime judgment about whether to load — re-enters whenever delivery depends on the agent or runtime making a load decision. The originating failure (an agent skipping S0 because it judged the immediate task didn't need prose discipline) was a classification failure. The same failure mode in delivery: an agent ignoring instructions to load files, or batching the loads as tool calls, or partially loading them, or having them retrieved unreliably by RAG. Same agent, same wrong-judgment risk, different layer.

### Two Delivery Mechanisms

The agent definition file declares always-load items as `@`-directive lines in a `## Required Reading` section — one directive per file, no surrounding prose. These directives are content-delivery instructions, not behavioral instructions to the agent.

**In `@`-aware runtimes (Claude Code), the runtime expands `@` directives at load time.** The harness reads the agent file, finds each `@path`, reads the target file, and inlines its content into the system prompt before the model sees the prompt. Recursive: included files' own `@` directives expand the same way. The agent never sees the directives; it sees the inlined content.

**In runtimes that don't process `@` (Claude.ai project upload, Cowork, generic API integrations), an offline build script resolves the directives.** The script walks the agent file, expands every `@` directive recursively, and writes the result to `deploy/agents/<name>.md` — a self-contained bundle with all required-reading content already inlined. The bundle is what gets uploaded or pasted as the system prompt.

Both mechanisms produce the same end state: required-reading content is in the system prompt from turn one. The difference is *who* does the expansion (runtime vs. build-time script). Neither asks the agent to participate in delivery.

### Why Always-Load Concatenates and Conditional Stays Separate

This separation is load-bearing for the architecture. Both library designers and library consumers need to understand it.

**Always-load content concatenates** because every output the agent produces depends on it. Concatenating into a self-contained bundle removes the runtime's judgment about whether to load, the agent's judgment about whether to fetch, and the latency cost of sequential fetches. The bundle *is* the system prompt; everything that needs to be in the system prompt is already there.

**Conditional addenda stay separate** because they're work-specific. Inlining all of them would force every output through every funder profile, every cultural context, every project. The whole point of the conditional table is that the agent reads it as runtime instruction and pulls the right addendum for the work in front of it. The conditional table's `load_when:` triggers are the agent's instruction set for that selectivity.

The cost of conditional separation is real: it depends on the runtime's ability to fetch the right addendum at work-time when the trigger fires. In Claude Code with files visible in the project tree, that's reliable. In Claude.ai project upload with conditional addenda also uploaded as project files, retrieval-style mechanisms surface them when relevant. In runtimes without reliable file access at work-time, the agent recognizes the trigger but has no way to load the addendum.

### The All-Inclusive Bundle Variant

For runtimes where conditional fetch at work-time is unreliable, the build script supports an `--all-inclusive` flag that produces a heavier bundle variant. The variant inlines every conditional addendum's content alongside the always-load content, with the conditional table preserved so the agent retains per-work selectivity over already-loaded content.

The trade is straightforward: the variant guarantees content availability in any runtime, at the cost of token weight on every turn (every conditional item carried whether the work needs it or not). The standard bundle is the default; the all-inclusive variant is the documented fallback when conditional fetch reliability becomes a production problem.

count_tokens.py reports against the standard bundle only — the all-inclusive variant intentionally carries content beyond the 10% per-agent budget, and budget compliance applies to the universally-loaded set.

### The Optionality Problem

Both Claude.ai's RAG-style retrieval over uploaded project files and Claude Code's `@`-include expansion present uploaded/referenced files as *optional context* rather than *required context* at the model layer. The model has the architectural option to not engage with the file content, even when the prompt says "you must read this." Eden's testing surfaced exactly this: an agent treated mandatory-read prose instructions as discretionary tool work, sometimes skipping the load entirely.

The skill's response is to make peace with this and design around it, not pretend it's solvable at the prompt level. The classification names which content governs every output; the delivery mechanism gets that content into the system prompt without asking the model to participate. Where the runtime is reliable (Claude Code with `@`, Claude.ai with the bundle as a project file plus uploaded conditional addenda for retrieval), the standard bundle works. Where the runtime is unreliable (no fetch, no retrieval, or known-flaky retrieval for specific content), the all-inclusive bundle removes the runtime variable.

The library consumer (the human deploying the library to a runtime) needs to know which bundle variant their runtime requires. The library designer (the user running the skill) needs to know that the architectural decision between the variants is about runtime reliability, not about the library's content. The deployment-doc that ships in the output library's README articulates both.

---

## Single Source of Truth

Each piece of information exists in exactly ONE module. Other modules incorporate that content by cross-reference, not by restatement. The proposal's Ownership and Use-Shape table commits to *both* which module owns each content area *and* the specific shape used by every other module that needs it.

Ownership is necessary but not sufficient. Naming an owner without specifying use-shape leaves the build agent to decide at write-time how a using module incorporates the content — and the path of least resistance is to restate. Specifying use-shape in Design removes that decision from Build.

### The Four Use-Shapes

When a module needs content owned by another module, the proposal commits the using module to one of four shapes:

**Cross-reference only.** The using module names the content area and points to the owner. No restatement, no descriptive prose. Example: an addendum that adapts a shared constant to a particular context opens with "[Constants from the owner module] apply throughout this addendum — see [owner]." The addendum content then begins with the adaptation, not with restated constants.

**Brief restatement of subset.** The using module restates a specific, scoped subset (one phrase or one short sentence) and cross-references the full content. Reserve this for cases where the using module's reasoning genuinely needs the subset present in-line for the agent to follow. The restated subset must be smaller than the full owned content — if it isn't, the use-shape is wrong; either the content has a different owner, or the using module should cross-reference only.

**Invocation by name.** The using module names a thing without describing it (a standard, a methodology, a framework — referenced by its name only) and lets the runtime agent encounter the description elsewhere when it needs it. Use when the name itself carries enough signal for the using module's purpose, and the description belongs to another module or addendum.

**Indirection through reach-beyond.** The using module instructs the agent to load the addendum or invoke the skill when it needs the content, rather than carrying any of it. This is the default for volatile data (figures, names, lists) — the module tells the agent *when* to reach for the data, never *what* the data is.

### What This Replaces

The pattern that violates SSoT is restatement: a using module describes the content it needs in the using module's own prose, often expanded for the using context. Each restatement creates a place that goes stale when the canonical source updates, and the restatements drift from each other over time. The four use-shapes all avoid restatement. When the build agent reaches for content during Section Plan (Phase 4, Step 5), the use-shape from the proposal tells it which of these four shapes to produce — not whether to restate.

### Cross-Reference Format

```markdown
> See [Module Name] for [specific information].
```

For brief restatement of subset:

```markdown
[The scoped subset, one phrase or short sentence.] See [Module Name] for the full [content area].
```

---

## Content Verification

**All content must be verified.** Every fact must trace to a working source.

**Working sources** are:
- Original source files marked `ready` in the source index
- Any user-provided supplementary materials

### Write-Time Source Protocol

Modules must be written with sources open, not from memory.

**Required process:**
1. Identify which source files inform this module (from proposal)
2. Read those files (even if read earlier in the session)
3. Write the module with sources visible
4. For HIGH-STAKES content (legal names, EINs, addresses, titles, credentials, financial figures): copy exact text

**Verification log format (removed before delivery):**
```markdown
<!-- VERIFICATION
| Fact | Source | Exact Text |
|------|--------|------------|
| California LLC | Organization Information.md | "Entity Type: California Limited Liability Company" |
-->
```

### Build-Time Markers

- `[PROPOSED]` — Inferences the agent made. Rewrite to make inferential status clear in language before removing.
- `[HIGH-STAKES]` — Content requiring exact-copy verification. Remove when exact text is locked in.

Both markers are build artifacts removed before delivery.

### Content Stakes Classification

**HIGH STAKES** — Legal claims, financial figures, credentials, public commitments. Exact-copy discipline from sources.

**MEDIUM STAKES** — Service descriptions, methodologies, timelines. Should be verifiable; `[PROPOSED]` acceptable during build.

**LOW STAKES** — General descriptions, internal terminology. `[PROPOSED]` acceptable based on pattern inference.

---

## Token Budget Management

**The budget per agent is 10% of the target model's context window** (e.g., 20K tokens for a 200K-context model). The budget counts items that are `always_load` (they're in context every time, regardless of container — module or addendum). Items that are `conditional` do not count against the budget; they're loaded only when their `load_when:` trigger fires.

This is a change from earlier skill versions, which excluded all addenda from the budget. The change reflects the load-discipline classification: budget is determined by what's *always* in context, not by container type.

### The Budget Is Room, Not a Ceiling

The budget tells you how much space you have for useful verified content. **An agent using well under its budget isn't efficient — it's underserved.** The goal is to fill the budget with content that makes the agent better at its job.

**Under-budget is a quality signal, not a success metric:**
- An agent at 60% of budget probably lacks context for nuanced decisions
- Multiple agents under 50% suggests over-compression or missing content
- Modules under 1,000 tokens are almost certainly too thin — a 600-800 token module suggests the behavioral guidance was stripped to facts

**Over-budget requires actual trimming, not compression:**
- Cut duplicated content across modules
- Cut explanations of general concepts (not org-specific)
- Remove modules the agent doesn't actually use
- Move volatile data to addenda

**DO NOT artificially compress content to "save tokens."** If the content is verified and helps the agent make better decisions, include it. The right size is determined by content value, not by an arbitrary target.

### Individual Module Sizing

Most modules should be **2,000-4,000 tokens**. This is enough for substantive behavioral guidance without becoming monolithic.

Run `python scripts/count_tokens.py` to measure actual usage. The script flags both over-budget agents AND under-budget agents (below 50%) as quality concerns.

---

## Module Naming Convention

Format: `{tier_prefix}{number}_{descriptive_name}.md`

- `F1_organizational_identity.md`
- `S3_client_engagement.md`
- `D2_sales_process.md`

Lowercase with underscores. Descriptive but concise.

---

## Standard Guardrail Modules

Every context library includes two standard guardrail modules, copied from `templates/guardrails/` during Design:

### F0_agent_behavioral_standards (Foundation)

**All agents load this module.** Process gates for:
- Source-before-statement
- Epistemic calibration
- Reframe-before-committing
- Second-order check
- HIGH-STAKES condition test
- Professional challenge

### S0_natural_prose_standards (Shared)

**External-facing agents load this module.** Covers:
- Banned AI-detectable vocabulary
- Banned syntactic patterns
- Required writing behaviors
- Practitioner voice gate

### When to Load Each

| Agent Type | F0_agent_behavioral_standards | S0_natural_prose_standards |
|------------|------------------------------|---------------------------|
| Marketing/communications | Required | Required |
| Content creation | Required | Required |
| Internal documentation | Required | Skip |
| Research/analysis | Required | Skip (unless published) |

---

## Information Gaps

When working sources lack needed information:

1. Note the gap in the source index (Setup)
2. Carry gaps forward to the proposal (Design)
3. Classify impact:
   - **BLOCKING**: Agent cannot function — must resolve before building
   - **LIMITING**: Agent works but reduced capability — note in build state
   - **ENHANCING**: Would improve but not essential — low priority
4. Ask user about BLOCKING gaps before proceeding

**Never invent information to fill gaps.** A thin module with verified facts is better than a rich module with hallucinations.

---

## Session Architecture

### Why Sessions Exist

When Claude Code's auto-compact triggers during a build:
- **Skill instructions vanish** — critical rules (transform don't transcribe, re-read sources) are lost
- **Specific facts blur** — titles, names, dates get reconstructed from memory, producing confident wrong information
- **Classification decisions are lost** — the agent reverts to default summarize/paraphrase behavior

### How the Architecture Prevents This

1. **Phase-specific instruction files** in `references/phases/` — self-contained with their own critical rules
2. **Embedded rules in data files** — source-index.md, proposal.md, and templates contain rules as redundant safety nets
3. **Build state tracking** — `build-state.md` records current phase, completed work, and a pointer to the next phase file

### How to Resume From Any Point

1. Read `<OUTPUT_PATH>/build-state.md`
2. Read the phase instruction file it points to
3. Continue from where work left off
