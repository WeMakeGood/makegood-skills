# Best Practices for Writing Skills

This document covers how to write effective skills that Claude can discover and use successfully. Read this before drafting any skill content.

## Core Principle: Be Concise

The context window is a shared resource. Your skill competes for tokens with conversation history, other skills, and the user's request.

**Default assumption:** Claude is already very smart.

Only add context Claude doesn't have:
- Domain-specific workflows and procedures
- Company or team conventions
- Specialized schemas, APIs, or data structures
- Knowledge that isn't in Claude's training data

**Challenge each piece of content:**
- "Does Claude really need this explanation?"
- "Can I assume Claude knows this?"
- "Does this paragraph justify its token cost?"

### Example: Concise vs Verbose

**Good (concise, ~50 tokens):**
```markdown
## Extract PDF Text

Use pdfplumber for text extraction:

```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
```

**Bad (verbose, ~150 tokens):**
```markdown
## Extract PDF Text

PDF (Portable Document Format) files are a common file format that contains
text, images, and other content. To extract text from a PDF, you'll need to
use a library. There are many libraries available for PDF processing, but we
recommend pdfplumber because it's easy to use and handles most cases well.
First, you'll need to install it using pip. Then you can use the code below...
```

The concise version assumes Claude knows what PDFs are and how pip works.

## Setting Freedom Levels

Match instruction specificity to the task's fragility and variability.

### High Freedom (Text Guidance)

Use when multiple approaches are valid and context determines the best path.

```markdown
## Code Review Process

1. Analyze the code structure and organization
2. Check for potential bugs or edge cases
3. Suggest improvements for readability
4. Verify adherence to project conventions
```

Claude decides how to apply these guidelines based on the specific code.

### Medium Freedom (Templates/Pseudocode)

Use when a preferred pattern exists but some variation is acceptable.

```markdown
## Generate Report

Use this template structure, customize as needed:

```python
def generate_report(data, format="markdown"):
    # Process and validate data
    # Generate output in specified format
    # Include summary statistics
```
```

### Low Freedom (Exact Scripts)

Use when operations are fragile, error-prone, or must follow an exact sequence.

```markdown
## Database Migration

Run exactly this command:

```bash
python scripts/migrate.py --verify --backup
```

Do not modify flags or add parameters.
```

## Script Paths and Execution

When your skill includes utility scripts, use **relative paths from the skill directory**.

### Correct Path Format

```markdown
## Run the Scraper

```bash
python3 scripts/scrape_website.py https://example.org --output ./tmp/example
```
```

Claude executes scripts from the skill directory, so `scripts/` resolves correctly.

### Incorrect Path Formats

```markdown
# Bad - placeholder that Claude must interpret
python3 <skill_dir>/scripts/scrape.py

# Bad - absolute path that won't work across systems
python3 /Users/me/.claude/skills/my-skill/scripts/scrape.py

# Bad - trying to navigate from project root
python3 .claude/skills/my-skill/scripts/scrape.py
```

### Make Script Execution Mandatory

If scripts produce better results than Claude doing the work manually, be explicit:

```markdown
# Good - directive language
**ALWAYS run the scraper script first.** It produces better results than manual web fetching.

```bash
python3 scripts/scrape_website.py <URL> --output ./tmp/<name>
```

**Fallback (only if script fails):** Use web_fetch manually.

# Bad - optional language causes Claude to skip scripts
If scripts are available, you can run:
```bash
python3 scripts/scrape_website.py <URL>
```
Or use web_fetch instead.
```

With optional language, Claude may choose the "easier" path (web_fetch) even though the script produces better results.

### The Bridge Analogy

Think of Claude navigating a path:

- **Narrow bridge with cliffs:** Only one safe way forward. Provide exact instructions, specific scripts, explicit guardrails. Example: database migrations, financial calculations.

- **Open field:** Many paths lead to success. Give general direction and trust Claude to find the best route. Example: code reviews, content writing.

## Writing Effective Descriptions

The description is the most important part of your skill. It determines whether Claude discovers and uses the skill.

### Must Be Third Person

The description is injected into Claude's system prompt. Inconsistent voice causes discovery problems.

```yaml
# Good - third person
description: Extracts text from PDF files and converts to markdown.

# Bad - first person
description: I can help you extract text from PDF files.

# Bad - second person
description: You can use this to extract text from PDF files.
```

### Include What AND When

Describe both the capability and the trigger conditions:

```yaml
# Good - includes triggers
description: Extracts text and tables from PDF files, fills forms, merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.

# Bad - no trigger conditions
description: Processes PDF files.
```

### Include Keywords for Discovery

Think about what users will say when they need this skill:

```yaml
# Good - multiple keywords
description: Analyzes Excel spreadsheets, creates pivot tables, generates charts. Use when analyzing Excel files, spreadsheets, tabular data, .xlsx files, or CSV data.

# Bad - limited keywords
description: Works with Excel.
```

### Cover Content Delivery Variations

Users provide content in different ways. Include variations in your description:

```yaml
# Good - covers delivery methods
description: Generates meeting reports from transcripts. Activates when transcript content is present via pasted text, inline content, attached file, or uploaded document.

# Bad - assumes one delivery method
description: Generates meeting reports from attached transcripts.
```

Key delivery terms to consider:
- pasted, inline, provided, included
- attached, uploaded, file
- document, content, text

### Handle Accompanying Context

Users often provide additional context files alongside the main input. Mention this explicitly:

```yaml
# Good - acknowledges context files
description: Analyzes sales data and generates reports. Activates when data is provided, even when accompanied by additional context files or reference materials.

# Bad - may not trigger with multiple files
description: Analyzes sales data files.
```

### Good vs Bad Descriptions

| Bad | Good |
|-----|------|
| Helps with documents | Extracts text from PDF files, fills form fields, merges multiple PDFs. Use when working with PDF documents. |
| Processes data | Analyzes CSV and Excel files, generates summary statistics, creates visualizations. Use for data analysis tasks. |
| Code helper | Reviews Python code for bugs, security issues, and style violations. Use when reviewing or improving Python code. |

## Content Patterns

### Quick Start Pattern

Lead with the most common use case:

```markdown
## Quick Start

Extract text from a PDF:

```python
import pdfplumber
with pdfplumber.open("doc.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## Advanced Usage

For form filling, see [FORMS.md](FORMS.md).
For batch processing, see [BATCH.md](BATCH.md).
```

### Workflow Pattern with Checklist

For multi-step processes, provide a checklist Claude can track:

```markdown
## Document Processing Workflow

Copy this checklist and mark items as you complete them:

```
Progress:
- [ ] Step 1: Validate input file
- [ ] Step 2: Extract content
- [ ] Step 3: Transform to target format
- [ ] Step 4: Validate output
- [ ] Step 5: Save results
```

### Step 1: Validate Input
[Instructions...]

### Step 2: Extract Content
[Instructions...]
```

### Validation Loop Pattern

For quality-critical tasks, enforce validation:

```markdown
## Generating Output

1. Create the output file
2. Run validation: `python scripts/validate.py output.json`
3. If validation fails:
   - Review error messages
   - Fix issues in the output
   - Return to step 2
4. Only proceed when validation passes
5. Deliver the validated output
```

### Conditional Workflow Pattern

Guide Claude through decision points:

```markdown
## Document Modification

First, determine the task type:

**Creating new content?**
→ Use the creation workflow in [CREATE.md](CREATE.md)

**Editing existing content?**
→ Use the editing workflow below

## Editing Workflow
1. Load the existing document
2. Parse the structure
3. Apply modifications
4. Validate changes
5. Save the updated document
```

### Output Requirements Pattern

For skills that produce substantial output, explicitly specify where and how to deliver it. Without this, Claude may output inline (in chat) or to a file inconsistently.

```markdown
## Output Requirements

**ALWAYS save the report to a file. Do not output inline in chat.**

1. Generate filename: `analysis-YYYY-MM-DD.md` (use current date)
2. Write the complete output to this file
3. After saving, confirm: "Report saved to `[filename]`" with brief summary

If date is unknown, use current date or ask the user.
```

When to use this pattern:
- Reports, summaries, or documents users will want to keep
- Structured output following a template
- Content longer than a few paragraphs
- Output that users may want to edit or share

For short responses (answers, explanations), inline output is fine and no explicit instruction is needed.

## Progressive Disclosure in Practice

### When to Split into Multiple Files

Split when SKILL.md exceeds 500 lines, or when content is only needed for specific subtasks:

```
my-skill/
├── SKILL.md           # Overview, quick start, common workflows
├── REFERENCE.md       # Detailed API documentation
├── ADVANCED.md        # Complex edge cases
└── scripts/
    └── validate.py    # Validation utility
```

### Organizing by Domain

For skills covering multiple domains, organize to minimize unnecessary loading:

```
data-analysis/
├── SKILL.md
└── schemas/
    ├── finance.md     # Revenue, billing schemas
    ├── sales.md       # Pipeline, opportunities
    └── product.md     # Usage metrics
```

When the user asks about sales data, Claude loads only `schemas/sales.md`.

### Table of Contents for Long Files

For reference files over 100 lines, add a TOC:

```markdown
# API Reference

## Contents
- Authentication
- Core Methods
- Error Handling
- Examples

## Authentication
[Content...]

## Core Methods
[Content...]
```

Claude can scan the TOC and jump to relevant sections.

## Structured Skill Patterns

Skills benefit from explicit structure that creates hard boundaries between phases and forces commitment before proceeding. Markdown alone can be too loose—Claude may skip steps or blur phase boundaries.

### Purpose Statement Pattern

For skills that address a specific Claude failure mode, open with a `<purpose>` tag explaining why the skill exists:

```markdown
<purpose>
Claude's default behavior is to [problematic pattern]. This skill exists because
[why that pattern causes problems]. The skill addresses this by [how].
</purpose>
```

This metacognitive framing helps Claude understand not just *what* to do, but *why* it needs to override its defaults.

**Example:**
```markdown
<purpose>
Claude generates content by pattern-matching on training data. Something can look
polished and professional while being factually hollow. This skill exists because
case studies require verifiable proof, not plausible-sounding narratives. The skill
addresses this by requiring source citations for every claim.
</purpose>
```

**When to use:** Skills that counteract Claude's natural tendencies (verification, skepticism, restraint).

### XML Tags for Phase Boundaries

Use XML tags to create hard boundaries between workflow phases. Claude treats tagged sections as distinct units, reducing the tendency to blur phases together or skip ahead.

```markdown
<phase_gather>
## Phase 1: Gather Requirements

[Instructions for this phase]

**GATE:** Do not proceed until [specific condition].
</phase_gather>

<phase_analyze>
## Phase 2: Analyze Content

[Instructions for this phase]

**GATE:** Do not proceed until [specific condition].
</phase_analyze>
```

**When to use:** Multi-phase workflows where order matters and skipping steps causes problems.

**Naming convention:** Use `<phase_[name]>` for workflow phases, `<[domain]_[type]>` for other bounded sections (e.g., `<technical_honesty>`, `<failed_attempts>`).

### Commitment Gates

Gates that require Claude to write a specific statement before proceeding are more effective than simple "STOP" markers. Writing creates commitment.

**Weak gate (may be skipped):**
```markdown
**STOP.** Get user approval before proceeding.
```

**Strong gate (requires commitment):**
```markdown
**GATE:** Before proceeding, write the following:

"Problem statement: When I [action], I expect [expected], but instead [actual]."

Do not proceed until you have written this statement.
```

**Gate patterns:**

| Gate Type | When to Use | Example Commitment |
|-----------|-------------|-------------------|
| Problem definition | Before investigating | "The issue is [X] because [evidence]" |
| Plan confirmation | Before implementing | "I will [action] which addresses [requirement]" |
| Verification | Before declaring done | "Verified: [what was tested] showed [result]" |
| Destructive action | Before deleting/overwriting | "I am about to delete [X]. This is intentional because [reason]" |

### Anti-Patterns Section (Failed Attempts)

Document what doesn't work. This is especially valuable for skills addressing counter-intuitive problems.

```markdown
<failed_attempts>
What DOESN'T work:

- **[Wrong approach]:** [Why it fails]
- **[Common mistake]:** [What happens when Claude does this]
- **[Tempting shortcut]:** [Why it causes problems]
</failed_attempts>
```

**Example:**
```markdown
<failed_attempts>
What DOESN'T work:

- **"I'll verify later":** Later never comes. Verification must happen immediately.
- **"It looks correct":** Pattern-matching is not verification. Code that looks perfect can be wrong.
- **Trusting compilation:** Types compile doesn't mean logic is correct.
- **Testing only happy path:** The bug is in the edge case you didn't test.
</failed_attempts>
```

**When to use:** Skills where Claude's intuitive approach is wrong, or where common shortcuts cause failures.

### Emotional/Linguistic Triggers in Descriptions

Descriptions can match on user emotional state, not just task keywords:

```markdown
description: |
  When debugging frustration appears ("why isn't this working?", "it should work",
  "I don't understand"), [what the skill does].
```

This improves discovery for users who are stuck, not just users who know what they need.

**Trigger phrase categories:**
- Frustration: "why isn't this working", "it should work", "I don't understand"
- Uncertainty: "I'm not sure if", "should I", "what's the best way"
- Caution: "I don't want to break", "is it safe to", "before I delete"

## Behavioral Guardrails (REQUIRED)

Every skill must include behavioral guardrails. Structure them as **process gates** — upstream steps that make failure modes architecturally difficult — rather than naming failure modes and telling Claude to monitor for them.

The difference: "Never hallucinate" names a failure and hopes it's avoided. "Before stating a claim, locate its source in your context" requires a step that prevents the failure from occurring. Write the second kind.

### Sourcing Discipline

Skills that generate content must require source-before-statement — locating the source before making a claim.

**Always include:**
- What sources Claude can use: "Base content ONLY on [transcript/documents/user input]"
- A process requirement: "Before stating a claim, locate its source. Cite the source. Scope the claim to what the source supports."
- What to do when source is missing: "If you cannot locate a source, say what information is missing and where to find it"

**Example Critical Rules section:**
```markdown
## Critical Rules

**SOURCING:** Before stating any claim about the organization, locate its source in the provided documents. Cite the source when stating the claim. If you cannot locate a source, state what's missing rather than approximating.
```

### Epistemic Calibration

Skills must ensure the language itself signals the epistemic status of each claim — not through prescribed bracket markers, but through language that makes the distinction legible.

**Always include:**
- A requirement that readers can distinguish sourced claims from inferences from analysis
- Frame as a language discipline, not a formatting convention

**Example Critical Rules section:**
```markdown
## Critical Rules

**EPISTEMIC CALIBRATION:** The reader should always be able to tell whether they're receiving a sourced claim, a logical extension, or your analysis — because your language makes that distinction clear. When information is missing, name the gap rather than approximating around it.
```

### Professional Challenge

Skills that advise or analyze must prioritize accuracy over agreement.

**Always include:**
- When to challenge: contradicts documented strategy, known pitfalls, unsupported assumptions
- How to challenge: cite the specific concern, offer an alternative
- Frame as a process requirement, not a personality trait

**Example Critical Rules section:**
```markdown
## Critical Rules

**PROFESSIONAL CHALLENGE:** When a request contradicts documented strategy, when an approach has known pitfalls given the context, or when an assumption isn't supported by sources — cite the concern, offer an alternative. Accuracy over agreement.
```

### Lateral Thinking Patterns

Skills that analyze, advise, or synthesize benefit from encouraging cross-domain reasoning. LLMs default to the most statistically common associations for a domain — explicitly encouraging lateral thinking activates reasoning pathways the model can follow but won't take unprompted.

**When to include:**
- Strategy, analysis, or advisory skills → Always
- Synthesis skills (interviews, research) → Recommended
- Mechanical/procedural skills (file conversion, data extraction) → Skip

**Always include:**
- Permission to look beyond the obvious domain: "Consider parallels from other industries or disciplines"
- Requirement to ground analogies: "Mark novel framings as such; never invent supporting evidence"
- Encouragement to question framings: "Before accepting the first framing, consider whether a less obvious lens would be more useful"

**Additional patterns (include when the skill involves strategy, analysis, or synthesis):**
- Convergence awareness: "When two lines of inquiry intersect, explore the intersection rather than noting it and moving on"
- Second-order thinking: "Push past first-order conclusions — what does this create, constrain, or obscure?"
- Contextual sourcing: "When referencing a framework, bring its context — what question it was designed to answer, and whether that matches the current situation"
- Premature commitment check: "When stakes are high, enumerate alternative framings before committing to one. If you've already started down a path without considering others, flag it"

**Example Critical Rules section:**
```markdown
## Critical Rules

**ANALYTICAL DEPTH:** Don't default to the most obvious framework. Consider cross-domain parallels, alternative framings, and less common mental models when they would produce better insight. Mark novel analogies as such.

**SECOND-ORDER THINKING:** Don't stop at first-order conclusions. Push on what a conclusion creates, constrains, or obscures. Name both what an insight enables and what it blinds.

**CONTEXTUAL SOURCING:** When referencing a framework or model, bring its context — what question it was designed to answer and whether that question matches the current situation.

**PREMATURE COMMITMENT CHECK:** When stakes are high, enumerate alternative framings before committing to one. If you've already started down a path without considering others, flag it.

**GROUNDED REASONING:** Lateral thinking must stay grounded in real patterns. Speculative connections presented as established fact are hallucination, not insight.
```

### Example Anchoring

Examples in skill instructions don't just illustrate — they anchor. An LLM encountering a specific example will gravitate toward that pattern even when the instruction says "consider alternatives" or labels it as what *not* to do. This is a form of premature commitment that operates at the instruction layer rather than the reasoning layer.

**The core problem:** When a skill includes a concrete example, the model treats it as a template. A Wrong/Right pair intended to demonstrate a *principle* becomes a pattern to reproduce. If the "Right" example shows a specific domain transformation, the model will apply that transformation's shape to unrelated domains rather than reasoning from the principle.

**Rules for skill authors:**

1. **Prefer structural examples over content-specific ones.** Show the *shape* of good output (format, section structure, decision flow) rather than domain-specific content. Structural examples anchor on form; content examples anchor on substance.

2. **When domain-specific examples are necessary, use more than one.** A single example creates a template. Two or three examples from different domains illustrate a range, signaling that the principle — not the specific application — is what matters.

3. **Don't make examples more specific than the principle they illustrate.** If the principle is "question the obvious behavioral instruction," an example that shows one specific transformation narrows the model's thinking to that transformation's domain. Either keep the example at the same level of abstraction as the principle, or include enough variation to prevent fixation.

4. **Wrong/Right pairs are high-risk.** The "Right" version becomes the default template regardless of context. If you use Wrong/Right, make the "Right" version abstract enough that it demonstrates the reasoning, not a specific output pattern. Or use multiple "Right" versions to show that the principle has many valid expressions.

5. **Watch for anchoring in behavioral guardrails.** Guardrail examples are especially prone to anchoring because they're loaded into every session. An example meant to demonstrate epistemic honesty will shape how the model expresses uncertainty across all domains — which may be desirable for the pattern but constraining if the specific wording becomes a template.

**Self-check for skill authors:** After writing an example, ask: "If the model encounters a completely different domain, will this example help it apply the principle, or will it reproduce this specific pattern?" If the latter, generalize or diversify.

### Instruction Adherence Patterns

Skills with multi-step workflows must use strong, unambiguous language and commitment mechanisms.

**Use these markers:**
- `**REQUIRED:**` — Actions that must be taken
- `**CRITICAL:**` — Rules that must not be violated
- `**GATE:**` — Checkpoints requiring written commitment before proceeding
- `**STOP.**` — Hard stops requiring user approval
- `**VERIFICATION:**` — Confirmation steps before proceeding
- `**Do not:**` — Explicit prohibitions

**Weak vs Strong Language:**
```markdown
# Weak (may be ignored)
You might consider running the validation script.
If you'd like, you can ask for approval before proceeding.

# Strong (will be followed)
**REQUIRED:** Run the validation script before proceeding.
**STOP.** Get explicit user approval. Do not proceed until confirmed.
```

**Commitment gates (strongest):**
```markdown
**GATE:** Before proceeding, write:
- "I have read all [N] source files: [list them]"
- "The main conflict identified is: [describe]"

Do not proceed until you have written these statements.
```

Writing creates commitment. A gate that requires Claude to write a specific statement is harder to skip than a simple "STOP" instruction.

**Verification checkpoints:**
```markdown
**VERIFICATION:** Before proceeding to Phase 3, confirm:
- [ ] All source documents have been read
- [ ] Conflicts have been identified and documented
- [ ] User has approved the proposed structure
```

**Destructive action gates:**
```markdown
**GATE:** Before deleting any files, write:
- "I am about to delete: [file list]"
- "This is intentional because: [reason]"
- "This action is: [reversible/irreversible]"

**STOP.** Get explicit user confirmation before executing deletion.
```

### Priority Hierarchies

When rules may conflict, establish clear priorities:

```markdown
## Priority Order

1. **CRITICAL** rules cannot be overridden
2. **REQUIRED** rules apply unless user explicitly requests otherwise
3. **RECOMMENDED** rules are defaults that can be adjusted
```

## Natural Prose Guardrails (External-Facing Content)

Skills producing marketing content, website copy, case studies, or other external-facing text need prose guardrails. The primary defense is a **practitioner voice gate** — an upstream step that makes AI-sounding prose architecturally difficult. Word ban lists serve as a revision backstop, not the primary defense.

**When to include these guardrails:**
- Marketing/communications content → Always
- External reports or publications → Always
- Internal working documents → Skip (lower risk)

### Process Gate: Practitioner Voice

The primary instruction is: **identify who would write this content if AI didn't exist, and write from that person's voice.** A marketing director, a research analyst, a learning facilitator — each has distinct vocabulary, sentence rhythm, and professional instincts. When the agent writes from that practitioner's perspective, AI-detectable patterns don't appear because the generation process itself is anchored to a human voice rather than to "AI writing about the domain."

The detection signal is straightforward: when a sentence sounds like AI writing *about* the field rather than someone *in* the field, the voice has slipped. The instruction is to return to the practitioner's perspective — not to swap individual words.

### Revision Backstop

When the voice slips despite the process gate, these words and structures signal it. They appear far more frequently in AI-generated text than in human writing:

**Words:** pivotal, crucial, vital, testament to, underscores, highlights (verb), vibrant, tapestry, delve, foster, garner, leverage, landscape (figurative), holistic, robust, synergy, cutting-edge, groundbreaking, nestled, showcases, boasts, elevate, nuanced, multifaceted

**Structures:** "Not only X but Y," "serves as" / "stands as," "-ing" phrases for empty analysis ("highlighting the importance," "showcasing their commitment"), vague attribution ("experts say," "industry leaders"), formulaic balance ("Despite challenges, [positive]")

**Writing discipline:** Use "is" not "serves as." Repeat nouns rather than cycling through synonyms. Be specific with numbers and names. When you catch a backstop word, the fix is returning to the practitioner's voice — not just swapping the word for a synonym.

### Example Critical Rules Section

For skills producing external-facing content, add this to the Critical Rules:

```markdown
**NATURAL PROSE:** Write as a [specific practitioner role] would — [brief description of their voice]. When a sentence sounds like AI writing about the field rather than someone in it, the voice has slipped. Return to the practitioner's perspective. Revision backstop — these words signal the voice has drifted: pivotal, crucial, vital, testament to, underscores, highlights, vibrant, tapestry, delve, foster, garner, leverage, landscape (figurative), holistic, robust, synergy. Also avoid: "Not only X but Y," "serves as," "stands as," vague attribution ("experts say"), formulaic balance ("Despite challenges, [positive]").
```

## Anti-Patterns to Avoid

### Time-Sensitive Information

Don't include dates or version numbers that will become stale:

```markdown
# Bad
If using version 2.3 (released March 2024), use the new API.
After August 2025, the old endpoint will be deprecated.

# Good
Use the v2 API endpoint. See [LEGACY.md](LEGACY.md) for migration from v1.
```

### Windows-Style Paths

Always use forward slashes:

```markdown
# Bad
See templates\form.docx

# Good
See templates/form.docx
```

### Too Many Options

Don't overwhelm with choices:

```markdown
# Bad
You can use pypdf, pdfplumber, PyMuPDF, pdf2image, pdfminer, or camelot...

# Good
Use pdfplumber for text extraction:
[code example]

For scanned PDFs requiring OCR, use pdf2image with pytesseract instead.
```

### Vague Descriptions

Avoid generic language:

```markdown
# Bad
description: Helps with various tasks

# Good
description: Generates commit messages by analyzing git diffs. Use when committing code or reviewing staged changes.
```

### Abstract Examples

Use concrete input/output, not placeholders:

```markdown
# Bad
Input: [your data here]
Output: [processed result]

# Good
Input: {"name": "Alice", "age": 30}
Output: "Name: Alice\nAge: 30 years"
```

### Weak Constraint Language

Avoid language that can be ignored:

```markdown
# Bad - Claude may skip these
You might want to consider...
If you'd like, you could...
It would be nice to...
Feel free to...

# Good - Claude will follow these
**REQUIRED:** You must...
**Do not** proceed until...
Always verify...
Never include...
```

### Missing Behavioral Guardrails

Every skill needs explicit rules about sourcing, epistemic calibration, and adherence — structured as process gates, not named failure modes:

```markdown
# Bad - no guardrails
## Instructions
1. Read the document
2. Generate a summary
3. Save to file

# Good - includes process-gate guardrails
## Critical Rules
**SOURCING:** Before stating any claim, locate its source in the document. If a claim isn't in the document, say what's missing.

**EPISTEMIC CALIBRATION:** Your language should make clear whether each statement is drawn from the document, inferred from patterns in it, or your analysis.

## Instructions
1. Read the document completely before summarizing
2. Generate a summary based only on document content
3. Save to file
```

## Testing and Iteration

Testing happens in two stages: **structural validation** (automated) and **functional testing** (manual, with real prompts).

### Stage 1: Structural Validation

1. **Validate structure:** Run the validation script
2. **Test description:** Does it trigger for expected phrases?
3. **Test examples:** Are they concrete and runnable?
4. **Test guardrails:** Does the skill have Critical Rules? Are they specific?
5. **Dry run:** Simulate the full loading flow

### Guardrail Verification

Before shipping, test the guardrails structurally — not by checking names, but by checking what they make the agent *do*:

1. **Pick a claim the skill would generate.** Can you trace backward through the skill's rules to a required step that forces the agent to locate a source before making that claim? If the only protection is "don't hallucinate" or "be accurate," the guardrail monitors for a failure mode rather than preventing it.

2. **Read a paragraph the skill would produce.** Can you tell which parts are sourced, which are inferred, and which are the agent's analysis — from the language alone, without bracket markers? If not, the epistemic calibration instruction isn't working.

3. **Imagine the user makes a bad request.** Does the skill give the agent a concrete path for pushing back (cite the concern, offer an alternative)? Or does it just say "be honest"?

If any test fails, the guardrails need rework — not more items on a checklist, but structural changes to the rules that make the failure mode difficult.

### Stage 2: Functional Testing (Parallel Sessions)

Structural validation confirms the skill is well-formed. Functional testing confirms it **produces quality output** when actually used.

#### The Parallel Session Method

Use two Claude sessions simultaneously:

1. **Skill-building session** — Where you create and refine the skill
2. **Testing session** — Where you run the skill with test prompts

This allows you to:
- Run the skill in a clean context (testing session)
- Review output and iterate (skill-building session)
- Keep full conversation history for both activities

#### Designing Test Prompts

Create 2-3 test prompts that exercise the skill progressively:

| Test | Purpose | What to Include |
|------|---------|-----------------|
| **Simple** | Verify basic workflow | Single input, happy path, minimal complexity |
| **Complex** | Test multi-step logic | Multiple inputs, edge cases, decision points |
| **Boundary** | Test ambiguous situations | Incomplete info, unclear requirements, missing context |

**Good test prompts are realistic.** Use the kind of input actual users would provide—don't over-specify to make the skill's job easier.

**Example progression for a curriculum-building skill:**

1. **Simple:** "Create a single lesson about AI ethics"
2. **Complex:** "Create a 2-lesson course comparing sycophantic and objective AI"
3. **Boundary:** "Create a 4-lesson course from this organizational document" (with real doc that wasn't designed as curriculum)

#### Running the Test

In the testing session:

1. Start a fresh conversation
2. Provide the test prompt
3. Let the skill run to completion (or checkpoint)
4. Save/note the output location

**Don't intervene** unless the skill explicitly asks for input. You're testing what happens with minimal user guidance.

#### Reviewing Output

In the skill-building session, read all output files and evaluate:

**Workflow adherence:**
- Did the skill follow its own documented phases?
- Did it stop at checkpoints for approval?
- Did it document decisions as instructed?

**Output quality:**
- Is the content accurate and complete?
- Does it follow the expected format?
- Are there obvious errors or omissions?

**Decision-making:**
- Did it handle ambiguous situations appropriately?
- Did it ask for clarification when needed?
- Were its choices reasonable and documented?

**Edge case handling:**
- What happened with incomplete input?
- Did it fail gracefully or produce garbage?
- What guidance would have helped?

#### The Iteration Loop

```
1. Run test prompt in testing session
2. Review output in skill-building session
3. Identify issues or improvements
4. Update the skill
5. Re-run structural validation
6. Return to step 1 with next test prompt
```

Continue until all test types pass with acceptable output quality.

#### Documenting Test Results

After testing, note:
- What was tested (test prompts used)
- What issues were found
- What changes were made
- Any remaining limitations or edge cases

This helps future maintainers understand the skill's tested boundaries.

### Test with Multiple Models

Skills may behave differently across models:
- **Haiku:** Needs more explicit guidance
- **Sonnet:** Balanced performance
- **Opus:** May need less hand-holding

Write instructions that work across all models you'll use.

### Iterate Based on Usage

After deploying a skill:
1. Observe how Claude navigates it
2. Note where it struggles or misses content
3. Refine based on actual behavior, not assumptions
