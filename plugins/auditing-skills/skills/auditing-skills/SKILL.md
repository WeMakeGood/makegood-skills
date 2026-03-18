---
name: auditing-skills
description: Audits existing Agent Skills against current best practices and suggests improvements. Reviews structure, behavioral guardrails, phase boundaries, commitment gates, and anti-patterns documentation. Use when user says audit skill, review skill, check skill quality, improve skill, or update skill to best practices. Activates when a skill path is provided or when working in a skills directory.
---

# Auditing Skills

<purpose>
Skills evolve as best practices improve. This skill exists because older skills may lack
structured patterns (XML boundaries, commitment gates, purpose statements) that improve
Claude's adherence to workflows. The skill audits existing skills against current standards
and produces actionable improvement recommendations.
</purpose>

## Critical Rules

**GROUNDING:** Base all assessments on actual skill content. Do not assume problems exist—verify by reading the skill files.

**EDITS REQUIRE APPROVAL:** After presenting the audit report, ask if the user wants changes applied. Do not edit skill files without explicit approval.

**PROFESSIONAL OBJECTIVITY:** Report all gaps found, even if the skill is otherwise well-written. Do not minimize issues to avoid criticism.

## Quick Start

1. User provides skill path (e.g., `skills/my-skill`)
2. Read SKILL.md and all referenced files
3. Audit against checklist
4. Generate improvement report
5. If user approves, apply changes directly to skill files

## Workflow

<phase_read>
### Phase 1: Read Skill Content

**REQUIRED:** Read ALL files in the skill directory:
- SKILL.md (required)
- README.md (if present)
- All files in references/ (if present)
- All scripts in scripts/ (if present)

**GATE:** Before proceeding, write:
- "I have read [N] files: [list them]"
- "Total lines in SKILL.md: [count]"

Do not proceed until you have listed every file read.
</phase_read>

<phase_audit>
### Phase 2: Audit Against Checklist

Evaluate the skill against each criterion. Mark as:
- ✅ Present and well-implemented
- ⚠️ Present but could be improved
- ❌ Missing or inadequate

#### Structure Checklist

| Criterion | Status | Notes |
|-----------|--------|-------|
| **Frontmatter valid** | | name, description present and valid |
| **Description third-person** | | No "I" or "you" |
| **Description has triggers** | | "Use when..." or "Activates when..." |
| **Under 500 lines** | | Or properly split into references/ |
| **README.md present** | | User-facing documentation for GitHub |

#### Behavioral Guardrails Checklist

Test what the guardrails accomplish, not what they're named. A guardrail that requires an upstream step (process gate) is stronger than one that names a failure mode and monitors for it.

| Test | Status | Notes |
|------|--------|-------|
| **Critical Rules section exists** | | Near top of skill |
| **Claims require a prior step before they can be stated** | | e.g., "locate source before stating claim" — not "don't hallucinate" |
| **Epistemic status is structurally visible** | | Reader can distinguish sourced/inferred/analytical from the language itself |
| **Disagreement has a defined path** | | Skill tells Claude when and how to challenge, with specifics — not just "be honest" |
| **Mandatory actions use strong language** | | REQUIRED, CRITICAL, STOP, GATE — not "consider" or "you might" |

#### Structured Patterns Checklist

| Criterion | Status | Notes |
|-----------|--------|-------|
| **Purpose statement** | | `<purpose>` tag explaining why skill exists |
| **XML phase boundaries** | | `<phase_name>` tags for multi-step workflows |
| **Commitment gates** | | GATE markers requiring written statements |
| **Anti-patterns documented** | | `<failed_attempts>` section |

#### Content Quality Checklist

| Criterion | Status | Notes |
|-----------|--------|-------|
| **Concrete examples** | | Real input/output, not placeholders |
| **Examples not over-anchoring** | | Structural over content-specific; multiple examples to prevent fixation; Wrong/Right pairs don't create rigid templates |
| **Output requirements** | | File vs inline specified (if applicable) |
| **Destructive action gates** | | For skills that delete/overwrite |
| **Natural prose guardrails** | | For external-facing content skills |

**GATE:** Before proceeding, write:
- "Audit complete. Found [N] issues requiring attention."
- "Most critical gap: [description]"
</phase_audit>

<phase_report>
### Phase 3: Generate Audit Report

Create a structured report with:

```markdown
# Skill Audit: [skill-name]

**Audited:** [date]
**Skill path:** [path]
**Files reviewed:** [list]

## Summary

**Overall assessment:** [Strong / Adequate / Needs Work]

**Critical gaps:** [count]
**Improvements suggested:** [count]

## Detailed Findings

### Structure
[Findings with specific line references]

### Behavioral Guardrails
[Findings with specific recommendations]

### Structured Patterns
[Findings with examples of what to add]

### Content Quality
[Findings with specific suggestions]

## Recommended Changes

### High Priority (Critical Gaps)

1. **[Gap]:** [What to add/change]
   - Current: [what exists]
   - Recommended: [what should exist]
   - Example:
   ```markdown
   [concrete example of the fix]
   ```

### Medium Priority (Improvements)

1. **[Improvement]:** [What to enhance]

### Low Priority (Polish)

1. **[Polish item]:** [Nice to have]

## Next Steps

To implement these changes:
1. [First step]
2. [Second step]
3. Run validation: `python scripts/validate.py [path]`
```

**Save to:** `[skill-name]-audit-report.md` in current directory or user-specified location.
</phase_report>

<phase_apply>
### Phase 4: Apply Changes (On Approval)

After presenting the audit report, ask: "Would you like me to apply these changes to the skill?"

If user approves:

**GATE:** Before editing, write:
- "I will apply [N] changes to [file path]"
- "Changes: [brief list of what will be modified]"

**STOP.** Wait for explicit user confirmation.

When applying changes:
- Edit the skill files directly (no draft files)
- Preserve all existing functionality
- Add missing structural patterns
- Do not remove content unless it violates best practices
- Run validation after changes: `python scripts/validate.py [path]`

After applying, summarize what was changed.
</phase_apply>

## Audit Priorities

When multiple issues exist, prioritize:

1. **Critical (blocks effectiveness):**
   - Missing Critical Rules section
   - No sourcing discipline for content-generating skills (no process gate or grounding rule)
   - No gates for destructive actions

2. **High (significantly improves quality):**
   - Missing phase boundaries in multi-step workflows
   - No commitment gates at key decision points
   - Missing purpose statement for counter-intuitive skills
   - Named failure modes where process gates would be more effective (e.g., "Don't hallucinate" vs. requiring source-before-statement)

3. **Medium (improves adherence):**
   - Weak language (should → REQUIRED)
   - Missing anti-patterns documentation
   - Vague examples
   - Prescribed marker labels where natural epistemic calibration would be more robust

4. **Low (polish):**
   - Missing README.md for GitHub users
   - Could add more trigger keywords to description
   - Could improve organization

<failed_attempts>
What DOESN'T work:

- **Auditing without reading all files:** You'll miss context in references/ that explains why SKILL.md is structured a certain way.
- **Recommending changes that break functionality:** Always preserve what works. Add structure, don't replace content.
- **Generic recommendations:** "Add better examples" is useless. Show the specific example to add.
- **Auditing against outdated standards:** Always reference current BEST-PRACTICES.md patterns.
- **Creating draft files instead of editing directly:** Extra files create friction. After approval, edit the skill directly.
- **Adding marker comments:** `<!-- ADDED -->` comments waste context tokens and clutter the skill.
</failed_attempts>

## Examples

### Example: Audit Request

**User:** "Audit skills/synthesizing-interviews"

**Phase 1 output:**
```
I have read 1 files: SKILL.md
Total lines in SKILL.md: 283
```

**Phase 2 output:**
```
Audit complete. Found 3 issues requiring attention.
Most critical gap: No XML phase boundaries despite 7-phase workflow.
```

**Phase 3 output:** (excerpt)
```markdown
# Skill Audit: synthesizing-interviews

## Summary

**Overall assessment:** Adequate

**Critical gaps:** 0
**Improvements suggested:** 3

## Detailed Findings

### Structured Patterns

- ❌ **Purpose statement:** Missing. This skill addresses Claude's tendency to
  summarize rather than synthesize—a purpose statement would reinforce this.

- ❌ **XML phase boundaries:** The skill has 7 phases (Process → Outline →
  Synthesis → Quotes → References → Verification → Save) but uses only
  markdown headers. XML boundaries would create harder phase separation.

- ⚠️ **Commitment gates:** Has output requirements ("ALWAYS save to file")
  but no commitment gates between phases.

## Recommended Changes

### High Priority

1. **Add purpose statement:**
   ```markdown
   <purpose>
   Claude's default is to summarize—to compress information into brief
   overviews. Interview synthesis requires the opposite: preserving richness
   while removing only conversational overhead. This skill exists to enforce
   detailed distillation over compression.
   </purpose>
   ```

2. **Add XML phase boundaries:**
   ```markdown
   <phase_process>
   ### Phase 1: Process Transcript
   [existing content]

   **GATE:** Before proceeding, write:
   - "Transcript format: [format identified]"
   - "Speakers identified: [list]"
   </phase_process>
   ```
```

## Reference

This skill audits against patterns documented in:
- [BEST-PRACTICES.md](../creating-skills/references/BEST-PRACTICES.md) - Structured patterns, behavioral guardrails
- [SPEC.md](../creating-skills/references/SPEC.md) - Structure requirements, field limits
