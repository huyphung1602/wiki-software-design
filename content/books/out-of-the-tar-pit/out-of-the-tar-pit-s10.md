---
title: "S10: Example of an FRP System"
tags: [frp, relational-model, example]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# S10: Example of an FRP System

This section demonstrates [[functional-relational-programming]] through an estate agency system. The example tracks properties, offers, owner decisions, and agent commissions, illustrating all four FRP components.

**Essential State** is defined as six base relvars: Property, Offer, Decision, Room, Floor, and Commission. Each relvar has typed attributes. Only data that users directly input (property registrations, offers, decisions) is treated as essential state.

**Essential Logic** includes three pure functions (price band classification, area code mapping, sale speed calculation) and thirteen derived relations. Internal derived relations like Acceptance (positive decisions), CurrentOffer (latest offer per bidder per property), RawSales (accepted offers joined with property data), and SalesCommissions build on each other using relational algebra. External derived relations -- OpenOffers, PropertyForWebSite, CommissionDue -- serve direct user needs. The entire business logic is expressed declaratively without control flow or mutable variables.

**Integrity Constraints** enforce candidate and foreign keys, plus domain-specific rules: every property must have at least one room; owners cannot bid on their own property; no offers after a sale; at most 50 premium properties on the website; at most 10 offers per bidder per property. Because constraints are declarative and non-interacting, adding new ones increases complexity only linearly. The FRP infrastructure automatically rejects any state modification that would violate constraints.

**Accidental State and Control** consists of three performance hints: store PropertyInfo (cache a derived relation), store Room and Floor together (denormalize physically without affecting logical separation), and store Property photos separately (infrequently accessed). These hints affect only physical storage, not the essential system.

The example powerfully demonstrates how FRP achieves separation: the business logic knows nothing about caching or storage strategy, and the performance hints know nothing about each other. Feeders and observers would be specified declaratively, potentially requiring no custom code.

Part of [[out-of-the-tar-pit]]

## Related
- [[functional-relational-programming]] — the architecture being demonstrated
- [[relational-model]] — the data foundation
- [[integrity-constraints]] — declarative rules that grow linearly
- [[accidental-state]] — performance hints separated from logic
- [[out-of-the-tar-pit-s09]] — Functional Relational Programming
- [[out-of-the-tar-pit-s11]] — Related Work
