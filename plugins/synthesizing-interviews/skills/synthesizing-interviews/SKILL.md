---
name: synthesizing-interviews
description: Synthesizes interview transcripts into comprehensive research documents with structured insights, key quotes, speaker information, and verified references. Use when user says synthesize interview, extract insights from transcript, distill conversation, process interview, or analyze interview. Activates when transcript content is present via pasted text, inline content, attached file, or uploaded document, even when accompanied by additional context files or reference materials. NOT for meeting reports with action items.
---

# Synthesizing Interviews

Extracts structured insights, key quotes, and discussion analysis from interview transcripts for later research use. This is NOT a meeting report generator - it distills the substance of conversations.

<purpose>
Claude's default is to summarize—to compress information into brief overviews.
Interview synthesis requires the opposite: preserving richness while removing only
conversational overhead. This skill exists to enforce detailed distillation over
compression, ensuring every significant point, quote, and viewpoint is captured.
</purpose>

## Critical Rules

**GROUNDING:** Base all synthesis ONLY on what speakers actually said. Every claim in the synthesis must trace to specific transcript content.

**QUOTE INTEGRITY:** Preserve speaker meaning, not transcription errors. Clean transcription artifacts (false punctuation, filler words, stutters, [inaudible] markers) while keeping the speaker's actual words and intent intact. Never change word choice, combine separate statements, or alter meaning.

**EPISTEMIC CALIBRATION:** Your language should make clear whether a point is what a speaker said, your inference from context, or your analytical judgment. If speakers made claims you cannot verify, note this. If there are contradictions between speakers, surface them. If transcript quality limits what you can extract, name the limitation.

**PROFESSIONAL OBJECTIVITY:** Report what was said, including tensions, disagreements, or concerning statements. Do not sanitize to make subjects look better. The user needs the actual substance of the conversation.

**CONVERGENCE AWARENESS:** When themes from different speakers or different parts of the conversation intersect, name the intersection and what it reveals. Don't let convergences pass as merely interesting — they often expose the underlying dynamics of the topic.

**SECOND-ORDER THINKING:** Push past surface-level takeaways. If a speaker describes a successful approach, note what it may also constrain or what it depends on. If multiple speakers agree on a point, consider what that consensus might obscure.

**PREMATURE COMMITMENT CHECK:** If you find yourself building the synthesis around the first major theme that emerged, pause. Check whether the transcript supports alternative organizing principles that might surface different insights.

## Quick Start

1. User provides transcript (any format: SRT, VTT, Google Meet, Teams, DOCX, plain text)
2. Optionally user provides context files (org dossiers, reference materials)
3. Generate comprehensive synthesis document
4. Save to file: `./tmp/[subject]-interview-synthesis-YYYY-MM-DD.md`

## Workflow

```
Progress:
- [ ] Phase 1: Process transcript and identify speakers
- [ ] Phase 2: Build discussion outline
- [ ] Phase 3: Write main synthesis
- [ ] Phase 4: Extract key quotes
- [ ] Phase 5: Compile and verify references
- [ ] Phase 6: Note spelling/verification issues
- [ ] Phase 7: Save output file
```

<phase_process>
### Phase 1: Process Transcript

Accept transcripts in any format:
- **Subtitle files** (.srt, .vtt) - time codes and speaker labels
- **Recorder transcripts** - speaker names, may lack time codes
- **Google Meet/Teams transcripts** - time codes and speaker labels
- **Plain text/pasted** - raw conversation text
- **DOCX files** - word processor documents

If context documents provided:
- Use them to verify spellings of names, organizations, tools
- Apply relationship context to analysis
- Cross-reference background information

**GATE:** Before proceeding, write:
- "Transcript format: [format identified]"
- "Speakers identified: [list names]"
</phase_process>

<phase_outline>
### Phase 2: Build Discussion Outline

Create a high-level flow of the conversation:
- Hierarchy limited to 3 levels deep
- Serves as quick navigation reference
- Captures the arc and structure of discussion
</phase_outline>

<phase_synthesis>
### Phase 3: Write Main Synthesis

This is the core output. NOT a summary - a detailed distillation.

**REQUIRED:**
- Capture ALL significant points and ideas from the transcript
- Preserve the tenor and flow of conversation
- Include direct quotes with attribution throughout — clean transcription artifacts but preserve speaker's words
- Identify individual viewpoints and perspectives
- Surface areas of agreement, disagreement, or tension between speakers — do not smooth over conflicts
- Explain and contextualize ideas discussed (don't just list them)
- Maintain enough detail for later research use

**Length:** Substantially longer than a typical summary. The goal is preserving richness while removing conversational overhead.

**Viewpoint Tracking:**
When speakers express positions, be explicit about who said what:
> "Martinez argued that the timeline was unrealistic, citing previous project delays: 'We've never hit a Q3 deadline in five years.' Chen disagreed, pointing to new tooling as a differentiator."

**CRITICAL — Do not omit:**
- Disagreements or tensions between speakers
- Statements that may be unflattering to a speaker
- Claims that appear questionable or unsubstantiated
- Moments of uncertainty or confusion in the discussion

**Tone/Tenor:** Note the character of discussion - collaborative, contentious, exploratory, uncertain, etc. If the conversation was tense or difficult, say so.

**GATE:** Before proceeding to quotes, confirm:
- "I have captured [N] significant topics"
- "Viewpoints tracked for: [speaker list]"
- "Tensions/disagreements documented: [yes/no with brief description]"
</phase_synthesis>

<phase_quotes>
### Phase 4: Extract Key Quotes

Pull significant quotes with:
- Speaker attribution
- Organization by theme or topic
- Cleaned transcription artifacts

**Transcription Cleanup (REQUIRED):**

Remove these artifacts — they are transcription noise, not speaker intent:
- False punctuation (periods, question marks mid-sentence from speech recognition)
- Filler words (um, uh, you know, like)
- Stutters and false starts
- [inaudible] or [unclear] markers — omit the marked section or skip the quote
- Repeated words from speech disfluency

Preserve these — they are what the speaker actually said:
- Word choice (never substitute synonyms)
- Grammar that reflects natural speech
- Incomplete thoughts (if meaningful)
- Emphasis and phrasing

**Example cleanup:**
- Raw: "We don't want to hallucinate. Time estimates. We don't want to hallucinate. Um. Date and times"
- Cleaned: "We don't want to hallucinate time estimates. We don't want to hallucinate date and times"

Focus on quotes that:
- Capture key insights or positions
- Reveal speaker priorities or concerns
- Provide memorable articulation of ideas
- Show points of agreement or disagreement
</phase_quotes>

<phase_references>
### Phase 5: Compile and Verify References

**REQUIRED:** Actively search for URLs for all references mentioned.

Extract any mentioned:
- Articles, papers, books
- Websites and tools
- People referenced (not speakers)
- Historical events or context
- Organizations

**For each reference mentioned by name:**
1. Use web search to find the actual URL
2. Verify the result matches what was discussed (not just a name match)
3. If you cannot verify a reference, mark it as "[URL not verified]"
4. If a reference appears to not exist, note this: "[Could not locate — may be misremembered or proprietary]"

Do not include URLs you are not confident are correct.
</phase_references>

<phase_verification>
### Phase 6: Spelling/Verification Notes

Flag:
- Unusual spellings that may be transcription errors
- Discrepancies between transcript and context documents
- Items that couldn't be verified via search
- Names or terms that appear inconsistent
</phase_verification>

<phase_save>
### Phase 7: Save Output

**GATE:** Before saving, confirm:
- "References searched: [count]"
- "Unverified items flagged: [count]"

**ALWAYS save to file in `./tmp/`. Do not output inline in chat.**

Filename: `./tmp/[subject-or-interviewee]-interview-synthesis-YYYY-MM-DD.md`

After saving, confirm with brief summary of what was captured.
</phase_save>

## Output Structure

```markdown
# Interview Synthesis: [Subject/Interviewee]

**Date:** [Interview date if known]
**Participants:** [Names and roles]

## Discussion Outline

1. [Topic]
   1.1. [Subtopic]
   1.2. [Subtopic]
2. [Topic]
   ...

## Speaker Information

### [Speaker Name]
- **Role:** [Title/position if known]
- **Background:** [Relevant bio notes]
- **Contact:** [If mentioned]

[Repeat for each speaker]

## Synthesis

[Detailed distillation of the discussion - this is the main content]

## Key Quotes

### [Theme 1]

> "[Quote with transcription artifacts cleaned]" — [Speaker Name]

> "[Quote with transcription artifacts cleaned]" — [Speaker Name]

### [Theme 2]

> "[Exact quote]" — [Speaker Name]

[Continue by theme]

## References

### Articles & Publications
- [Title](URL) - [Brief context of how it was mentioned]

### Tools & Websites
- [Name](URL) - [How it was discussed]

### People Mentioned
- [Name] - [Context/relevance]

### Organizations
- [Name] - [Context]

## Verification Notes

- [Any spelling uncertainties]
- [Unverified references]
- [Discrepancies found]
```

## Key Differentiators from Meeting Reports

| Meeting Reports | Interview Synthesis |
|-----------------|---------------------|
| Action items focus | Ideas and insights focus |
| Decisions made | Viewpoints expressed |
| Brief summaries | Detailed distillation |
| What was decided | How discussion unfolded |
| Assignments | Quotes and attribution |

**If user wants action items, decisions, or assignments - that's a meeting report, not an interview synthesis.**

## Examples

### Example Input

User provides Google Meet transcript:
```
0:00:15 Sarah Chen: Thanks for joining. I wanted to discuss the Riverside project.
0:00:22 Marcus Johnson: Sure. I think we're at a critical juncture here.
0:00:28 Sarah Chen: What do you mean by critical?
0:00:35 Marcus Johnson: The community feedback has been overwhelming. We received over 200 comments on the environmental impact study.
...
```

### Example Output Excerpt

```markdown
# Interview Synthesis: Riverside Project Discussion

**Date:** 2024-03-15
**Participants:** Sarah Chen (Project Lead), Marcus Johnson (Community Liaison)

## Discussion Outline

1. Project Status Overview
   1.1. Current timeline concerns
   1.2. Stakeholder alignment
2. Community Feedback Analysis
   2.1. Volume and nature of responses
   2.2. Key concerns identified
3. Environmental Impact Considerations
   ...

## Synthesis

The conversation revealed significant tension between project timeline pressures and community engagement needs. Johnson characterized the project as being at a "critical juncture," emphasizing that community feedback had exceeded expectations both in volume and intensity.

Chen initially approached the discussion from an operational standpoint, focused on deliverables and deadlines. However, Johnson's framing shifted the conversation toward relationship management: "We can hit every milestone and still fail if we lose community trust."

The environmental impact study emerged as a flashpoint. Johnson noted that "over 200 comments" had been received, describing the response as "overwhelming." He interpreted this not as opposition but as engagement: "People care enough to participate. That's actually a good sign if we handle it right."

Chen expressed concern about timeline implications...

## Key Quotes

### On Community Engagement

> "We can hit every milestone and still fail if we lose community trust." — Marcus Johnson

> "People care enough to participate. That's actually a good sign if we handle it right." — Marcus Johnson

### On Project Priorities

> "I need to understand if this changes our Q3 targets." — Sarah Chen

## References

### Tools & Websites
- [PublicInput.com](https://publicinput.com) - Platform mentioned for managing community feedback

### People Mentioned
- Dr. Elena Vasquez - Environmental consultant referenced regarding the impact study
```

<failed_attempts>
What DOESN'T work:

- **Summarizing instead of synthesizing:** Compression loses the richness. The synthesis should be substantial—longer than a summary, preserving detail.
- **Preserving transcription errors in quotes:** False punctuation, filler words, and speech recognition artifacts are not what the speaker said. They create broken token sequences that confuse downstream LLM processing. Clean them.
- **Changing word choice in quotes:** Cleaning artifacts is required; substituting synonyms or "improving" phrasing is forbidden. The speaker's actual words must be preserved.
- **Smoothing over tensions:** If speakers disagreed, report the disagreement. Sanitizing conflict loses valuable information.
- **Skipping reference lookup:** Users need verified URLs. "I'll add links later" means links never get added.
- **Outputting inline:** Always save to file. Long synthesis documents are unusable in chat.
- **Ignoring context documents:** If provided, they contain verified spellings and background that improve accuracy.
- **Creating meeting reports:** If the user wants action items, decisions, or assignments—that's a meeting report, not an interview synthesis.
</failed_attempts>
