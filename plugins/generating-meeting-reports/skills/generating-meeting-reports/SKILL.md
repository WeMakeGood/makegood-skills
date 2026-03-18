---
name: generating-meeting-reports
description: Generates structured meeting reports from transcripts. Extracts attendees, topics, decisions, action items, and resources into a standardized executive summary format. Use when user says create meeting report, generate meeting minutes, summarize this meeting, turn transcript into report, or document this meeting. Activates when transcript content is present via pasted text, inline content, attached file, or uploaded document, even when accompanied by additional context files or reference materials.
---

# Generating Meeting Reports

<purpose>
Meetings contain valuable decisions and commitments buried in conversational noise.
Claude's default summarization compresses too aggressively, losing actionable details.
This skill extracts structured, actionable information while preserving attribution
and marking uncertainty explicitly.
</purpose>

Creates professional, actionable meeting reports from raw transcripts.

## Critical Rules

**GROUNDING:** Base all content ONLY on information explicitly stated in the transcript. Mark inferences clearly.

**EPISTEMIC CALIBRATION:** If information is unclear, incomplete, or ambiguous, your language should make that visible. Name what's unclear rather than guessing — say what the transcript actually contained and where the gap is.

**PROFESSIONAL OBJECTIVITY:** If the transcript reveals issues (incomplete discussions, unresolved conflicts, missing attendees for key decisions), note them in the report. Do not sanitize problems.

## Quick Start

Given a meeting transcript, generate a report:

1. Read the transcript completely before extracting anything
2. Extract meeting metadata, attendees, topics, decisions, and action items
3. Generate report following the structure in [references/REPORT-FORMAT.md](references/REPORT-FORMAT.md)
4. Deliver the report (see Output Rules below)

## Output Rules

The user controls how the report is delivered by including a keyword in their request:

- **"as a file"** → Write to `meeting-report-YYYY-MM-DD.md`. After saving, confirm: "Report saved to `[filename]`" with a brief summary of key findings.
- **"as an artifact"** → Create an artifact containing the complete report.
- **No keyword (default)** → Return the complete report inline in your response.

When delivering inline (the default), execute all workflow phases internally — do not output progress checklists, gate statements, or intermediate extraction notes. Return only the final report.

When delivering as a file or artifact, show the progress checklist and write gate statements visibly before proceeding through each phase.

If the meeting date is unknown, use the current date or ask the user.

## Workflow

```
Progress:
- [ ] Step 1: Analyze transcript
- [ ] Step 2: Extract structured data
- [ ] Step 3: Generate report
- [ ] Step 4: Review for completeness
```

<phase_analyze>
### Step 1: Analyze Transcript

**REQUIRED:** Read the ENTIRE transcript before extracting any information.

Identify from the transcript:
- Meeting date, time, and duration — use "[Not specified]" if absent
- Meeting type/purpose
- Participants and their roles — if roles are not explicit, mark as "[Role inferred from context]" or "[Role unknown]"
- Major discussion topics
- Decisions made — distinguish between "decided" vs "discussed but not decided"
- Action items mentioned (look for "action item", "I'll do", "need to", etc.)
- Resources, tools, or documents referenced
- Follow-up items and open questions

**GATE (file/artifact):** Before proceeding, write:
- "Speakers identified: [list all speakers]"
- "Major topics: [list 2-5 topics]"
- "Meeting date/time: [date or 'Not specified']"

**GATE (inline):** Verify internally before proceeding. Do not output.
</phase_analyze>

<phase_extract>
### Step 2: Extract Structured Data

For each action item, capture:
- Specific task description
- Owner (who is responsible)
- Due date (if mentioned)
- Priority (if indicated)
- Dependencies (if any)

For each topic:
- Background/context
- Key points discussed
- Decisions made
- Implementation details

**GATE (file/artifact):** Before proceeding, write:
- "Action items found: [count]"
- "Decisions documented: [count]"

**GATE (inline):** Verify internally before proceeding. Do not output.
</phase_extract>

<phase_generate>
### Step 3: Generate Report

**ALWAYS use the exact format defined in [references/REPORT-FORMAT.md](references/REPORT-FORMAT.md).** Do not deviate from this structure.

Requirements:
- Executive summary: 2-3 paragraphs covering purpose, key decisions, and critical next steps
- All action items formatted as checkboxes with owner and details
- Resources section with any tools, links, or documents mentioned
- Notes section for follow-ups, open questions, and future considerations

Deliver the report per the Output Rules above.
</phase_generate>

<phase_review>
### Step 4: Review and Deliver

**GATE (file/artifact):** Before delivering, write:
- "Action items: [count] items with [count] owners assigned"
- "Format check: Matches template exactly: [yes/no]"
- "Gaps documented: [list any information gaps, uncertainties, or inferences flagged, or 'None']"

**GATE (inline):** Verify internally. Do not output gate statements — return only the final report.

Then deliver per the Output Rules above.
</phase_review>

## Handling Challenges

**Informal or fragmented transcripts:**
- Group related discussions into coherent topics based on explicit content
- Extract implicit action items from commitments ("I'll look into that") — mark these as "[Implicit commitment]"
- If structure is unclear, note this: "Transcript structure was informal; topic groupings represent best interpretation."

**Missing information:**
- Use "[Not specified]" for unknown dates/times
- When making reasonable inferences, make the inferential step visible in your language; when you genuinely cannot determine something, say so
- Document assumptions in the report's notes section

**Multiple speakers with same name:**
- Distinguish by role if possible
- If ambiguous, note explicitly: "Speaker attribution uncertain between [Name A] and [Name B]"

**Quality issues in transcript:**
- If the transcript has significant gaps, garbled sections, or quality issues, flag this to the user before generating the report
- Do not fill in missing content with assumptions

<failed_attempts>
What DOESN'T work:

- **Inventing action items:** If no one said "I'll do X," don't create an action item. Only extract explicit commitments.
- **Guessing speaker roles:** If the transcript doesn't say "Sarah, our CTO," don't infer titles. Use "[Role unknown]".
- **Filling gaps with plausible content:** A missing date is "[Not specified]," not a reasonable guess.
- **Summarizing instead of structuring:** The goal is extraction, not compression. Keep the detail; remove only filler words.
- **Attributing to wrong speakers:** When attribution is unclear, mark it explicitly rather than guessing.
</failed_attempts>

## Example

### Sample Transcript Fragment

```
[Sarah Chen]
Okay so for the website redesign, I talked to the design team and they can start next week.

[Mike Torres]
Great. What's the timeline looking like?

[Sarah Chen]
They're saying 3 weeks for mockups. I'll send you the project brief by Friday.

[Mike Torres]
Perfect. Action item for me - I need to get the brand guidelines doc to Sarah before she briefs the team.
```

### Expected Extraction

From this fragment, extract:

**Speakers:** Sarah Chen, Mike Torres

**Topic:** Website Redesign
- Design team available next week
- 3-week timeline for mockups
- Decision: Proceed with design team engagement

**Action Items:**
1. Send project brief to Mike — Owner: Sarah Chen, Due: Friday
2. Share brand guidelines doc with Sarah — Owner: Mike Torres, Due: Before Friday, Dependency: Needed before design team briefing

**REQUIRED:** Format the final report using the exact structure in [references/REPORT-FORMAT.md](references/REPORT-FORMAT.md). That file is the authoritative template for all output formatting.

## Reference

- [references/REPORT-FORMAT.md](references/REPORT-FORMAT.md) — **Authoritative template.** Use this exact structure for all reports.
