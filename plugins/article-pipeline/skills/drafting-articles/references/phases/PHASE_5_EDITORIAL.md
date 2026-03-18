# Phase 5: Editorial Cycle + Quality Check + Present

> **CRITICAL RULES — Read these first:**
> - **Read the project manifest FIRST.** Load the writing standards module and voice profile from their manifest paths. **Do not proceed without loading both.** This session starts cold — these documents are not in your context unless you load them now.
> - Re-read the draft file before starting editorial work. Do not work from memory of what you wrote.
> - Re-read the voice profile before each editorial round. The voice profile is the standard — not your memory of what the draft should sound like.
> - Re-read [references/ARCHITECTURE.md](../ARCHITECTURE.md) before starting.
> - Re-read the skill's Critical Rules section (in SKILL.md) — sourcing, epistemic calibration, prose address, and genre rules apply throughout editorial.
> - Apply the writing standards module during every revision pass. This means re-reading the actual standards document, not applying a general sense of "good prose."
> - Apply the Source Before Statement gate — verify sourcing hasn't drifted during revision.
> - Do not tell the user the draft is good. Name weaknesses. The user decides what works.

---

## What This Phase Does

Three sub-phases in one session: multi-round editorial revision, quality standards check, and final presentation. All are revision-focused, operating on the draft artifact.

**This session starts cold.** You did not write the draft — a previous session did. You inherit the draft and the process log but not the context that produced them. The activation gate below ensures you have loaded what you need before editing begins.

---

## Before You Start

1. **Read the project manifest** — locate the voice profile and writing standards paths.
2. **Load the writing standards module** — from the manifest's writing standards path. Read the full module.
3. **Load the voice profile** — from the manifest's voice profile path. Read the full document.
4. **Read `Drafts/article-[N]-plan.md`** — review the `<role>` block (your identity assignment), comprehension findings, and the structural plan (metaprompts).
5. **Read the draft file** — `Drafts/[article-number]-[short-title]-draft-[date].md`.
6. **Read [references/ARCHITECTURE.md](../ARCHITECTURE.md)** — the full file.
7. **Read the process log** — `Drafts/article-[N]-process-log.md`. Review self-corrections from the draft phase — these are the draft's known vulnerabilities. **If the log contains structural corrections from user input** (identified by phrases like "user input," "user direction," "structural revision"), these corrections override the original plan entries. Treat them as binding constraints for the editorial cycle, not suggestions.

### Activation GATE

**REQUIRED before any editorial work begins.** Write to the process log:
- "Role block read: [yes]."
- "Writing standards loaded: [filename]."
- "Voice profile loaded: [filename]. Leading generative mode for this draft: [mode from role block]."
- "Process log reviewed. Key self-corrections from draft phase: [list the 2–3 most important]."
- "Voice check: read draft opening paragraph against the role block. Assessment: [does this sound like the person established in the role block, or like a competent AI writing about their topics? Could any writer have written this, or could only this person?]"

If the voice check finds the draft doesn't sound like the person, note this as a CRITICAL finding for Round 1.

---

<phase_editorial>
## Editorial Cycle

The editorial cycle produces the actual quality. The initial draft is a starting point.

**The cycle runs multiple rounds.** Each round is logged. Continue until a round produces no structural changes — only line-level fixes. Expect 2–4 rounds.

### Each Editorial Round

**Step 0 — Voice fidelity check.** Re-read one gate from the voice profile (rotate gates across rounds). Then read the draft's opening paragraph and one paragraph from the middle. The question is not "does this match the profile's features?" — it is "does this sound like the person?" A person, not a style. If you read the paragraph and it could have been written by any competent writer on this topic, the role has slipped — regardless of whether individual features (short sentences, action verbs) are present.

Use the gates as diagnostic tests:
- **Gate 2:** Did the role naturally produce these sentence structures, or are they default prose?
- **Gate 4:** Are the person's distinctive patterns present because the role produced them, or absent entirely?

If the role has slipped, this is a CRITICAL or structural finding — not a line-level fix. Do not insert missing features. Return to the voice profile, re-adopt the role, and regenerate the passage.

**Step 1 — Reread as a standalone reader.** Read the draft as someone who has never seen the research, the outline, or any other article in the series. For each section:

1. Does the argument follow from evidence *presented in this article*?
2. Is every reference intelligible to someone reading only this article?
3. Are structural claims grounded in the specific situation the article has developed, or are they compressed formulas from research documents?
4. Does every section advance *this article's* argument?
5. Does the single thread from the story connect section to section?
6. Where did the agent follow the outline instead of the argument?

**Step 2 — Check framework consistency.** Read the draft's claims against each other. Does the article contradict its own framework anywhere? These contradictions are highest-priority fixes.

**Step 3 — Apply connection-finding from your behavioral standards.**
- *Reframe before committing:* For any section that feels settled, generate one alternative framing. If better, use it.
- *Cross-domain check:* Does unused evidence illuminate the argument?
- *Second-order check:* What does acting on this article's argument create that wasn't intended?

**Step 4 — Note everything.** Write editorial notes to the log in a numbered table:

| # | Problem | Type | Response |
|---|---------|------|----------|
| 1 | [description] | CRITICAL / structural / line-level / framework / missing connection | [fix or decision] |

**Step 5 — Revise.** Apply fixes. Update the draft file. If a section needs to be deleted and rewritten from scratch rather than edited, do that — editing a fundamentally wrong section produces a polished version of the wrong thing.

**Step 6 — Log the round.** Record what changed and why. Note whether changes were structural or line-level. Note patterns — if the same error type keeps appearing, name the pattern.

**Repeat** until a round produces no structural changes.

### Editorial GATE

Write to the process log:
- "Editorial rounds completed: [number]"
- "Structural changes by round: [summary per round]"
- "Voice fidelity by round: [which gates were checked, what was found, what was regenerated]"
- "Patterns identified: [recurring error types]"
- "Draft current as of: [filepath, final word count]"
- "Reread as standalone: [confirmed — argument holds without reference to unread material]"
</phase_editorial>

---

<phase_quality>
## Quality Check

Run the draft against the loaded writing standards and voice profile. **This is not a confirmation pass.** The quality check's purpose is to find problems the editorial cycle missed because it was focused on argument and structure. If the quality check finds nothing, the check was not run rigorously enough.

**Run these checks in order:**

- **Voice profile** — Read the draft's first paragraph, a middle paragraph, and the closing paragraph. For each, answer: does this sound like the person described in the voice profile, or like a competent AI? Then test against each gate as a diagnostic. Write one sentence per gate to the log. This is the primary quality check — an article that doesn't sound like the person is not a draft of their article regardless of how well-argued it is.

- **Writing standards module** — Apply the loaded writing standards document's process gates and revision backstop. When flagged words or structures appear, the fix is not swapping the word — it is returning to the voice profile and rewriting from the practitioner's perspective. The word is a symptom; the lost voice is the problem.

- **Epistemic integrity** — Does the article help readers think critically, or just feel enthusiastic? Does it preserve the reader's need to think? Are limitations named? Is every empirical claim sourced? Is every analytical move marked as analysis?

- **Research grounding** — Would this article exist without the project's specific research? If any section could have been written by someone with the general topic but not the research base, that section hasn't been written well enough.

**Closing question test:** Read the closing question. Does it genuinely require thought, or does it telegraph the "right" answer?

**LOG:** For each module checked, record one specific finding per module — even if the finding is "no issues in [area]." Use the editorial notes table format (one row per finding). Do not expand findings into paragraphs. A blank "no issues" across all modules is not a valid quality gate output.

**Process log compression (all editorial phases):** Editorial round logs use the numbered table format. Each row is one finding — problem, type, response. Do not write narrative paragraphs between rounds. The table IS the log.

### Quality GATE

Write to the process log:
- "Quality checks run: voice profile, writing standards, epistemic integrity, research grounding"
- "Voice profile check: [one finding per gate]"
- "Issues found and fixed: [list by check type]"
- "Issues found and flagged: [items needing author decision]"
- "Known weaknesses in this draft: [list honestly]"
</phase_quality>

---

<phase_present>
## Present

Present the draft to the user with:

1. The draft filepath
2. The process log filepath
3. Quality gate outputs — including known weaknesses
4. The story, emotional arc, and single thread — so the author can evaluate whether the draft achieved them
5. Connections from Comprehend that didn't make it into the draft — the author may want them
6. Narrative elements from Comprehend that didn't make it into the draft — the author may want them in revision
7. Specific questions about editorial decisions where the plan left room
8. Places where evidence didn't support what the outline proposed
9. Patterns from the editorial cycle — recurring error types to watch for

**CRITICAL:** The draft is a starting point for the author's revision, not a finished article. Present it as such.

### Present STOP

After presenting, wait for the author's response. The author may:

- **Accept** — the skill's work is complete for this session
- **Provide editorial feedback** — treat as a new editorial round. Re-enter the editorial cycle (it continues; it doesn't restart). The log accumulates.
- **Reject and redirect** — if a fundamental problem (wrong story, wrong evidence emphasis, wrong structure), return to the appropriate earlier phase rather than fixing a draft built on the wrong foundation

Do not proceed or take further action until the author responds.
</phase_present>

---

## After This Phase

Update the article plan:
- Mark Phase 5 checkbox complete
- **Current phase:** Complete

The process log and the draft are the deliverables. The log's editorial round tables are the primary record of how the draft evolved.
