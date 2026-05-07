---
name: writing-project-dossiers
description: Creates comprehensive project dossiers through interactive guided conversation. Produces scope documents covering objectives, deliverables, timeline, budget, team roles, risks, and communication plans suitable for client approval. Accepts multiple input documents (meeting reports, client dossiers, example deliverables, templates) in any format. Use when user says write a project dossier, create a project scope document, build a project plan, draft a project brief, scope a project, or create a campaign dossier. Activates when project planning materials are provided via pasted text, attached file, or uploaded document, even when accompanied by additional context files.
---

# Writing Project Dossiers

<purpose>
LLMs default to generating plausible-looking project plans filled with invented details — fake
timelines, assumed deliverables, hallucinated team structures. This skill exists because project
dossiers are approval documents: clients sign off on budget, timeline, and deliverables based on
what's written. Every invented detail is a promise the team didn't make. The skill addresses this
by grounding every claim in provided materials and explicitly marking gaps rather than filling them.
</purpose>

## Critical Rules

**SOURCING:** Before stating any project detail (deliverable, date, budget figure, team member, requirement), locate its source in the provided materials. Cite which document or conversation it came from. If a detail isn't in the source materials, mark it as "To be determined" or ask the user — never invent it.

**EPISTEMIC CALIBRATION:** The reader should always be able to tell whether a statement comes from source materials, from the user's answers during the interactive session, or is a recommendation from you. Your language should make that distinction clear without bracket markers.

**SCOPE HONESTY:** Dossiers are approval documents. Over-specifying creates false promises. When source materials don't contain hours, dates, or specific quantities, leave those fields explicitly open rather than estimating. The phrase "To be determined during detailed planning" is more honest than a plausible guess.

**PROFESSIONAL CHALLENGE:** When a request contradicts standard project management practice, when scope seems unrealistic given stated resources, or when deliverables overlap or conflict — cite the concern, offer an alternative. The user needs accurate scoping, not agreement.

**NATURAL PROSE:** Write as a project manager would — direct, specific, structured. When a sentence sounds like AI writing about project management rather than someone managing a project, the voice has slipped. Return to the practitioner's perspective. Revision backstop — these words signal drift: pivotal, crucial, vibrant, tapestry, delve, foster, leverage, synergy, holistic, robust, groundbreaking. Avoid: "Not only X but Y," "serves as," "stands as," vague attribution.

**LATERAL THINKING:** Different project types share structural patterns that surface better questions. A software migration has the same dependency logic as a physical office move; a content production pipeline has the same bottleneck structure as a manufacturing line. When scoping a project, actively look for cross-domain parallels that reveal hidden risks, dependencies, or scope gaps the user hasn't mentioned. Name these connections when they surface useful questions — don't just ask the standard checklist.

**DOWNSTREAM COMPATIBILITY:** The deliverables section must be structured so the `generating-teamwork-imports` skill can consume it. This means: deliverables grouped by area of concern (not timeline phase), each deliverable with clear ownership, and explicit separation of what's known vs. what needs planning. See [references/TEAMWORK-HANDOFF.md](references/TEAMWORK-HANDOFF.md).

## Quick Start

1. User provides project planning materials (meeting notes, client dossiers, briefs, examples)
2. Skill detects project type and asks targeted questions to fill gaps
3. User reviews and approves each major section
4. Skill generates the complete dossier as a file

## Process Log

**REQUIRED:** Maintain a process log file throughout the session. Create `[project-name]-process-log.md` (or `dossier-process-log.md` if no project name yet) at the start of Phase 1 and append to it at every gate.

The process log captures:
- Gate statements from each phase
- Questions asked and key answers received
- Cross-domain connections surfaced
- Decisions made and their rationale
- Scope changes during review

Format each entry with a phase marker:

```markdown
## Phase 1: Gather Inputs
**Materials reviewed:** [list]
**Project type detected:** [type]
**Known details:** [summary]
**Gaps requiring clarification:** [list]

## Phase 2: Interactive Scoping
### Batch 1 — [topic]
**Asked:** [key questions posed]
**Answered:** [key decisions/answers from user]
**Reframes:** [any scope reframes triggered by user answers]

### Batch 2 — [topic]
**Asked:** [key questions posed]
**Answered:** [key decisions/answers from user]
**Cross-domain connection:** [if surfaced]

### Deliverables Gate
**Deliverables confirmed:** [count] across [count] areas
**Cross-domain risks surfaced:** [list]

### Batch 3 — Team / Timeline / Budget
**Asked:** [key questions posed]
**Answered:** [key decisions/answers from user]

### Scope Summary
[Final confirmed scope before drafting]

## Phase 3: Draft
**Sections written:** [list]
**TBD items:** [list]

## Phase 4: Review
**Changes requested:** [list or none]

## Phase 5: Deliver
**Dossier saved to:** [path]
```

This log serves two purposes: it makes the skill's reasoning visible for review, and it creates a decision record that explains why the dossier is scoped the way it is.

## Workflow

Copy this checklist and track progress:

```
Dossier Progress:
- [ ] Phase 1: Gather inputs and detect project type
- [ ] Phase 2: Interactive scoping conversation
- [ ] Phase 3: Draft dossier
- [ ] Phase 4: User review and approval
- [ ] Phase 5: Finalize and deliver
```

<phase_gather>
### Phase 1: Gather Inputs and Detect Project Type

**Read all provided materials first.** Before asking any questions, thoroughly read every document the user has provided — meeting reports, client dossiers, example deliverables, templates, images, PDFs.

**If no source materials are provided:** Skip material review. The entire scoping conversation in Phase 2 becomes the primary source — all dossier content will be attributed to the interactive session. Adjust the gate below accordingly (materials reviewed: "none — building from conversation").

From the materials, identify:
- **Project type** (web development, marketing campaign, brand identity, content production, software build, consulting engagement, event, or hybrid)
- **What's already known** (objectives, deliverables, team, timeline, budget)
- **What's missing** (gaps that need interactive clarification)

**GATE:** Append to the process log and write in chat:
- "Materials reviewed: [list each document/input]"
- "Project type detected: [type]"
- "Known details: [summary of what source materials establish]"
- "Gaps requiring clarification: [list]"
</phase_gather>

<phase_interactive>
### Phase 2: Interactive Scoping Conversation

Work through each gap identified in Phase 1. Ask questions in logical groups — don't dump everything at once, but don't ask one trivial question at a time either.

**Question sequence** (skip any already answered by source materials):

#### 2a. Project Identity
- Project name
- Client name
- Project ID (if the organization uses one)
- One-sentence objective

#### 2b. Scope and Deliverables
This is the most important section. For each deliverable identified in source materials:
- Confirm it belongs in scope
- Clarify whether it's recurring or one-time
- Identify which area of concern it falls under (e.g., Editorial, Design, Development, Marketing, Strategy)
- Identify dependencies between deliverables

For deliverables NOT in source materials but mentioned by the user:
- Get enough detail to describe what it includes
- Confirm area of concern and ownership

**Do not ask about hours or dates unless the user volunteers them.** If the user provides them, include them. If not, mark as "To be determined during detailed planning." This prevents the dossier from over-promising before scope is fully understood.

**GATE:** Append to the process log and write in chat:
- "Deliverables confirmed: [count] deliverables across [count] areas of concern"
- "Cross-domain risks surfaced: [list or 'none identified']"
- "Proceeding to team, timeline, and budget questions"

#### 2c. Team and Roles
- Who is on the client team and what are their roles?
- Who is on the delivery team and what are their roles?
- Who approves deliverables?
- Who is the primary point of contact on each side?

#### 2d. Timeline
- Are there hard deadlines? (launches, events, regulatory dates)
- Are there known phases or milestones?
- What's the expected overall duration?

Only include dates that come from the user or source materials. Do not estimate or suggest dates.

#### 2e. Budget
- Has a budget been established?
- Is it a fixed fee, hourly, or retainer arrangement?
- Are there budget constraints the dossier should reflect?

If no budget information exists, the budget section will state that allocations are determined during detailed planning.

#### 2f. Communication and Process
- How will the teams communicate? (meetings, tools, cadence)
- What's the approval process for deliverables?
- Are there reporting requirements?

#### 2g. Expected Outcomes
- How will the client or team know this project succeeded?
- Are there measurable criteria (metrics, deliverable acceptance, user adoption)?
- If not established yet, mark as TBD — but ask the question.

#### 2h. Risks and Constraints
- Known risks or blockers?
- Dependencies on external parties?
- Technical or organizational constraints?

**Questioning approach:**
- Use the AskUserQuestion tool for short-answer, multiple-choice, or confirmation questions (project type confirmation, yes/no on deliverables, selecting from options)
- Use regular conversation for open-ended questions that need detailed answers (describing deliverables, explaining team structure, articulating objectives)
- Batch related questions together — ask 2-3 related questions per turn, not 10

**GATE:** Append to the process log and write in chat:
- "Scope confirmed: [list of deliverables by area of concern]"
- "Team confirmed: [client team / delivery team summary]"
- "Timeline: [known dates or 'No hard dates established']"
- "Budget: [arrangement or 'To be determined']"
- "Gaps remaining: [list or 'None — ready to draft']"

**STOP.** Present the scope summary to the user and get explicit approval before drafting.
</phase_interactive>

<phase_draft>
### Phase 3: Draft Dossier

Generate the dossier using the template in [references/DOSSIER-TEMPLATE.md](references/DOSSIER-TEMPLATE.md).

**Writing principles:**
- Lead each section with a narrative paragraph, then structured details
- Every factual claim traces to source materials or user-provided answers
- Deliverables section groups by area of concern, not timeline
- "To be determined" is always preferable to an invented detail
- Write for a client audience — clear enough for someone outside the project to understand what they're approving

**Deliverables structure** (critical for downstream Teamwork import):
- Group deliverables under area-of-concern headings (e.g., Design, Development, Editorial, Marketing)
- For each deliverable: description, ownership, recurring/one-time, dependencies
- Include hours and dates ONLY if provided by user or source materials
- Never organize deliverables by timeline phase

**GATE:** Append to the process log and write in chat:
- "Dossier drafted with sections: [list]"
- "Deliverables organized by area: [list areas]"
- "Details marked as TBD: [list]"
</phase_draft>

<phase_review>
### Phase 4: User Review and Approval

Present the complete dossier for review. Ask specifically:

1. Does the project overview accurately capture the objective?
2. Are all deliverables accounted for and correctly described?
3. Is the team structure correct?
4. Are there any scope items to add or remove?
5. Is anything misrepresented?

Make requested changes. Re-present if changes are substantial.

**GATE:** Append to the process log and write in chat:
- "User approved dossier: [yes/no]"
- "Changes requested: [list or 'none']"
</phase_review>

<phase_deliver>
### Phase 5: Finalize and Deliver

**ALWAYS save the dossier to a file or artifact. Do not output inline in chat.**

1. Generate filename: `[project-name]-dossier.md`
2. Write the complete dossier to this file
3. After saving, confirm with a brief summary:
   - File location
   - Number of deliverables scoped
   - Key areas of concern covered
   - Any items flagged as "To be determined"

If the user requests an artifact, create an artifact instead of a file.

**Next step prompt:** After confirming delivery, tell the user: "To generate a Teamwork import from this dossier, you can say: 'Generate a Teamwork import from `[dossier-file-path]`'"

**GATE:** Append to the process log and write in chat:
- "Dossier saved to: [path]"
- "Process log saved to: [path]"
- "Ready for client review"
- "For Teamwork import: deliverables are organized by area of concern and can be consumed by the generating-teamwork-imports skill"
</phase_deliver>

## Examples

### Example 1: Software Migration (Cross-Domain Questioning)

**Input materials:** Meeting report from discovery call

**Interactive session showing lateral thinking:**
```
Skill: Based on the discovery call notes, this is a platform migration
— moving from a legacy ERP to a cloud-based system. I've identified
these deliverables:
- Data migration (customer records, transaction history)
- API integration layer
- User training program
- Parallel run period

One thing the meeting notes don't address: migration projects share a
structural pattern with physical moves — there's always a "last mile"
problem where the final cutover reveals dependencies nobody mapped.
Who owns the go/no-go decision for the cutover? And is there a
rollback plan if the parallel run surfaces blocking issues?

User: Good question. The CFO has final sign-off on cutover. We haven't
discussed rollback — that needs to be in the dossier as an open item.
```

**Dossier excerpt:**
```markdown
# Deliverables

## Technical
### Data Migration
Migration of customer records and transaction history from legacy
ERP to cloud platform. Includes data validation and reconciliation.
- Ownership: Engineering team
- Type: One-time
- Dependencies: Data mapping document (from client IT)

### API Integration Layer
Integration between cloud platform and existing third-party systems
(payment processor, CRM, shipping provider).
- Ownership: Engineering team
- Type: One-time
- Dependencies: Third-party API documentation, data migration completion

## Operations
### Parallel Run Period
Both systems operating simultaneously to validate data integrity
and workflow accuracy before cutover.
- Ownership: Operations lead
- Type: One-time
- Dependencies: Data migration, API integration

### User Training Program
Role-based training for finance, operations, and customer service teams.
- Ownership: Training coordinator
- Type: One-time (with recurring refreshers TBD)
- Dependencies: Parallel run completion
```

### Example 2: Consulting Engagement (Handling Missing Details)

**Input materials:** Brief email thread, no formal kickoff**

**When source materials are thin:**
```markdown
# Project Overview

Regional Health Partners has engaged a consulting team to assess
their patient intake workflow and recommend process improvements.
The engagement scope was described in a three-paragraph email
from the client director; detailed requirements will be
established during the discovery phase.

# Budget

Budget allocations will be determined during detailed planning.
The client has indicated a target range but has not confirmed
final figures.

# Timeline and Milestones

The client referenced a "board presentation in Q4" as the
deadline for final recommendations (per email from director).
Specific milestone dates will be established during the
discovery phase.

# Appendix

## Open Items
- Rollback plan: not yet discussed — flagged during scoping
- Training frequency: initial sessions confirmed, recurring
  schedule to be determined
- Budget: target range indicated, awaiting formal confirmation
- Milestone dates: to be established during discovery
```

<failed_attempts>
## What DOESN'T Work

- **Inventing timelines:** "This should take about 3 weeks" is a hallucination when no source establishes duration. Leave it as TBD.

- **Estimating hours:** Unless the user or source materials provide hour estimates, do not guess. The Teamwork import skill handles time estimates separately.

- **Timeline-organized deliverables:** Grouping deliverables as "Phase 1: Discovery, Phase 2: Design, Phase 3: Build" creates a waterfall structure that doesn't map to how work is actually tracked. Group by area of concern.

- **Generic risk sections:** "Risk: Timeline may slip. Mitigation: Monitor closely." is not useful. Either identify specific risks from the source materials or ask the user what they're concerned about.

- **Filling gaps silently:** When information is missing, the temptation is to write something plausible. The correct move is to mark it as TBD and note what's needed.

- **Asking about everything:** If the meeting report already names the team, don't ask about the team. Only ask about gaps.
</failed_attempts>

## References

- [references/DOSSIER-TEMPLATE.md](references/DOSSIER-TEMPLATE.md) — Full dossier structure template
- [references/TEAMWORK-HANDOFF.md](references/TEAMWORK-HANDOFF.md) — How to structure deliverables for Teamwork import compatibility
