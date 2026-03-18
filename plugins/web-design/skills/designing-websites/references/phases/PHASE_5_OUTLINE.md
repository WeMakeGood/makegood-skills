# Phase 5: Outline

> **PROCESS GATES — Read these first:**
> - **Purpose Before Section:** Before writing any section into an outline, write its purpose statement first. The purpose must name what the section does for the visitor in the conversion funnel. If you cannot articulate a purpose, the section does not exist yet — do not create a placeholder and fill in the purpose later.
> - **Source Before Content:** Every section's "Source" field must be filled before the "Key content" field. Identify where the content comes from (source doc, user conversation, or `needs-input`) before describing what the content is. This prevents inventing content to fill a structural slot.
> - **One Owner Per Content:** Before adding content to a section, check if any other page outline already contains it. If so, one page owns that content and the other links to it. Duplicate content across pages wastes visitor attention and context window tokens.

---

## What This Phase Does

Create a structural outline for every page in the sitemap — section by section, with purpose statements and source attribution. The output is a set of outline files in `<OUTPUT_PATH>/outlines/` that Phase 6 will follow when generating full content. Outlining reveals structural problems before full content is written.

---

<phase_outline_load>
## Step 0: Load Session C Context

**GATE:** Load in this order before any outline work. The loading order matters — source documents provide the specifics that outlines reference, context modules provide organizational reasoning, and voice/standards must be fresh when content generation begins in Phase 6.

1. `<OUTPUT_PATH>/build-state.md`
2. `<OUTPUT_PATH>/process-log.md` — this contains all strategy decisions (CTAs, audience journeys, conversion paths)
3. `<OUTPUT_PATH>/source-index.md` — the complete source inventory
4. `<OUTPUT_PATH>/sitemap.md`
5. **All source documents from the source index** — brand guides, org docs, interview syntheses, existing copy. These contain the specifics that outlines reference: the org's actual language, program details, facts vs. gaps. Without them, the outline's "Source" field is written from compacted memory.
6. Agent definition (from context library manifest in build state — read the file, not just the path)
7. **Every context module listed in the agent definition's `modules:` frontmatter** — read each module file. These contain the organizational reasoning that shapes content voice and decisions. Do not skip any.
8. [references/CONTENT-FORMAT.md](../CONTENT-FORMAT.md) — template syntax reference
9. [references/TECHNICAL-CONTEXT.md](../TECHNICAL-CONTEXT.md) — platform specifics
10. **Voice profile LAST** (from context library manifest — may be a module like `S0_natural_prose_standards.md` or a separate file)
11. **Writing standards LAST** (from context library manifest — if separate from voice profile)

Write to build state: "Session C loaded: build-state, process-log, source-index, sitemap, [count] source documents re-read, agent definition [name], [count] context modules read: [list module IDs], voice profile [yes/no], writing standards [yes/no]"

If you believe you already know the content from previous sessions, you are likely post-compaction. Re-read anyway. Source documents contain the specifics outlines reference. Context modules contain organizational reasoning that shapes every content decision. If either compact, the agent defaults to generic web copy.
</phase_outline_load>

---

<phase_outline_build>
## Step 1: Create Page Outlines

For each page in the sitemap, follow the per-page protocol:

### Per-Page Outline Protocol

**Before outlining each page:**

1. Read the page's sitemap entry — CTA, audience, purpose, source assignments
2. **Re-read every source file listed in the page's source assignments.** Use the index IDs to locate files in `source-index.md`. Even if you read these files during the session loading gate, re-read the specific sections noted in the sitemap's source annotations before outlining this page. Memory of source content drifts across pages.
3. Then outline the page

**Outline format:**

```markdown
# [Page Title]
**Slug:** [from sitemap]
**Template:** [from sitemap]
**CTA:** [from sitemap — specific action and button text]
**Primary audience:** [which audience segment this page primarily serves]
**Page purpose:** [one sentence — what this page accomplishes in the conversion funnel]
**Sources:** [from sitemap — index IDs and what each contributes to this page]

## Section Outline

### 1. [Section Name]
**Purpose:** [Why this section exists on this page — what it does for the visitor]
**Key content:** [What information or elements this section contains]
**Source:** [Index ID and specific material — e.g., "#3 brand guide, 'permanently affordable' language" or "needs-input: local housing statistics"]

### 2. [Section Name]
**Purpose:** [...]
**Key content:** [...]
**Source:** [...]

[...repeat for all sections]

### [Final Section — CTA]
**Purpose:** Convert visitor interest into [CTA action]
**Handoff:** [How this section connects to the CTA page/form]
```

**Outlining order:**
1. Homepage (sets the tone and navigation structure)
2. Primary CTA destination page (what conversion looks like)
3. Top-level navigation pages
4. Child pages
5. Utility pages (search, 404, thank-you)
6. Post/CPT entry templates

---

## Step 2: Cross-Page Analysis

After outlining all pages, check:

- **Content duplication:** Do multiple pages contain the same section? If so, one page owns that content and others link to it.
- **Conversion flow:** Does each audience segment have a clear path from entry to CTA? Walk each journey through the outlines.
- **Section justification:** Re-read every section's purpose statement. Does each one serve the page's CTA, or does it exist because "websites have an 'Our Values' section"?
- **Missing pages:** Does the outline work reveal pages the sitemap missed?
- **Orphaned content:** Is there source material that doesn't appear in any outline? Should it?

**LOG:** Cross-page analysis findings — duplication resolved, flow issues identified, sections cut or restructured.
</phase_outline_build>

---

## GATE

Write to build state:
- "Page outlines created: [count]"
- "Pages with sections requiring user input: [count]"
- "Cross-page content duplication resolved: [list or 'none found']"
- "Conversion flow verified for [N] audience journeys"
- "Sections cut for lacking purpose: [count]"
- "Sitemap changes needed: [list or 'none']"

---

## STOP

**Present to the user:**
- Page outline summary — count, key structural decisions
- Any sections that were cut and why
- Content that requires user input (count and types)
- Cross-page analysis findings
- Any sitemap changes recommended based on outlining

This is not a hard stop — proceed after acknowledgment unless the user raises concerns about the outline structure.

**After the user responds, log to `process-log.md`:**
- Outline decisions and user corrections
- Sections added, cut, or restructured
- Cross-page issues resolved

---

## After This Phase

Update build state:
- **Current phase:** Phase 6 (Content)
- **Next phase file:** `references/phases/PHASE_6_CONTENT.md`

Proceed directly to Phase 6 in the same session.
