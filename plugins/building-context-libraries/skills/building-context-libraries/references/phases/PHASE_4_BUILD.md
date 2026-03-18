# Phase 4: Build

> **CRITICAL RULES — Read these first:**
> - **Read [references/ARCHITECTURE.md](../ARCHITECTURE.md) now.** Re-read the reasoning-context hierarchy, transformation rules, and token budget management.
> - **Read `proposal.md` now.** The proposal defines module scopes, shared source ownership, and build order.
> - Modules provide organizational reasoning context — how the organization thinks. Before writing any section, verify it is written as an **instruction to the agent**, not an **explanation about the organization**. Narrative prose that explains the organization to the agent is not a metaprompt, even if it contains reasoning.
> - Re-read sources in the SAME TURN you write each module. Source-index classifications (legacy, reference, etc.) are Setup triage labels, NOT Build-time reading permissions. If a source is assigned to this module, read it.
> - Check the Shared Source Ownership table before writing each module. If content is assigned to another module, cross-reference — do not restate.
> - **Token budget is room for useful content.** An under-budget module needs more depth, not congratulation.

---

## What This Phase Does

Write all modules, addenda, and agent definitions. One module at a time, each with a commitment gate that prevents content-copying. Then validate the complete library.

---

## Session Loading Gate

**Every session that includes Build work must start with these reads.**

**GATE:** Load in this order before writing any module:
1. This phase file (you're reading it)
2. [references/ARCHITECTURE.md](../ARCHITECTURE.md) — reasoning-context rules, transformation, token management
3. `<OUTPUT_PATH>/build-state.md` — what's done, what's next
4. `<OUTPUT_PATH>/process-log.md` — decisions and corrections from earlier phases and previous Build sessions
5. `<OUTPUT_PATH>/proposal.md` — module scopes, shared source ownership, build plan
6. `<OUTPUT_PATH>/source-index.md` — the complete source inventory (you need this to locate source files for each module)

Write to the build state: "Build session loaded: phase file, ARCHITECTURE.md, build-state, proposal, source-index"

If you believe you already know the rules, you are likely post-compaction. Re-read anyway.

**The per-module re-read (Step 2 in the protocol below) is separate and mandatory.** The session bootstrap gets the rules and structure into context. The per-module re-read gets the actual source content into context before you write each module. Neither substitutes for the other.

---

<phase_build_modules>
## Per-Module Protocol

Build modules in the order specified by the proposal. For EACH module:

### Step 1: Commitment Gate

**GATE:** Before writing, answer these three questions in the build state:

1. **"This module equips the agent to think about:"** — What organizational reasoning does this module provide? Be specific about what the agent will understand, not what procedures it will follow.

2. **"Without this module, agents would:"** — What wrong default does this module prevent? Name the gap in reasoning, not a missing procedure.

3. **"The reach-beyond test:"** — Does this module try to contain everything the agent needs for this domain, or does it also tell the agent when to load addenda (specific data), invoke skills (capabilities), or ask the user (judgment calls)? A module that never points beyond itself is probably trying to be a procedure manual.

4. **"Source grounding:"** — Name one specific organizational pattern from a source file you re-read in Step 2 that this module will capture. Not from comprehension findings. Not from memory. From a source you read in this turn. If you can't name one, you haven't engaged with the sources — go back to Step 2.

**If you cannot answer all four, the module may not need to exist.** Raise this with the user before writing.

### Step 2: Re-Read Sources

**GATE:** Identify which source files feed this module (from the proposal). **Read those files now** — even if you read them earlier in this session. Do not write from memory.

**Source-index classifications do not override this gate.** If a source is assigned to this module in the proposal, read it — regardless of whether the source index labels it "legacy," "reference," "pre-reorg," or anything else. Those labels are Setup triage classifications. They do not determine what gets read during Build. The proposal's source assignment is authoritative.

Write to the build state: "Module [ID] — sources re-read: [list of files read for this module, including any classified as legacy/reference]"

**Do not proceed to Step 3 until you have read every source file assigned to this module in the proposal.** A module written from memory of sources — even recent memory — drifts from what the sources actually say.

For HIGH-STAKES content (legal names, EINs, addresses, titles, credentials, financial figures): locate the exact text in the source. You will copy it verbatim.

### Step 3: Check for Overlap

Before writing, check:
- The Shared Source Ownership table — is any content assigned to a different module?
- Already-completed modules — does any content you're about to write already exist?

If overlap exists: cross-reference (`See [Module Name] for [topic]`), do not restate.

### Step 4: Write the Module

Use the module template from [references/TEMPLATES.md](../TEMPLATES.md).

**The metaprompt transformation gate — apply to every section you write:**
Before writing any module section, identify:
1. The **organizational reasoning** it provides (how does the organization think about this?)
2. The **novel-situation test** (could an agent use this to handle a situation the author didn't anticipate?)
3. The **instruction test** (is this written as an instruction to the agent, or as an explanation about the organization?)

If the section explains the organization to the agent rather than instructing the agent how to think and act — it's narrative documentation, not a metaprompt. Rewrite it as instructions. "The organization prioritizes X" is explanation. "When evaluating Y, prioritize X because [reasoning]" is instruction. "Christopher drew a sharp distinction between..." is narrative. The organizational reasoning that distinction encodes, stated as guidance for the agent, is metaprompting.

**No narrative prose in modules.** No historical arcs. No "about us" writing. No quoted material used as content. If you catch yourself writing a sentence that describes the organization in third person, you are writing documentation, not a system prompt component.

**Write (in order of priority):**
- Reasoning context: principles, values, tradeoffs, and the *why* behind organizational decisions — these equip the agent to think well in novel situations
- Decision frameworks: what factors to weigh and why — the agent makes the decision, the module equips it
- Reach-beyond signals: when to load addenda (specific data), invoke skills (capabilities), or ask the user (judgment calls)
- Prescriptive rules: only for genuine constraints where violation causes real organizational harm

**Do NOT write:**
- Facts without reasoning context
- Lists without the principles that generated them
- "If X, do Y" rules for every scenario (capture the reasoning; the agent applies it)
- Summaries of source documents
- Procedures that should be skills or addenda

**Include a verification log (removed before delivery):**
```markdown
<!-- VERIFICATION
| Fact | Source | Exact Text |
|------|--------|------------|
| [fact] | [source file] | [exact quote from source] |
-->
```

Mark inferences with `[PROPOSED]`. Mark exact-copy content with `[HIGH-STAKES]`.

### Step 5: Self-Check

After writing each module, verify:

1. **Instruction test:** Read each section aloud as if you were an agent receiving it. Does every section tell you what to do, how to think, or how to weigh factors — or does any section explain the organization to you like documentation? Rewrite any section that reads as "about us" prose.
2. **Narrative check:** Copy one paragraph from the module. Does it contain third-person descriptions of the organization ("Make Good is...", "The team believes..."), historical narrative ("Founded in...", "Over the years..."), or quoted material used as content? If yes, the module has narrative contamination. Rewrite those passages as agent instructions.
3. **Reasoning density:** Would removing this module change how the agent *thinks* about its domain? If not, the module is content, not context.
4. **Scope boundaries:** Did you stay within the proposal's scope for this module? No content from other modules' domains?
5. **Single source of truth:** Is any fact stated here also stated in another module? If so, remove from one and cross-reference.
6. **Volatile check:** Are there any counts, prices, named lists, or other volatile data? Move to addenda.
7. **HIGH-STAKES check:** Are legal names, EINs, financial figures, credentials copied exactly from sources?
8. **Token depth:** Is this module substantive enough? A module under 1,000 tokens probably needs more behavioral guidance. A module at 600 tokens has almost certainly been stripped to facts.
9. **Source verification:** Can you trace every fact to a source file? Remove anything you can't verify.
10. **Cross-references:** Are connections to related modules explicit?
11. **Audience reasoning check:** If this module governs engagement, qualification, or content production — does it include reasoning about the humans on the other end? Not persona profiles or sector categories, but a needs-based framework: what do the people this agent interacts with or writes for actually need, and how do those needs interact and shift by context?

### Step 6: Update Build State and Process Log

After completing each module, update `build-state.md`:
- Mark module as complete
- Update token estimates

**Log to `process-log.md`:**
- What reasoning this module captures and why it's structured this way
- Any user corrections or direction changes during this module's writing
- Decisions about what was included vs. cut and why
- Source insights that surprised you or changed your approach
- Anything the next module or next session needs to know
</phase_build_modules>

---

<phase_build_addenda>
## Building Addenda

After all modules are complete, build the addenda.

Addenda contain **data only** — no behavioral instructions, no decision logic. They are reference material agents consult when a module directs them to.

For each addendum:
1. Re-read the source files that inform it
2. Extract the data (prices, bios, catalogs, etc.)
3. Include source attribution
4. Specify update frequency ("Review quarterly" / "Update when pricing changes")
5. Verify all data against sources — addenda get the same verification discipline as modules

**Addenda are not second-class modules.** They contain the volatile specifics that modules reference. Inaccurate addenda produce inaccurate agent responses.
</phase_build_addenda>

---

<phase_build_agents>
## Writing Agent Definitions

After modules and addenda are complete, write the agent definition files.

**Agent definitions are system prompt preambles.** They are loaded into the agent's context at runtime — they tell the agent who it is, what it does, and what modules to load. Write them as instructions TO the agent, not documentation ABOUT the agent.

For each agent (from the proposal):

1. **Re-read the proposal's agent definition** for this agent
2. **Review all modules this agent will load** — skim each one to confirm the module set serves this agent's role
3. **Write the agent definition** using the template from [references/TEMPLATES.md](../TEMPLATES.md)

**The runtime section (what the agent reads) must include:**
- Identity and role — written in second person ("You are...", "You handle...")
- Module loading instructions — which modules to load, in what order, with a brief note on what each provides
- Addenda triggers — when to consult reference data
- Domain-specific guidelines — behavioral extensions beyond standard guardrails

**The build metadata section (HTML comment, not visible to the agent) tracks:**
- Token budget breakdown and utilization assessment
- Module rationale table (why each module was assigned)
- Build notes (decisions made about this agent's configuration)

**Budget assessment for each agent:**
- Calculate total tokens from assigned modules
- Compare to 10% of target model context window
- If under 50%: flag as potentially underserved — review whether modules need more depth or additional modules are needed
- If over 100%: identify what to trim — remove modules not essential for this role, not compress existing modules

**Do not write custom guardrail sections in agent definitions.** Load the standard guardrail modules and add only domain-specific extensions if needed.

**The test:** Read the agent definition back. Does it sound like a system prompt that configures an agent, or like a project management document that describes one? If the latter, rewrite it as instructions the agent will follow.
</phase_build_agents>

---

<phase_build_validate>
## Final Validation

After all modules, addenda, and agent definitions are complete:

### Script Validation

Run each script and fix any issues:

```bash
# Validate library structure
scripts/validate_library.py <OUTPUT_PATH>

# Check token budgets (flags both over-budget AND under-budget agents)
scripts/count_tokens.py <OUTPUT_PATH>

# Verify facts against sources (run for each module)
scripts/verify_module.py <OUTPUT_PATH>/modules/<module_file> <SOURCE_PATH>
```

### Quality Checklist

**For each module:**
- [ ] Transformation test passes — every section tells agents what to do, not just what exists
- [ ] All facts trace to source files
- [ ] No content duplicated across modules
- [ ] Cross-references are explicit and correct
- [ ] No volatile data in modules (moved to addenda)
- [ ] HIGH-STAKES content copied exactly from sources
- [ ] Build artifacts removed (`[PROPOSED]`, `[HIGH-STAKES]`, `<!-- VERIFICATION -->`)
- [ ] Token count is substantive (not under 1,000)

**For each addendum:**
- [ ] Contains data only — no behavioral instructions
- [ ] All data verified against sources
- [ ] Update frequency specified
- [ ] Source attribution included

**For each agent definition:**
- [ ] Role is behavioral (actions), not taxonomic (knowledge areas)
- [ ] Module set serves the agent's actual decision-making needs
- [ ] Token budget assessed — neither starved nor bloated
- [ ] Standard guardrails loaded (F0_agent_behavioral_standards for all; S0_natural_prose_standards for external-facing)

**Library-wide:**
- [ ] Single source of truth — no fact in more than one module
- [ ] All cross-references resolve to real modules
- [ ] All addenda references resolve to real addenda files
- [ ] BLOCKING gaps resolved or documented
- [ ] Build artifacts fully removed from all files
</phase_build_validate>

---

## GATE

Write to the build state:
- "Modules built: [count] / [total]"
- "Addenda built: [count] / [total]"
- "Agent definitions written: [count] / [total]"
- "Validation scripts run: [list results]"
- "Under-budget agents: [list or 'none']"
- "Over-budget agents: [list or 'none']"
- "Build artifacts removed: [yes/no]"
- "Quality checklist complete: [yes/no]"

---

## STOP

**Present to the user:**
- Complete library summary — modules, addenda, agents
- Token budget report — per-agent utilization
- Validation results — any issues found and fixed
- Any remaining gaps or limitations
- The library is ready for use

**Ask:**
- Would you like to review any specific modules in detail?
- Are the agent definitions correct — roles, module assignments?
- Any adjustments before finalizing?

---

## After This Phase

The build is complete. The context library is at `<OUTPUT_PATH>/` and ready for deployment.

**Library structure:**
```
<OUTPUT_PATH>/
├── source-index.md
├── build-state.md
├── process-log.md
├── proposal.md
├── modules/
│   ├── foundation/
│   ├── shared/
│   └── specialized/
├── addenda/
└── agents/
```

**To use:** Load an agent's definition file, then load the modules it specifies into the agent's system prompt. Consult addenda on demand as modules direct.
