---
name: designing-article-series
description: Designs article series or single-article projects from existing research. Through interactive series-level comprehension, produces series maps, research indexes, audience documents, and project manifests that the drafting-articles skill reads. Use when planning a series, setting up an article project, organizing research for articles, or when the user says design series, plan articles, set up article project, or prepare research for drafting. Also activates for single article setup when user provides research and wants to scaffold before drafting.
---

# Designing Article Series

<purpose>
Claude's default when given research and asked to plan a series is to pre-comprehend the evidence
for each article — producing article outlines that are argument sequences rather than broad strokes.
This skill counters that by keeping series-level planning at the "what this article carries" level,
not the "how this article argues" level. Article-level comprehension belongs in the drafting skill.

This skill enters after research is done (or done enough). The origin conversations, domain research
sessions, and cross-cutting document development happen naturally in exploratory sessions. This skill
formalizes what that exploration produced into architectural documents the drafting skill can use.
</purpose>

## Critical Rules

**SOURCING:** Every claim about what the research shows must trace to a specific research document. If a pattern is identified across documents, name the documents. If a finding is attributed to a domain, name the source.

**EPISTEMIC CALIBRATION:** The user should always be able to tell whether a series architecture decision is grounded in the research, inferred from cross-document patterns, or the skill's analytical interpretation.

**PROFESSIONAL CHALLENGE:** If the research doesn't support the number of articles the user wants, or if the evidence suggests a different series structure than the user envisions — name the discrepancy and propose an alternative. The user's intent shapes the series; the evidence constrains what the series can credibly argue.

**SERIES-LEVEL ONLY:** The series map provides broad strokes per article — thesis, structural role, misconception, research-to-load. It does NOT provide per-section argument sequences, section structures, evidence selections for specific sections, or narrative inventories. Article-level comprehension belongs in the drafting-articles skill's Comprehend and Design phases. Pre-comprehending at the series level anchors the drafting agent on compressed conclusions.

**SCAFFOLD FOR DRAFTING:** The project manifest is a contract with the drafting-articles skill. Every path in the manifest must be accurate. Every field in the series map must match what the drafting skill's Setup phase expects.

---

## Workflow

```
Article Series Design:
- [ ] Phase 1: Gather research and context
- [ ] Phase 2: Comprehend at series level
- [ ] Phase 3: Design the architecture
- [ ] Phase 4: Produce the artifacts
- [ ] Phase 5: Review with user
```

<phase_gather>
### Phase 1: Gather Research and Context

**First: establish the output location and scaffold the project directory.**

Ask the user where the project should live. Then create the directory structure:

```
[output-location]/
├── project-manifest.md    (empty — populated in Phase 4)
├── Context/               (voice profile, org identity, writing standards, other context modules)
├── Research/              (research documents, organized by domain or topic)
├── Sources/               (primary source materials — PDFs, transcripts, audio, reference data)
├── Drafts/                (where the drafting skill writes output)
├── Archive/               (deprecated documents — never loaded for bootstrapping)
```

If the user already has a directory with files in it, use that as the output location and create only the missing pieces. Do not move or reorganize existing files. If research documents are already present (in any directory), note their location rather than asking the user to move them.

If the user provides a voice profile path, copy or note it in `Context/`. If they have organizational context modules (identity, brand, ethical framework, content methodology), those go in `Context/` as well.

**STOP.** Tell the user: "I've scaffolded the project directory at `[path]`. The structure is ready for:
- Research documents in `Research/` (or tell me where they already are)
- Voice profile and any context modules in `Context/`
- Primary sources (PDFs, transcripts, audio) in `Sources/`

Let me know when files are in place, or point me to where they already live."

Do not proceed until the user confirms the research is accessible.

**Then gather context:**

1. **Research documents** — Where are they? Confirm the path. If the user placed them in the scaffolded `Research/` directory, read that directory. If they're elsewhere, note the path.

2. **Author intent** — What does the user want this series (or article) to do? Who is the audience? What's the thesis or driving question? This can be rough — the comprehension phase will refine it.

3. **Voice profile** — Does one exist? Where is it? If not, note that the drafting skill can work without one (using its default prose), or the user can generate one with the extracting-voice-profiles skill.

4. **Writing standards** — Does the user have custom writing standards? Want to select from available baselines? Or use the default? Available baselines (read from `drafting-articles/references/baselines/`): list the `.md` files by name. The selected baseline will be copied into the project's `Context/` directory during Phase 4 so the drafting skill can find it locally.

5. **Series or single?** — Is this a multi-article series or a single article? This determines whether the output includes a series map or an article brief.

**GATE:** Before proceeding, write:
- "Project directory: [path]"
- "Research located: [count] documents in [location]"
- "Author intent: [1-2 sentences]"
- "Voice profile: [path or 'none']"
- "Writing standards: [path, baseline selection, or 'default']"
- "Project type: [series / single]"
</phase_gather>

<phase_comprehend>
### Phase 2: Comprehend at Series Level

**Read** [references/COMPREHENSION-GUIDE.md](references/COMPREHENSION-GUIDE.md) before beginning.

Read all research documents. This is not extraction — it is comprehension. The goal is to understand what the research body makes visible as a whole, not to mine individual documents for article content.

**Step 1: Read all research through.** Note initial impressions — what feels like it adds up, what patterns emerge across documents, what surprises.

**Step 2: Identify the series arc** (or article thesis for single articles). What does the reader understand after the full series that they couldn't from any single article?

**Step 3: Find natural article boundaries** (series only). Articles divide where the reader needs a new frame, not where the topic changes.

**Step 4: For each article, identify the structural payload.** What does the reader carry forward? What would they miss without this article?

**Step 5: Assign research to articles.** Primary, supporting, and background — as a loading manifest, not as interpretation.

**Step 6: Check the build.** Read the entries in order. Does each article build on what came before? Could any article be removed?

**GATE:** Before presenting, write:
- "Series arc: [one sentence]"
- "Article count: [N] articles"
- "Each article passes necessity test: [yes/no — list any that don't]"
- "Research coverage: [all documents assigned / gaps exist in: list]"

**STOP.** Present to the user:
- The series arc (or article thesis)
- Proposed article boundaries with structural payloads
- Research assignments (primary/supporting per article)
- Any places where the research doesn't support the author's intended structure
- What's missing — research gaps that would strengthen the series

Ask: "Does this match how you see the series? Are there articles I'm missing or articles that should be combined? Are the research assignments right?"

Do not proceed until the user confirms or redirects.
</phase_comprehend>

<phase_design>
### Phase 3: Design the Architecture

With the user's confirmed comprehension as input, design the full series architecture.

**For each article, produce** (using the series map template at [templates/series-map.md](templates/series-map.md)):
- What This Article Carries (structural payload)
- Argument Arc (logical sequence at series level — NOT section structure)
- Thesis Elements (specific derivations or framework elements established)
- Misconception to Reframe (one sentence)
- Keyword Targets (if keyword research exists)
- Research to Load (primary and supporting, as a table)
- Cross-Domain Connections (to other articles)
- What the Reader Has After This Article

**For the audience document** (using the template at [templates/audience-document.md](templates/audience-document.md)):
- Work with the user to define: who the reader is, what they're experiencing, how they search, what register the series uses, editorial rules, prose address, and the formation move

**For the research index** (using the template at [templates/research-index.md](templates/research-index.md)):
- Inventory all research documents with tags, organized by category
- Separate research inputs from analytical outputs (framework documents are not evidence)

**For single articles:** Produce an article brief instead of a series map — thesis, argument arc, misconception, keyword targets, and research-to-load for the one article.

**What a well-scoped series map entry looks like** (showing abstraction level, not content — your entries will be specific to the research):

> **What This Article Carries:** Establishes that the measurable failures in the system are concentrated in information-layer functions — pattern matching, protocol adherence, knowledge retrieval — not in relational judgment. This distinction is what later articles build on.
>
> **Argument Arc:** Reader's own experience → system-level data confirming the pattern → the information/relational distinction → what this means for where technology enters.
>
> **Research to Load:** Primary: healthcare-ai-disruption-research, justice-gap-research. Supporting: occupational-disruption-index.

This is the right level. It says what the article carries and how the evidence builds — not what sections exist, not which paragraph uses which finding, not what the opening looks like.

**GATE:** Before proceeding, write:
- "Series map entries: [count] articles"
- "Audience document: [drafted / needs user input on specific sections]"
- "Research index: [count] documents indexed"
- "Gaps identified: [list or 'none']"

**STOP.** Present the designed architecture to the user before writing files:
- Per-article series map entries (or article brief for single articles)
- Audience document draft (flag sections needing user input)
- Research index organization
- Any gaps or concerns

Ask: "Does this architecture match your intent? Are the article payloads right? Is the audience document accurate? I'll write these to files once confirmed."

Do not proceed to writing files until the user confirms.
</phase_design>

<phase_produce>
### Phase 4: Produce the Artifacts

Write all artifacts to the user's specified output location:

1. **Project manifest** — using template at [templates/project-manifest.md](templates/project-manifest.md). Populate all paths. The manifest is the contract the drafting-articles skill reads.

2. **Series map** (or article brief for single articles) — populated from Phase 3.

3. **Research index** — populated from Phase 3.

4. **Audience document** — populated from Phase 3.

5. **Writing standards baseline** — if the user selected a baseline (e.g., `longform`, `structured-analysis`, `web-explainer`), copy it from the drafting-articles skill's `references/baselines/` directory into the project's `Context/` directory. The manifest's writing standards path should point to this local copy (e.g., `Context/writing-standards-longform.md`), not back to the skill directory. This ensures the drafting skill can find the file regardless of working directory, and the user can customize it for their project.

6. **Create the drafts directory** if it doesn't exist.

**Verify the manifest:** Every path in the manifest must point to a real file. Read the manifest back and confirm each path resolves.

**GATE:** Write:
- "Manifest written to: [filepath]"
- "Series map written to: [filepath]"
- "Research index written to: [filepath]"
- "Audience document written to: [filepath]"
- "Writing standards copied to: [filepath, or 'custom — already at user-specified path']"
- "All manifest paths verified: [yes/no — list any broken paths]"
</phase_produce>

<phase_review>
### Phase 5: Review With User

Present the complete project architecture:

1. The project manifest — showing where everything lives
2. The series map — per-article structural payloads, argument arcs, and research assignments
3. The audience document — who the reader is and how the series addresses them
4. The research index — what's available and how it's organized
5. Any gaps — research that would strengthen specific articles
6. Recommended next step: "To draft Article [N], start a new session and say 'Draft Article [N].' The drafting skill will read the manifest and begin."

**STOP.** Wait for the user to review. The user may:
- **Approve** — the project is scaffolded and ready for drafting
- **Revise** — adjust article boundaries, research assignments, audience definition, or series arc
- **Add research** — identify gaps to fill before drafting begins

Do not proceed until the user confirms.
</phase_review>

---

## Output Requirements

**ALWAYS save all artifacts to files.** The manifest, series map, research index, and audience document are all file-based outputs. Do not present them only inline.

---

<failed_attempts>
## What DOESN'T Work

- **Over-compressing the series map into argument sequences.** The series map's job is broad strokes — what each article carries, not how it argues. When the series map includes per-section structures, argument sequences, or evidence-to-section mappings, the drafting agent inherits compressed conclusions instead of reasoning from the research. The drafting skill's Comprehend phase does the article-level analytical work.

- **Treating the series map as a collection of rough drafts.** If the series map entries read like article summaries — with specific claims, specific evidence deployments, and specific narrative choices — they are too detailed. The series map should say "this article establishes the distinction between X and Y using domain research from healthcare and education." It should NOT say "Section 1 opens with a personal healthcare narrative, Section 2 presents UCSF data showing 23% misdiagnosis rates."

- **Pre-assigning evidence to specific sections.** "The UCSF study goes in Section 2" over-specifies. The drafting skill's Orient and Comprehend phases determine section structure and evidence deployment. The series map says which documents are primary evidence for each article — not where they land.

- **Skipping the author interaction at comprehension.** The series architecture must reflect the author's intent, not just the research's logical structure. The research may suggest a 6-article series; the author may want 4. The research may emphasize one domain; the author may want balance. These decisions require conversation.

- **Producing a series map without checking the build.** If articles can be removed without breaking the series, they don't earn their place. The necessity test applies at the series level: what can the reader NOT understand in later articles without this one?

- **Conflating research inventory with research interpretation.** The research index inventories documents — what they contain, where they are, what tags they carry. It does not interpret them. "This document argues that AI bias is primarily a data problem" is interpretation. "This document covers AI bias in healthcare diagnostics, sourced from UCSF and Commonwealth Fund data" is inventory.
</failed_attempts>

---

## Reference Files

- [references/COMPREHENSION-GUIDE.md](references/COMPREHENSION-GUIDE.md) — Series-level comprehension process
- [templates/project-manifest.md](templates/project-manifest.md) — Project manifest structure
- [templates/series-map.md](templates/series-map.md) — Series map structure
- [templates/research-index.md](templates/research-index.md) — Research index structure
- [templates/audience-document.md](templates/audience-document.md) — Audience document structure
