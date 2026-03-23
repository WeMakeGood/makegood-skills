# Generating Writing Standards

Generates structured writing standards modules from writing samples of a target publication, genre, or editorial tradition. Produces process-gate craft rules that shape how an LLM writes at the publication level.

## When to Use

Use this skill when you need to:
- Create writing standards from a set of publication samples
- Capture a publication or genre's craft-level rules for LLM use
- Build a writing standards module that the drafting-articles skill can load
- Analyze what makes a specific publication's prose distinctive

## How to Invoke

Say things like:
- "Generate writing standards from these Atlantic articles"
- "Create prose standards for investigative feature writing"
- "Analyze this publication's writing style"
- "Build writing rules from these samples"

## What You'll Need

- At least 5 writing samples from the target publication or genre (ideally 10+, from multiple authors)
- Context about what publication or genre the samples represent
- An output location for the standards file

## Related Skills

| Skill | Relationship |
|-------|-------------|
| **extracting-voice-profiles** | Complementary — voice profiles capture a person's voice; writing standards capture a publication's craft rules. Load both at generation time. |
| **drafting-articles** | Consumer — the drafting skill loads writing standards modules at Draft phase. Specify the path in a project manifest or reference a baseline. |
| **designing-article-series** | Upstream — the series design skill asks about writing standards preference and writes the selection into the project manifest. |

## What You'll Get

A `writing-standards-[name].md` file containing:
- 3 process gates (upstream craft rules, not checklists)
- Writing discipline section (explicit consequences of the gates)
- Revision backstop (banned language, flagged language, structural flags)
- Scope statement

## How It Works

The skill runs in five phases:

| Phase | What Happens |
|-------|-------------|
| 1: Gather | Collect samples, assess sufficiency, get context |
| 2: Analyze | Work through samples against 3 dimensions (structural discipline, evidence handling, prose mechanics) |
| 3: Draft | Transform patterns into process gates |
| 4: Review | User evaluates recognition, completeness, overclaiming |
| 5: Deliver | Remove scaffolding, save final module |

## Key Distinction

Writing standards capture the **publication**. Voice profiles capture the **person**. The test: would a different author publishing in the same venue follow this rule? If yes, it's a writing standard. If no, it's a voice pattern.

## Tips

- Samples from a single author will blend voice and standards — use multiple authors for publication-level rules
- Focus on divergences from LLM defaults — patterns the LLM would get wrong without guidance
- The revision backstop catches what process gates miss — don't skip it
- Generated modules are compatible with the S0 natural prose standards format from building-context-libraries
