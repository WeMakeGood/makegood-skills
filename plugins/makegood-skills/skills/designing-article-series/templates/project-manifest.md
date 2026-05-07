---
project: [project name]
type: series | single
updated: YYYY-MM-DD
---

# Project Manifest

## Voice and Standards

| Component | Path |
|-----------|------|
| Voice profile | [path to voice-profile-*.md] |
| Writing standards | [path to writing-standards-*.md in Context/] |

## Audience

| Component | Path |
|-----------|------|
| Audience document | [path] |

## Research

| Component | Path |
|-----------|------|
| Research directory | [path to directory containing research documents] |
| Research index | [path to research-index.md, or "none — see research directory"] |

## Series Architecture

| Component | Path |
|-----------|------|
| Series map | [path to series-map.md — omit for single articles] |
| Core thesis | [path to thesis/framework document — optional] |
| Article brief | [path or inline — for single articles only] |

## Output

| Component | Path |
|-----------|------|
| Drafts directory | [path where drafts and process logs are saved] |

## Context Modules (Optional)

Organizational context modules in `Context/` that inform drafting. These are not research — they are organizational knowledge the drafting skill may load for accuracy and alignment. List only modules that exist; omit this section if no context modules are available.

| Component | Path |
|-----------|------|
| [e.g., Organizational identity] | [path] |
| [e.g., Ethical framework] | [path] |
| [e.g., Content methodology] | [path] |

---

## Update Rules

**Updating paths:** Change paths when files move. The drafting-articles skill reads this manifest to find its files — incorrect paths break the handoff.

**Adding overrides:** Add an Overrides section below for project-specific rules that affect drafting (e.g., "Skip keyword targeting", "No series build context"). Keep overrides minimal — the skill's own process handles most concerns.

**Do not:** Add content, analysis, or editorial notes to this file. It is a file locator, not a working document.
