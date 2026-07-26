# ADR-002 — Generic Business-System compiler (folder object model)

Status: accepted
Date: 2026-07-26
Owner: founder
Decision Type: architecture
SVOS Version: 2.0.0
Affected Version: 2.1.0 (minor — compiler generalized; output contract preserved)
Supersedes: none · Related: [ADR-001](ADR-001-adopt-compiler-supersede-b3.md)

# Context

The compiler (`scripts/compile_sessionvue.py`) hardcoded the **Executive** Business System: an 18-folder anatomy, Executive-specific folder indices for placement (Jobs→`12 Jobs`, etc.), and ~22 "Executive" wording literals. A second Business System (Operations, `BS-002`) requires a **different** 20-folder anatomy and its own wording, which the hardcoded compiler could not produce.

# Decision Required

Make the compiler Business-System agnostic: compile folder anatomy, labels, and system wording from each system input rather than from Executive-specific hardcoding.

# Founder Decision

`ACCEPTED` (2026-07-26). Adopt **one canonical folder object model**; the compiler derives everything from it. Implement in two stages, each independently proven before commit.

# The folder object model

Each system input carries a single `folders` array. Each folder object:

```json
{ "id": "02 Strategic Planning", "index": 2, "title": "Strategic Planning", "role": "component", "purpose": "…" }
```

- `id` — the on-disk folder name (with numeric prefix).
- `index` — order.
- `title` — human label; component doc filename is `title.upper()`.
- `role` — one of: `control_center, charter, component, decision_management, founder_approval, metrics, jobs, automations, knowledge, decisions, improvements, archive`.
- `purpose` — descriptive text for component / decision_management / founder_approval docs.

The compiler derives folder creation, artifact placement, the Control Center System Map, and all system wording (via a system `label`, default = `name` minus " System") from this single array. No parallel `folder_roles` / `components` structures.

# Rationale

- One source of truth for a system's anatomy → less drift.
- New Business Systems declare structure as data, not code.
- Wording is parameterized by `label`; no per-system code branches.

# Consequences

- `compile_sessionvue.py` generation logic is fully parameterized (only a docstring names "Executive").
- `validate_output` discovers each system's Control Center + Charter instead of hardcoding Executive paths.
- Every `*.system.json` must declare `label` + `folders`.

# Backward compatibility — proof

Executive output must not change. A per-file SHA-256 **golden snapshot** of the current Executive subtree was captured before the refactor; after the refactor + Executive migration, the recompiled Executive subtree is **byte-identical** (55/55 files). This is the acceptance gate for Stage 1.

# Rollout (status: complete)

- **Stage 1 — committed (`439e975`):** generic compiler + `executive.system.json` migration + byte-identical proof (55/55) + validation + smoke. Passed.
- **Stage 2 — committed (`bb99a6e`):** `operations.system.json` (BS-002) migrated to the folder object model + Operating System Protocol and Approval Rules knowledge objects + validation + smoke. Executive parity re-verified.

## Post-adoption additions (committed, founder-approved)

- **Decision-registry fallback:** a system with no `decision_management` folder folds its Decision Registry into its `decisions` folder (Operations); Executive unchanged.
- **Overridable charter wording:** optional system-level `operating_boundary` / `success_condition` (defaults reproduce Executive; Operations overrides them).
- **Project Registry** generated at `06 Registry/Project Registry.md` from copied Project inputs; **`referenced-external`** knowledge-source convention (non-resolving by design) — commit `f8d1138`.
- **Per-system byte-identical golden regression tests** (`tests/goldens/001.sha`, `002.sha`) — commit `1e47d2a`.
- **Per-system anatomy retained** (Option A, founder-approved 2026-07-26); no shared-shell standard adopted.

# Validation Required

- architecture · naming · links · YAML · ontology · registries · acceptance tests · release gates · Executive byte-identical parity

# Rollback

All changes on `main` via reviewable commits; generated output is disposable/gitignored. Revert the Stage commit + recompile to restore the prior compiler; the golden snapshot proves restoration.
