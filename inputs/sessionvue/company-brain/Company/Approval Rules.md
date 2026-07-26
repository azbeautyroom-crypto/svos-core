---
title: Approval Rules
object_type: knowledge
status: review
owner: founder
updated: 2026-07-26
version: 1.0.0
contract: CONTRACT-001
source_of_truth: true
generated: false
---

# Approval Rules

Canonical rules for what requires founder approval and how approvals are routed. Consumed by the Operations System (BS-002) approval-routing path.

## Source

Assembled from approved sources: the SVOS Execution Contract (`contracts/EXECUTION_CONTRACT.md`, CONTRACT-001) approval requirements and the locked Founder Directives (`Facts.md` §10). Where a specific approval threshold is not recorded, it is marked `NOT IN SOURCE`.

## What requires founder approval

- Strategic changes, company-wide policies, and final company-level decisions.
- Resource-allocation changes (time, money, capacity, strategic attention).
- Architecture changes (require an ADR, per Change Control).
- New external write permissions, production/database writes, sending or publishing.
- Activating any automation (dry run first; founder approval before activation).

## Approval object requirements (Execution Contract)

Every Approval must define: the requested decision, evidence, approver, options, result, expiration, and follow-up actions. Every approval names an approver.

## Locked approval-related directives

- Waitlist RLS: anon-INSERT-only forever; anon SELECT never (LOCKED 2026-07-22).
- No file auto-merge: never merge/compress existing files without founder approval (LOCKED 2026-07-25).
- Build on demand: systems built when real need exists; no empty scaffolds (LOCKED 2026-07-22).

## Routing

Operations routes items requiring founder approval to the founder approval queue and tracks approval aging; it does not itself grant approvals. Founder decisions are owned by Executive.

## Thresholds

Specific numeric approval thresholds (e.g., spend limits): `NOT IN SOURCE — needs founder`.

## Authority

Canonical; subordinate to current founder instruction and locked decisions.

## Review Cadence

On any founder ruling that changes approval policy; otherwise at each package release.

## Update Conditions

Update only from an approved founder ruling or a verified change to the Execution Contract / Facts.md. Never edit generated output; correct this input and recompile.

## Conflict Handling

The Execution Contract governs approval object structure; `Facts.md` is canonical for locked decisions. A rule absent from source is `NOT IN SOURCE`, not assumed.
