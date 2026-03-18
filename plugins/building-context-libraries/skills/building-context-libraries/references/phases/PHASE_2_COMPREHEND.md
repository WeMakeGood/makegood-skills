# Phase 2: Comprehend

> **CRITICAL RULES — Read these first:**
> - This phase exists because the agent's default is to read source titles, guess at a taxonomy, and propose modules. Comprehension is the counter — understand how the organization thinks before committing to any structure.
> - **Do not propose any module structure in this phase.** Structure comes in Phase 3 (Design).
> - Apply the Source Before Statement gate to every claim about the organization.
> - Re-read sources as needed. Memory blurs; sources don't.
> - Buried-signal sources (transcripts, raw notes) are handled HERE — extract the organizational reasoning directly, don't rewrite them into clean documents first.

---

## What This Phase Does

The agent reads what it indexed and thinks about it — not to organize information into categories, but to understand how the organization *thinks*: its principles, values, tradeoffs, and reasoning patterns. What makes it distinct? How does it make decisions? What would an agent need to understand to think well on its behalf? The output is a set of comprehension findings: organizational reasoning patterns, convergences, tensions, and gaps. No structural decisions yet.

---

<phase_comprehend_sources>
## Step 0: Load All Sources

**GATE:** Before any comprehension work, read every source file listed in the source index. Not skim — read. The comprehension that follows depends entirely on having the actual source content in context, not on summaries or memories from Setup.

1. Read `<OUTPUT_PATH>/source-index.md` — get the complete file list
2. Read every source file in the index, in order
3. Write to the build state: "Sources loaded for comprehension: [count] files read in this session"

**Do not proceed to Step 1 until all sources are loaded.** If the source set is too large to read in one pass, read in clusters — but every source must be read before the GATE at the end of this phase. Comprehension built on partial reading produces partial understanding.

---

## Step 1: Work Through the Sources

Now work through the source documents — not as files to categorize, but as evidence of how the organization operates.

For each source (or cluster of related sources):
- What organizational **reasoning** does this reveal? (Not "what facts does it contain" but "what does this tell us about how the organization thinks, decides, and evaluates tradeoffs?")
- What principles or values drive the decisions described here?
- **How does this organization think about the people it serves and writes for?** Look for audience reasoning embedded in how the org talks about discovery conversations, content strategy, qualification, and communication. The signal won't be "our audience needs X" — it will be in how they describe adapting to different situations.
- What surprised you? What contradicts your initial assessment from Setup?
- Where does this source agree with or create tension with others?

**For buried-signal sources (transcripts, interviews, raw notes):** Extract the organizational reasoning directly. The filler words, false starts, and conversational hedging are noise — the principles and tradeoffs underneath are the signal. You do not need to create a clean rewrite. You need to understand what the person was actually revealing about how the organization thinks.

**LOG:** For each source or cluster, write 2-3 sentences: the organizational reasoning this source reveals and why it matters for how agents should think. Do not summarize the document.

---

## Step 2: Find Convergences

Different sources often describe the same underlying organizational pattern without using the same terms. A strategy document might describe the principle one way while a process document encodes it as a specific operational step. These convergences reveal something about the organization that neither document says alone.

Look for:
- **Same pattern, different language** — two sources describing one organizational behavior
- **Complementary evidence** — one source explains *why*, another shows *how*
- **Cross-domain connections** — an external-facing pattern that mirrors an internal operations pattern

**LOG:** Write each convergence as 2-3 sentences: what connects, and what the connection reveals about how the organization thinks.

---

## Step 3: Identify Tensions and Conflicts

Where do sources disagree or create tension? Not just factual contradictions (those were flagged in Setup), but philosophical or strategic tensions:
- Does the stated strategy align with the operational reality?
- Do different stakeholders describe the same process differently?
- Are there aspirational positions that don't match current practice?

These tensions need resolution before modules can be built. Some are real conflicts requiring user input. Others are complementary perspectives that modules should reconcile.

**LOG:** Each tension with: what conflicts, which sources, and whether it's a real conflict (needs user resolution) or a complementary perspective (modules should integrate both).

---

## Step 4: Map What Agents Need to Understand

Based on your comprehension — not based on source file categories — identify:

- **The reasoning patterns agents need to internalize.** How does the organization think about its core domains? What principles, values, and tradeoffs should shape how agents approach their work? (These become module content.)
- **The situations agents will face.** What contexts will agents encounter where they need organizational reasoning to think well? (These shape module scope.)
- **How the organization thinks about its audiences.** Who does this organization serve, and how does it reason about what those people and organizations need? Who reads or receives the organization's work, and what determines how the org adapts for different audiences? Frame as interacting needs on spectrums, not as persona types or sector categories. (This becomes audience reasoning within relevant modules.)
- **The boundaries agents should respect.** What genuine constraints exist where violation causes real harm? (These become the rare prescriptive rules.)
- **Where agents should reach beyond modules.** What kinds of situations require specific data (addenda), capabilities (skills), or human judgment (user input)? (These become reach-beyond signals in modules.)
- **What's missing.** What would an agent need to understand that the sources don't provide? (These are gaps to carry forward.)

Refine the agent roles from Setup based on deeper understanding. Do agents align with the reasoning domains you've now identified, or do they need restructuring?

**LOG:** Updated agent roles with: what each agent needs to understand (reasoning, not procedures), what situations it will face, what organizational thinking it needs to navigate those situations well.
</phase_comprehend_sources>

---

## GATE

Write to the build state:
- "Reasoning patterns identified: [list — how the organization thinks about its core domains]"
- "Convergences found: [list — where different sources reveal the same underlying principle]"
- "Tensions requiring resolution: [list or 'none']"
- "Agent roles refined: [list — what each agent needs to understand and what situations it will face]"
- "Reach-beyond needs: [list — where agents will need addenda, skills, or user judgment]"
- "Gaps carried forward: [list — what agents need to understand that sources don't provide]"
- "Comprehension complete: all sources read for organizational reasoning, not just cataloged"

---

## STOP

**Present to the user:**
- The key reasoning patterns you identified — how the organization thinks about its core domains, what principles and tradeoffs drive its decisions
- Convergences — where different sources reveal the same underlying principle
- Tensions — real conflicts that need resolution vs. complementary perspectives
- Refined agent roles — what each agent needs to understand and what situations it will face
- Reach-beyond needs — where agents will need addenda, skills, or user judgment
- Gaps — what's missing and how it affects agent capability
- Any sources that turned out to be less relevant than initially classified

**Ask:**
- Do these reasoning patterns match your understanding of how the organization thinks?
- Are the tensions I identified real, or am I misreading the sources?
- Do the refined agent roles match the work you need agents to do?
- For the gaps — can you provide the missing information, or should we note the limitation?

**This is the validation point for comprehension.** The user validates the *understanding* before any structure is proposed. If the understanding is wrong, everything built on it will be wrong.

**Do not proceed until the user confirms or provides additional direction.**

**After the user responds, log to `process-log.md`:**
- Key comprehension insights and why they matter for the library
- User corrections or direction changes from the STOP review
- Anything that shifted your understanding from what you expected after Setup

---

## After This Phase

Update build state:
- **Current phase:** Phase 3 (Design)
- **Next phase file:** `references/phases/PHASE_3_DESIGN.md`

**Tell the user:** "Comprehension is complete. **Start a new session before Design** — Design needs the metaprompt transformation rules and architecture reference fresh in context, not buried under source material from this session. Say 'Resume building context library' to continue."

**The boundary between Session A and Session B is mandatory.**
