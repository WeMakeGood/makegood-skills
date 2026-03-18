# Context Library Architecture

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

| Component | Contains | Changes When | Loaded | Token Budget |
|-----------|----------|-------------|--------|-------------|
| **Modules** | Reasoning context, decision frameworks, organizational principles | Processes redesigned | Always (per agent) | Counts against per-agent limit |
| **Addenda** | Data — pricing, bios, catalogs, inventories | Business evolves | On demand | Does NOT count against limit |

Modules reference addenda; addenda don't reference modules.

---

## Single Source of Truth

Each piece of information exists in exactly ONE module. Other modules cross-reference:

```markdown
> See [Module Name] for [specific information].
```

The proposal's Shared Source Ownership table assigns each content area to one module. During the build, check this table before writing — if content is owned by another module, cross-reference it.

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

**The budget per agent is 10% of the target model's context window** (e.g., 20K tokens for a 200K-context model). Addenda do not count. This limit scales as models gain larger context windows.

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
