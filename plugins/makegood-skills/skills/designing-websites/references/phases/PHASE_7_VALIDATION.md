# Phase 7: Validation

> **PROCESS GATES — Read these first:**
> - **Check Before Present:** Run every validation check before presenting the package to the user. Fix structural issues (missing CTAs, broken links, orphaned pages) before delivery — the user reviews content quality, not structural integrity.
> - **Sitemap as Truth:** Every page in `sitemap.md` must have a corresponding content file. Every content file must appear in the sitemap. Discrepancies are errors, not edge cases.
> - This phase may combine with Session C if context permits. If starting a new session, load build state and process log first.

---

## What This Phase Does

Run structural validation across all generated content, fix issues, and present the complete package to the user. The output is a validated content package ready for design and development.

---

<phase_validation_run>
## Step 0: Load Context (if new session)

If starting a new session (Session D):

1. `<OUTPUT_PATH>/build-state.md`
2. `<OUTPUT_PATH>/process-log.md`
3. `<OUTPUT_PATH>/sitemap.md`

---

## Step 1: Validation Checks

### Sitemap Sync
- Every page in `sitemap.md` has a corresponding content file in `content/`
- No content files exist that aren't in the sitemap

### CTA Coverage
- Every content file has a `cta_primary` in frontmatter
- Every content file has a CTA section or CTA element in the body
- CTA destinations exist as pages

### Link Integrity
- All internal links (`/path/to/page`) reference pages that exist in the sitemap
- Pending links marked with `#` are listed for resolution

### Placeholder Inventory
- All `{{needs-input:}}` placeholders cataloged
- All `{{placeholder:}}` markers cataloged
- All `{{verify:}}` blocks cataloged

### Form Coverage
- Every form referenced in content files has a spec in `forms/`

---

## Step 2: Fix Issues

Fix any structural issues found:
- Missing CTA assignments
- Broken internal links
- Missing content files for sitemap pages
- Template spec gaps

Document fixes in the process log.

---

## Step 3: Generate Deliverables

Write to `<OUTPUT_PATH>/_validation/`:

- `checklist.md` — completion checklist for handoff
- `placeholders.csv` — all placeholders requiring user input
- `missing-links.csv` — links that need resolution
- `orphaned-pages.csv` — pages without proper CTA connections (should be empty after fixes)
</phase_validation_run>

---

## GATE

Write to build state:
- "Validation complete: [pass/fail]"
- "Issues found and fixed: [count]"
- "Remaining placeholders: [count]"
- "Remaining broken links: [count]"
- "Content files: [count]"
- "Forms: [count]"
- "CPTs: [count or 'none']"

---

## STOP (Final)

**Present the complete package to the user:**

- **Content summary:** file count, page hierarchy, content structure
- **Validation results:** all checks should pass
- **Placeholders:** grouped list of items requiring user input
- **Completion checklist:** what's done and what needs user action
- **Recommendations:** priorities for content review, design considerations, development notes

**Output structure:**
```
<OUTPUT_PATH>/
├── build-state.md
├── process-log.md
├── source-index.md
├── sitemap.md
├── outlines/
│   └── [page-name].md
├── content/
│   ├── pages/
│   ├── posts/
│   └── [cpt-name]/
├── cpts/
│   └── spec.md
├── forms/
│   └── [form-name].md
├── globals/
│   ├── header.md
│   └── footer.md
└── _validation/
    ├── checklist.md
    ├── placeholders.csv
    ├── missing-links.csv
    └── orphaned-pages.csv
```

---

## After This Phase

Update build state:
- **Current phase:** Complete
- Mark all phases as complete in the phase completion table.

**LOG:** Final validation results and any recommendations for the user.
