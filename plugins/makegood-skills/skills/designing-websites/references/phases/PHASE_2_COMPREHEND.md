# Phase 2: Comprehend

> **PROCESS GATES — Read these first:**
> - **Comprehend Before Structure:** This phase exists because the agent's default is to hear "website" and immediately produce a sitemap. The gate: all sources must be read, reasoning patterns identified, and comprehension findings validated by the user BEFORE any strategy, CTA, or sitemap decisions exist. If you find yourself thinking about page structure, you've skipped ahead.
> - **Source Before Statement:** Before stating any claim about the organization, locate the source in a document or conversation. Write the source reference. Then state the claim. If no source exists, name the gap.
> - **Reasoning Over Summary:** For each source, log what organizational *reasoning* it reveals — not what facts it contains. "This org thinks about audiences as partners, not customers" is reasoning. "Founded in 2015, serves 500 clients" is summary. Log reasoning.

---

## What This Phase Does

Read the source material and conversation history to understand how the organization *thinks* — its principles, values, how it talks about its work and its audiences. The output is a set of comprehension findings: organizational reasoning patterns, convergences, tensions, and gaps. No strategy decisions yet.

---

<phase_comprehend_sources>
## Step 0: Load All Sources

**GATE:** Before any comprehension work, read every source document indexed in build state. Not skim — read. Load the agent definition if one was provided.

Write to build state: "Sources loaded for comprehension: [count] files read in this session"

Do not proceed to Step 1 until all sources are loaded. If the source set is too large to read in one pass, read in clusters — but every source must be read before the GATE at the end of this phase.

---

## Step 1: Work Through the Sources

For each source document or cluster:

- What organizational **reasoning** does this reveal? (Not "what facts does it contain" but "what does this tell us about how the organization thinks, decides, and talks about its work?")
- What principles or values drive the decisions described here?
- **How does this organization talk about the people it serves?** Look for language patterns — do they say "clients" or "partners"? "Help" or "empower"? "Users" or "community members"? This language shapes the website's voice.
- What surprised you? What contradicts your initial assessment from Gather?
- Where does this source agree with or create tension with others?

**LOG:** For each source or cluster, write 2-3 sentences: the organizational reasoning this source reveals and why it matters for the website. Apply the Reasoning Over Summary gate — if your log entry describes what the document contains rather than how the organization thinks, rewrite it.

---

## Step 2: Find Convergences

Different sources often describe the same underlying pattern without using the same terms. A brand guide might describe the organization's values one way while an interview transcript shows those values in action with completely different language.

Look for:
- **Same pattern, different language** — two sources describing one organizational behavior
- **Complementary evidence** — one source explains *why*, another shows *how*
- **Cross-domain connections** — how they describe internal culture mirrors how they want to be perceived externally

**LOG:** Write each convergence as 2-3 sentences: what connects, and what the connection reveals about how the website should present this organization.

---

## Step 3: Identify Tensions

Where do sources disagree or create tension? Not just factual contradictions (those were flagged in Gather), but positioning tensions:

- Does the brand guide's aspirational tone match the operational reality in their existing content?
- Do different stakeholders describe the organization's value proposition differently?
- Is there a gap between how they talk about themselves and how their audiences would describe them?

These tensions need resolution before strategy can proceed. Some are real conflicts requiring user input. Others are complementary perspectives the website should reconcile.

**LOG:** Each tension with: what conflicts, which sources, and whether it's a real conflict (needs user resolution) or a complementary perspective (content should integrate both).

---

## Step 4: Map Audience Reasoning

Based on sources and conversation (not assumptions):

- Who actually uses this organization's services/products? How do *they* describe their needs? (This is often different from how the organization describes serving those needs.)
- What language do audiences use to search for this kind of organization?
- Where is the gap between organizational messaging and audience search behavior?
- Are there audience segments the organization hasn't articulated but the sources reveal?

**LOG:** Audience reasoning refined from sources — how audiences think about their own needs, not just who they are demographically.

---

## Step 5: Update Source Index with Website Mappings

After comprehension is complete, update `<OUTPUT_PATH>/source-index.md` with what each source contributes to the website. Add a new section after the reading checklist:

```markdown
## Website Content Mappings

| ID | Source File | Website Contribution | Key Material | Comprehension Finding |
|----|-------------|---------------------|-------------|----------------------|
| #1 | [path] | [what this source provides for the website] | [specific sections, language, or details to use] | [which reasoning pattern this connects to] |
| #2 | [path] | [...] | [...] | [...] |
```

Use the same numeric IDs from the Source Files table in `source-index.md`. These IDs are what the sitemap will reference in Phase 4 when assigning sources to pages.

For each source file:
- **Website Contribution:** Not what the file contains — what it gives the website. "#3 (brand guide) provides the 'permanently affordable' language that should anchor the value proposition" not "#3 (brand guide) contains brand standards."
- **Key Material:** Specific sections, phrases, data points, or reasoning that content writers need. "Resale formula on p.3, buyer testimonial language in section 2" — not "the whole document."
- **Comprehension Finding:** Which reasoning pattern or convergence from Steps 1-4 this source connects to. "Convergence 1 (partner, not vendor)" or "Pattern 3 (qualification function)." This is the bridge between understanding and construction.

This table is what Phase 4 (Sitemap) reads to assign sources to pages. The sitemap then carries those assignments forward so Phase 5 and 6 know exactly which files to re-read for each page.
</phase_comprehend_sources>

---

## GATE

Write to build state:
- "Organizational reasoning patterns: [list — how this org thinks about its core work]"
- "Convergences found: [list — where different sources reveal the same underlying principle]"
- "Tensions requiring resolution: [list or 'none']"
- "Audience reasoning refined: [how audiences think about their needs, in their language]"
- "Gaps carried forward: [what's missing]"
- "Source index updated with website content mappings: [count] sources mapped"
- "Comprehension complete: all sources read for organizational reasoning, not just cataloged"

---

## STOP

**Present to the user:**
- Key reasoning patterns — how the organization thinks about its work, what principles drive decisions
- Convergences — where different sources reveal the same underlying pattern
- Tensions — real conflicts that need resolution vs. complementary perspectives
- Audience reasoning — how their audiences think about their own needs (this often surprises the user)
- Gaps — what's missing and how it affects strategy
- Any sources that turned out to be less relevant than initially expected

**Ask:**
- Do these reasoning patterns match your understanding of the organization?
- Are the tensions I identified real, or am I misreading the sources?
- Does the audience reasoning sound right? (Often users realize their audience thinks about their needs differently than the org assumed.)
- For the gaps — can you provide the missing information?

**This is the validation point for comprehension.** The user validates the *understanding* before any strategy is proposed. If the understanding is wrong, everything built on it will be wrong.

**Do not proceed until the user confirms or provides additional direction.**

**After the user responds, log to `process-log.md`:**
- Key comprehension insights and why they matter for the website
- User corrections or direction changes from the STOP review
- Anything that shifted your understanding from what you expected after Gather

---

## After This Phase

Update build state:
- **Current phase:** Phase 3 (Strategy)
- **Next phase file:** `references/phases/PHASE_3_STRATEGY.md`

**Tell the user:** "Comprehension is complete. **Start a new session before Strategy** — Strategy needs the comprehension findings and source material fresh in context, not buried under the analysis from this session. Say 'Resume designing website' to continue."

**The boundary between Session A and Session B is mandatory.**
