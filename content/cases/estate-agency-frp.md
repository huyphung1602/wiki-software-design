---
title: Estate Agency FRP System
tags: [case, functional-relational-programming, relational-model, architecture]
concepts: [functional-relational-programming, essential-state, accidental-state, relational-model, integrity-constraints, referential-transparency, data-independence, access-path-independence, declarative-specification, separation-of-concerns]
sources: [out-of-the-tar-pit]
crossroad: false
created: 2026-04-09
updated: 2026-04-09
---

# Estate Agency FRP System

## The Story

Moseley and Russell's paper presents a complete hypothetical Estate Agency system built using Functional Relational Programming (FRP). The system manages property listings, bids from potential buyers, and agent commissions. Rather than showing toy examples, the paper walks through a realistic domain: properties have rooms and floors, buyers make offers, decisions are made on offers, and agents earn commission based on sale speed and price band.

The system is specified entirely in terms of relations — no nested structures, no object references, no mutable state. The essential logic is expressed as relational algebra extended with pure user-defined functions. All integrity constraints are declared declaratively and enforced by the infrastructure. The result is a system where errors in business logic can never put the database in a "bad state" — the worst that can happen is the infrastructure rejecting a transaction that would violate a constraint.

## Fragments

### Essential State as Relations

All essential state in the Estate Agency system takes the form of flat relations with no nesting. The base relvars include Property (address, price, agent, dateRegistered), Offer (address, offerDate, bidderName, bidderAddress, offerPrice), Decision (address, offerDate, bidderName, bidderAddress, accepted), Room (address, roomName, width, breadth, type), Floor (address, floorName), and Commission (priceBand, areaCode, saleSpeed, commission).

Notably, there are no product types — no nested records, no object references linking entities. The relational model handles all associations through attribute values rather than pointers. This design choice means the system has no "access paths" baked into the data structure — any relationship between data can be queried ad-hoc rather than being predetermined.

Illustrates: [[essential-state]], [[relational-model]], [[access-path-independence]]

### Derived Relations via Relational Algebra

The system defines 13 derived relations using the eight relational algebra operators (restrict, project, product, union, intersection, difference, join, divide) extended with aggregation. These include internal derived relations like RoomInfo (extends Room with computed area), Acceptance (accepted offers), Rejection (rejected offers), PropertyInfo (extends Property with computed priceBand, areaCode, numberOfRooms, squareFeet), CurrentOffer (most recent offer per bidder per property), and external derived relations like OpenOffers (current offers without a decision), PropertyForWebSite (unsold properties for external display), and CommissionDue (total commission per agent).

The derived relations are defined declaratively — for example:

```
RoomInfo = extend(Room, (roomSize = width*breadth))
OpenOffers = join(CurrentOffer, minus(project_away(CurrentOffer, offerPrice), project_away(Decision, accepted decisionDate)))
```

Because these are derived rather than stored, the infrastructure maintains them automatically as base data changes. No triggers, no materialized view maintenance code — just equations that always hold.

Illustrates: [[declarative-specification]], [[relational-model]], [[data-independence]]

### Integrity Constraints as Boolean Expressions

The system specifies integrity constraints declaratively using relational algebra expressions that must evaluate to true at all times. The infrastructure rejects any state modification that would violate a constraint.

Standard constraints include candidate keys and foreign keys (e.g., every Offer address must exist in Property). Domain-specific constraints are more interesting: a rule that no bidder may submit an offer on their own property (owners are assumed to reside at the address they're selling), a rule that no offers may be submitted after a sale is agreed, a rule limiting the website to 50 PREMIUM price band properties, and a rule that no single bidder may have more than 10 offers on any one property.

The constraint checking is entirely declarative:

```
count(restrict(Offer | bidderAddress == address)) == 0
count(restrict(join(Offer, project(Acceptance, address decisionDate)) | offerDate > decisionDate)) == 0
```

Critically, constraints cannot interact with each other — each is evaluated independently. This means constraint complexity grows linearly, not quadratically.

Illustrates: [[integrity-constraints]], [[declarative-specification]]

### Feeders, Observers, and the Outside World

The FRP architecture cleanly separates the relational core from the outside world. Feeders convert user input into relational assignment commands — they observe external events and translate them into state changes. Observers watch derived relvars and generate output when they change.

A key insight: feeders and observers never directly modify derived state. If a feeder observed some output and fed it back as input, it would create derived accidental state masquerading as essential state. The only things that enter the system as essential state are genuinely external inputs (new properties, offers, decisions from agents).

The infrastructure mediates all state changes:

```
relvar := newRelationValue
```

If this assignment would violate an integrity constraint, the infrastructure rejects it outright.

Illustrates: [[separation-of-concerns]], [[essential-state]]

### Referential Transparency in User Functions

The user-defined functions (priceBandForPrice, areaCodeForAddress, datesToSpeedBand) are purely functional — they accept arguments and return values without accessing or modifying any state. This means the same function call with the same arguments always returns the same result, anywhere in the system.

This referential transparency has direct testing benefits: function behavior can be verified once and trusted everywhere. It also means the functions can be composed freely in derived relation definitions without concern for hidden dependencies or ordering effects.

The paper notes this is a deliberate design choice: FRP forbids functions from accessing state, ensuring the functional component of the logic is always safe to reason about in isolation.

Illustrates: [[referential-transparency]]

## Source

- [[out-of-the-tar-pit-s09]] — Functional Relational Programming overview
- [[out-of-the-tar-pit-s10]] — Estate Agency system in detail
