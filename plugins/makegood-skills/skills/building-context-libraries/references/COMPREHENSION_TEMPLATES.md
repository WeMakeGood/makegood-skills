# Comprehension Templates

Templates for the artifacts produced during Phase 2 (Comprehend). Pass 1 produces recognition artifacts (per-source notes, signal log, expectations-vs-findings, conflicts). Pass 2 produces synthesis artifacts (pattern-pointers, convergences, cross-domain parallels, agent-needs).

All artifacts live in `<OUTPUT_PATH>/_comprehension/`. The `_` prefix keeps the directory visible to the user but signals it is not part of the runtime library.

```
<OUTPUT_PATH>/_comprehension/
├── per-source-notes/                  (Pass 1 — one file per source)
│   ├── [source-filename].md
│   └── ...
├── signal-log.md                      (Pass 1)
├── expectations-vs-findings.md        (Pass 1)
├── conflicts.md                       (Pass 1, resolutions added at STOP)
├── pattern-pointers.md                (Pass 2)
├── convergences.md                    (Pass 2)
├── cross-domain-parallels.md          (Pass 2)
└── agent-needs.md                     (Pass 2)
```

---

## Pass 1: Recognition Artifacts

Pass 1 captures observations at the moment of reading. Recognition is fast and field-shaped — most fields are one phrase or "none." The discipline: write what you noticed, not what you concluded.

### Per-Source Notes Template

One file per source: `<OUTPUT_PATH>/_comprehension/per-source-notes/[source-filename].md`. Use the same base filename as the source (without path).

```markdown
# Per-Source Notes: [source filename]

**Read:** YYYY-MM-DD
**Source-index classification:** [type, signal from source-index.md]

---

## Observational fields

**Surprises:** [What surprised you in this source — content, framing, or absence. One phrase, or "none."]

**Conflicts with sources read so far:** [What this source contradicts or tensions with. Source pointers if applicable. One phrase, or "none."]

**Gaps:** [Information this source references but doesn't contain. One phrase, or "none."]

---

## Signal-collection fields

**Distinctive vocabulary:** [Words or phrases this source uses in distinctive ways — terms the organization has its own meaning for, recurring framings, conspicuous word choices. One phrase per item, or "none."]

**Distinctive evasions:** [Topics this source dances around, hedges, or leaves unsaid that you'd expect a candid version to address. One phrase per item, or "none."]

---

## Triage field

**Signal density:** [thick | medium | thin]

- **thick** — high density of organizational reasoning per page; multiple patterns evidenced
- **medium** — some organizational reasoning, mixed with content that's primarily factual or operational
- **thin** — primarily factual or operational; little organizational reasoning to surface

This is different from the source-index's `clear`/`buried` (signal *clarity*). Density is about how much organizational reasoning is present, not how directly it's stated. Pass 2 uses density as a re-read priority signal.

---

## Notes

[Free-text space for anything that doesn't fit above. Optional. Keep brief — this is not the place to write up the source.]
```

The fields are differently purposed:

- **Observational fields** (Surprises, Conflicts, Gaps) capture what you noticed about *this* source as you read it. Each is one phrase or "none."
- **Signal-collection fields** (Distinctive vocabulary, Distinctive evasions) feed the cross-source signal log. They are recurring-pattern raw material.
- **Triage field** (Signal density) helps Pass 2 prioritize re-reads.

Resist the urge to write up the source. The audit trail exists to be re-read with the source if needed; it is not a substitute for the source.

**Worked example:**

```markdown
# Per-Source Notes: founder-interview-2024-09.md

**Read:** 2026-04-12
**Source-index classification:** transcript, buried

---

## Observational fields

**Surprises:** Founder describes turning down their largest funder in year 3; sources read so far framed funder relationships as uniformly preserved.

**Conflicts with sources read so far:** strategy-doc.md says all funder relationships are "long-term partnerships"; this transcript names a deliberate exit.

**Gaps:** Doesn't specify what made this funder different from others — references "values mismatch" without elaborating.

---

## Signal-collection fields

**Distinctive vocabulary:** "values mismatch" (used as binary, not spectrum); "earn the work" (recurring frame for new engagements); "we don't pitch" (used three times).

**Distinctive evasions:** Does not say what the org does when a current client's needs shift toward values-mismatch territory; topic deflected toward "we earn the work."

---

## Triage field

**Signal density:** thick

---

## Notes

Reach-beyond: agent answering qualification questions will need to know that values-mismatch can override revenue.
```

The example shows: one phrase per observational field, two-to-three items per signal-collection field, named distinctive evasions (not generic "didn't cover X"), and a reach-beyond observation captured inline.

---

### Signal Log Template

Single running file: `<OUTPUT_PATH>/_comprehension/signal-log.md`. Append entries as you read sources sequentially.

```markdown
# Cross-Source Signal Log

**Started:** YYYY-MM-DD
**Last updated:** YYYY-MM-DD

The signal log captures lateral observations the build agent surfaces while reading sources sequentially. Unlike per-source notes (which are per-source), signal log entries name patterns that span multiple sources.

Append entries; do not overwrite.

---

## Entry Format

```
- Signal: [short name]
  Sources: [files where evidenced — minimum 2; if only 1, this is a per-source observation, not a cross-source signal]
  Type: [recurring vocabulary | recurring framing | recurring evasion | contradiction | convergence | gap pattern]
  Observation: [one phrase — what you noticed]
  Status: [open | resolved | user-attention]
```

**Type values:**
- **recurring vocabulary** — same distinctive word/phrase across multiple sources
- **recurring framing** — same way of describing a domain across sources, even with different vocabulary
- **recurring evasion** — same topic ducked or hedged across multiple sources
- **contradiction** — sources contradict on a specific point (will become a conflict if substantive)
- **convergence** — different sources reach the same point through different reasoning (Pass 2 will examine these)
- **gap pattern** — same kind of information missing across sources where you'd expect it

**Status values:**
- **open** — observation logged, not yet examined
- **resolved** — Pass 2 incorporated this signal into a pattern-pointer or convergence; entry can stay for audit-trail purposes
- **user-attention** — this signal needs user input before it can be resolved (typically because it's a contradiction the agent can't tell is real or apparent)

---

## Entries

(populated during Pass 1)
```

**Worked example:**

```
- Signal: "earn the work" as the org's selection language
  Sources: founder-interview-2024-09.md, intake-template.md, three discovery-call transcripts
  Type: recurring vocabulary
  Observation: phrase appears across roles and contexts; the org uses it to describe a pre-engagement period that's distinct from "pitching" or "qualifying" — closer to a relational calibration with stakes attached
  Status: open

- Signal: capacity is not staffing-defined
  Sources: founder-interview-2024-09.md, ops-doc-2025-01.md
  Type: recurring framing
  Observation: when "capacity" appears, it refers to the team's ability to hold relational depth, not to billable hours; the staffing-hours framing is conspicuously absent
  Status: open

- Signal: silence on competitor comparison
  Sources: 7 sources reviewed so far
  Type: recurring evasion
  Observation: no source positions the org against named competitors; even materials that would conventionally compare (sales decks, capability statements) frame distinctively rather than comparatively
  Status: user-attention
```

The example shows: signal names are short and specific (not "vocabulary about engagements"); observations capture the organizational move the signal points to (not what the signal "means"); user-attention status used when the signal needs interpretation the agent can't provide alone.

---

### Expectations-vs-Findings Template

Single file: `<OUTPUT_PATH>/_comprehension/expectations-vs-findings.md`. Written at the end of Pass 1 by comparing Pass 1's findings against Phase 1's Initial Expectations.

```markdown
# Expectations vs. Findings

**Pass 1 reflection date:** YYYY-MM-DD

This file compares what the build agent expected to find in the sources (per Phase 1's Initial Expectations) against what Pass 1 actually surfaced. The middle section — what was expected but not found — is the most underused signal type in comprehension and the most diagnostic.

---

## Expectations Comparison Table

| Expected reasoning pattern | Source types expected to inform it | Found? | Notes |
|---|---|---|---|
| [pattern from Phase 1 Initial Expectations] | [source types] | [yes — sources] / [partial — note] / [no] | [one phrase if Found is anything but a clean yes] |

---

## What I Expected to Find but Didn't

The negative-space list. Each entry is a deliberate observation about absence — not a generic "wasn't covered" but a specific reasoning pattern, claim, or framing the agent expected to find evidenced in the sources and did not.

```
- Expected: [the pattern, claim, or framing — short]
  Why expected: [Phase 1 expectation source — e.g., "any organization in this sector reasons through X"]
  What was found instead: [if anything — could be "nothing on this topic" or "X was discussed but only as Y, not as Z"]
  Implications: [one phrase — does this absence tell us something about how the org actually thinks, or is it a sourcing gap?]
```

Absence can mean:
- The organization genuinely doesn't reason this way (a finding about the organization)
- The organization reasons this way but didn't say so in the sourced material (a gap in sourcing)
- The agent's expectation was wrong (a finding about the agent's framing)

The implications field is where the agent commits to an interpretation, which Pass 2 will refine.

---

## What I Found That I Didn't Expect

The agent's own surprises, aggregated across the source set. Each entry is a distinctive pattern, framing, or move that the agent didn't anticipate from the source index alone.

```
- Found: [the pattern, claim, or framing — short]
  Sources: [where evidenced]
  Why surprising: [one phrase — what about this is unexpected]
  Implications: [one phrase — what this suggests about the organization]
```

Unexpected findings often carry more signal than expected ones, because expected findings can be rationalized; unexpected ones force the agent to update its model.

---

## Updated Expectations for Pass 2

Based on the comparison above, what new questions does Pass 2 need to answer that Phase 1 didn't anticipate?

- [Question]
- [Question]

These shape Pass 2's synthesis priorities.
```

**Worked example:**

```markdown
## Expectations Comparison Table

| Expected reasoning pattern | Source types expected to inform it | Found? | Notes |
|---|---|---|---|
| How the org calibrates engagement intensity to client maturity | strategy-doc, transcripts | partial — sources | Found in transcripts, absent from strategy doc; the org reasons this way but doesn't formalize it |
| Disqualification criteria for new engagements | intake-template, sales materials | yes — intake-template, founder-interview | "Values mismatch" is the disqualifier the org names |
| Pricing logic | proposal-templates, financial-doc | no | Pricing materials describe rates, not the reasoning behind them |

## What I Expected to Find but Didn't

- Expected: explicit articulation of how the org weighs reach (more clients) against depth (deeper work per client)
  Why expected: any service org at this scale faces this tradeoff; expected to find it named in strategy
  What was found instead: depth-favoring decisions are visible in actions across sources; the tradeoff is never explicitly framed
  Implications: the org makes this tradeoff implicitly; modules need to capture the implicit reasoning so agents can apply it — finding about the organization, not a sourcing gap

- Expected: discussion of staff retention strategy
  Why expected: small org with high client-relationship continuity; assumed staffing is a strategic concern
  What was found instead: nothing in any source addresses staff retention specifically
  Implications: likely a sourcing gap (staffing decisions probably exist in HR materials not in this set) rather than an organizational silence; flag as gap to user

## What I Found That I Didn't Expect

- Found: pattern of refusing engagements above a certain budget threshold
  Sources: founder-interview-2024-09.md, board-minutes-2023-11.md
  Why surprising: budget thresholds typically work as floors, not ceilings; this org treats them as ceilings
  Implications: signals that capacity (relational, not staffing) is the binding constraint, and engagement size scales with depth-served, not with revenue

## Updated Expectations for Pass 2

- Pass 2 should examine whether reach-vs-depth tradeoff has a consistent reasoning shape across sources, or whether it varies by domain
- Pass 2 should look for whether the budget-ceiling pattern extends to other forms of "more is worse" reasoning
```

The example shows: "yes/partial/no" answers are followed by one-phrase notes that name the *shape* of the finding; negative-space entries commit to an interpretation (organizational vs. sourcing gap vs. wrong expectation); unexpected findings include why the surprise itself is signal.

---

### Conflicts Template

Single running file: `<OUTPUT_PATH>/_comprehension/conflicts.md`. Pass 1 surfaces conflicts; resolutions are added during Pass 1 STOP review with the user.

```markdown
# Conflicts

**Surfaced during:** Pass 1
**Resolutions added at:** Pass 1 STOP

A conflict is a substantive disagreement between sources — not a factual contradiction (those go in source-index gaps), but a tension in how the organization reasons or what it claims about itself.

---

## Conflict Format

```
### Conflict: [short name]

**Sources in conflict:** [files, with pointers]

**What conflicts:** [one or two sentences — what the sources actually disagree about]

**Why it matters for the library:** [one phrase — what's at stake for module content if this isn't resolved]

**Type:** [real conflict | apparent conflict | time-travel artifact | other]

**What user input would resolve it:** [for real conflicts — what the user needs to clarify]

**Resolution:** [filled in by user during STOP — pending until then]
```

**Type values:**

- **real conflict** — sources genuinely disagree on substance; user input needed
- **apparent conflict** — sources disagree on surface but reconcile under closer reading; the agent has confirmed the reconciliation and is logging the conflict for transparency, not for resolution
- **time-travel artifact** — sources from different organizational states (e.g., pre-reorg and post-reorg, pre-strategic-shift and post) describe the org as it existed at different times; the apparent contradiction is actually a record of change. These are NOT resolved by picking one version; they're handled as contamination patterns (modules describe the *current* state, with historical context only when it explains current reasoning)
- **other** — the conflict shape doesn't fit the above; describe in the conflict's text

---

## Conflicts

(populated during Pass 1)
```

**Worked examples (one per type):**

```markdown
### Conflict: stated vs. acted client selection

**Sources in conflict:** strategy-doc.md (page 4) and three transcripts (founder-interview, partner-call-2024-03, advisor-call-2024-08)

**What conflicts:** Strategy doc claims the org accepts engagements based on a documented capability-fit assessment. Transcripts describe a different selection move centered on values-mismatch as the disqualifier, with capability-fit assumed.

**Why it matters for the library:** Modules covering qualification need to teach the actual selection reasoning. Teaching the documented version produces an agent that asks the wrong questions during discovery.

**Type:** real conflict

**What user input would resolve it:** Confirmation of which framing is current — is the strategy doc out of date, or are the transcripts describing edge cases?

**Resolution:** [pending]
```

```markdown
### Conflict: scope of "values" in selection

**Sources in conflict:** founder-interview-2024-09.md and intake-template.md

**What conflicts:** Founder interview describes "values" broadly (mission alignment, working style, leadership posture). Intake template lists narrower criteria (mission alignment only).

**Why it matters for the library:** Determines whether qualification reasoning is mission-only or multi-dimensional.

**Type:** apparent conflict

**What user input would resolve it:** None — the closer reading shows the intake template captures the formal screen and the interview describes the informal calibration that follows; they're sequential, not contradictory.

**Resolution:** No user resolution needed. Modules treat formal screen and informal calibration as two stages of the same selection process.
```

```markdown
### Conflict: organizational structure description

**Sources in conflict:** board-minutes-2022-11.md and ops-doc-2025-01.md

**What conflicts:** 2022 minutes describe a three-arm operating structure; 2025 ops doc describes a two-arm structure with the third arm as a "former program."

**Why it matters for the library:** Modules describing the organization need to describe its current shape, not its historical one. Without identifying the time-travel artifact, an agent might describe a defunct program as current.

**Type:** time-travel artifact

**What user input would resolve it:** Confirmation that the 2025 doc reflects current state; the 2022 minutes describe a structure that has since been retired.

**Resolution:** [pending]
```

The examples show: "What conflicts" is one or two sentences, not a paragraph; "Why it matters" connects to module content (not abstract significance); type is named precisely; for apparent conflicts and time-travel artifacts, the resolution path differs from real conflicts.

---

## Pass 2: Synthesis Artifacts

Pass 2 produces synthesis with sources mostly out of context. The recognition artifacts are loaded in; sources are read on-demand when a synthesis move needs verification.

### Pattern-Pointers Template

Single file: `<OUTPUT_PATH>/_comprehension/pattern-pointers.md`. The dedicated, scannable home for the pattern-pointer format that previously lived in process-log.

```markdown
# Pattern-Pointers

**Pass 2 synthesis output**
**Last updated:** YYYY-MM-DD

Each pattern-pointer names an organizational reasoning pattern, points to its source evidence, describes the *shape* of the reasoning, and provides a pointer (not a summary) to find it in the source.

The pointer is an index entry. It lets Design and Build locate the pattern in the source. It is not itself useful as standalone material to generate from — that would mean the pointer became a summary, which means the agent would generate from the summary instead of from the source.

---

## Format

```
- Pattern: [short name for the pattern]
  Sources: [file(s) where evidenced]
  Shape: [principle | tradeoff | decision criterion | constraint | tension | value | identity claim]
  Pointer: [one phrase that lets you find this pattern in the source — NOT a summary of what the pattern says]
  Surface specificity check: [pass | regenerate]
```

**Surface specificity check:** the pattern name should NOT be one that could apply to any organization in this sector without modification. "How the org thinks about client engagement" is sector-applicable; "How the org decides which client situations require capacity-building vs. delivery" is organization-specific. If the pattern name is sector-applicable, mark "regenerate" and return to the source for specificity. (See PHASE_4_BUILD.md, Step 4 — Substantive Source Surface, for the full sector-genericity test logic.)

---

## Pattern-Pointers

(populated during Pass 2)
```

**Worked examples (showing pass and regenerate cases):**

```
- Pattern: capacity-driven engagement scoping
  Sources: founder-interview-2024-09.md, board-minutes-2023-11.md, ops-doc-2025-01.md
  Shape: tradeoff
  Pointer: discussion of why the org turns away well-funded engagements that exceed
           what current team capacity can sustain without quality loss
  Surface specificity check: pass

- Pattern: values-mismatch as binary disqualifier
  Sources: founder-interview-2024-09.md, intake-template.md
  Shape: decision criterion
  Pointer: "values mismatch" treated as override regardless of revenue or capacity availability
  Surface specificity check: pass

- Pattern: how the org thinks about client engagement
  Sources: 12 sources
  Shape: principle
  Pointer: discussion of engagement throughout the source set
  Surface specificity check: regenerate — name is sector-applicable; "how the org thinks about client engagement" could describe any service org. Return to sources for the specific reasoning move.
```

The examples show: pattern names are short and name the *organizational move*, not the *topic* (capacity-driven engagement scoping vs. "engagement reasoning"); pointers describe where to look without summarizing what the pattern says; the third example illustrates a regenerate case — the pattern name is too generic and needs to be replaced with what the org *specifically* does.

---

### Convergences Template

Single file: `<OUTPUT_PATH>/_comprehension/convergences.md`.

```markdown
# Convergences

**Pass 2 synthesis output**
**Last updated:** YYYY-MM-DD

A convergence is the moment when different sources reveal the same underlying pattern through different language. The convergence reveals something neither source says alone — the organizational principle or move that surfaces only when the sources are read together.

---

## Format

```
- Convergence: [short name for what connects]
  Sources: [files involved — minimum 2]
  Connection: [one phrase naming what they share — not a summary of the underlying principle]
  What it reveals: [one phrase — what the convergence shows that neither source alone shows]
  Type: [same-pattern-different-language | complementary-evidence | cross-domain]
  Where the convergence is partial: [optional, but encouraged — what each source preserves that the convergence framing doesn't capture]
```

**Type values:**

- **same-pattern-different-language** — two sources describing one organizational behavior using different vocabulary or frames
- **complementary-evidence** — one source explains *why*, another shows *how*; together they make the reasoning legible
- **cross-domain** — an external-facing pattern that mirrors an internal-operations pattern, or vice versa; the convergence is across organizational domains, not just across documents

**Why "where the convergence is partial" matters:** convergences can be over-applied. Two sources reaching the "same" point can have important differences — context, nuance, scope, audience — that the convergence framing obscures. Naming what each source preserves that the convergence doesn't carry forward keeps modules from collapsing the sources into a flatter version than either source actually supports. This is the convergence equivalent of cross-domain parallels' "where the parallel breaks down" requirement.

The field is optional rather than required because some convergences are clean — the sources genuinely say the same thing through different language, and there is nothing partial to flag. When the convergence is clean, leave the field blank or write "clean — no partiality to flag." When the convergence is doing work the sources individually don't fully support, name what each source preserves.

---

## Convergences

(populated during Pass 2)
```

**Worked examples:**

```
- Convergence: capacity (relational) and pricing (depth-scaled) describe the same constraint
  Sources: founder-interview-2024-09.md, financial-doc-2024.md, ops-doc-2025-01.md
  Connection: what one source calls "team capacity" and another calls "depth pricing" both refer to the same underlying constraint — how many clients can be served at the depth the org commits to
  What it reveals: the org has one constraint (relational capacity) appearing as two managerial frames (capacity language in operations, pricing language in finance) — modules should treat them as one thing
  Type: same-pattern-different-language
  Where the convergence is partial: financial-doc-2024.md treats depth-pricing as a deliberate pricing strategy (a choice the org makes); founder-interview-2024-09.md describes capacity as a structural fact (a constraint the org operates within). The convergence flattens choice into constraint; modules should preserve that the org has chosen this constraint, not just inherited it.

- Convergence: "earn the work" and "values mismatch as override"
  Sources: founder-interview-2024-09.md, partner-call-2024-03.md, intake-template.md
  Connection: the pre-engagement period the org calls "earning the work" is the same period during which values-mismatch becomes detectable; one source explains the why, others show the how
  What it reveals: the relational calibration the org does before engagement is not a sales process but a values-screen mechanism
  Type: complementary-evidence
  Where the convergence is partial: clean — no partiality to flag. The sources genuinely describe the same mechanism from different angles; nothing meaningful is lost in the convergence.
```

The examples show: convergence names what connects (not the principle revealed); "what it reveals" is one phrase that names the underlying organizational reasoning the convergence surfaces; type is named; partiality is named when it exists, marked clean when it doesn't. The first example illustrates a non-trivial partiality (choice vs. constraint) that modules need to preserve; the second illustrates a clean convergence where the field is appropriately empty.

---

### Cross-Domain Parallels Template

Single file: `<OUTPUT_PATH>/_comprehension/cross-domain-parallels.md`. New in Phase 2 — promotes F0's Cross-Domain Reasoning requirement to a comprehension deliverable.

```markdown
# Cross-Domain Parallels

**Pass 2 synthesis output**
**Last updated:** YYYY-MM-DD

A cross-domain parallel names a structural similarity between this organization's reasoning and a pattern from a different domain. The value of a parallel is in what the structural similarity reveals about the underlying principle — not in the surface resemblance.

When a parallel doesn't hold under scrutiny, do not record it. False parallels mislead more than they illuminate.

---

## Format

```
- Parallel: [short name]
  Organizational pattern: [the pattern from this organization, with source pointer]
  Cross-domain analogue: [the pattern from a different domain]
  Structural similarity: [one or two sentences — what the shared structure illuminates]
  Where the parallel breaks down: [one phrase — every parallel has limits; name them so the parallel doesn't get over-applied]
```

The "where the parallel breaks down" field is required. A parallel that's named without its limits gets applied as if it were identity rather than analogy, and produces wrong conclusions when the surface resemblance fails.

---

## Cross-Domain Parallels

(populated during Pass 2)
```

**Worked example (and a counter-example showing what NOT to record):**

```
- Parallel: relational capacity-binding resembles an artisan studio's commission load
  Organizational pattern: the org treats engagement load as bound by relational depth, not by staffing hours (founder-interview-2024-09.md, ops-doc-2025-01.md)
  Cross-domain analogue: small artisan studios — a master-craftsman shop binds commissions by the master's attention bandwidth, not by total shop hours
  Structural similarity: both have a non-substitutable input (relational depth / master attention) that scales linearly with output and cannot be supplemented by adding hours from substitutable inputs. The org is not a service business with a craftsmanship analogy; it is structurally a craftsmanship business doing service work.
  Where the parallel breaks down: artisan studios sell artifacts; this org sells outcomes. Outcome-quality measurement is harder than artifact-quality measurement, so the same constraint structure produces different management problems.
```

A counter-example — the kind of parallel that should NOT be recorded:

```
- Parallel: the org's qualification process is "like" sales qualification
  Organizational pattern: pre-engagement values screening
  Cross-domain analogue: B2B sales qualification (BANT, MEDDIC, etc.)
  Structural similarity: both filter prospects before commitment.
  Where the parallel breaks down: standard sales qualification is a fit-to-product screen; the org's screen is a values-mutuality screen. The structures are not the same — they share only the surface feature of "filtering before commitment."
```

The counter-example illustrates why the "where the parallel breaks down" field is required: the parallel here is decorative (filtering before commitment is too generic to illuminate anything specific) and should be removed, not recorded with a caveat. If the parallel doesn't survive its own breakdown analysis, it doesn't belong in the file.

The good example shows: a structural similarity that names a non-obvious organizational truth (this org is structurally a craftsmanship business); a breakdown that's specific (artifacts vs. outcomes) rather than generic.

---

### Agent-Needs Template

Single file: `<OUTPUT_PATH>/_comprehension/agent-needs.md`. Moves from old Phase 2 Step 4 to Pass 2 — agent-needs is synthesis-shaped work that depends on the pattern-pointers being in place.

```markdown
# Agent Needs

**Pass 2 synthesis output**
**Last updated:** YYYY-MM-DD

For each agent role (refined from Phase 1's Initial Agent Needs based on Pass 2 synthesis), name what reasoning the agent needs, what situations it will face, and where it will reach beyond its modules.

---

## Format

```
- Agent: [name]

  Decisions it makes: [list — what the agent will be asked to decide]

  Reasoning patterns it needs: [pattern names from pattern-pointers.md, with source pointers — NOT restated content]

  Situations it will face: [contexts that require organizational reasoning to think well]

  Audience reasoning: [if the agent governs engagement or content production — what active needs the people it interacts with present, framed as needs on spectrums rather than persona types]

  Reach-beyond needs: [what data/skills/judgment it will need from outside its modules]

  Escalation triggers: [situations where the agent should ask rather than answer — patterns surfaced from sources where the right move is deferral to a principal/sponsor/user, not the agent's best inference. These become the agent file's `## Ask the [Role]` block in Phase 4.]

  Gaps: [what's missing from sources that this agent would need]

  Refinement note: [one phrase — what changed from Phase 1's initial agent role for this agent, and why]
```

The reasoning-patterns column references pattern-pointers.md by pattern name. Do not restate the patterns here.

**Escalation triggers vs. reach-beyond needs:** reach-beyond names what the agent loads or invokes (an addendum, a skill, a user prompt for missing data). Escalation triggers name situations where the agent must defer the *decision* — work that crosses into territory only the engagement principal / sponsor / user can resolve. The distinction matters: reach-beyond is mechanical ("load X when Y"); escalation is judgmental ("don't proceed without input from a human in role Z"). Both surface from Pass 2 synthesis, but they get rendered as distinct sections in the agent definition file.

---

## Agent Needs

(populated during Pass 2)
```

**Worked example:**

```
- Agent: client engagement agent

  Decisions it makes: whether to advance an early conversation toward a formal engagement; whether to flag a values-mismatch concern to the user; how to scope an engagement once advancement is decided

  Reasoning patterns it needs:
    - capacity-driven engagement scoping (see pattern-pointers.md)
    - values-mismatch as binary disqualifier (see pattern-pointers.md)
    - "earn the work" as pre-engagement calibration (see pattern-pointers.md)

  Situations it will face: discovery conversations with prospective clients; conversations with current clients about scope expansion; situations where a prospective engagement looks attractive on revenue but presents values-mismatch signals

  Audience reasoning: the people the agent interacts with present interacting needs — prospective clients carry needs around being understood, being challenged, and being given honest assessment; the agent calibrates which need is most active in a given exchange rather than treating prospects as a fixed audience type

  Reach-beyond needs:
    - addendum: current capacity (which engagements would compete with this one)
    - skill: drafting-proposals (when advancement is decided)
    - user: when values-mismatch signals appear and the agent can't resolve whether they're surface or substantive

  Escalation triggers:
    - prospective engagement requires resourcing decisions beyond the agent's current-capacity addendum (e.g., team reassignment, hiring questions)
    - values-mismatch signal appears and the agent's reasoning produces a confident answer in either direction — confidence in this terrain is a signal to escalate, not to proceed
    - prospect names a relationship or affiliation the library doesn't surface (sources didn't anticipate the connection)

  Gaps: sources don't address how the agent should handle current-client scope expansion that drifts toward values-mismatch territory; this is a known gap to flag

  Refinement note: Phase 1 had this agent named as "qualification agent"; Pass 2 surfaced that the org doesn't think of this as qualification (a sales-shaped frame) but as relational calibration with stakes — renaming to "client engagement" preserves the agent's actual scope without importing sales framing
```

The example shows: decisions are concrete and scoped; reasoning patterns are referenced by name (not restated); audience reasoning frames as needs-on-spectrums rather than persona types; reach-beyond is split by addendum/skill/user; escalation triggers are named situations where the agent defers (each one becomes an `## Ask the [Role]` bullet in the agent file); gaps are named specifically; refinement note explains the change from Phase 1.
