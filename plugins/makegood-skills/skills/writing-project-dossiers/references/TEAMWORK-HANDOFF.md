# Teamwork Import Handoff

This document explains how to structure the dossier's Deliverables section so the `generating-teamwork-imports` skill can consume it directly.

## Why This Matters

The `generating-teamwork-imports` skill converts project planning documents into Teamwork.com import files. It reads dossiers as source material. If the dossier's deliverables are structured correctly, the Teamwork skill can extract task lists, tasks, and assignments without ambiguity.

## Structure Requirements

### Mapping to Teamwork Hierarchy

| Dossier Element | Teamwork Element |
|----------------|-----------------|
| Area of Concern heading (## Design) | Task List |
| Deliverable heading (### Homepage Redesign) | Task |
| Sub-items within a deliverable | Subtasks (only if naturally divisible) |

### Required Fields Per Deliverable

The Teamwork skill needs these from each deliverable:

| Field | Dossier Source | Required? |
|-------|---------------|-----------|
| Task name | Deliverable heading | Yes |
| Description | Narrative paragraph | Yes |
| Assignee | Ownership field | Yes (role is sufficient if no email) |
| Due date | Due date field | No — only if known |
| Time estimate | Estimated time field | No — only if known |
| Type | One-time / Recurring | Helpful for Teamwork tagging |
| Dependencies | Dependencies field | Helpful for task ordering |

### What to Leave Out

The dossier is an approval document. The Teamwork import is a work-tracking document. Some dossier details don't need to transfer:

- **Strategy sections** — Teamwork tracks tasks, not strategy
- **Communication plans** — These inform process, not task structure
- **Risk sections** — These inform planning, not individual tasks
- **Budget breakdowns** — Teamwork tracks time, not money

### Handling "To Be Determined" Items

When the dossier marks something as TBD, the Teamwork skill will:
- Leave the corresponding field empty in the import
- Flag it in the audit document for the user to fill in

This is the intended behavior. Empty fields in Teamwork are honest; plausible-looking values are hallucinations.

## Example Handoff

**Dossier deliverable:**
```markdown
## Development
### CMS Migration
Migration from existing WordPress installation to new CMS platform.
Includes content migration and data migration from the existing database.
- Ownership: Development team
- Type: One-time
- Dependencies: Design approval, content inventory
```

**What the Teamwork skill extracts:**
```
Task List: Development
Task: CMS Migration
Description: Migration from existing WordPress installation to new CMS platform. Includes content migration and data migration from the existing database.
Assignee: Development team (will need email assignment in Teamwork)
Due date: [empty — not specified]
Time estimate: [empty — not specified]
```
