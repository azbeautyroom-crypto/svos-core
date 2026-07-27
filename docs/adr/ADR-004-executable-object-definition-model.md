# ADR-004 — Executable Object Definition Model (EODM)

Status: accepted
Date: 2026-07-26
Owner: founder
Decision Type: architecture
Related: ADR-002 (folder object model), CONTRACT-001 (Execution Contract), SVOS Constitution (Art. V, VI, IX, XI, XII)
Extends: ADR-002's "names → objects" principle, applied to executable objects
Does NOT modify: ADR-002, the SVOS Constitution, or ownership boundaries

# 1. Context

SVOS Core v1 is complete. Executive (BS-001), Operations (BS-002), and Marketing (BS-003) are canonical
Business Systems — compiled, golden-locked, and `status: review`. They are **authored** but not yet
**operable**: their Jobs, Metrics, and Automations exist as objects but carry no executable content.

An Operationalization Framework assessment, an Operational Object Model (OOM) architecture session, and
an adversarial ADR-004 Design Package were completed. The Design Package concluded (Recommendation B) that
the correct next evolution is a **narrowed** change: enrich executable-object *definitions* only, and defer
Operating State and Evidence to a future ADR. This ADR authors that decision.

# 2. Problem Statement

An authored Business System cannot become operable while its executable objects are name-only. CONTRACT-001
mandates a 19-section execution anatomy that every governed object "must define," but the input model
carries only names, so the compiler renders those sections as `NOT IN SOURCE`. A Job with no real trigger,
steps, decision logic, permissions, or completion condition cannot be executed deterministically by a human
or delegated deterministically to an agent.

The minimum constitutional evolution required is a **carrier** for the execution definition that
CONTRACT-001 already requires — nothing more.

# 3. Repository Evidence

- Executable objects are name strings; each generated Metric has 7 `NOT IN SOURCE` fields.
- CONTRACT-001 defines the 19 mandatory execution sections (Purpose … Improvement Loop) every governed
  object "must define."
- CONTRACT-001 L195: "Knowledge must never silently contain a procedure that should be a Job" — so
  execution definitions cannot be smuggled into Company Brain / Knowledge.
- The compiler already accepts **string-or-object** for `connected_systems` (`cs_name`) and
  `knowledge_sources` (`ks_path`) — the backward-compatible pattern already exists.
- Every compiled object is `status: review` — **nothing is executing today**, so an Operating State /
  Evidence layer would have no runs to store.

# 4. Decision

Adopt the **Executable Object Definition Model (EODM)**: each executable object (Job, Metric, Automation)
MAY be authored in canonical input as a **definition object** carrying the CONTRACT-001 execution anatomy,
instead of a bare name. The compiler renders the real content when a definition is present, and falls back
to the current name-only rendering when it is not.

EODM addresses exactly **one** stage of the execution lifecycle — the canonical definition:

```
[ Canonical Definition ]  → Execution → Evidence → Operating State → Improvement ↺   (EODM = the first stage only)
```

The remaining stages are out of scope (§6, §11).

## Canonical definition per object

Fields are **canonical** because they are the stable "what the object is" (Constitution Art. V); anything
that varies per run is **prohibited** from canonical input because it is operating state (Art. VI), deferred.

**Job** (definition object) —
- Required: `trigger`, `inputs`, `required_sources`, `preconditions`, `execution` (ordered steps),
  `decision_logic` (IF / THEN / ESCALATE), `outputs`, `destinations`, `updates`, `validation`, `approval`,
  `exceptions`, `permissions` (`allowed_reads` / `allowed_writes` / `prohibited_actions`),
  `completion_condition`, `improvement_loop`.
- Optional: `connected_objects`, `dry_run`, `escalate_when`, `metrics_fed`.
- Prohibited (operating state, deferred): run instances/state, per-run outputs/values, run timestamps,
  evidence records.

**Metric** (definition object) —
- Required: `definition`, `formula`, `source`, `cadence`, `target`, `warning_threshold`,
  `failure_threshold`, `action`, `owner`.
- Optional: `measured_object`, `improvement_link`.
- Prohibited: current value, time series, last-measured timestamp.

**Automation** (definition object) —
- Required: `executed_job` (binding to a Job), `trigger`, `tools`, `credential_refs` (references only),
  `permissions`, `dry_run`, `approval_gate`, `monitoring`, `retries`, `rollback`, `disable_procedure`,
  `enabled`.
- Optional: `schedule`, `connected_objects`.
- Prohibited: credential values, last-run / logs / health, live external effects.

The delegation fields (`permissions`, `approval`, `dry_run`, `escalate_when`) make human execution and AI
delegation identically deterministic and bounded (Constitution Art. XII; CONTRACT-001 §13/§15). EODM
defines only these governing fields — it designs no agents.

# 5. Architectural Scope

In scope:
- Executable-object input schema: name string **or** definition object (reusing the existing
  string-or-object mechanism).
- The CONTRACT-001 execution anatomy as the definition shape for Job / Metric / Automation.
- A compiler **rendering extension** (render real content when a definition is present; string fallback
  otherwise). Implementation of that extension is a **separate, founder-approved implementation session** —
  this ADR authorizes the model, not the code.

# 6. Explicit Non-Goals

ADR-004 does **not** introduce, and forbids bundling:
- **Operating State** (deferred — §11).
- **Evidence architecture** (evidence records, evidence ledger — deferred; note: "Execution Event" and
  "Evidence Ledger" were classified as implementation details, not architecture).
- **Runtime execution** of any object.
- **AI agents** (only the governing object fields that bound them).
- **Analytics or any new Business System.**
- Any change to **ADR-002**, the **SVOS Constitution**, the **Object Model's ownership boundaries**, or
  multi-tenant structure.

# 7. Backward Compatibility

- Input accepts a **name string OR a definition object** per executable object; the two coexist within and
  across systems.
- Un-enriched (string) objects render exactly as today, including their `NOT IN SOURCE` sections.
- Therefore Executive, Operations, and Marketing remain **byte-identical** until deliberately enriched
  (golden regression is the guarantee).

# 8. Migration Strategy

- **Opt-in, per object, need-driven** (Operating Doctrine "build on need"): enrich one object at a time,
  starting with the system being operationalized.
- No forced rewrite; a system may hold a mix of name-only and enriched objects.
- Enrichment is authored in the owning Business System's canonical input (never in Company Brain — Art. VII;
  CONTRACT-001 L195); definitions **reference** canonical truth via `required_sources`, they do not copy it.
- The compiler rendering extension ships in a later approved implementation session; a system's golden
  baseline is re-emitted only when that system is deliberately enriched.

# 9. Acceptance Gates

Before any EODM implementation may be accepted:
1. Un-enriched systems remain **byte-identical** (goldens `001.sha`, `002.sha`, `003.sha`).
2. Name-string and definition-object **coexist** (a mixed input compiles).
3. An enriched object renders every applicable CONTRACT-001 section with **real content**
   (0 `NOT IN SOURCE` for enriched fields).
4. Canonical/operating boundary holds: **no runtime value, state, or evidence** appears in canonical input.
5. Delegation bounds present on enriched Jobs/Automations (`permissions`, `approval`, `dry_run`,
   `escalate_when`); **no self-expansion** of authority (Art. XII).
6. **No Company Brain duplication** — definitions reference, not copy (Art. VII).
7. `validate_generated` + the full regression suite pass; enriched systems get a fresh golden baseline.
8. **ADR-002 unchanged; Constitution unchanged.**

# 10. Consequences

- Business Systems become **operable**: an enriched Job/Metric/Automation carries real, deterministic
  content executable by a human or a bounded agent.
- One shared definition model serves **all** current and future systems (Analytics, Product, Engineering,
  Sales, Customer Success), reducing future architectural complexity — no per-system operational mechanism.
- Canonical inputs grow for enriched objects; mitigated by enriching only objects that actually operate.
- "Operable" is not yet "fully operational": tracking, automation of runs, and the improvement loop require
  the deferred Operating State / Evidence layer (§11).

# 11. Future Work — Operating State and Evidence (deferred)

Operating State (Art. VI) and Evidence (Art. VI/XI) are real and constitutionally grounded but **premature**:
nothing executes yet, so there is no evidence to store. They are deferred to a **separate future ADR
(ADR-005)**, gated on the first real execution of an enriched object. That ADR will define the minimum
lifecycle stages that follow the definition — Execution → Evidence (validated) → Operating State →
Improvement — and must itself preserve the Constitution, golden parity, and backward compatibility.

# Rollback

Governance/document only. This ADR authors a model; no code changes ship with it. Reverting it removes the
EODM direction with no effect on generated output.

# Founder Decision

`ACCEPTED` — 2026-07-26. EODM adopted as the next constitutional evolution (definitions only; Operating State and Evidence deferred to ADR-005). Compiler implementation is a separate, founder-approved session.
