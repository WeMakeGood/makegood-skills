# Phase 4: Build

> **CRITICAL RULES — Read these first:**
> - **Read [references/ARCHITECTURE.md](../ARCHITECTURE.md) now.** Re-read in particular: "The Runtime Agent's Perspective" (modules are read by an agent that has no awareness of sources, the build, or the library), "Shape Reference: F0 as a Worked Example" (what mixed-shape content looks like), "Single Source of Truth" (the four use-shapes), and the reasoning-context hierarchy.
> - **Read `proposal.md` now.** The proposal's Ownership and Use-Shape table commits using modules to specific shapes. Build executes the table; it does not redecide it.
> - Modules provide organizational reasoning context — how the organization thinks. Sections are committed to a shape (reasoning context | decision framework | prescriptive rule | cross-reference | reach-beyond signal) in the Section Plan *before* writing. Drift between plan and prose means the plan was wrong; redo the plan, do not edit the prose.
> - Re-read sources in the SAME TURN you write each module. Source-index classifications (legacy, reference, etc.) are Setup triage labels, NOT Build-time reading permissions. If a source is assigned to this module, read it.
> - **Token budget is room for useful content.** An under-budget module needs more depth, not congratulation.
> - **If this is a redo session after a rolled-back build:** follow the redo-session protocol below before writing anything.

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

**The per-module re-read (Step 3 in the protocol below) is separate and mandatory.** The session bootstrap gets the rules and structure into context. The per-module re-read gets the actual source content into context before you write each module. Neither substitutes for the other.

---

## Redo-Session Protocol

**Triggers (any of these):**

- A previous Build attempt was rolled back, and this session is starting fresh from the existing proposal and sources
- The session bootstrap's redo triage detected a redo signal (see TEMPLATES.md, "Session Bootstrap")
- The user rolls back the build mid-session (mid-Build, mid-Phase 3 review, etc.) — see TEMPLATES.md, "Mid-Session Rollback"

The failure mode this protocol prevents: retrospective documents (audit.md, post-mortem.md, etc.) from the rolled-back attempt anchor the new attempt. The build agent reads the retrospective as high-status reference text and generates from its examples — producing a near-copy of the failed work with the same structural problems redistributed.

The structural intervention is **physical separation**. The build agent cannot anchor to text it cannot read.

### Step R1: Identify Retrospective Documents and Prior-Attempt Artifacts

In `<OUTPUT_PATH>/`, identify any documents whose content is "what went wrong with the previous attempt" — typical names: `audit.md`, `audit-*.md`, `retrospective.md`, `post-mortem.md`, `failure-analysis.md`, or any document the user names as a retrospective.

Also identify any of the following from the rolled-back attempt:

- **Build artifacts:** module files in `<OUTPUT_PATH>/modules/`, addendum files in `<OUTPUT_PATH>/addenda/`, agent definition files in `<OUTPUT_PATH>/agents/`. Reading them produces close paraphrase of the failed work.
- **Build planning artifacts:** per-module plan files in `<OUTPUT_PATH>/_scratch/` from the rolled-back attempt. The plans encode the planning judgments that produced the failed modules; using them to plan the new attempt produces the same failures.
- **Comprehension artifacts** (if the rollback is to or before Phase 2): files in `<OUTPUT_PATH>/_comprehension/` from the rolled-back attempt. The synthesis artifacts (pattern-pointers, convergences, cross-domain parallels, agent-needs) anchor a fresh Pass 2 the same way module files anchor a fresh Build. The recognition artifacts (per-source notes, signal log, expectations-vs-findings, conflicts) are softer anchors but still anchors — Pass 2 of the new attempt should generate from sources (or fresh Pass 1), not from the prior attempt's recognition.

Treat all four categories as anchoring artifacts. The principle is the same: physical separation prevents the build agent from generating from a prior attempt's interpretation rather than from the sources.

### Step R2: Confirm and Move Retrospective and Prior-Attempt Artifacts

Present the file inventory to the user before moving anything:

- "Retrospective documents I will move to `_retrospective_archive/`: [list]"
- "Prior-attempt module/addendum/agent files I will move: [list]"
- "Prior-attempt per-module plan files I will move (from `_scratch/`): [list]"
- "Prior-attempt comprehension artifacts I will move (from `_comprehension/`, if rollback to/before Phase 2): [list]"
- "Files I am NOT moving (current working set): proposal.md, source-index.md, process-log.md, build-state.md, anything in templates/guardrails/, plus any artifacts from phases that the rollback is preserving (e.g., if rollback is to Phase 4 only, comprehension artifacts stay)"

Ask: "Is this inventory correct? Anything to add, remove, or reclassify?"

**STOP.** Wait for explicit user confirmation before moving any file. File moves are reversible but consequential — the archive determines what the build agent can and cannot read for the rest of the attempt.

After confirmation, create `<OUTPUT_PATH>/_retrospective_archive/` and move the confirmed files. The directory prefix `_` keeps the archive visible to the user but signals it is not part of the working set. **Do not read any file in `_retrospective_archive/` during this build attempt.** If the user asks you to consult the archive for a specific question, follow Step R5.

If the user's instructions or earlier session notes pointed you toward the retrospective, that pointer is now obsolete — confirm with the user that the redo protocol applies and the archive is sealed.

### Step R3: Get the Failure-Pattern List from the User

Ask the user: "What named failure patterns from the previous attempt should I architecturally avoid in this attempt?"

Write the user's list — **names only, no examples, no rewrite suggestions, no document content** — into `build-state.md` under the "Known failure patterns to avoid (this attempt)" section.

If the user attempts to share retrospective content (paragraphs, examples, before/after pairs), ask them to give you pattern names instead. The pattern names go in build-state. The content does not.

Examples of acceptable pattern names:
- "narrative prose in modules"
- "build-perspective contamination"
- "single-source-of-truth drift"
- "quote contamination"
- "comprehension shorthand crowding out source substance"

The names function as a watch-list. The build agent's structural protections are in the per-module protocol — the names are not the prevention; they are awareness.

### Step R4: Confirm Working Set

Confirm to the user:
- Retrospective documents moved to `_retrospective_archive/`: [list]
- Prior-attempt module/addendum/agent files moved: [list]
- Prior-attempt plan files moved: [list]
- Prior-attempt comprehension artifacts moved (if applicable): [list]
- Working set for this attempt: `proposal.md` (if preserved), `source-index.md`, `process-log.md`, `build-state.md`, source files in `<SOURCE_PATH>/`, `templates/guardrails/` for F0 and S0, and any phase artifacts the rollback explicitly preserved
- Failure-pattern names noted in build-state: [list]

If the user wants to revise the proposal before re-attempting Build, the redo protocol pauses here. The proposal can be revised; once revised, Build resumes from the per-module protocol.

### Step R5: Archive Consultation (Exceptional, Not Routine)

If during the build the user explicitly asks you to consult something in the archive (for example, "the previous F2 had three attempts — was the second-attempt approach the closest to right?"), the consultation is bounded:
- Read only the file the user names
- Answer only the question asked
- Do not let the consultation feed module content; the answer goes in process-log, not in modules
- Return to the per-module protocol immediately

The archive is for the user's reference and rare bounded questions, not for the build agent's working memory.

---

<phase_build_modules>
## Per-Module Protocol

Build modules in the order specified by the proposal. For EACH module, follow these seven steps. **Steps 1, 4, and 5 are planning artifacts the agent commits to before writing prose. Skipping them produces the structural failure modes this protocol is designed to prevent — narrative-prose modules, build-perspective contamination, restated canonical content, and modules that don't reflect source substance.**

### Where Planning Artifacts Live

The planning artifacts (Steps 1, 2, 4, 5) for each module are written to a single scratch file: `<OUTPUT_PATH>/_scratch/[module-id]-plan.md`. Create `_scratch/` if it doesn't exist; the `_` prefix keeps it visible to the user but signals it is not part of the runtime library.

**Why a file, not working memory:** Planning artifacts in working memory are invisible to the user during review, vulnerable to compression under context pressure across a long Build session, and lost on session break. Forcing them to disk makes the discipline visible (the user can read the plan and challenge it before module prose is written), survives context compaction (you can re-read your own plan after a long stretch of work), and produces an auditable record of the reasoning that produced each module.

**The file format** for `<OUTPUT_PATH>/_scratch/[module-id]-plan.md`:

```markdown
# Plan: [module-id]

**Step 1 — Runtime Frame:**
[The single sentence from Step 1 below + the commitment statement]

**Step 2 — Commitment Gate:**
1. This module equips the agent to think about: ...
2. Without this module, agents would: ...
3. Reach-beyond test: ...
4. What this module is NOT: ...

**Step 4 — Substantive Source Surface:**
1. [Pattern]: ...
   Source(s): ...
   Source pointer: ...
   Will appear as: ...
2. [Pattern]: ...
[etc.]

**Step 5 — Section Plan:**

Section: [name]
Reasoning captured: ...
Shape: ...
Why this shape (not another): ...
Source patterns this section encodes: ...
Owned content this section needs: ...
Quote/individual handling: ...

[Repeat for each section]
```

Plans are per-module; one file per module. After the module is complete and the process-log entry is written, the plan file remains in `_scratch/` as part of the audit trail. It does not need to be cleaned up at end of build.

These are scratch artifacts, not deliverables — but they are *visible* scratch, which is the point.

### Step 1: Runtime Frame Set

**GATE:** Before any other work on this module, create `<OUTPUT_PATH>/_scratch/[module-id]-plan.md` and write the Step 1 section:

> "This module will be loaded into the system prompt of an agent that does [domain of work]. The agent has access only to its loaded modules and user input — no source files, no build documents, no awareness that this module came from anywhere."

Then commit (write this in the plan file):

> "If I write a sentence that only makes sense to someone who knows about the build, the source files, the proposal, or the library — that sentence is contamination, not context. I will catch it during planning, not after writing."

This commitment is the precondition for the rest of the protocol. The runtime frame is established here so that Steps 4–6 generate from inside the runtime perspective, not from inside the build.

See ARCHITECTURE.md, "The Runtime Agent's Perspective," for the contamination phrases to watch for.

### Step 2: Commitment Gate

Answer these four questions in `<OUTPUT_PATH>/_scratch/[module-id]-plan.md` under the Step 2 section. The answers do NOT go in build-state.

1. **"This module equips the agent to think about:"** — what organizational reasoning does this module provide? Be specific about what the agent will understand, not what procedures it will follow.

2. **"Without this module, agents would:"** — what wrong default does this module prevent? Name the gap in reasoning, not a missing procedure.

3. **"The reach-beyond test:"** — does this module try to contain everything the agent needs for this domain, or does it also tell the agent when to load addenda (specific data), invoke skills (capabilities), or ask the user (judgment calls)? A module that never points beyond itself is probably trying to be a procedure manual.

4. **"What this module is NOT:"** — name two or three things the agent might expect this module to contain that it should NOT contain (because they belong to other modules per the Ownership and Use-Shape table, or to addenda, or to skills, or to user judgment).

**If you cannot answer all four, the module may not need to exist.** Raise this with the user before writing.

### Step 3: Re-Read Sources

**GATE:** Identify which source files feed this module (from the proposal). **Read those files now** — even if you read them earlier in this session. Do not write from memory.

**Source-index classifications do not override this gate.** If a source is assigned to this module in the proposal, read it — regardless of whether the source index labels it "legacy," "reference," "pre-reorg," or anything else. Those labels are Setup triage classifications. They do not determine what gets read during Build. The proposal's source assignment is authoritative.

For HIGH-STAKES content (legal names, EINs, addresses, titles, credentials, financial figures): locate the exact text in the source. You will copy it verbatim.

**Do not proceed to Step 4 until you have read every source file assigned to this module in the proposal.** A module written from memory of sources — even recent memory — drifts from what the sources actually say.

### Step 4: Substantive Source Surface

After re-reading the sources, write — in `<OUTPUT_PATH>/_scratch/[module-id]-plan.md` under the Step 4 section — a list of the *specific organizational reasoning patterns* from the just-read sources that this module will capture.

Format (3–7 entries, depending on module size):

```
1. [Pattern]: [one phrase naming what the source reveals about how the org thinks]
   Source(s): [files where this pattern is evidenced]
   Source pointer: [where in the source — section, topic, or phrase]
   Will appear in module as: [shape — reasoning context | decision framework | prescriptive rule | reach-beyond signal]
```

**Strict rules for the surface:**

- **Patterns must come from the source files you re-read in Step 3.** Not from comprehension findings. Not from process-log entries. Not from memory of earlier work. The surface is what you got from re-reading the actual sources in this turn.
- **If a pattern came from comprehension findings rather than the just-read source, mark it explicitly** ("comprehension-derived, not direct from source") and verify it in the source before using it. Comprehension shorthand crowding out source substance is a recurring failure mode; the surface is where that gets caught.
- **The surface lists patterns, not their content.** "How the org calibrates engagement intensity to client maturity" is a pattern. "The org uses quick wins to avoid overwhelming early-stage clients" is content — and writing the content here means you'll generate the module from your own paraphrase rather than from the source.
- **The surface is a contract.** What appears in the surface is what the module captures. After writing, you verify (in self-check) that the surface's patterns are present in the module — not just facts.

**Two thinness checks before locking the surface:**

*Quantitative thinness.* If the surface has fewer than 3 patterns, the module's source set is probably wrong, or the sources don't support the module the proposal specifies. Stop and raise this with the user before continuing.

*Qualitative thinness — the sector-genericity test.* For each surface entry, ask: "Could this pattern name be applied to any organization in this sector without modification?" If yes, the entry is too generic — the surface captured the *kind of thing* the source talked about rather than the *specific way this organization thinks about it*. Generic patterns produce modules that are technically grounded in sources but indistinguishable from a generic-template version of the same module.

Examples of generic vs. organization-specific:

- **Generic:** "How the organization thinks about client engagement"
- **Specific:** "How the organization decides which client situations require capacity-building vs. delivery, with the tradeoff that capacity-building takes longer but produces better long-term outcomes — sources cite the [specific reasoning] behind this preference"

The specific entry names the actual judgment the organization has worked through. The generic entry names a topic. Topics produce summary-shaped modules; named judgments produce metaprompts.

If a surface entry can apply to any organization in the sector, return to the source and reach for the specificity. The right pattern names the organization's actual reasoning move, not the domain that reasoning happens within.

### Step 5: Section Plan

Plan every section the module will contain *before* writing prose. The Section Plan is the structural intervention against narrative-prose drift, quote contamination, name contamination, and content restatement — because each is decided here, not edited out after.

For each section, write — in `<OUTPUT_PATH>/_scratch/[module-id]-plan.md` under the Step 5 section:

```
Section: [name]
Reasoning captured: [one sentence]
Shape: [reasoning context | decision framework | prescriptive rule | cross-reference | reach-beyond signal]
Why this shape (not another): [one phrase — the alternative shape that was rejected and why]
Source patterns this section encodes: [reference Step 4's surface entries by number]
Owned content this section needs: [content area + use-shape from proposal's Ownership and Use-Shape table]
Quote/individual handling: [for any source quote or named individual that informed this section: the EXTRACTED REASONING that will appear, with the explicit note that the quote/name will not]
```

The "Why this shape" line surfaces the reasoning path alongside the conclusion. When self-check or user review identifies a shape failure, this line is what the failure-recovery protocol uses to diagnose whether the plan was wrong (the reasoning misjudged what the content is) or the prose drifted from a correct plan. Without it, diagnosis collapses to guesswork.

**Strict rules for the plan:**

- **Shape is committed to before writing.** If the plan says "reasoning context," writing the section as third-person prose about the organization means the prose drifted from the plan — redo the plan or redo the prose, but do not "edit toward" the right shape. (See the failure-recovery protocol below.)
- **For shape reference, see ARCHITECTURE.md, "Shape Reference: F0 as a Worked Example."** F0 illustrates how reasoning context, decision framework, and prescriptive rule coexist in one module. When uncertain what shape a section should take, look at F0.
- **The Ownership and Use-Shape table is authoritative.** If a section needs content that another module owns, the plan names the use-shape from the proposal. Restatement is not a use-shape. If the proposal didn't specify a use-shape and the situation needs one, pause and update the proposal with the user.
- **Quote and named-individual handling is mandatory whenever a source quote or named individual informed the section.** Write the extracted reasoning in the plan. The quote does not appear in the plan as text-to-include; the name does not appear in the plan as a person-to-attribute. Quote-extraction is the default path because the plan forces it before generation.

If a section's plan reveals that the section duplicates another module's content, doesn't have a clear shape, or depends on quotes/names you can't extract — that's a structural problem to fix in the plan, not in the prose.

### Step 6: Write the Module

Use the module template from [references/TEMPLATES.md](../TEMPLATES.md).

Write each section *as the plan committed to it*. The plan named the shape, the source patterns, the use-shape for any owned content, and the extracted reasoning for any quote or named individual. Generate prose from the plan.

**While writing:**

- The runtime frame from Step 1 governs every sentence. If a sentence only makes sense to someone in the build, it is contamination — even if the sentence contains accurate organizational reasoning. Rewrite without the build-perspective referent.
- Source quotes and named individuals do not appear in the prose. The plan extracted the reasoning; the prose states the reasoning as instruction to the agent. If a quote or name surfaces in the prose, you are generating from the source rather than from the plan — return to the plan.
- Owned content uses the shape from the plan. Cross-reference, subset, invocation by name, or reach-beyond. Restatement is not a shape.
- Reasoning context shape is *instruction to the agent*, not third-person description. "When evaluating X, weigh A more heavily than B because [reasoning]" is instruction. "The organization weighs A more heavily than B" is description and contaminates the module with explanatory shape.

**Include a verification log (removed before delivery):**

```markdown
<!-- VERIFICATION
| Fact | Source | Exact Text |
|------|--------|------------|
| [fact] | [source file] | [exact quote from source] |
-->
```

Mark inferences with `[PROPOSED]`. Mark exact-copy content with `[HIGH-STAKES]`.

### Step 7: Self-Check

After writing, verify against the Section Plan and the Substantive Source Surface — not as a fresh evaluation of the prose, but as a comparison against what was committed to.

**Plan-vs-prose checks:**

1. **Section shape:** For each section, does the prose match the shape committed to in the plan? A section the plan called "reasoning context" written as third-person description is a shape failure — the prose drifted from the plan. Redo the plan or redo the prose; do not line-edit toward the right shape. (See the failure-recovery protocol below.)

2. **Source surface presence:** For each entry in the Substantive Source Surface (Step 4), can you point to the section where it appears? If a surface entry has no presence in the module, either the surface was wrong or the writing dropped it. Decide which and fix accordingly.

3. **Use-shape compliance:** For each section that incorporates owned content, does the prose use the shape committed to (cross-reference, subset, invocation, reach-beyond)? Restatement is a shape failure — the using module is restating canonical content instead of pointing to it.

4. **Quote and name extraction:** Search the prose for direct quotes (look for quotation marks around extended source phrases), named individuals (people from the source who appear by name), and anecdote framing ("when [person] said," "the team noted that"). For each hit, return to the plan's extracted reasoning and rewrite the passage as instruction to the agent. If the plan didn't extract reasoning for that quote or name, the plan was incomplete — redo it.

**Runtime-frame checks:**

5. **Contamination scan:** Search the prose for: "the source," "the sources," "the source set," "the library," "the build," "the proposal," any source filename, any date attached to document provenance ("in 2025-era sources," "the late-2024 strategy"), "as documented in," "per the [document type]." Each hit is contamination. Rewrite the sentence so it makes sense to a runtime agent that has none of those referents.

6. **Runtime-test:** Pick three sentences from the module at random. For each, ask: "Would this make sense to a reader who knows nothing about how this module came to exist?" If any of the three doesn't make sense without build context, the module has a contamination pattern that needs structural fixing.

**Substance and discipline checks:**

7. **Single source of truth:** Is any content in this module also stated in another module that already exists? If so, the canonical version stays in its owner module per the Ownership and Use-Shape table; this module cross-references.

8. **Volatile check:** Are there any counts, prices, named lists, or other volatile data? Move to addenda.

9. **HIGH-STAKES check:** Are legal names, EINs, financial figures, credentials copied exactly from sources?

10. **Token depth:** Is this module substantive enough? A module under 1,000 tokens probably needs more behavioral guidance. A module at 600 tokens has almost certainly been stripped to facts.

11. **Source verification:** Can you trace every fact to a source file? Remove anything you can't verify.

12. **Cross-references:** Are connections to related modules explicit?

13. **Audience reasoning check:** If this module governs engagement, qualification, or content production — does it include reasoning about the humans on the other end? Not persona profiles or sector categories, but a needs-based framework: what do the people this agent interacts with or writes for actually need, and how do those needs interact and shift by context?

If checks 1–6 fail, the module has structural problems. Follow the failure-recovery protocol below — do not regenerate the module by re-running Step 6.

If only checks 7–13 fail, line-level edits are appropriate.

### Step 8: Update Build State and Process Log

**Build-state gets one line.** Status only.

```
Module [ID] — sources re-read: [list of files] — complete
```

That is all that goes in build-state. Do not log commitment-gate answers, source-grounding statements, surface entries, plan summaries, self-check results, or any other substantive reasoning in build-state. Build-state stays terse so it functions as a session-bootstrap and resume reference.

**Process-log gets one substantive entry per module:**

- What organizational reasoning the module captures
- Any user corrections or direction changes during this module's writing
- Decisions about what was included vs. cut and why
- Source insights that surprised you or changed your approach
- Anything the next module or next session needs to know

Keep the entry concise — reasoning and decisions, not narratives.

The planning artifacts (Step 1's frame statement, Step 2's gate answers, Step 4's surface, Step 5's plan) live in `<OUTPUT_PATH>/_scratch/[module-id]-plan.md`. The plan file remains in `_scratch/` after the module is complete — it is part of the audit trail. The user can read any module's plan to understand how the module came to look the way it does, and the failure-recovery protocol uses the plan to diagnose what went wrong when a module fails.

If a planning artifact contained a decision or insight that matters for *later modules* or future builds, surface it in the process-log entry as well. The plan file is per-module; the process-log entry connects modules.

---

## When a Module Fails (Failure-Recovery Protocol)

A module *fails* when checks 1–6 in self-check don't pass, or when the user reviews the module and identifies structural problems (narrative prose, quote contamination, build-perspective contamination, restated canonical content, missing source substance, wrong shape).

The default move is "rewrite differently" — re-run Step 6 with the same plan and hope for a different result. This produces oscillation: the rewrite fixes the named failure mode but introduces a different one, because the underlying planning was wrong but the rewriting started from the same plan.

**The protocol when a module fails:**

### Step F1: Name the Failure Mode

Be specific. Not "the module didn't pass" — name the pattern:

- Narrative prose: third-person description of the organization rather than instruction to the agent
- Build-perspective contamination: sentences that only make sense inside the build
- Quote or name contamination: source quotes or named individuals appearing in module text
- Restated canonical content: the module describes content that another module owns
- Missing source substance: the module captures generic patterns rather than what the sources specifically reveal
- Wrong shape: a section the plan called reasoning context is written as decision framework, or a section that should be reasoning context is written as a flattened gate-set, or vice versa
- Other: name it specifically

If the failure mode isn't on this list, name it precisely in your own terms before continuing.

### Step F2: Locate the Upstream Cause

For each named failure mode, the cause is in one of the planning steps:

| Failure mode | Likely upstream cause |
|--------------|------------------------|
| Narrative prose | Step 5 (Section Plan) didn't commit to a shape, or the shape was wrong for the content |
| Build-perspective contamination | Step 1 (Runtime Frame Set) was skipped or thin |
| Quote/name contamination | Step 5 (Section Plan) didn't extract reasoning from the quote/name |
| Restated canonical content | Step 5 (Section Plan) didn't apply the use-shape from the Ownership and Use-Shape table |
| Missing source substance | Step 4 (Substantive Source Surface) was thin, or surface entries came from comprehension findings rather than just-read sources |
| Wrong shape | Step 5 (Section Plan) committed to the wrong shape — usually because the underlying judgment about what the content is wasn't worked through |

### Step F3: Redo the Upstream Step

Do not regenerate the prose. Redo the planning step that was thin or wrong.

- Wrong shape → redo the Section Plan for that section, with the correct shape committed
- Missing source substance → re-read sources and redo the Substantive Source Surface; the surface must come from the just-read sources
- Build-perspective contamination → restate the Runtime Frame and identify the specific build-perspective referent the contaminated sentences depended on; rewrite without that referent
- Quote/name contamination → redo the Section Plan's Quote/individual handling for the contaminated section; extract the reasoning explicitly
- Restated canonical content → consult the Ownership and Use-Shape table; pick the correct shape; redo the Section Plan for the affected section
- Narrative prose → diagnose more specifically. If the section's plan called for reasoning context but the prose became narrative, the plan was correct but the writing drifted (Step 6); rewrite with the plan visible. If the plan also was wrong, redo Step 5 first.

### Step F4: Regenerate from the Corrected Plan

Now write again — but only the affected sections, and only from the corrected plan. The corrected plan is the input to writing; the prose is the output.

If multiple sections failed for the same upstream cause, fix the upstream cause once and regenerate all affected sections from the corrected plan.

### Step F5: Log the Diagnosis

In process-log:

```
- Module [ID]: failed on [named pattern]. Upstream cause: [planning step]. Fix: [what was redone]. Sections regenerated: [list].
```

This produces a compact record of why the module looks the way it does on its second attempt — and prevents the build agent from re-running the failed planning step on the next module.

**The architectural intervention:** the build agent cannot rewrite a failed module without first naming the failure mode, locating the upstream cause, and redoing the planning step that produced it. This converts oscillation into convergence — each fix targets the actual cause, not a symptom.

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

**Agent definitions are system prompt preambles.** They are loaded into the agent's context at runtime — they tell the agent who it is, what it does, and what items are always in its context vs. conditionally loaded. Write them as instructions TO the agent, not documentation ABOUT the agent.

For each agent (from the proposal):

1. **Re-read the proposal's agent definition** for this agent
2. **Re-read the proposal's Load-Discipline Classification table** for this agent's rows. The classification commits which items are `always_load` vs. `conditional` and the `load_when:` triggers. Build executes the table; do not redecide at agent-write time.
3. **Review all `always_load` items** — skim each one to confirm the always-loaded set serves this agent's role
4. **Write the agent definition** using the template from [references/TEMPLATES.md](../TEMPLATES.md)

**The runtime section (what the agent reads) must include:**

- Identity and role — written in second person ("You are...", "You handle...")
- The `always_load` set — items in the agent's system prompt every time, with brief notes on what each provides
- The `conditional` set — items with `load_when:` triggers in plain language; the agent reads these as runtime instructions for when to load each
- Domain-specific guidelines — behavioral extensions beyond standard guardrails

**The manifest frontmatter must use the `always_load` / `conditional` shape from the template, not earlier tier-grouped shapes.** The body of the agent definition mirrors the manifest's classification (group items by load discipline, not by tier). Tier folders (`modules/foundation/`, `modules/shared/`, `modules/specialized/`) are structural file locations for humans and tooling — they do not describe load discipline. The runtime agent reads the manifest, not the folder structure.

**The build metadata section (HTML comment, not visible to the agent) tracks:**
- Token budget breakdown — total of `always_load` items only (conditional items don't count against the budget)
- Module rationale table (why each item is in this agent's set, and the classification reasoning)
- Build notes (decisions made about this agent's configuration)

**Budget assessment for each agent:**
- Sum tokens from `always_load` items (modules and addenda alike — both count when always-loaded)
- Compare to 10% of target model context window
- If under 50%: flag as potentially underserved — review whether the agent needs richer modules or additional always-loaded context
- If over 100%: identify what to trim — remove items not essential for this role, not compress existing items

**Do not write custom guardrail sections in agent definitions.** Load the standard guardrail modules (F0 always; S0 always for any agent that writes anything) and add only domain-specific extensions if needed.

### Hard-Rule Self-Check

After writing each agent's manifest, verify:

- **F0_agent_behavioral_standards is in `always_load`** if it appears in this agent's set. If it's in `conditional`, the manifest is wrong — fix before continuing. (Hard rule. Not a judgment call.)
- **S0_natural_prose_standards is in `always_load`** if it appears in this agent's set. If it's in `conditional`, the manifest is wrong — fix before continuing. (Hard rule. Not a judgment call.)
- **Every `conditional` item has a `load_when:` trigger** that meets the Trigger Discipline (see ARCHITECTURE.md): one axis, plain "when X" phrasing, right-side specificity. If a trigger is missing or fails the discipline, fix before continuing.
- **The classification matches the proposal's Load-Discipline Classification table** for this agent. If you disagreed with the proposal's classification while writing, surface that to the user — do not silently change it.

**The test:** Read the agent definition back. Does it sound like a system prompt that configures an agent, or like a project management document that describes one? If the latter, rewrite it as instructions the agent will follow. Does the manifest's `always_load` set match what the agent's runtime context will be? If a runtime task could plausibly be one where the agent skips an `always_load` item by judgment, that item should not be `always_load` — or it should be `always_load` with the discipline that the agent does not skip it. The classification removes the judgment call; the manifest must reflect that.
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
- [ ] Section shapes match what was committed in the Section Plan (no narrative-prose drift)
- [ ] Substantive Source Surface entries are present in the module (not just facts)
- [ ] Owned content from other modules uses the committed use-shape (cross-reference, subset, invocation, or reach-beyond — never restatement)
- [ ] No quoted material from sources used as content; no named individuals attached to organizational reasoning
- [ ] No build-perspective contamination ("the source," "the library," "the build," named source files, document-provenance dates, "as documented in")
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
- [ ] Item set serves the agent's actual decision-making needs
- [ ] Manifest uses `always_load` / `conditional` shape (not tier-grouped)
- [ ] F0 in `always_load` if present (hard rule)
- [ ] S0 in `always_load` if present (hard rule)
- [ ] Every `conditional` item has a `load_when:` trigger meeting Trigger Discipline
- [ ] Token budget assessed (always_load items only) — neither starved nor bloated
- [ ] Standard guardrails loaded (F0 for all; S0 for any agent that writes anything)

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
