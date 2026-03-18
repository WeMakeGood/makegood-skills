# Phase 4: Sitemap

> **PROCESS GATES — Read these first:**
> - **Strategy Before Structure:** Every page in the sitemap must trace to a strategy decision in the process log. Before adding a page, name which audience journey it serves and which CTA it exits toward. If a page exists because "websites have one" rather than because a strategy decision requires it, cut it.
> - **Dead-End Test:** For every page, answer in writing: "After reading this page, what does the visitor do next?" If the answer requires inventing a new path, the page needs a CTA assignment before it can exist in the sitemap.
> - **Exit Before Entry:** Assign the CTA (exit action) before writing the content purpose. This prevents pages that accumulate content without a conversion destination.

---

## What This Phase Does

Transform the conversion strategy into a flow-based sitemap: page hierarchy, CTA assignments, template assignments, source assignments, and custom post type identification. The output is `sitemap.md` — the construction plan that determines every content file Phase 6 will create and which sources to build each page from.

---

<phase_sitemap_build>
## Step 0: Confirm Strategy Context

Verify strategy decisions from the process log are loaded. Re-read the Phase 3 strategy log entry if uncertain.

Write to build state: "Strategy decisions confirmed from process log: Primary CTA [action], [N] audience segments, conversion paths defined"

---

## Step 1: Build Page Hierarchy

Using the strategy decisions from the process log (CTAs, audience journeys, conversion paths):

For each audience segment's journey, what pages are needed?
- Where do they enter?
- What do they need to see at each stage?
- Where does each journey converge on a CTA?

Build the hierarchy from conversion paths, not from convention. If "About Us" doesn't serve a conversion path, it doesn't belong. If it does, define *which* conversion path it serves.

**Dead-end test:** For every page, answer: "After reading this page, what does the visitor do next?" If the answer is "leave," the page needs restructuring.

---

## Step 2: Assign CTAs

Every page gets a CTA assignment:
- Which CTA (primary, secondary, or tertiary) is this page's exit action?
- Where does the CTA button/link lead?
- Is the CTA placement appropriate for this page's position in the funnel?

Pages closest to conversion get the primary CTA. Pages early in the funnel may use secondary or tertiary CTAs to avoid asking for commitment too soon.

---

## Step 3: Assign Templates

Every page gets a template assignment:
- `homepage` — landing page with multiple audience paths
- `page` — standard content page
- `archive` — listing page for posts or CPT entries
- `single` — individual post or CPT entry
- `search` — search results
- `404` — error page

---

## Step 4: Identify Custom Post Types

Based on the sitemap, do any content types need CPT treatment?

Signs a CPT is needed:
- Multiple entries with the same structure (team members, programs, services, case studies)
- Content that needs filtering or sorting
- Content with structured fields beyond title/body

If CPTs are identified, note them in the sitemap with their archive and single template assignments.

---

## Step 5: Write Sitemap

Write `<OUTPUT_PATH>/sitemap.md`. For every page, include:
- Title and slug
- Template assignment
- CTA assignment (which CTA, button text, destination)
- Primary audience segment
- Parent/child relationships
- Form assignments (if applicable)
- One-sentence content purpose (what this page does in the conversion funnel)
- **Source assignments** — which source files (by index ID from `source-index.md`) inform this page and what each contributes

**Source assignment format for each page:**
```
- **Sources:**
  - #3 (brand guide) — value proposition language, "permanently affordable" framing
  - #5 (program docs) — resale formula details, eligibility criteria
  - #7 (S1_community_engagement) — audience reasoning, how org thinks about community members
  - #9 (interview synthesis) — founder's voice on why the model works
```

This is the construction plan. When Phase 5 outlines a page and Phase 6 writes it, the agent re-reads exactly these files — not the entire source set. The source index ID tells you where the file is. The annotation tells you what to look for in it.

The sitemap is the single source of truth for what pages exist, what each one does, and what to build it from. The process log records *why* (strategy decisions). The sitemap records *what* and *from what*.

Template assignments live in the sitemap. Do not create separate template spec files — WordPress developers know what page, archive, single, and 404 templates contain.
</phase_sitemap_build>

---

## GATE

Write to build state:
- "Sitemap contains [N] pages"
- "All pages have assigned CTAs: [yes/no]"
- "All pages have assigned templates: [yes/no]"
- "No dead ends identified: [yes/no]"
- "Custom post types identified: [list or 'none']"
- "Forms required: [list or 'none']"

---

## STOP

**Present to the user:**
- Page hierarchy with CTA assignments
- Template assignments
- Any pages where CTA assignment was uncertain
- Custom post types recommended (if any)
- Forms required
- Dead-end analysis — confirm no pages are dead ends

**Ask:**
- Does this page hierarchy cover all the content you need?
- Are the CTA assignments appropriate?
- Are there pages missing?
- Are there pages that shouldn't exist?
- Do the custom post types make sense?

**Do not proceed until the user confirms the sitemap.** The sitemap determines every content file that will be created. Changes after content generation starts mean rewriting pages.

**After the user responds, log to `process-log.md`:**
- Sitemap decisions and user corrections
- Pages added, removed, or restructured
- CTA assignment changes

---

## After This Phase

Update build state:
- **Current phase:** Phase 5 (Outline)
- **Next phase file:** `references/phases/PHASE_5_OUTLINE.md`

**Tell the user:** "Sitemap is complete. **Start a new session before content work** — content generation needs voice profile and writing standards fresh in context, loaded last. Say 'Resume designing website' to continue."

**The boundary between Session B and Session C is mandatory.**
