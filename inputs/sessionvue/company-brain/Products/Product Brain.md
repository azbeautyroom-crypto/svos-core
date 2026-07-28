---
title: Product Brain
object_type: knowledge
status: review
owner: founder
updated: 2026-07-27
version: 2.1.1
contract: CONTRACT-001
source_of_truth: true
generated: false
---

# Product Brain

Canonical **founder product specification** for SessionVue. Single Product Brain for product intent/truth (founder ruling 2026-07-27). Do not split Product Brain into multiple Product Brain files until size genuinely requires modularization.

This document describes the **intended product**. It does not describe implementation state.

## Architecture (LOCKED 2026-07-27)

| Object | Owns | Does not own |
|---|---|---|
| **Product Brain** (this file) | Founder product specification; locked principles; intended lifecycles | Live code behavior; gap tracking |
| **[[Product Implementation Audit]]** | What the app does today; gaps vs this Brain; code evidence | Product truth; Marketing expression source |

Rules: **link; never merge.** Marketing expresses this Brain. The Audit is an engineering reference. Recording scope here does not authorize implementation. See Founder Directives: Product Brain / Implementation Audit split.

Product Business System (BS-005) remains deferred until this Brain matures.

---

## Audience concepts (owned here)

Client and Professional concepts are owned by Product Brain. There is no separate Customers Company Brain object (founder ruling 2026-07-27).

| Audience | Product experience |
|---|---|
| Clients | Consumer-focused Client Discovery only |
| Professionals (licensed beauty professionals) | Professional Discovery / knowledge network only |

## Locked product principles (LOCKED 2026-07-27)

### Discovery purpose

Everything in the product exists to increase discovery. Education, social features, booking, and content types exist because they improve discovery.

### Completed Session as core asset

The most important object in SessionVue is the **completed Session**. Everything begins with a completed appointment. A professional documents the completed Session once. That Session becomes the structured business asset that powers multiple systems. Professionals should never recreate the same work in multiple places. One completed Session should continue creating value after the appointment ends.

### Product principle (exclusive owner: Product Brain)

Every completed Session should simultaneously improve:

- Client discovery
- Professional discovery
- Marketing
- Reputation
- Education
- Future bookings

without requiring professionals to recreate the work.

Do **not** duplicate this principle in Business Model (founder ruling 2026-07-27).

### Dual discovery worlds (LOCKED)

The same completed Session powers **two** experiences. They intentionally expose different information. They must never merge.

| World | Audience | Rules |
|---|---|---|
| Client Discovery | Clients | Never show professional education. Consumer Library. Bookmark look. Book look. View service itinerary and service stack. Customize when needed. Receive itinerary before appointment. Attach inspiration bookmarks. No requirement to understand professional terminology. Goal: confidence booking curated services instead of guessing from a menu. |
| Professional Discovery | Professionals | Never show the simplified client experience. Professional knowledge network over completed Sessions. Structured professional information. Interconnected objects. Everything discoverable through something else. |

### Professional growth philosophy

Professionals should not need to become influencers to grow. Work becomes discoverable because it is structured correctly. The platform reduces manual marketing work. Professionals spend time performing appointments. The platform maximizes the value of those appointments afterward.

## Session knowledge model

A completed Session is not only a portfolio entry. It is a structured knowledge asset.

One completed Session simultaneously powers: Client Discovery, Professional Discovery, portfolio, reputation, marketing, education, and future bookings.

### Professional Session structure (non-exhaustive)

A Session may include structured professional information such as:

- Base Service
- Styles / Variations
- Techniques
- Products
- Formulas
- Notes
- Videos
- References

### Relationships

Every object connects to related objects. Opening a Base Service, Technique, Product, Style, or Formula shows every Session using that object. Knowledge is interconnected through relationships.

## Knowledge layers

Sessions are the foundation. Additional professional content types support Professional Discovery:

| Type | Role |
|---|---|
| Masterclasses | Long-form educational content |
| Techniques | Focused instructional content |
| Product Reviews | Product knowledge |
| Salon Tours | Business and workspace exploration |
| Discussions | Professional exchange of ideas |
| Feedback | Anonymous critique of completed work |

These are separate content types. All support professional discovery.

## Discussions (canonical scope; not implementation authorization)

Professionals can create Discussions. They choose audience, category, city, and state. Comments are ranked by agreement. Higher agreement surfaces higher. Disagreement lowers visibility. Goal: surface the strongest professional insight rather than simple chronology.

## Feedback (canonical scope; not implementation authorization)

Professionals can anonymously request feedback on completed work. Anonymous posting protects credibility while encouraging honest improvement. Feedback uses the same agreement-driven discussion model.

## Chair Marketplace (canonical scope; not implementation authorization)

Marketplace for workspace rentals. Professionals can list available chairs or workspaces. Others can rent hourly, half-day, daily, weekly, or longer-term. Goal: improve resource utilization and help new and traveling professionals access workspace.

## Client Discovery (filters)

Clients should discover professionals quickly using combinations such as:

Category · City · State · Specialty · Price Point · additional structured filters.

Discovery should be immediate. The platform organizes these relationships.

## Industry Leaders

Canonical term for trusted professionals within specific specialties and regions (replaces temporary “Power Pros” terminology; founder ruling 2026-07-27). Apply consistently throughout SessionVue.

Early platform growth begins with a curated group of Industry Leaders. As professionals onboard they connect into those networks. Industry Leaders gain visibility, authority, community, and additional discovery. Success inside SessionVue should strengthen their businesses outside the platform.

Membership **Power** tier (pricing and activation) remains defined in Membership Brain. Industry Leaders is the product/network term. Never use “pros” as shorthand.

## Professional Categories (14 canonical, verified 2026-07-21)

Lash Technician · Brow Specialist · Permanent Makeup (PMU) Artist · Hair Stylist · Nail Technician · Esthetician / Skin Specialist · Makeup Artist · Wax Specialist · Tan Specialist · Massage Therapist · Body Sculpting Specialist · Piercer · Laser Specialist · Aesthetic Injector.

TBD specialty lists (incomplete): Laser procedures, Body sculpting procedures, Dental categories. `NOT IN SOURCE — needs founder`.

## Platform

Supabase-backed. Waitlist live (anon-INSERT-only). Cities seeded: 6,610.

## Product Tiers

See [[Membership Brain]] for the Visitor / Launch / Growth / Power / Salon structure.

Membership capability intent that shapes discovery and booking (founder rulings recorded in Tier Architecture where labeled):

- Visitor: spectator; no booking access (founder ruling 2026-07-23).
- Launch: filtered discovery (findable); portfolio on own feed; booking begins at Launch.
- Growth: photo discovery (lookbook); Book this look; work compounds; tickets become education content.
- Power: by application + mandatory training only; Industry Leaders network role; never purchasable.

## Intended lifecycles (specification)

These name the product arcs the specification covers. **Do not treat this list as a claim about shipped code.** Implementation state: [[Product Implementation Audit]].

| Lifecycle | Intended outcome |
|---|---|
| Professional Lifecycle | Licensed beauty professionals enter, become findable at the correct membership stage, and operate without becoming influencers |
| Client Lifecycle | Clients discover and book with confidence inside Client Discovery only |
| Discovery Lifecycle | Discovery is organized; dual worlds never merge |
| Booking Lifecycle | Discovery becomes a reservation with look, itinerary, and inspiration context |
| Appointment Lifecycle | The appointment is performed; capture prepares the Session |
| Session Lifecycle | Completed appointment becomes the completed Session asset |
| Documentation Lifecycle | The Session is documented once into structured knowledge |
| Portfolio Lifecycle | Completed Session powers the professional’s portfolio |
| Lookbook Lifecycle | Client photo discovery and Book this look from Session exposure |
| Professional Discovery Lifecycle | Professionals discover knowledge through Sessions and knowledge layers |
| Client Discovery Lifecycle | Clients find professionals and looks without professional education |
| Review Lifecycle | Completed work compounds reputation |
| Education Lifecycle | Real work becomes teaching without recreation |
| Retention Lifecycle | Completed Sessions create future bookings and ongoing relationships |
| Compounding Lifecycle | One Session improves discovery, marketing, reputation, education, and future bookings without rework |

## Relationship to Product Implementation Audit

| Document | Owns |
|---|---|
| **Product Brain** (this file) | Founder product intent and locked principles |
| **[[Product Implementation Audit]]** | What the application does today; gaps vs this Brain; code evidence |

When intent and code disagree: Product Brain remains the specification; the Audit records the gap. Closing a gap requires founder authorization to change product or to change code. Recording a gap authorizes neither.

## Source

Founder business architecture rulings 2026-07-27; prior Facts.md §3–§6 (categories, platform, tier pointer); Membership Brain; Mission; Founder Directives; founder-labeled Tier Architecture rulings.

## Authority

Canonical product truth (intent). Subordinate only to current founder instruction and locked founder decisions. Marketing may express product truth; Marketing may not redefine it.

## Owner

Founder (Angel Platt). Future consumer/owner System: Product (BS-005), deferred until this Brain matures.

## Consumers

Executive and Marketing Systems (by reference); future Product System; Projects that touch product scope; any Job that states product truth; [[Product Implementation Audit]] (by reference for Desired End State).

## Review Cadence

On founder ruling that changes product principles or scope; otherwise each release.

## Update Conditions

Update only from an approved founder ruling. Never edit generated output; correct this input and recompile. Recording scope does not authorize build or deploy. Do not fold live implementation state into this file; update [[Product Implementation Audit]] instead.

## Conflict Handling

Product Brain wins on product truth (intent). Membership Brain wins on tier pricing and activation. Mission wins on company purpose. Voice Guide wins on expression rules (including never “pros”; use Industry Leaders where that role is meant). [[Product Implementation Audit]] wins on statements about what the code does today. A fact absent from source is `NOT IN SOURCE`, not invented.
