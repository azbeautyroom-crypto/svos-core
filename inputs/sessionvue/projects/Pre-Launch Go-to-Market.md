---
title: Pre-Launch Go-to-Market
object_type: project
status: in-progress
owner: founder
updated: 2026-07-24
version: 1.0.0
contract: CONTRACT-001
source_of_truth: true
generated: false
source: "SessionVue-OS/02 Projects/SessionVue/60 Marketing/Pre-Launch Go-to-Market.md"
---

# Project — Pre-Launch Go-to-Market (content → waitlist)

## Objective

The umbrella project for everything between a stranger seeing the founder's content and a beauty professional on the waitlist.

**Goal (founder, verbatim):** get beauty professionals interested and ultimately signed up for the waitlist. The app is the destination; the content is the front door.

## Status (verbatim from source)

- project_status: **LIVE 2026-07-24 — content-pipeline runner installed (07:45 daily); brief extended with GTM section**
- next_action: **Founder red-pens the first content queue (60 Marketing/Content/Queue/2026-07-24)**

## The Funnel

Content (6 platforms) → landing page → waitlist (stage-routed) → gates-open conversion.

- Platforms: Instagram, TikTok, YouTube, email/newsletter, Pinterest, blog/SEO
- Cadence: daily (founder commitment, 2026-07-24)
- Destination: the built waitlist landing page (deploy blocked on domain — this project's biggest dependency)
- Conversion: career-stage routing (already built)

## Automations (consolidated — one new runner, not four)

| # | Automation | How it lands |
|---|---|---|
| 1 | Content pipeline (daily) | NEW runner (Daily-Brief pattern; vault-write-only). Drafts the day's queue per platform for the founder's red pen. Drafts only — nothing publishes itself. |
| 2 | Funnel report (daily) | Extends the existing daily brief — signups by career stage. Per-platform split BLOCKED on a source/UTM field. |
| 3 | Email drafts | Folded into runner #1 — missing stage tracks drafted into review. Sends stay manual and domain-blocked. |
| 4 | Project brief | Folded into the existing daily brief — GTM section (queue status, funnel numbers, blockers, next action). |

**Boundaries:** vault-write-only; never posts to a platform, never sends an email, never touches repo/db/prod. All drafts obey the Voice-Guide (incl. the no-external-names hard line).

## Dependencies / Blockers

- Landing-page deploy (sending-domain blocker).
- Source/UTM attribution field — blocks the per-platform funnel split (founder decision).

## Connected Systems

- System 002 — Content Engine (this project's engine): `80 Operations/Systems/002 Content Engine/Control Center`
- System 001 — Professional Waitlist: `80 Operations/Systems/001 Professional Waitlist/Control Center`

## Completion Condition

`NOT IN SOURCE — needs founder`

## Metrics

- Signups by career stage (funnel report). Per-platform split: `NOT IN SOURCE` (blocked on the source/UTM field).
