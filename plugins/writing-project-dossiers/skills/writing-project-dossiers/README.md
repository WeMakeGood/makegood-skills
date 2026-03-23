# Writing Project Dossiers

Creates comprehensive project dossiers through interactive guided conversation, producing scope documents suitable for client approval.

## When to Use

Use this skill when you need to:
- Scope a new project for client approval
- Create a project brief covering deliverables, timeline, budget, and team
- Turn meeting notes and planning materials into a structured project document
- Produce a dossier that can feed into Teamwork.com task imports

## How to Invoke

Say things like:
- "Help me write a project dossier for this website redesign"
- "Create a project scope document from these meeting notes"
- "I need to scope a marketing campaign for client approval"

## What You'll Need

- Project planning materials in any format (MD, PDF, DOCX, images, pasted text)
  - Meeting reports or kickoff notes
  - Client dossiers or background documents
  - Example deliverables or reference materials
  - Template files (optional)

Not everything needs to be provided upfront — the skill asks targeted questions to fill gaps.

## What You'll Get

A markdown dossier file (`[project-name]-dossier.md`) containing:
- Project overview and objectives
- Deliverables organized by area of concern (Design, Development, Editorial, etc.)
- Team structure and roles
- Timeline and milestones (only confirmed dates)
- Budget information (if available)
- Communication plan
- Risks and mitigation strategies

The deliverables section is structured for direct consumption by the `generating-teamwork-imports` skill.

## Example

**Input:** Discovery call meeting report + client organization dossier for a platform migration

**Output:** A dossier with deliverables grouped under Technical (data migration, API integration) and Operations (parallel run, user training), with team roles, known deadlines, and items explicitly marked "To be determined" where details haven't been confirmed. The skill surfaces cross-domain risks during scoping — for instance, identifying that migration projects share "last mile" dependency patterns with physical moves.

## Tips

- Provide as many source documents as you have — the skill extracts what it needs
- The skill won't invent dates or hours; if you want those in the dossier, provide them
- Deliverables are grouped by area of concern (not timeline phase) for Teamwork compatibility
- After the dossier is approved, run the `generating-teamwork-imports` skill to create task imports
