---
name: building-context-libraries
description: Builds modular context libraries that change how AI agents behave with organizational knowledge. Transforms source documents (transcripts, strategy docs, process documents, interviews) into metaprompt modules — system prompt components that shape agent decision-making. Use when user says build context library, create context library, create agent context, build knowledge base, transform documents into agent context, build domain context, or create organizational context modules. Activates when organizational source documents are provided via file path or directory.
---

# Building Context Libraries

<purpose>
Claude defaults to copying content from sources — restating facts in cleaned-up form feels
productive but produces modules useless as agent context. This skill exists because context
libraries must contain metaprompting (instructions that change how agents behave), not content
(facts agents can parrot back). The skill enforces transformation at every phase through
commitment gates that require demonstrating behavioral change before any module is written.
</purpose>

## Core Concept

**You are creating system prompt components for LLM agents, not documentation for humans.**

Modules are metaprompts. They change how agents *behave* — what they decide, how they respond, what they prioritize. A module that an agent could ignore without changing its behavior is a failed module.

| Level | What It Is | Test |
|-------|-----------|------|
| **Content** (wrong) | Facts copied from sources | Agent behavior unchanged if removed |
| **Context** (minimum) | Processed knowledge shaping decisions | Agent makes different choices with it loaded |
| **Metaprompting** (target) | Behavioral instructions with decision logic | Agent acts on it without interpretation |

See [references/ARCHITECTURE.md](references/ARCHITECTURE.md) for the full module design philosophy, content transformation rules, and token management.

---

## Critical Rules

**SOURCING:** Every fact in the library must trace to a source document. Before stating any claim about the organization, locate its source. If you cannot locate a source, state what's missing rather than approximating. NEVER invent details. NEVER fill gaps.

**EPISTEMIC CALIBRATION:** The reader should always be able to tell whether a claim is sourced from documents, inferred from cross-document patterns, or your analytical interpretation — because your language makes the distinction clear. During the build, use `[PROPOSED]` markers for inferences (removed before delivery).

**PROFESSIONAL CHALLENGE:** When a user's proposed module structure contradicts what the sources support, when an approach has known pitfalls (taxonomy-based modules, content-copying, over-compression), or when assumptions aren't grounded in sources — cite the concern, offer an alternative.

**TRANSFORM, DON'T TRANSCRIBE:** Before writing any module section, identify the organizational reasoning it provides and whether an agent could apply it to situations the author didn't anticipate. Modules provide reasoning context — how the organization thinks — not procedures or exhaustive rules. Prescriptive "If X, do Y" rules are rare, reserved for genuine constraints where violation causes real harm.

**CONVERGENCE AWARENESS:** When source documents describe the same underlying pattern differently, the convergence reveals something about the organization that neither document says alone. Explore intersections rather than filing information into the first plausible module.

**CONFLICT RESOLUTION:** When source documents contradict, surface the conflict to the user. Do not silently pick one version.

---

## Reference Files

Read the phase instruction file before each phase. Re-read after any context compaction.

| File | Purpose |
|------|---------|
| [references/ARCHITECTURE.md](references/ARCHITECTURE.md) | Module design, content transformation, token management, stakes classification |
| [references/TEMPLATES.md](references/TEMPLATES.md) | Templates for all build artifacts |
| Phase files in [references/phases/](references/phases/) | Self-contained instructions per phase |

---

## Build Process

4 phases across 2-3 sessions. Each phase has a dedicated instruction file containing everything needed.

| Phase | Name | Instruction File | Function |
|-------|------|------------------|----------|
| 1 | Setup | [PHASE_1_SETUP.md](references/phases/PHASE_1_SETUP.md) | Load sources, create manifest, classify, identify agent needs |
| 2 | Comprehend | [PHASE_2_COMPREHEND.md](references/phases/PHASE_2_COMPREHEND.md) | Read all sources, extract organizational patterns, find convergences |
| 3 | Design | [PHASE_3_DESIGN.md](references/phases/PHASE_3_DESIGN.md) | Propose module architecture, agent definitions, content assignments |
| 4 | Build | [PHASE_4_BUILD.md](references/phases/PHASE_4_BUILD.md) | Write modules with per-module gates, build addenda, validate |

### Session Architecture

| Session | Phases | Why Together |
|---------|--------|-------------|
| A | Setup + Comprehend | Comprehension needs source documents fresh in context |
| **MANDATORY BREAK** | | Design needs a full context window for structural reasoning |
| B | Design + Build | Design feeds directly into module writing |

Session A and B must be separate sessions. **The boundary is mandatory** — Comprehend processes many source documents, and Design needs the metaprompt transformation rules fresh in context, not buried under source material.

Build may extend into Session C if the library is large. Each module is self-contained — resume from `build-state.md`.

---

<phase_start>
## Starting a New Build

1. **Ask the user:**
   - "Where are your source documents?" → `SOURCE_PATH`
   - "Where should I create the context library?" (default: `./context-library/`) → `OUTPUT_PATH`
   - "What domain agents will use this library?" (optional — can be derived in Comprehend)

2. **Read the Phase 1 instruction file:** [references/phases/PHASE_1_SETUP.md](references/phases/PHASE_1_SETUP.md)

3. **Begin Phase 1.**
</phase_start>

---

<phase_resume>
## Resuming a Build

If `<OUTPUT_PATH>/build-state.md` exists:

1. **Read `build-state.md`** — it tells you the current phase, what's done, and what's next.
2. **Read the phase instruction file** it points to.
3. **Continue from where work left off.**

If `build-state.md` does not exist but `source-index.md` does:

1. **Read `source-index.md`** — check its status field and reading checklist.
2. **Determine the current phase** from the index status.
3. **Create `build-state.md`** to track progress going forward.
</phase_resume>

---

<failed_attempts>
## What DOESN'T Work

- **A separate synthesis phase:** The old architecture spent an entire session rewriting transcripts into "clean working documents." This produced restatements, not insights. Comprehension handles messy sources directly — the behavioral pattern is what matters, not a polished rewrite.

- **Running all phases in one session:** Context compaction destroys metaprompt transformation rules. By the time the agent reaches module writing, it's reverted to copying content because the instructions governing transformation are gone. The mandatory session break exists so Design and Build start with fresh rules.

- **Deriving agents after building modules:** The old architecture built modules first, then designed agents to use them — an afterthought. Agent definitions belong in Design because who needs what context is a structural question that shapes module architecture.

- **Proposing structure before understanding sources:** The default is to read source titles, guess at a taxonomy, and propose modules. Comprehension forces the agent to understand what the organization actually *does* before committing to any structure. Without this, modules organize facts instead of shaping behavior.

- **Token minimization:** The old architecture's budget framing ("warning at 80%") produced lean agents that lacked the context to make good decisions. An agent using 60% of its budget isn't efficient — it's underserved. The budget is room for useful content, not a ceiling to stay under.

- **Content-copying disguised as synthesis:** Restating "they said X" with quotation marks is not transformation. The test: does this module instruction tell an agent what to *do* in a specific situation, or does it just report what someone said?

- **Skipping source re-reads across sessions:** The agent assumes it remembers sources from previous sessions. It doesn't — after a session break, context is empty. Every phase has a mandatory loading gate that requires reading actual source files before doing any work. Design without sources produces structures based on memory. Build without sources produces modules based on impressions. Both drift from what the sources actually say.

- **Narrative prose disguised as metaprompting:** The agent writes modules that read as "About Us" pages — historical narratives, explanatory prose, third-person descriptions of the organization. These pass the agent's own transformation test because they contain reasoning, but they're expressed as explanation rather than instruction. The test must be sharper: "Is this written as an instruction to the agent, or as an explanation about the organization?"

- **Source-index classifications as skip permissions:** Labels like "legacy," "pre-reorg," or "reference only" assigned during Setup triage get carried into Build as authority on what to read. A pre-reorganization document often describes operational reality that hasn't changed. The source index classifies signal clarity and triage priority — it does not determine what gets read during module writing. The proposal's source assignments are authoritative.

- **Commitment gates answerable from summaries:** The agent can articulate "this module equips the agent to think about X" from comprehension findings alone, without ever re-reading a source file. The gate tests articulation of purpose, not source engagement. A source-grounding question forces the agent to name a specific pattern from a source file it read in the current turn.

- **AI-centrism in module content:** The agent gravitates toward AI-related content in sources and builds modules around it, underweighting work that predates or exists alongside AI adoption. If the organization has twenty years of non-AI work, that work must be proportionally represented in modules — AI is part of the organizational story, not its summary.

- **Validation as a separate phase:** Quality built into per-module commitment gates catches problems at the source. A final-stage validation pass can't fix modules that were written as content instead of metaprompts — the structural problem is upstream.
</failed_attempts>
