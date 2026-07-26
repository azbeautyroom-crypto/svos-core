# SVOS Object Model
Version: 1.0.0
Status: LOCKED

---

# Purpose

Every entity inside SessionVue is represented as an Object.

Objects define the language of the operating system.

Objects are permanent.

Projects, Jobs, Workflows, and Automations operate on Objects.

Objects never depend on Projects.

Projects depend on Objects.

---

# Core Rule

Everything in SVOS is either:

• An Object
• A Relationship
• A State
• An Event

Nothing else exists.

---

# Object Hierarchy

SVOS

↓

Business System

↓

Project

↓

Workflow

↓

Job

↓

Automation

↓

Output

↓

Metric

---

# Object Types

## Company

Represents the business.

Source of Truth

Company Brain

---

## Business System

Permanent operating department.

Examples

Executive

Operations

Marketing

Engineering

Finance

Analytics

Customer Success

Support

Legal

People

---

## Project

Temporary initiative.

Created

Executed

Archived

Never permanent.

---

## Workflow

Defines execution order.

Reusable.

Can be activated by multiple Projects.

---

## Job

Atomic unit of work.

Jobs belong to Business Systems.

Projects activate Jobs.

Jobs produce Outputs.

---

## Automation

Executes Jobs.

Never changes architecture.

Never owns knowledge.

---

## Decision

Permanent company decision.

Stored forever.

Versioned.

Founder approval required when strategic.

---

## Metric

Represents measurable performance.

Examples

Revenue

MRR

Activation

Retention

Bookings

Waitlist

Conversion

Content Velocity

---

## Integration

External system connected to SVOS.

Examples

GitHub

Supabase

Airtable

PostHog

Sentry

Google Workspace

Cursor

Claude

Obsidian

Email

---

## Asset

Reusable company resource.

Examples

Brand

Logo

Template

Prompt

Video

Graphic

Document

---

## Customer

Represents every user type.

Beauty Client

Visitor

Launch Pro

Growth Pro

Power Pro

Salon

Brand

Educator

Agency

Vendor

---

# Every Object Has

ID

Name

Description

Owner

State

Source of Truth

Relationships

Created

Updated

Version

---

# Object Lifecycle

Created

↓

Validated

↓

Active

↓

Deprecated

↓

Archived

Objects are never deleted.

---

# Ownership

Every Object has exactly one owner.

Objects may have multiple consumers.

Objects may never have multiple owners.

---

# Source of Truth

Every Object points to exactly one canonical location.

Duplicate ownership is prohibited.

---

# Relationships

Objects reference each other.

Objects never duplicate each other.

Relationships are directional.

Company

↓

Business System

↓

Project

↓

Workflow

↓

Job

↓

Automation

↓

Output

↓

Metric

---

# Generated Objects

Business Systems

Projects

Jobs

Registries

Indexes

Dashboards

Validation Reports

All generated from templates.

Never become canonical.

---

# Canonical Objects

Company Brain

Architecture

Templates

Specifications

Brand

Mission

Vision

Pricing

Memberships

These are authored manually.

Everything else compiles from them.

---

# Validation Rules

Every Object must

Have an owner

Have an ID

Have a Source of Truth

Have relationships

Have a lifecycle

Pass validation

No orphan Objects.

No duplicate Objects.

No circular ownership.