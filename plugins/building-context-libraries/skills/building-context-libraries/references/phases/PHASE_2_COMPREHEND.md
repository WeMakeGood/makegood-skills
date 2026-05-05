# Phase 2: Comprehend

> **CRITICAL RULES — Read these first:**
> - This phase exists because the agent's default is to read source titles, guess at a taxonomy, and propose modules. Comprehension is the counter — understand how the organization thinks before committing to any structure.
> - **Do not propose any module structure in this phase.** Structure comes in Phase 3 (Design).
> - Apply the Source Before Statement gate to every claim about the organization.
> - Re-read sources as needed. Memory blurs; sources don't.
> - Buried-signal sources (transcripts, raw notes) are handled HERE — extract the organizational reasoning directly, don't rewrite them into clean documents first.
> - **Comprehension outputs are pattern-pointers, not summaries.** A pattern-pointer names the pattern, points to its source, and describes the *shape* of the reasoning — not its content. Summary prose written here becomes the cached working memory the build agent reaches for instead of the sources during Build, and it crowds out source substance. The pointer should be useful as an index into the sources; it should NOT be useful as standalone material to generate from.
> - **This phase has two passes with a mandatory session break between them.** Pass 1 is recognition (sources loaded, observational artifacts produced). Pass 2 is synthesis (sources mostly out of context, recognition artifacts loaded, lateral synthesis happens). The break is what allows Pass 2 to do the cognitive moves F0's Analytical Depth Requirements ask for — moves that are difficult or impossible from inside a saturated source context.

---

## What This Phase Does

The agent reads the indexed sources and surfaces what's there (Pass 1), then steps back from the sources and synthesizes what was surfaced (Pass 2). Pass 1 produces observational artifacts at the moment of reading. Pass 2 produces pattern-pointers, convergences, conflicts-as-resolved, cross-domain parallels, and refined agent-needs.

The output of Phase 2 is in `<OUTPUT_PATH>/_comprehension/`:
```
_comprehension/
├── per-source-notes/[source].md       (Pass 1)
├── signal-log.md                      (Pass 1)
├── expectations-vs-findings.md        (Pass 1)
├── conflicts.md                       (Pass 1, resolutions added at STOP)
├── pattern-pointers.md                (Pass 2)
├── convergences.md                    (Pass 2)
├── cross-domain-parallels.md          (Pass 2)
└── agent-needs.md                     (Pass 2)
```

Templates for all eight artifacts are in [references/COMPREHENSION_TEMPLATES.md](../COMPREHENSION_TEMPLATES.md). Read it before starting Pass 1.

No structural decisions in either pass — that's Phase 3.

---

## Why Two Passes

Recognition and synthesis are different cognitive operations. Recognition needs sources in context — what is here, what surprised me, what's missing, what vocabulary recurs. Synthesis needs cognitive room to step back — what does this collectively reveal, what convergences span sources, what cross-domain parallel does this resemble.

Doing both at once on a large source set fails predictably:

- **Synthesis collapses toward summary.** With sources saturating context, synthesis becomes "what the sources collectively said" rather than "what the underlying organizational reasoning is." Pattern-pointers come out generic.
- **Lateral moves get crowded out.** F0's Analytical Depth Requirements (Reframe Before Committing, Cross-Domain Reasoning, Convergence as Signal) require stepping back. From inside saturated context, the sources' first framing is the dominant framing, cross-domain parallels rarely surface, and convergences register as surface similarities rather than deeper intersections.
- **Outliers get averaged out.** The unusual signal in source #43 — the surprise, the conspicuous absence, the unexpected vocabulary — blends into the dominant signal across all sources. Findings reflect the average, not the surprises.

The two-pass structure separates these concerns. Pass 1 captures observations at the moment of reading, when memory is sharp and signal is fresh. Pass 2 synthesizes from those observations with cognitive room to do the lateral work.

The mandatory session break between passes is what makes this real. Without the break, Pass 2 inherits all of Pass 1's source context and the structural advantage disappears.

---

<phase_comprehend_pass1>
## Pass 1: Recognition

**This pass runs in Session A (continuing from Phase 1 Setup). Sources are loaded. Observational artifacts are written at the moment of reading.**

### Pass 1, Step 0: Load All Sources

**GATE:** Before any comprehension work, read every source file listed in the source index. Not skim — read. The recognition that follows depends entirely on having the actual source content in context.

1. Read `<OUTPUT_PATH>/source-index.md` — the complete file list
2. Read `<OUTPUT_PATH>/build-state.md` — confirm Phase 1's Initial Expectations are recorded; you'll need them for the expectations-vs-findings artifact at the end of Pass 1
3. Read [references/COMPREHENSION_TEMPLATES.md](../COMPREHENSION_TEMPLATES.md) — templates for all Pass 1 artifacts
4. Read every source file in the index, in order
5. Create `<OUTPUT_PATH>/_comprehension/` and `<OUTPUT_PATH>/_comprehension/per-source-notes/`
6. Write to the build state: "Sources loaded for Pass 1: [count] files read in this session"

**If the source set is too large to read in one pass, read in clusters** — but every source must be read before the Pass 1 GATE. Per-source notes are still captured at the moment of reading regardless of cluster boundaries; the cluster boundary is for context-window management, not for the recognition discipline.

**Do not proceed to Step 1 until all sources are loaded.** Recognition built on partial reading produces partial observations, and the negative-space check at the end of Pass 1 fails silently.

### Pass 1, Step 1: Per-Source Notes (Written While Reading)

For EVERY source, as you read it, create `<OUTPUT_PATH>/_comprehension/per-source-notes/[source-filename].md` using the per-source-notes template. Write the notes at the moment of reading, before moving to the next source. Memory blurs across documents; per-source notes prevent that blur.

The fields are:

- **Observational fields** (Surprises, Conflicts with sources read so far, Gaps) — what you noticed about this source
- **Signal-collection fields** (Distinctive vocabulary, Distinctive evasions) — recurring-pattern raw material that feeds the signal log
- **Triage field** (Signal density: thick/medium/thin) — Pass 2 uses this to prioritize re-reads

Most fields will be one phrase or "none." Resist the urge to write up the source. The notes are an audit trail, not a substitute for the source.

For buried-signal sources (transcripts, interviews, raw notes): extract organizational reasoning directly. The filler words, false starts, and conversational hedging are noise — the principles and tradeoffs underneath are the signal. You do not need to create a clean rewrite. You need to understand what the person was actually revealing about how the organization thinks. Per-source notes for transcripts are usually denser than for clean documents — the buried reasoning takes more pointers to capture.

### Pass 1, Step 2: Signal Log (Updated as You Read)

Maintain a single running file: `<OUTPUT_PATH>/_comprehension/signal-log.md`. Use the signal-log template.

The signal log captures *cross-source* observations — patterns that span multiple sources. Per-source notes capture single-source observations; the signal log captures relationships *between* sources.

Append entries as patterns become visible:

- **Recurring vocabulary** — same distinctive word/phrase appears in multiple sources
- **Recurring framing** — same way of describing a domain, even with different vocabulary
- **Recurring evasion** — same topic ducked or hedged across multiple sources
- **Contradiction** — sources contradict on a specific point
- **Convergence** — different sources reach the same point through different reasoning (Pass 2 will examine these)
- **Gap pattern** — same kind of information missing across sources where you'd expect it

The signal log is the synthesis substrate Pass 2 will work from. It is the artifact that most directly transmits Pass 1's observations into Pass 2. Write entries as patterns become visible, not at the end — entries written during reading are sharper than entries written from memory.

If a signal needs user input to resolve (typically a contradiction the agent can't tell is real or apparent), mark it `user-attention`. These surface at the Pass 1 STOP.

### Pass 1, Step 3: Expectations vs. Findings (At End of Pass 1)

After all sources are read and per-source notes are complete, create `<OUTPUT_PATH>/_comprehension/expectations-vs-findings.md` using the expectations-vs-findings template.

This artifact compares Phase 1's Initial Expectations (recorded in build-state.md) against what Pass 1 actually surfaced. It has three sections:

1. **Comparison table** — for each expected reasoning pattern, was it found? Partially? Not at all?
2. **What I expected to find but didn't** — the negative-space list. The most diagnostic of the three sections.
3. **What I found that I didn't expect** — the agent's own surprises, aggregated.

The negative-space list is the hardest of the three to produce because it requires deliberate comparison. Without explicit comparison against initial expectations, absences register as "wasn't covered" rather than as "I expected this and didn't find it." Phase 1's Initial Expectations make negative space visible; this artifact captures the visibility.

For each negative-space entry, commit to an interpretation: does this absence reveal something about how the organization actually reasons (a finding about the organization), is it a sourcing gap (a finding about the sources), or was the expectation itself wrong (a finding about the agent's framing)? Pass 2 will refine the interpretation; Pass 1 surfaces the candidate.

### Pass 1, Step 4: Conflicts File (Updated as You Read)

Maintain a single running file: `<OUTPUT_PATH>/_comprehension/conflicts.md`. Use the conflicts template.

A conflict is a substantive disagreement between sources — not a factual contradiction (those go in source-index gaps), but a tension in how the organization reasons or what it claims about itself.

For each conflict, log:
- What conflicts (with source pointers)
- Why it matters for the library
- Type: real conflict | apparent conflict | time-travel artifact | other
- What user input would resolve it (for real conflicts)

**Time-travel artifact** is a specific type worth flagging: sources from different organizational states (e.g., pre-reorg and post-reorg) describe the org as it existed at different times. The apparent contradiction is actually a record of change. These are NOT resolved by picking one version; they're handled as contamination patterns — modules describe the *current* state, with historical context only when it explains current reasoning. If you suspect a conflict is a time-travel artifact, mark it that way; the user confirms or corrects at the STOP.

Resolutions are added during the Pass 1 STOP review with the user.

### Pass 1, Step 5: Reach-Beyond Observations (Inline in Per-Source Notes)

While reading, watch for *reach-beyond signals* — places where an agent doing the work would need information the modules can't reasonably contain (specific data → addendum, capability → skill, judgment → ask user). These observations land in per-source notes' free-text "Notes" section as you encounter them, prefixed with "Reach-beyond:" — Pass 2 will collate them into agent-needs.

</phase_comprehend_pass1>

---

## GATE — End of Pass 1

Write to the build state (terse — counts, not summaries):
- "Pass 1 complete. Sources read: [count] / [total]"
- "Per-source notes written: [count]"
- "Signal log entries: [count] ([open] / [resolved] / [user-attention])"
- "Expectations comparison: [N] expected patterns, [M] found, [K] not found (negative space)"
- "Conflicts surfaced: [count] ([real] / [apparent] / [time-travel] / [other])"
- "Pass 1 thick/medium/thin source breakdown: [counts]"

Substantive content lives in `_comprehension/`, not build-state.

---

## STOP — End of Pass 1 (Recognition Review)

Before the session break, the user reviews recognition outputs.

**Present to the user:**
- The signal log — cross-source patterns surfaced during reading, with type and status
- The expectations-vs-findings reflection — what was expected but not found, what was found but not expected
- The conflicts file — what conflicts you saw, how you typed them, what user input each needs
- A summary of per-source notes patterns: which sources were thick/medium/thin in signal density, which had the most surprises, which had distinctive vocabulary that became signal-log entries
- Any signals marked `user-attention`

**Ask:**
- Are the conflicts you surfaced real, apparent, time-travel artifacts, or something else? (For each conflict — get the type confirmed and any resolutions captured.)
- For signals marked `user-attention` — what input do you need to provide?
- Do the expectations-vs-findings observations track with what you'd expect this organization's sources to show? In particular: are the things I expected to find but didn't actually absent, or did I miss them?
- Are there sources that turned out to be less relevant than initially classified, or more relevant?
- Anything I noticed in the signal log that you want me to investigate further before Pass 2?

**This is the recognition validation point.** Get observation accuracy locked in before synthesis. If recognition is wrong, synthesis built on it will be wrong in a way that's harder to diagnose later.

**After the user responds:**
- Add resolutions to `_comprehension/conflicts.md` for confirmed conflict types
- Update signal log entries from `user-attention` → `resolved` where the user provided input
- Log substantive corrections to `process-log.md`: what the user changed about your observations, and why

---

## MANDATORY SESSION BREAK

**Pass 2 must run in a new session.**

Tell the user: "Pass 1 (recognition) is complete and reviewed. **Start a new session before Pass 2 (synthesis).** The session break is what allows synthesis to do the lateral cognitive work — sources mostly out of context, recognition artifacts loaded, cognitive room to step back. Say 'Resume building context library' to continue."

The boundary between Pass 1 and Pass 2 is mandatory. Without it, Pass 2 inherits Pass 1's saturated source context and the structural advantage of two passes disappears. This is the same discipline as the Comprehend → Design break, applied at a finer boundary.

---

<phase_comprehend_pass2>
## Pass 2: Synthesis

**This pass runs in Session B. Sources are NOT loaded at session start. Recognition artifacts ARE loaded. Pass 2 reaches back into specific sources on demand when synthesis requires verification.**

### Pass 2, Step 0: Load Recognition Substrate

**GATE:** Before any synthesis work, load the recognition substrate. Do NOT load source files — synthesis depends on having cognitive room that source loading would consume.

1. Read [references/ARCHITECTURE.md](../ARCHITECTURE.md) — needed in context for synthesis to be aware of module-architecture constraints
2. Read [references/COMPREHENSION_TEMPLATES.md](../COMPREHENSION_TEMPLATES.md) — Pass 2 artifact templates
3. Read `<OUTPUT_PATH>/build-state.md` — Phase 1's Initial Expectations and Pass 1 status
4. Read `<OUTPUT_PATH>/process-log.md` — user corrections from Pass 1 STOP
5. Read `<OUTPUT_PATH>/source-index.md` — file list (not files themselves)
6. Read `<OUTPUT_PATH>/_comprehension/signal-log.md` — the synthesis substrate
7. Read `<OUTPUT_PATH>/_comprehension/expectations-vs-findings.md` — synthesis priorities
8. Read `<OUTPUT_PATH>/_comprehension/conflicts.md` — including resolutions

Per-source notes are NOT loaded at session start. They are loaded on demand during synthesis when a specific verification is needed.

Write to the build state: "Pass 2 session loaded: ARCHITECTURE.md, COMPREHENSION_TEMPLATES.md, signal-log, expectations-vs-findings, conflicts (with resolutions). Per-source notes loaded on demand."

### Pass 2, Step 1: Pattern-Pointers

Working from the signal log, expectations-vs-findings, and your reading of the sources during Pass 1, generate pattern-pointers in `<OUTPUT_PATH>/_comprehension/pattern-pointers.md`. Use the pattern-pointers template.

For each pattern:
- Apply the surface specificity check (sector-genericity test). The pattern name should NOT be applicable to any organization in this sector without modification. If it is, return to the source and reach for the specificity. (See PHASE_4_BUILD.md, Step 4 — Substantive Source Surface, for the full test.)
- Verify by re-reading specific sources when needed. The signal log entries' source pointers tell you which sources to reach back into; the per-source notes' signal-density flags help prioritize which sources are likely to repay re-reading.
- Mark each pattern's surface specificity check as `pass` or `regenerate`. Do not move on with `regenerate` patterns; either fix them or remove them.

This is the artifact Phase 3 and Phase 4 will rely on most heavily. Quality here directly determines module quality.

### Pass 2, Step 2: Convergences

Generate convergences in `<OUTPUT_PATH>/_comprehension/convergences.md`. Use the convergences template.

For each convergence:
- Name what connects (not the underlying principle — the connection itself)
- State what the convergence reveals that neither source shows alone
- Type: same-pattern-different-language | complementary-evidence | cross-domain

Convergences are where F0's "Convergence as Signal" guidance lands in comprehension. When two sources reach the same point through different reasoning, the convergence reveals something about the organization that neither source surfaces alone. Pursue it rather than treating it as a footnote.

### Pass 2, Step 3: Cross-Domain Parallels

Generate cross-domain parallels in `<OUTPUT_PATH>/_comprehension/cross-domain-parallels.md`. Use the cross-domain-parallels template.

This is a new Phase 2 deliverable. F0's Cross-Domain Reasoning requirement applies to runtime agents but should also apply to the build's comprehension. Look for structural parallels between this organization's reasoning and patterns from other domains.

For each parallel:
- Name the organizational pattern (with source pointer)
- Name the cross-domain analogue
- State what the structural similarity illuminates
- **Required:** name where the parallel breaks down

The "where the parallel breaks down" field is required because parallels named without limits get applied as identity rather than analogy, producing wrong conclusions when the surface resemblance fails.

If no genuine cross-domain parallels surface, write that explicitly in the file ("No cross-domain parallels surfaced during synthesis"). Do not invent parallels to fill the file. False parallels mislead more than they illuminate.

### Pass 2, Step 4: Agent Needs

Generate agent-needs in `<OUTPUT_PATH>/_comprehension/agent-needs.md`. Use the agent-needs template.

This is synthesis work — it depends on the pattern-pointers being in place. For each agent role (refined from Phase 1's Initial Agent Needs based on Pass 2 synthesis):

- Decisions it makes
- Reasoning patterns it needs (referenced from pattern-pointers.md by name; do not restate)
- Situations it will face
- Audience reasoning (for engagement/content production agents — needs on spectrums, not persona types)
- Reach-beyond needs (data, skills, or judgment from outside its modules)
- Gaps the sources don't fill
- Refinement note: what changed from Phase 1's initial role for this agent, and why

Refine the agent roles from Phase 1 based on what Pass 2 surfaced. Do agents align with the reasoning domains synthesis identified, or do they need restructuring? Re-naming, splitting, merging, or removing agents are all valid moves — Phase 1 was preliminary.

### Pass 2, Step 5: Re-Read Discipline

Synthesis without verification produces patterns that sound right but don't reflect the sources. When a synthesis move depends on what a specific source actually says — not what the signal log or per-source notes summarize about it — re-read the source.

Re-read triggers:
- Pattern-pointer source pointer doesn't carry enough specificity from memory
- Convergence requires checking that two sources actually align (vs. sounding like they do)
- Cross-domain parallel requires confirming the organizational side of the analogy
- Conflict resolution requires checking what the conflicting sources actually say
- Surface specificity check fails and you need to reach for organization-specific reasoning

Re-reads are targeted, not bulk. The signal log entries' source pointers are precise enough to make targeted re-reads cheap. Loading the whole source set would defeat the structural advantage of Pass 2 being out-of-context.

**Track which sources you re-read.** Maintain a running list (in working context, or in a small scratch note) of sources re-read during Pass 2, with their signal-density classification from Pass 1's per-source notes. The Pass 2 GATE will ask for this breakdown — it surfaces a specific failure mode (re-reading thin sources at the expense of thick ones because the thick sources' patterns felt familiar from Pass 1, when in fact familiarity is exactly what should trigger verification).

</phase_comprehend_pass2>

---

## GATE — End of Pass 2

Write to the build state (terse — counts, not summaries):
- "Pass 2 complete. Pattern-pointers: [count] (all surface-specificity checks passed: [yes/no])"
- "Convergences: [count]"
- "Cross-domain parallels: [count or 'none surfaced']"
- "Agent roles refined: [list of names]"
- "Reach-beyond needs cataloged: [yes/no]"
- "Sources re-read during synthesis: thick [count], medium [count], thin [count]"
- "BLOCKING gaps remaining: [list of names or 'none']"
- "Comprehension complete: synthesis grounded in Pass 1 recognition; sources re-read targetedly during Pass 2 as needed"

If thick-source re-reads are notably lower than medium- or thin-source re-reads, examine why. Thick sources are the ones most likely to repay verification, and Pass 1's thick classification means more organizational reasoning was identified there. Disproportionate re-reading of thinner sources usually means the agent skipped re-reading thick sources because their patterns felt familiar from Pass 1 — exactly the case where verification is most needed. Surface this to the user at STOP if the breakdown looks skewed.

Substantive content lives in `_comprehension/`, not build-state.

---

## STOP — End of Pass 2 (Synthesis Review)

**Present to the user:**
- The pattern-pointers — how the organization thinks about its core domains, with source pointers and surface-specificity status
- Convergences — where Pass 2 found the same underlying principle revealed across sources through different reasoning
- Cross-domain parallels — where the organization's reasoning structurally resembles patterns from other domains, with limits named
- Refined agent roles — what each agent needs to understand, what situations it will face, what shifted from Phase 1
- Reach-beyond needs cataloged across modules
- Gaps remaining — what's missing and how it affects agent capability
- Conflict resolutions from Pass 1 STOP, with the resulting library implications

**Ask:**
- Do these pattern-pointers match how this organization actually reasons? In particular: are any of them sector-applicable rather than organization-specific? (Surface-specificity is the most common synthesis failure.)
- Are the convergences real, or am I seeing surface similarities?
- Do the cross-domain parallels illuminate, or are they decorative?
- Do the refined agent roles match what you need agents to do?
- For remaining gaps — can you provide the missing information, or should we note the limitation?

**This is the synthesis validation point.** The user validates the *understanding* before any structure is proposed in Phase 3. If the understanding is wrong, everything built on it will be wrong.

**Do not proceed until the user confirms or provides additional direction.**

**After the user responds, log to `process-log.md`:**
- Key synthesis insights and why they matter for the library
- User corrections to pattern-pointers, convergences, parallels, or agent roles
- Anything that shifted understanding from Pass 1 expectations or from what was expected after Setup

---

## After This Phase

Update build state:
- **Current phase:** Phase 3 (Design)
- **Next phase file:** `references/phases/PHASE_3_DESIGN.md`

Phase 3 (Design) follows Pass 2 in the same session if context allows. The mandatory break for Phase 3 is between Pass 1 and Pass 2 (above), not between Pass 2 and Design — Design uses the synthesis artifacts directly.

If the Pass 2 + STOP review took most of Session B's context window, start a new session for Design. Design needs the metaprompt transformation rules and architecture reference fresh in context.
