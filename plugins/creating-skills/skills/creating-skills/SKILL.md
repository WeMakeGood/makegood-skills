---
name: creating-skills
description: Guides creation of new Agent Skills from prompts, context files, and requirements. Provides foundational knowledge about skill architecture, best practices, and testing procedures. Use when asked to create, build, develop, or convert content into an Agent Skill.
---

# Creating Skills

<purpose>
Claude's default when creating skills is to be verbose—adding explanations, options, and
context that waste tokens. This skill exists because effective skills are concise, structured,
and grounded in concrete examples. The skill enforces these patterns by requiring reference
doc reading, validation scripts, and explicit workflow phases with commitment gates.
</purpose>

This skill guides you through creating well-structured Agent Skills from prompts, documentation, or requirements.

## Critical Rules for All Skills

Every skill you create MUST include behavioral guardrails. These are non-negotiable.

Structure guardrails as **upstream process gates** — steps that make failure modes architecturally difficult — rather than naming failure modes and telling Claude to watch for them. The goal is to require an incompatible upstream step, not to describe the failure and hope it's avoided.

**SOURCING DISCIPLINE:** Skills must require locating a source before stating a claim. Include:
- What sources Claude can use (documents, transcripts, user input, context modules)
- A source-before-statement requirement: locate, cite, scope
- What to do when a source can't be found (ask, flag, or state what's missing)

**EPISTEMIC CALIBRATION:** Skills must ensure the language itself signals the status of each claim — sourced, inferred, or analytical. Include:
- A requirement that readers can always tell whether they're receiving a sourced claim, a logical extension, or the agent's reasoning
- This is a language discipline, not a formatting convention — avoid prescribing bracket markers like `[Inferred]`

**PROFESSIONAL CHALLENGE:** Skills must prioritize accuracy over agreement. Include:
- When to challenge (contradicts documented strategy, known pitfalls, unsupported assumptions)
- How to challenge (cite the concern, offer an alternative)

**INSTRUCTION ADHERENCE:** Skills must use strong, unambiguous language. Include:
- **REQUIRED/CRITICAL/STOP** markers for mandatory actions
- Explicit verification checkpoints
- Clear "do not proceed until X" gates
- Consequences of skipping steps

**NATURAL PROSE:** Skills producing external-facing content (marketing, website copy, case studies) must avoid AI-detectable writing patterns. Include explicit bans on AI vocabulary, formulaic structures, and promotional language (see BEST-PRACTICES.md).

## Before You Begin

**You must read the reference documentation before creating any skill:**

1. Read [references/SPEC.md](references/SPEC.md) to understand:
   - What skills are and how they differ from prompts
   - The three loading levels (metadata, instructions, resources)
   - Progressive disclosure and why it matters
   - Structure requirements and field limits

2. Read [references/BEST-PRACTICES.md](references/BEST-PRACTICES.md) to understand:
   - How to write concise, effective content
   - Setting appropriate freedom levels
   - Writing discoverable descriptions
   - Content patterns and anti-patterns

## Workflow

Copy this checklist and track progress:

```
Skill Creation Progress:
- [ ] Phase 1: Gather requirements
- [ ] Phase 2: Read reference docs
- [ ] Phase 3: Analyze source content
- [ ] Phase 4: Initialize skill structure
- [ ] Phase 5: Draft the skill
- [ ] Phase 6: Test and validate
- [ ] Phase 7: Create README
- [ ] Phase 8: Package and finalize
```

<phase_gather>
### Phase 1: Gather Requirements

Ask the user for:

1. **Purpose**: What capability should this skill provide?
2. **Target users**: Who will use this? (developers, writers, analysts, etc.)
3. **Inputs**: What will users provide? (files, data, requests)
4. **Outputs**: What should the skill produce?
5. **Context**: Any existing prompts, docs, or examples to convert?

Request any source materials:
- Existing prompts from `_prompts/` directory
- PDF documentation
- Text files with procedures
- Example inputs and outputs

Propose a skill name (lowercase, hyphens, gerund form preferred):
- `processing-pdfs` not `pdf-processor`
- `analyzing-data` not `data-analysis`
- `generating-reports` not `report-generator`

Name rules:
- 1-64 characters
- Lowercase letters, numbers, and hyphens only
- Cannot start or end with hyphen
- Cannot contain consecutive hyphens (`--`)

**GATE:** Before proceeding, write:
- "Skill name: [proposed-name]"
- "Purpose: [one sentence]"
- "Source materials: [list or 'none - creating from scratch']"
</phase_gather>

<phase_reference>
### Phase 2: Read Reference Documentation

**This step is mandatory.** Do not skip it.

Read the full content of:
- [references/SPEC.md](references/SPEC.md) - Understanding skill architecture
- [references/BEST-PRACTICES.md](references/BEST-PRACTICES.md) - Writing effective content

Key points to internalize:
- Only add context you (Claude) don't already have
- Description must be third person with trigger conditions
- Keep SKILL.md under 500 lines; use references/ folder for more
- Examples must show structure/format, not locked-in details

**GATE:** Before proceeding, confirm: "I have read SPEC.md and BEST-PRACTICES.md."
</phase_reference>

<phase_analyze>
### Phase 3: Analyze Source Content

If converting existing content (prompts, docs):

1. **Identify reusable patterns**
   - Workflows that apply across multiple uses
   - Domain-specific knowledge not in training data
   - Procedures with specific sequences

2. **Identify one-off content to remove**
   - Specific file names or paths
   - Dates or version numbers
   - Context specific to a single use case

3. **Determine structure**
   - Can it fit in under 500 lines? → Single SKILL.md
   - Needs detailed reference? → Add references/REFERENCE.md
   - Multiple domains? → Split into references/ files
   - Utility operations? → Add scripts/

**GATE:** Before proceeding, write:
- "Reusable patterns: [list]"
- "Content to remove: [list or 'N/A - no source content']"
- "Structure: [single file / split into references]"
</phase_analyze>

<phase_init>
### Phase 4: Initialize Skill Structure

Use the init script to create the standard directory structure:

```bash
python scripts/init_skill.py <skill-name> --path skills
```

This creates:
```
skills/<skill-name>/
├── SKILL.md           # Main instructions (template)
├── references/        # For additional documentation
│   └── REFERENCE.md   # Placeholder reference file
└── scripts/           # For utility scripts
```
</phase_init>

<phase_draft>
### Phase 5: Draft the Skill

#### Write the Frontmatter

```yaml
---
name: skill-name
description: [Third person. What it does. When to use it. Include keywords.]
---
```

Optional frontmatter fields:
- `license`: License terms (e.g., "MIT", "Apache-2.0")
- `compatibility`: Environment prerequisites (max 500 chars)
- `metadata`: Arbitrary key-value pairs
- `allowed-tools`: Pre-approved tools (experimental)

Description requirements:
- Third person ("Processes..." not "I process...")
- States what the skill does
- States when to use it (trigger conditions)
- Includes keywords users might say
- Covers content delivery variations (pasted, attached, uploaded, inline)
- Handles accompanying context files if relevant
- Under 1024 characters
- No angle brackets (< or >)

#### Write the Body

Structure for most skills:

```markdown
# Skill Title

<purpose>
[Why this skill exists - what Claude tendency it addresses or what capability it provides]
</purpose>

## Critical Rules
[REQUIRED: Sourcing discipline, epistemic calibration, professional challenge, and adherence rules specific to this skill]

## Quick Start
[Most common use case - get users productive fast]

## Workflow

<phase_gather>
### Phase 1: [Name]
[Instructions]

**GATE:** Before proceeding, write: "[commitment statement]"
</phase_gather>

<phase_execute>
### Phase 2: [Name]
[Instructions]

**GATE:** [Next commitment or checkpoint]
</phase_execute>

## Anti-Patterns

<failed_attempts>
What DOESN'T work:
- **[Wrong approach]:** [Why it fails]
</failed_attempts>

## Examples
[Show structure/format with generic details - avoid company names, specific numbers, or domain content that could bleed into unrelated outputs]

## Additional Resources
[Links to files in references/ folder if needed]
```

Writing guidelines:
- **ALWAYS include a Critical Rules section** with skill-specific behavioral guardrails
- **Use `<purpose>` tags** for skills that counteract Claude's default behaviors
- **Use XML tags for phase boundaries** (`<phase_name>`) in multi-step workflows
- **Use commitment gates** that require Claude to write a statement before proceeding
- **Include `<failed_attempts>` section** documenting what doesn't work
- Lead with Quick Start (most common case)
- Be concise - you're smart, skip obvious explanations
- Use appropriate freedom level (high/medium/low)
- Include examples showing structure/format (avoid locked-in details that bleed through)
- Link to references/ files for detailed content
- **For skills producing reports/documents**: Add an Output Requirements section specifying file output vs inline

See [references/BEST-PRACTICES.md](references/BEST-PRACTICES.md) for detailed guidance on structured patterns, commitment gates, and XML boundaries.

#### Critical Rules Section (REQUIRED)

Every skill MUST have a Critical Rules section near the top. Structure rules as process gates — upstream requirements that prevent failure — not named failure modes to monitor.

**Sourcing discipline (always include for content-generating skills):**
```markdown
**SOURCING:** Before stating any claim, locate its source in [source type]. Cite the source when stating the claim. Scope the claim to what the source supports. If you cannot locate a source, say what's missing and where to find it.
```

**Epistemic calibration (always include for content-generating skills):**
```markdown
**EPISTEMIC CALIBRATION:** The reader should always be able to tell whether they're receiving a sourced claim, a logical extension, or your analysis — because your language makes the distinction legible. This is a language discipline, not a formatting rule.
```

**Professional challenge (always include for advisory/analytical skills):**
```markdown
**PROFESSIONAL CHALLENGE:** When a request contradicts documented strategy, when an approach has known pitfalls, or when an assumption isn't supported by sources — cite the concern, offer an alternative. Accuracy over agreement.
```

**Instruction Adherence Rules (always include for multi-step workflows):**
```markdown
**REQUIRED/CRITICAL** — Use these markers for mandatory actions
**GATE:** — Commitment checkpoints requiring Claude to write a statement before proceeding
**STOP.** — Hard stops requiring explicit user approval
**VERIFICATION** — "Before proceeding, verify X"
```

**Destructive Action Gates (for skills that delete or overwrite):**
```markdown
**GATE:** Before [action], write:
- "I am about to [action]: [specifics]"
- "This is intentional because: [reason]"

**STOP.** Get explicit user confirmation before executing.
```

**GATE:** Before proceeding to testing, confirm:
- "SKILL.md drafted with: [list sections included]"
- "Description is third-person with triggers: [yes/no]"
- "Critical Rules section included: [yes/no]"
</phase_draft>

<phase_test>
### Phase 6: Test and Validate

Testing happens in two stages: **structural validation** (automated scripts) and **functional testing** (parallel session testing with real prompts).

#### Stage 1: Structural Validation

Run all validation scripts in sequence:

**1. Structure Validation**
```bash
python scripts/validate.py /path/to/new-skill
```
Fix any errors before proceeding.

**2. Description Quality**
```bash
python scripts/test-description.py /path/to/new-skill "expected trigger phrase"
```
Verify:
- Third-person voice
- Trigger conditions present
- Keywords match expected phrases

**3. Example Verification**
```bash
python scripts/test-examples.py /path/to/new-skill
```
Ensure:
- Examples section exists
- No placeholder patterns
- Concrete input/output pairs

**4. Full Simulation**
```bash
python scripts/dry-run.py /path/to/new-skill "test prompt"
```
Review:
- Token estimates are reasonable
- File references exist
- Trigger matching works

#### Stage 2: Functional Testing (Parallel Sessions)

Structural validation checks that the skill is well-formed. Functional testing checks that it **produces quality output**.

**The process:**

1. **Create test prompts** — Design 2-3 prompts that exercise the skill:
   - Simple case: The most common use case
   - Complex case: Edge cases, multiple inputs, or advanced features
   - Boundary case: Ambiguous inputs that test decision-making

2. **Run in parallel session** — Open a separate Claude session and run the skill with your test prompts. Keep the skill-building session open.

3. **Review output** — In the skill-building session, read and audit the output:
   - Did the skill follow the workflow correctly?
   - Is the output quality acceptable?
   - Were decisions documented appropriately?
   - What's missing or could be improved?

4. **Iterate** — Based on findings, update the skill and re-test:
   ```
   Test → Review → Fix → Re-test
   ```

5. **Document test results** — Note what was tested and what changes were made.

**Test prompt design tips:**

| Test Type | What It Validates | Example |
|-----------|-------------------|---------|
| Simple | Basic workflow executes correctly | Single input, happy path |
| Complex | Multi-step workflows, edge cases | Multiple inputs, dependencies |
| Boundary | Decision-making under ambiguity | Incomplete info, unclear requirements |

**What to look for during review:**

- Did the skill ask for clarification when needed?
- Did it follow checkpoints and get approval?
- Is the output format correct?
- Are decisions documented appropriately?
- Did it handle edge cases gracefully?
- What guidance would have prevented any issues?

See [references/BEST-PRACTICES.md](references/BEST-PRACTICES.md) for detailed functional testing methodology.

#### Validation Loop

```
1. Run structural validation scripts
2. Fix any errors
3. Run functional tests in parallel session
4. Review output in skill-building session
5. If issues found:
   - Update skill
   - Return to step 1
6. Only proceed when both stages pass
```

**GATE:** Before proceeding, confirm:
- "Validation scripts pass: [yes/no]"
- "Functional tests completed: [list test types run]"
- "Issues found and fixed: [list or 'none']"
</phase_test>

<phase_readme>
### Phase 7: Create README

Create a user-facing README.md in the skill directory. This file helps users understand how to use the skill when browsing the GitHub repository.

**README.md structure:**

```markdown
# [Skill Title]

[One sentence describing what this skill does.]

## When to Use

Use this skill when you need to:
- [Primary use case]
- [Secondary use case]
- [Additional use case if applicable]

## How to Invoke

Say things like:
- "[Example trigger phrase 1]"
- "[Example trigger phrase 2]"
- "[Example trigger phrase 3]"

## What You'll Need

- [Required input 1 - e.g., "A transcript file (any format: SRT, VTT, plain text)"]
- [Required input 2 if applicable]
- [Optional input with "(optional)" suffix]

## What You'll Get

[Describe the output - what file(s) are created, what format, where they're saved.]

## Example

**Input:** [Brief description of example input]

**Output:** [Brief description of what the skill produces]

## Tips

- [Helpful tip 1 for getting better results]
- [Helpful tip 2]
```

**Guidelines:**
- Write for humans browsing GitHub, not for Claude
- Keep it concise - users should understand the skill in 30 seconds
- Use concrete examples from the skill's actual capabilities
- "How to Invoke" should use natural language triggers, not slash commands
- Don't duplicate the full SKILL.md content - this is a quick reference
</phase_readme>

<phase_finalize>
### Phase 8: Package and Finalize

Present the complete skill to the user:
- Show SKILL.md content
- Show README.md content
- Explain any additional files
- Note any trade-offs or decisions made

Get user approval, then package for distribution:

```bash
python scripts/package_skill.py /path/to/new-skill --output dist
```

This creates a zip file ready for:
- Upload to Claude.ai (Settings > Features > Skills)
- Distribution to other users
- Extraction to `~/.claude/skills/` for local use
</phase_finalize>

## File Reference

This skill includes:

| File | Purpose |
|------|---------|
| [references/SPEC.md](references/SPEC.md) | Agent Skills specification |
| [references/BEST-PRACTICES.md](references/BEST-PRACTICES.md) | Writing effective skills |
| [references/EXAMPLES.md](references/EXAMPLES.md) | Before/after conversion examples |
| [scripts/init_skill.py](scripts/init_skill.py) | Initialize new skill directory |
| [scripts/validate.py](scripts/validate.py) | Structure validation |
| [scripts/test-description.py](scripts/test-description.py) | Description quality testing |
| [scripts/test-examples.py](scripts/test-examples.py) | Example verification |
| [scripts/dry-run.py](scripts/dry-run.py) | Full loading simulation |
| [scripts/package_skill.py](scripts/package_skill.py) | Package skill for distribution |

<failed_attempts>
## What DOESN'T Work

- **Vague descriptions:** "Helps with documents" won't trigger. Include specific trigger conditions: "Use when working with X" or "Activates when Y is provided."

- **Locked-in example details:** Examples should show structure/format, not specific content that gets copied into unrelated outputs. Show the *shape* of output without company names, specific numbers, or domain details that bleed through.

- **Skipping reference docs:** Creating skills without reading SPEC.md and BEST-PRACTICES.md produces verbose, poorly-structured skills that waste tokens.

- **Long SKILL.md files:** Over 500 lines means you're including content that should be in references/. Split by domain or move detailed reference content.

- **Weak constraint language:** "You might consider" and "feel free to" get ignored. Use "REQUIRED," "Do not proceed until," and commitment gates.

- **Missing behavioral guardrails:** Skills without Critical Rules sections produce hallucinated content and skip verification steps.
</failed_attempts>

## Common Issues

**"Description too vague"**
→ Add specific trigger conditions: "Use when working with X" or "Use for Y tasks"

**"SKILL.md too long"**
→ Move detailed content to references/ folder or split by domain.

**"Skill doesn't trigger"**
→ Add more keywords to description that match how users phrase requests.

**"Referenced file not found"**
→ Check path is relative to skill directory, uses forward slashes.

**"Name validation failed"**
→ Ensure name is lowercase, uses hyphens (not underscores), doesn't start/end with hyphen.
