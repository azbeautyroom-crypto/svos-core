---
title: Founder Directives
object_type: knowledge
status: review
owner: founder
updated: 2026-07-27
version: 1.2.0
contract: CONTRACT-001
source_of_truth: true
generated: false
---

# Founder Directives

## Locked Directives (never change without explicit founder approval)

| Directive | Ruling | Locked |
|---|---|---|
| Pricing display | Symbol-only ($/$$/$$$); three-layer naming (backend/form/display) | 2026-07-25 |
| Tier language | Stages, not hierarchy; forbidden-terms list enforced | 2026-07-24 |
| Voice: no external names | Zero competitors/partners named in brand/marketing | 2026-07-21 |
| Waitlist RLS | Anon-INSERT-only forever; anon SELECT never | 2026-07-22 |
| Build on demand | Systems built when real need exists; no empty scaffolds | 2026-07-22 |
| One launch event | Single gates-open, not sequential rollouts | 2026-07-24 |
| No file auto-merge | Never merge/compress existing files without founder approval | 2026-07-25 |
| Red-pen rule | Founder corrections fold into Voice-Guide with date | LOCKED |
| No spaced dash in brand writing | Never use spaced dash punctuation in SessionVue or founder-facing writing; rewrite instead (hyphens in compounds OK; meta/code out of scope) | 2026-07-27 |
| Audience language | Never “pros”; use beauty professionals / licensed beauty professionals / professionals / beauty business owners / artists / experts / Industry Leaders (when that role is meant) | 2026-07-27 |
| Industry Leaders term | Canonical term for trusted specialty-region professionals; replaces temporary “Power Pros”; apply consistently | 2026-07-27 |
| Rejected waitlist framing | Never “joining the story before the first chapter” or close story/chapter rewrites | 2026-07-27 |
| Founder social identity | Founder social handles `NOT IN SOURCE` until founder-supplied; never infer; `azbeautyroom` is not the founder personal account | 2026-07-27 |
| Brand lanes | Founder lane (Angel Platt) and company lane (SessionVue) stay separate; no legacy project handle in founder lane | 2026-07-27 |
| Mission vs GTM | Permanent Mission = organize discovery; “Content first, software second” = GTM strategy only | 2026-07-27 |
| Dual discovery worlds | Client Discovery and Professional Discovery stay separate; same Session, different exposure; never merge (product principle; detail in Product Brain) | 2026-07-27 |
| Product Brain ownership | Single Product Brain owns product intent/truth including Session principle; no Customers Brain; BS-005 deferred until Brain matures | 2026-07-27 |
| Product Brain / Implementation Audit split | Product Brain = founder product specification (intent only). Product Implementation Audit = living engineering reference (code reality + gaps vs Brain). Link the two; never merge. The Audit does not redefine product truth. Marketing expresses Product Brain; it does not treat the Audit as product truth. | 2026-07-27 |

Source: `Facts.md` §7, §10; founder language and product architecture rulings 2026-07-27 (including Product Brain / Implementation Audit architecture).

## Source

Authored from 10 Company/Facts.md (canonical source of truth, owner: founder). Where the canonical source has no value, the field is marked `NOT IN SOURCE — needs founder` rather than invented.

## Authority

Canonical. Subordinate only to current founder instruction and locked founder decisions. If any other document conflicts, this Company Brain and `Facts.md` win.

## Owner

Founder (Angel Platt).

## Consumers

Executive System (BS-001) and all downstream Business Systems, Projects, and Jobs that read company canonical Knowledge.

## Review Cadence

On every founder ruling that changes a locked fact; otherwise at each package release.

## Update Conditions

Update only from an approved founder ruling or a verified change to `Facts.md`. Never edit generated output; correct this input and recompile.

## Conflict Handling

`Facts.md` is the tie-breaker. A fact absent from source is `NOT IN SOURCE`, not assumed.
