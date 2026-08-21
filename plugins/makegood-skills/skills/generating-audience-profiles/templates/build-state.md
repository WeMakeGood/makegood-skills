# Build State

Single source of truth for session resume. One line per status update.

---

## Build identification

- **Output path:** [OUTPUT_PATH]
- **Source path:** [SOURCE_PATH]
- **Audience question:** [verbatim]
- **Library handoff:** [named library / no library / library being built in parallel]
- **Build started:** [date]

---

## Phase status

- **Phase 1 (Setup):** [pending / complete] — [date complete]
- **Phase 2 Pass 1 (Recognition):** [pending / complete] — [date complete]
- **Phase 2 Pass 2 (Synthesis):** [pending / complete] — [date complete]
- **Phase 3 (Design):** [pending / complete] — [date complete]
- **Phase 4 (Build):** [pending / in progress / complete] — [date complete]

---

## Source counts by class

- **Class A (direct audience):** [N]
- **Class B (competitive/sector):** [N]
- **Class C (internal strategy):** [N]
- **Class D (modeled-data, generated in Phase 2 Pass 2):** [N pictures produced]

---

## Comprehension artifacts

- per-source notes: [N of N sources]
- signal log: [last updated]
- expectations-vs-findings: [complete / in progress]
- conflicts log: [N entries, N open]
- modeled-data pictures: [N audiences]
- dimension candidates: [N candidates]
- agent-needs: [complete / pending]

---

## Matrix status

- **Dimensions committed:** [D1: values; D2: values, or "not yet"]
- **Cells total:** [N]
- **Cells substantive:** [N]
- **Cells thin:** [N]
- **Cells modeled-only:** [N]
- **Cells intentionally empty:** [N]
- **Cells coverage gap:** [N]

---

## Module status

One line per module:

- modules/[cell-coordinate].md: [pending / in progress / complete], [N words], [substantive / thin / modeled-only]
- ...

---

## Next action

- **Next phase:** [phase name]
- **Next phase file:** [relative path]
- **Session boundary:** [continue same session / mandatory break before resuming]
