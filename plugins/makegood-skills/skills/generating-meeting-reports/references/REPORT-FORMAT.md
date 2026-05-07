# Meeting Report Format

Use this exact structure for all meeting reports.

## Template

```markdown
# [Meeting Title] - Meeting Report

## Executive Summary

[2-3 paragraphs covering:]
- Meeting purpose and context
- Key decisions and outcomes
- Critical next steps and implications

## Meeting Details

**Date:** [YYYY-MM-DD]
**Time:** [HH:MM Timezone]
**Duration:** [X hours Y minutes]
**Type:** [Meeting Type/Purpose]

### Attendees

- [Name] ([Role/Organization])
- [Name] ([Role/Organization])

## Key Discussion Topics

### [Topic Name]

- **Background/Context:** [Brief context]
- **Key Points Discussed:**
  - [Point 1]
  - [Point 2]
- **Decisions Made:** [Clear statement of any decisions]
- **Implementation Details:** [If applicable]

[Repeat for each major topic]

## Action Items

- [ ] [Clear, specific action]
   * Owner: [Name/Role]
   * Due: [Date if specified, otherwise "Not specified"]
   * Priority: [If indicated]
   * Dependencies: [If any]

[Repeat for each action item, numbered]

## Resources Discussed

- **Tools:** [List with links if available]
- **Documents:** [List with links if available]
- **Systems:** [Internal platforms/tools mentioned]
- **Additional Resources:** [Other relevant materials]

## Notes

- **Follow-up Meetings:** [Scheduled or needed]
- **Open Questions:** [Unresolved items]
- **Future Considerations:** [Long-term items noted]
```

## Formatting Guidelines

### Executive Summary

Write in complete sentences. Focus on:
1. Why the meeting was held
2. What was decided
3. What happens next

Keep it scannable - busy executives should grasp the essentials in 30 seconds.

### Meeting Details

- Use ISO date format (YYYY-MM-DD)
- Include timezone for time
- Calculate duration from transcript if not explicit
- Infer meeting type from content (e.g., "Executive Planning", "Team Sync", "Project Review")

### Attendees

- List in order of appearance or by seniority
- Include role/title if mentioned
- Include organization if external participants

### Discussion Topics

- Create logical groupings from transcript flow
- Use descriptive topic names (not "Item 1")
- Decisions should be explicit statements, not summaries

### Action Items

- Start with action verb (Investigate, Schedule, Review, etc.)
- Be specific enough to be actionable
- Extract owner from transcript ("I'll do X" = that speaker is owner)
- Mark dates as "[Not specified]" if not mentioned

### Resources

Omit empty categories. If no resources mentioned, note: "No specific resources discussed."

### Notes

- Follow-ups: Include any scheduled meetings or needed check-ins
- Open Questions: Items raised but not resolved
- Future Considerations: Ideas for later discussion

## Example Output

```markdown
# Product Launch Planning - Meeting Report

## Executive Summary

The product team met to finalize plans for the Q2 mobile app launch. The meeting focused on three key areas: marketing timeline alignment, technical readiness assessment, and budget allocation for launch activities.

Major decisions included confirming the April 15th launch date, approving the $50,000 marketing budget for launch week activities, and selecting vendor Beta Corp for the press release distribution. The team also agreed to delay the Android release by two weeks to address outstanding performance issues.

Critical next steps involve completing the iOS App Store submission by March 20th, finalizing influencer partnerships, and conducting the final load testing by April 1st. A go/no-go meeting is scheduled for April 10th.

## Meeting Details

**Date:** 2026-03-10
**Time:** 10:00 AM PST
**Duration:** 1 hour 15 minutes
**Type:** Product Launch Planning

### Attendees

- Sarah Chen (VP of Product)
- Mike Torres (Engineering Lead)
- Lisa Park (Marketing Director)
- James Wilson (QA Manager)

## Key Discussion Topics

### Launch Timeline

- **Background/Context:** Review of launch readiness and timeline alignment
- **Key Points Discussed:**
  - iOS app passed final QA certification
  - Android version has 3 critical bugs remaining
  - Marketing materials 90% complete
- **Decisions Made:** Confirm April 15th iOS launch; delay Android to April 29th
- **Implementation Details:** Engineering to prioritize Android bug fixes; Marketing to adjust messaging for staggered launch

### Marketing Budget

- **Background/Context:** Approval needed for launch week spending
- **Key Points Discussed:**
  - Influencer campaign costs ($25,000)
  - Press release distribution ($8,000)
  - Launch event venue and catering ($12,000)
  - Contingency buffer ($5,000)
- **Decisions Made:** Approve $50,000 total budget
- **Implementation Details:** Lisa to submit purchase orders by March 15th

### Vendor Selection

- **Background/Context:** Choosing between two PR distribution vendors
- **Key Points Discussed:**
  - Alpha PR: Lower cost ($6,000) but limited tech media reach
  - Beta Corp: Higher cost ($8,000) but includes TechCrunch and Wired
- **Decisions Made:** Select Beta Corp for broader tech media coverage
- **Implementation Details:** Contract to be signed by March 12th

## Action Items

- [ ] Submit iOS app to App Store
   * Owner: Mike Torres
   * Due: March 20th
   * Priority: High

- [ ] Fix remaining Android critical bugs
   * Owner: Mike Torres
   * Due: April 15th
   * Priority: High
   * Dependencies: QA bug reports from James

- [ ] Finalize influencer partnership contracts
   * Owner: Lisa Park
   * Due: March 18th
   * Priority: High

- [ ] Book launch event venue
   * Owner: Lisa Park
   * Due: March 12th
   * Priority: Medium

- [ ] Complete final load testing
   * Owner: James Wilson
   * Due: April 1st
   * Priority: High

- [ ] Sign Beta Corp contract
   * Owner: Sarah Chen
   * Due: March 12th
   * Priority: Medium

- [ ] Schedule go/no-go meeting
   * Owner: Sarah Chen
   * Due: Not specified
   * Priority: Low

## Resources Discussed

- **Tools:** TestFlight, Firebase Crashlytics, Hootsuite
- **Documents:** Launch checklist (shared drive), Brand guidelines v2.1
- **Systems:** App Store Connect, Google Play Console

## Notes

- **Follow-up Meetings:** Go/no-go decision meeting scheduled for April 10th at 2 PM
- **Open Questions:** Whether to include tablet optimization in initial Android release
- **Future Considerations:** Planning for v1.1 feature set based on launch feedback
```
