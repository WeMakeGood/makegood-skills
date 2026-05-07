# Forms and Custom Post Types

Specification formats for forms and CPTs. Used during Phase 6 content generation.

---

## Form Specification

Write to `<OUTPUT_PATH>/forms/[form-name].md`.

```yaml
---
form_name: [slug]
form_title: [Display Title]
plugin: [from Phase 1 tech stack]
submit_button_text: [text]
redirect_url: [/thank-you/path]
---

# [Form Title]

## Purpose
[What this form does and where it appears]

## Fields

| Field | Type | Required | Validation | Notes |
|-------|------|----------|------------|-------|
| [name] | [text/email/tel/textarea/select/checkbox/radio/date/file] | [yes/no] | [rules] | [notes] |

## Conditional Logic
[If applicable — field visibility rules]

## On Submit

### Email Notifications
**To Admin:** [recipients, subject, body]
**To User:** [subject, body]

### Integrations
[CRM, email list, other — from Phase 1 tech stack]

## Success State
Redirect to: [path]
```

For multi-step forms, add `multi_step: true` to frontmatter and organize fields by step.

---

## Custom Post Type Specification

Write to `<OUTPUT_PATH>/cpts/spec.md`.

```markdown
# Custom Post Types

## [CPT Name]
- **Slug:** [slug]
- **Singular/Plural:** [Singular] / [Plural]
- **Public:** [Yes/No]
- **Has Archive:** [Yes (/path/)]
- **Supports:** [title, editor, thumbnail, excerpt]

## Custom Taxonomies

### [Taxonomy Name]
- **Slug:** [slug]
- **Applies to:** [cpt-slug]
- **Hierarchical:** [Yes/No]
- **Terms:** [initial terms]

## ACF Field Groups

### [Group Name]
**Location:** [cpt-slug] post type

| Field Name | Type | Required | Notes |
|------------|------|----------|-------|
| [name] | [text/textarea/number/email/url/select/checkbox/image/gallery/relationship/repeater] | [yes/no] | [notes] |
```

ACF JSON export (`cpts/acf-export.json`) can be generated for direct WordPress import if needed.
