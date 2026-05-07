# Phase 3: Design

> **CRITICAL RULES — Read these first:**
> - The story emerges from the comprehension findings. Do not commit to a structure before you've found the story.
> - Apply the Source Before Statement gate to every empirical claim.
> - Do not load any file from an `Archive/` directory.
> - The structural plan is NOT a blueprint the agent paraphrases into prose. It is a set of thinking orientations — metaprompts that tell the drafting agent how to think about each section, not what the prose should contain.

---

## What This Phase Does

Find the story the evidence tells, build an emotional arc, determine section structure, and write the structural plan as metaprompts. The output is a compact article plan that the Draft session reads cold — keep it tight, because it competes with voice profile and writing standards for context attention.

**Read [references/ARCHITECTURE.md](../ARCHITECTURE.md) now** — specifically Narrative Construction and Article Structure.

**Re-read the writing standards module and voice profile now.** They were loaded in Setup, but Comprehend's research processing may have pushed them deep in context. Design needs them fresh — the writing standards' structural conventions shape how sections open and connect, and the voice profile's thinking patterns determine which generative mode leads each section. Re-read both documents fully before proceeding.

---

<phase_design_story>
## Step 1: Find the Story

Work through these in order. Each builds on the previous. The comprehension findings from Phase 2 are your input — the story emerges from what you understood, not from the outline's argument arc.

**The story question:** What happened — or what is happening — that this article makes visible? Not "what is the thesis" but "what's the story that earns the thesis?"

**The emotional arc:** Where is the reader at the beginning — emotionally, not informationally? What do they feel? What do they believe? Where are they at the end? What shifted?

**The single thread:** What is the one narrative thread connecting the evidence? One sentence. If the evidence doesn't connect along a single thread, the article will read as a data arrangement.

**From the audience document:** Re-read for this specific article. Where is the reader in the series build (if series)? What register applies? What does search behavior tell you about what they need?

**From keyword research (if available):** What did the reader search for? The opening must connect to search intent within the first two paragraphs.

**From the voice profile:** Which generative mode leads? Where does the article shift between modes? How does this person think through problems — what's their entry point pattern, their reasoning sequence?

**From the writing standards:** What structural conventions govern this genre? How do sections open? How does evidence enter? How do passages land?

---

## Step 2: Determine Section Structure

After the story is clear, determine section structure based on the story, the emotional arc, the single thread, and the writing standards' structural conventions — not based on the evidence loading order or the outline's sequence.

For each section, identify:
- Purpose (what it does for the argument)
- Key evidence (2–3 findings that carry the structural claim)
- Reader entry point ("The reader already knows from their own work that...")

### Alternative Structure Check

**Before committing:** Generate at least one alternative structure. Name what each gains and what it loses. Choose — and log why. This is required, not optional.
</phase_design_story>

---

<phase_design_plan>
## Step 3: Write the Structural Plan as Metaprompts

The structural plan tells the Draft session how to *think about* each section — not what the prose should contain. Each section gets a metaprompt: a thinking orientation that tells the drafting agent what stance to take, what to look for in the research, what the reader should arrive at, and how this section connects to the ones around it.

**What a metaprompt is NOT:**
> 1. **Open with the dead end.** We had built educational materials for a denomination — videos that became the most-viewed content on their YouTube channel, lessons on a website... [paragraph of detail]

This is too detailed — it becomes a pre-draft. The agent paraphrases it instead of writing from research.

**What a metaprompt IS:**
> **Section 3: The Constraint.** You discovered that the insight from Section 2 doesn't scale naively — and the failure is what taught you the discipline. Think about this section as the moment where more became worse, and how the constraint itself became the methodology's origin. The reader should arrive at modular design as an inevitability, not as a framework you're teaching them. Re-read the research for the token economy discovery and the iterative loop.

The agent still re-reads research, finds material, writes from it. The metaprompt tells it what stance to take and what to look for — not what the prose contains.

### Write the Role Block

Before writing the section metaprompts, write the `<role>` block in the article plan. This is the identity assignment the Draft session will encounter when it loads the plan cold. It must be written in first person — as the author speaking, not a description of the author.

The role block draws from the voice profile (who the person is, how they think) and from the story and audience decisions you just made (which mode leads, what matters for this piece). Keep it to 4-6 sentences total. Include the manifest paths for voice profile and writing standards so the Draft session knows where to re-read the full documents.

**Test:** Read the role block back. Does it sound like a person stating who they are, or like an analyst describing someone? If the latter, rewrite it in first person.

### For Each Section, Write:

**Section title and metaprompt** — 3-6 sentences. What stance to take, what to look for in the research, what the reader should arrive at, how this section relates to the ones around it. Reference specific research elements the agent should re-read — by topic, not by quoting them.

**Closing handoff** — One sentence: the implicit question this section creates that makes the next section necessary.

**Key evidence** — 2-3 research elements (by short name/topic) that carry this section. The agent will re-read these during drafting.

### Structural Checks

**Structural question:** One question that every section answers from a different angle. Not the thesis — the question that makes the reader need the thesis. Write it in one sentence.

**Article movement:** In one phrase, describe the direction the reader moves: from what understanding to what different understanding?

**Frame persistence:** How does the opening frame (person, event, question) remain present throughout? One bullet per section.

**Necessity test:** For each section, state what the reader could NOT understand without it. If the answer is "nothing — they'd just miss supporting evidence," the section doesn't earn its place.
</phase_design_plan>

---

## Step 4: Create/Update the Article Plan

Using the template at [templates/article-plan.md](../../templates/article-plan.md), create or update `Drafts/article-[N]-plan.md`. Populate the Comprehension Findings from Phase 2 and the Structural Plan from the work above.

**Context economy:** The plan and process log are loaded at Draft time alongside voice profile and writing standards. Every line competes with voice and standards for context attention. The discipline: metaprompts contain thinking orientations (what stance to take, what to look for), not descriptions of what the prose should say. Logs contain reasoning and self-corrections, not restated source material. If the plan reads like a draft summary, it will anchor the drafting agent on paraphrase instead of fresh generation.

**LOG:** Write the story, emotional arc, single thread, and alternative structure tradeoffs to the process log. The structural plan itself goes in the article plan, not duplicated in the log.

---

## GATE

Write to the process log:
- "Writing standards re-read: [filename]"
- "Voice profile re-read: [filename]"
- "The story: [one paragraph]"
- "Emotional arc: reader starts [X], ends [Y]"
- "The single thread: [one sentence]"
- "Search entry point: [what they searched for]"
- "Generative mode: [from voice profile]"
- "Structural question: [one sentence]"
- "Article movement: [one phrase]"
- "Section count: [N], each with metaprompt, handoff, key evidence"
- "Role block written: [yes — first-person identity assignment in article plan]"
- "Alternative structure considered: [what, why rejected]"

---

## STOP 2

**Present to the user:**
- The story — what this article makes visible
- The emotional arc — where the reader starts and ends
- The single thread — one sentence
- The structural question and article movement
- The proposed section structure with metaprompts (the full thinking orientations, not summaries)
- The alternative structure considered, with tradeoffs
- Any places where the outline's argument arc doesn't match what the evidence supports
- Any additional research that would strengthen the article

**Ask:** Does this structural plan — the story, the section thinking orientations, the movement — match how you see the argument building? The Draft session will write from these metaprompts, so they need to capture the right thinking orientation for each section.

**This is the second validation point.** The user validates the *design* before drafting begins. Do not proceed until the user confirms or provides additional direction.

---

## After This Phase

Update the article plan:
- **Current phase:** Phase 4 (Draft)
- **Next phase file:** `references/phases/PHASE_4_DRAFT.md`

**Tell the user:** "The article plan is saved at `Drafts/article-[N]-plan.md`. **Start a new session before drafting** — the draft session needs a full context window for voice profile generation to work. Say 'Resume drafting Article [N]' to continue."

**The boundary between Session A and Session B is mandatory.** Always start a new session before Phase 4.
