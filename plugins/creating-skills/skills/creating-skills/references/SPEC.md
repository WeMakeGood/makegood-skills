# Agent Skills Specification

This document explains what Agent Skills are, how they work, and their technical requirements. Read this before creating any skill.

## What Are Agent Skills

Agent Skills are modular capabilities that extend Claude's functionality. Each skill is a **directory** containing instructions, metadata, and optional resources (scripts, templates, reference files) that Claude uses automatically when relevant.

**Skills vs Prompts:**
- **Prompts** are conversation-level instructions for one-off tasks
- **Skills** are reusable, filesystem-based resources that load on-demand across conversations

Skills package domain expertise - workflows, context, and best practices - that transform Claude from a general-purpose assistant into a specialist for specific tasks.

## How Skills Work: Three Loading Levels

Skills use **progressive disclosure** to minimize context window usage. Content loads in stages:

### Level 1: Metadata (Always Loaded)

At startup, Claude loads only the `name` and `description` from every skill's YAML frontmatter:

```yaml
---
name: processing-pdfs
description: Extracts text and tables from PDF files, fills forms, merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---
```

**Token cost:** ~100 tokens per skill
**Purpose:** Discovery - Claude uses this to decide which skill to invoke

### Level 2: Instructions (Loaded When Triggered)

When a user request matches a skill's description, Claude reads the SKILL.md body:

```markdown
# Processing PDFs

## Quick Start
[Primary use case instructions]

## Workflows
[Step-by-step procedures]
```

**Token cost:** Target under 5,000 tokens (under 500 lines recommended)
**Purpose:** Core instructions for completing the task

### Level 3: Resources (Loaded As Needed)

Skills can bundle additional files that Claude reads only when referenced:

```
processing-pdfs/
├── SKILL.md           # Level 2 - loaded when triggered
├── references/        # Level 3 - documentation folder
│   ├── FORMS.md       # Loaded if form filling needed
│   └── REFERENCE.md   # Loaded for API details
└── scripts/
    └── validate.py    # Level 3 - executed, output returned
```

**Token cost:** Effectively unlimited (loaded on-demand)
**Purpose:** Detailed reference, specialized workflows, utility scripts

### How Scripts Work

Scripts in a skill are **executed via bash**, not read into context. Claude runs the script and receives only its output:

```bash
python scripts/validate.py input.pdf
# Output: "Valid PDF with 3 form fields: name, date, signature"
```

This is efficient - complex validation logic stays in the script, only results consume tokens.

## Progressive Disclosure Pattern

The context window is a shared resource. Every token in your skill competes with:
- System prompt
- Conversation history
- Other skills' metadata
- The user's actual request

**Progressive disclosure ensures only relevant content loads:**

1. Metadata always present (lightweight discovery)
2. SKILL.md loads only when skill is triggered
3. Referenced files load only when that specific content is needed
4. Scripts execute without loading code into context

### File Reference Pattern

Keep references **one level deep** from SKILL.md:

**Good:**
```markdown
# SKILL.md
See [FORMS.md](FORMS.md) for form filling instructions.
See [REFERENCE.md](REFERENCE.md) for API details.
```

**Bad (nested references):**
```markdown
# SKILL.md
See [advanced.md](advanced.md)...

# advanced.md
See [details.md](details.md)...  # Claude may not follow this

# details.md
The actual information...
```

When Claude encounters nested references, it may partially read files or miss content entirely.

## Skill Structure Requirements

### Directory Structure

Every skill is a directory containing at minimum a `SKILL.md` file:

```
skill-name/
└── SKILL.md
```

Multi-file skills organize resources in standard folders:

```
skill-name/
├── SKILL.md           # Required - main instructions
├── references/        # Optional - additional documentation
│   ├── REFERENCE.md   # Detailed API/schema reference
│   └── EXAMPLES.md    # Extended examples
├── scripts/           # Optional - utility scripts
│   └── utility.py
└── assets/            # Optional - output templates, images
    └── template.docx
```

### YAML Frontmatter

SKILL.md must begin with YAML frontmatter containing `name` and `description`:

```yaml
---
name: skill-name
description: What this skill does and when to use it.
---
```

### Field Requirements

#### Required Fields

**name:**
- 1-64 characters
- Lowercase letters, numbers, and hyphens only
- Cannot start or end with a hyphen
- Cannot contain consecutive hyphens (`--`)
- No spaces or underscores
- Cannot contain reserved words: "anthropic", "claude"
- Must match the directory name

**description:**
- 1-1,024 characters
- Cannot contain angle brackets (`<` or `>`)
- Must be third person (see Best Practices)
- Should include trigger conditions and keywords for discovery

#### Optional Fields

**license:**
- Specifies licensing terms for the skill
- Example: `license: MIT` or `license: Apache-2.0`

**compatibility:**
- 1-500 characters
- Documents environment prerequisites
- Example: `compatibility: Requires Python 3.9+, pdfplumber package`

**metadata:**
- Arbitrary key-value string pairs for additional properties
- Example: `metadata: { author: "Team Name", version: "1.0" }`

**allowed-tools:**
- Space-delimited list of pre-approved tools (experimental feature)
- Example: `allowed-tools: read write bash`

### SKILL.md Body

- Recommended: under 500 lines
- If content exceeds this, split into referenced files
- Use markdown formatting
- Include concrete examples, not abstract placeholders

## Discovery Mechanism

Claude decides whether to use a skill by matching the user's request against skill descriptions. This happens automatically - users don't invoke skills by name.

**How matching works:**
1. User sends a request: "Extract the text from this PDF"
2. Claude scans skill descriptions in the system prompt
3. Description "Extracts text and tables from PDF files..." matches
4. Claude reads that skill's SKILL.md
5. Claude follows the skill's instructions to complete the task

**Why trigger conditions matter:**

A vague description like "Helps with documents" won't match specific requests. A specific description with trigger conditions matches reliably:

```yaml
# Bad - too vague
description: Helps with documents

# Good - specific with triggers
description: Extracts text and tables from PDF files, fills forms, merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

## Where Skills Run

Skills work across Claude's products with some differences:

### Claude Code
- Filesystem access to skill directories
- Can execute scripts via bash
- Skills in `~/.claude/skills/` (personal) or `.claude/skills/` (project)

### Claude API
- Upload skills via `/v1/skills` endpoints
- Skills shared organization-wide
- No network access in execution environment
- Only pre-installed packages available

### Claude.ai
- Upload as zip files through Settings > Features
- Individual to each user (not shared)
- Network access depends on user/admin settings
- **Has filesystem access**: Skills can write output to files, not just inline chat
- Skills may require a new conversation to load after uploading/updating

### Claude Agent SDK
- Place skills in `.claude/skills/` directory
- Enable via `allowed_tools` configuration
- Filesystem-based, automatically discovered

## Security Considerations

Skills provide Claude with new capabilities through instructions and code. Only use skills from trusted sources.

**Risks of untrusted skills:**
- Malicious instructions directing Claude to harmful actions
- Scripts that exfiltrate data or access unauthorized systems
- External URL fetches that inject malicious content

**Before using any skill:**
- Review all files: SKILL.md, scripts, resources
- Check for unexpected network calls or file access
- Verify operations match the skill's stated purpose
