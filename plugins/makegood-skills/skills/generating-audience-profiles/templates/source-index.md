# Source Index

One entry per source file inventoried during Phase 1. The source-index captures the source's identity (path, class, vintage, structural identity) — NOT what the source says about audiences. Audience-content claims live in per-source notes (Phase 2 Pass 1).

This separation is architectural. Even when sources are read fully for classification (required for accuracy), the entry text must stay structural. The "Audience-relevance scope" field is a structural claim only.

## The structural-claim discipline

The test for any "Audience-relevance scope" entry: *Could this sentence be written by someone who has confirmed the document's format and title, without reading its content for substance?*

**Allowed patterns:**
- "Peer-org dossier following the standard format."
- "Internal strategy doc; the org's own evaluation of [their situation]."
- "Sector synthesis memo addressing the principals directly."
- "Sector prompt; research planning artifact, not audience research."
- "Format specification document."
- "Combined dossier covering two operators plus a landscape overview."

**Disallowed patterns (content extraction smuggled in as structural description):**
- "Documents [specific audience segment] as unclaimed white space."
- "Names the [N] constituency buckets the [client artifact] uses."
- "Maps the [domain] landscape across [named competitors]."
- "Identifies competitor audience targeting."
- "Documents what audience segments each competitor reaches."

Used during Phase 2 Pass 1 as the reading checklist and during downstream library design to avoid re-reading sources already analyzed.

---

## Status

- **Total sources:** [N]
- **Read (per-source note complete):** [N]
- **Pending:** [N]

---

## Sources by class

### Class A — Direct audience research

#### [Source title]

- **Path:** [relative path from SOURCE_PATH]
- **Class:** A
- **Secondary class:** [if applicable — e.g., A+C if it's a client-published audience study]
- **Date / vintage:** [when produced]
- **Audience-relevance scope:** [structural claim only — e.g., "Peer-org dossier with standard format including an Audience Profile section" or "Internal strategy doc naming the org's stated target segments." Do NOT summarize what the source says about audiences.]
- **Read status:** [pending / read]
- **Per-source note:** [link to `comprehension-artifacts/[slug].md` — created in Pass 1, not Phase 1]

[Repeat for each Class A source]

### Class B — Competitive / sector research

[Same entry format]

### Class C — Internal strategy and program documents

[Same entry format]

### Class D — LLM modeled-data pictures (generated, not loaded)

For each modeled-data picture produced in Phase 2 Pass 2:

#### Modeled-data picture: [audience name]

- **Audience identified:** [by decision orientation]
- **File:** `comprehension-artifacts/modeled-data-[audience-slug].md`
- **Identifiable references count:** [N]
- **Test status:** [tested / partial / pending]

[Repeat for each modeled-data picture]

---

## Sources excluded

If any files in `SOURCE_PATH` were excluded from analysis, list them here with reason:

- [Source path]: [reason — e.g., "non-textual asset," "deprecated draft," "audience-irrelevant"]
