# Creating Skills

Guides creation of new Agent Skills from prompts, context files, and requirements.

## When to Use

Use this skill when you need to:
- Create a new Agent Skill from scratch
- Convert an existing prompt into a reusable skill
- Build skills that follow best practices

## How to Invoke

Say things like:
- "Help me create a new agent skill"
- "Convert this prompt into a skill"
- "Build a skill for processing documents"

## What You'll Need

- Clear purpose for the skill
- Source materials (prompts, docs, examples) - optional
- Target user and use case

## What You'll Get

A complete skill directory with:
- SKILL.md with proper frontmatter
- README.md for GitHub users
- Optional references/ and scripts/ folders

## Reference Documentation

This skill includes comprehensive reference materials:

| File | Purpose |
|------|---------|
| [references/SPEC.md](references/SPEC.md) | What skills are, how they work, technical requirements |
| [references/BEST-PRACTICES.md](references/BEST-PRACTICES.md) | Writing effective, concise skills |
| [references/EXAMPLES.md](references/EXAMPLES.md) | Before/after prompt-to-skill conversions |

## Validation Scripts

```bash
# Initialize new skill structure
python scripts/init_skill.py my-skill-name --path skills

# Validate skill structure
python scripts/validate.py skills/my-skill

# Test description triggers
python scripts/test-description.py skills/my-skill "expected trigger phrase"

# Verify examples are concrete
python scripts/test-examples.py skills/my-skill

# Simulate full loading
python scripts/dry-run.py skills/my-skill "test prompt"

# Package for distribution
python scripts/package_skill.py skills/my-skill --output dist
```

## Tips

- Read the reference docs (SPEC.md, BEST-PRACTICES.md) before creating skills
- Use the validation scripts to check your work
- Test with real prompts in a parallel session before finalizing
- Keep SKILL.md under 500 lines—split into references/ if needed
