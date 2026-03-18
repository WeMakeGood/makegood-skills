# Phase 6: Content

> **PROCESS GATES — Read these first:**
> - **Outline Before Prose:** Re-read the page outline before writing each page. Write to the section's stated purpose. If a section's purpose no longer makes sense during writing, update the outline first — then write the prose. The outline is the structural contract; prose that deviates from it produces pages that drift from the conversion funnel.
> - **Source Before Statement:** Before writing any organizational claim, locate it in the source registry or user conversation. If the source does not exist, write `{{needs-input: what is needed and why}}`. The placeholder is the output — not a sign of failure.
> - **Context Check Before Writing:** Before writing the first page, verify: can you describe the organizational reasoning from the context modules without re-reading them? If not, re-read them now. After every 3-4 pages, check again — context modules compact silently during long generation sessions. Voice profile and writing standards must be the most recent documents in context when generation begins.
> - **Practitioner Voice Test:** After writing each page, re-read the opening paragraph. Does it sound like the person who would write this if AI didn't exist — a marketing director, a nonprofit communications lead, a founder? Or does it sound like AI writing about the industry? If the latter, identify which practitioner would write this page and rewrite from their perspective.

---

## What This Phase Does

Generate one markdown content file per page in the sitemap, following the page outlines from Phase 5. The output is the complete content package in `<OUTPUT_PATH>/content/`.

---

<phase_content_generate>
## Step 0: Verify Context

Before writing any content:

1. Confirm page outlines are loaded (`<OUTPUT_PATH>/outlines/`)
2. Confirm process log is loaded (contains all strategy decisions — CTAs, audience journeys, conversion paths)
3. Confirm context modules are still active — if you cannot describe what organizational reasoning each module provides without re-reading it, re-read it now
4. If voice profile or writing standards were provided, confirm they are still fresh in context. If uncertain, re-read them — they must be the most recent documents loaded
5. If the session has been running since Phase 5 and multiple outlines were created, voice/standards may have compacted. Re-read them before writing any content.

---

## Step 1: Generate Global Elements

Write `<OUTPUT_PATH>/globals/header.md` and `<OUTPUT_PATH>/globals/footer.md`.

See [references/CONTENT-FORMAT.md](../CONTENT-FORMAT.md) for file format.

Header: navigation structure, CTA placement, logo/branding elements.
Footer: secondary navigation, contact information, social links, legal.

---

## Step 2: Generate Page Content

Follow this order:
1. Homepage
2. Primary CTA destination page
3. Top-level navigation pages
4. Child pages
5. Posts/CPT entry templates (if applicable)
6. Utility pages (search, 404, thank-you)

**Per-page content protocol:**

1. **Re-read the page outline** — confirm each section's purpose and source assignments.
2. **Re-read every source file listed in the page's source assignments** (from the sitemap, carried into the outline). Use the index IDs to locate files in `source-index.md`. Re-read the specific sections noted in the annotations — not the entire file unless the annotation calls for it. This is the same per-page re-read gate as Phase 5. Even if you read these files earlier in this session, re-read them now. Source content drifts across pages.
3. **Write frontmatter** using the format from [references/CONTENT-FORMAT.md](../CONTENT-FORMAT.md).
4. **Write each section** following the outline's purpose statements:
   - Write to the section's stated purpose, not around it
   - Source every organizational claim to the specific source file and section from the outline's Source field
   - Use `{{needs-input: description}}` for missing information — describe *what* is needed and *why*
   - Use template syntax (`{{button:}}`, `{{form:}}`, `{{card-grid:}}`, etc.) for non-text elements
5. **Verify the CTA section** connects to the conversion path from strategy.
6. **Voice check** — does this page sound like the person who would write this if AI didn't exist? If it sounds like AI writing about the industry, identify the practitioner and rewrite from their perspective.

Write to `<OUTPUT_PATH>/content/pages/[slug].md`.

---

## Step 3: Generate Forms

For each form identified in the sitemap:

See [references/FORMS-CPTS.md](../FORMS-CPTS.md) for form specification format.

Write to `<OUTPUT_PATH>/forms/[form-name].md`.

---

## Step 4: Generate CPT/ACF Specifications

If custom post types were identified in Phase 4:

See [references/FORMS-CPTS.md](../FORMS-CPTS.md) for CPT and ACF field specifications.

Write to `<OUTPUT_PATH>/cpts/`.
</phase_content_generate>

---

## GATE

Write to build state:
- "Content files generated: [count]"
- "Placeholders requiring user input: [count]"
- "Forms specified: [list]"
- "CPTs specified: [list or 'none']"
- "Voice/style consistency: [any drift noted, sections regenerated]"
- "Pages where source material was insufficient: [list or 'none']"

---

## STOP

**Present to the user:**
- Content file count and structure
- Placeholders requiring their input (grouped by type — organizational facts, images, testimonials, etc.)
- Any pages where voice consistency was difficult to maintain
- Any pages where source material was insufficient
- Forms and CPT specifications created

**Ask:**
- Would you like to review specific pages?
- Can you provide the missing information for placeholders?
- Any content direction that needs adjustment?

**After the user responds, log to `process-log.md`:**
- Content generation decisions
- Voice drift issues and how they were resolved
- User corrections

---

## After This Phase

Update build state:
- **Current phase:** Phase 7 (Validation)
- **Next phase file:** `references/phases/PHASE_7_VALIDATION.md`

Phase 7 may run in the same session if context permits. If the session is getting long, tell the user to start a new session.
