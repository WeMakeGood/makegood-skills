# Content File Format

Template syntax for elements markdown cannot represent. Used during Phase 6 content generation.

---

## Page Content File Structure

```yaml
---
title: [Page Title]
slug: [/path/from/sitemap]
type: [page | post | cpt-name]
template: [template from sitemap]
cta_primary: [destination path]
cta_text: [button text]
---

# [Page Title]

[Sections following page outline from Phase 5]
```

Optional frontmatter: `parent`, `seo_title`, `seo_description`, `excerpt`, `featured_image`, `categories`, `tags`, `custom_fields`.

---

## Template Syntax

Use `{{type: content | attribute=value}}` for non-text elements.

**Buttons:**
```
{{button: CTA Text | url=/path | style=primary}}
```

**Images (descriptions for production):**
```
{{image: Description of needed image | alt=Accessible description}}
```

**Forms:**
```
{{form: form-name}}
```

**Cards:**
```
{{card-grid: 3-column}}
{{card: Title | icon=icon-name}}
Content
{{/card}}
{{/card-grid}}
```

**Accordions:**
```
{{accordion: Section Title}}
{{item: Question}}
Answer
{{/item}}
{{/accordion}}
```

**Callouts:**
```
{{callout: info}}
Content
{{/callout}}
```

**Videos:**
```
{{video: Description | source=platform}}
```

---

## Placeholder Syntax

**Missing information (must come from user):**
```
{{needs-input: What is needed and why}}
```

**Specific values:**
```
{{placeholder: COMPANY NAME}} has served {{placeholder: REGION}} since {{placeholder: YEAR}}.
```

**Verification needed:**
```
{{verify: These statistics should be confirmed}}
Content with {{placeholder: NUMBER}} references.
{{/verify}}
```

These details require the Source Before Statement gate from Phase 6 — company details, contact info, pricing, testimonials, partner/client names, legal claims, staff names. If no source exists, use `{{needs-input:}}` placeholders.
