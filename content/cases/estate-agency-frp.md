---
title: Estate Agency FRP System
tags: [case, functional-relational-programming, relational-model, architecture]
concepts: [functional-relational-programming, accidental-state, relational-model, integrity-constraints, referential-transparency, data-independence]
sources: [out-of-the-tar-pit]
crossroad: false
created: 2026-04-09
updated: 2026-04-09
---

# Estate Agency FRP System

## The Story

Moseley and Marks present a complete hypothetical Estate Agency system built using Functional Relational Programming (FRP). The domain is familiar: an agency sells properties, buyers make offers, owners accept or reject offers, and agents earn commission on successful sales.

The system is small — six base relations, thirteen derived relations, seven integrity constraints, three user-defined functions. Yet it is complete enough to show how the FRP architecture eliminates an entire category of bugs: the "bad state" bug. In traditional systems, a bug in business logic can leave the database in an inconsistent state — a sale recorded without a matching offer, or an agent paid commission on a property that never sold. In FRP, the infrastructure rejects any transaction that would violate a constraint, before it touches the database.

## Fragments

### Six Base Relations — Essential State

All essential state lives in six flat relations. Each relation is a table with named, typed columns. There are no objects, no pointers, no nested structures.

```frp
def relvar Property :: {address, price, photo, agent, dateRegistered}
def relvar Offer :: {address, offerDate, bidderName, bidderAddress, offerPrice}
def relvar Decision :: {address, offerDate, bidderName, bidderAddress, decisionDate, accepted}
def relvar Room :: {address, roomName, width, breadth, type}
def relvar Floor :: {address, roomName, floor}
def relvar Commission :: {priceBand, areaCode, saleSpeed, commission}
```

`Property` records each listing. `Offer` records every bid ever made. `Decision` records each owner's response to an offer. `Room` and `Floor` describe the physical property. `Commission` defines how agents are paid based on price band, area, and sale speed.

The design is purely relational — relationships between entities are expressed through matching attribute values, not through object references or foreign key pointers baked into the structure.

### Thirteen Derived Relations — Computed on Demand

Rather than storing computed values, FRP derives them. The system defines thirteen derived relations — equations that always hold true as the base data changes.

The internal derived relations exist to support other derivations. `RoomInfo` extends each room with its computed area:

```frp
RoomInfo = extend(Room, (roomSize = width * breadth))
```

`PropertyInfo` extends each property with its price band, area code, room count, and total square footage:

```frp
PropertyInfo = extend(Property,
  (priceBand    = priceBandForPrice(price)),
  (areaCode     = areaCodeForAddress(address)),
  (numberOfRooms = count(restrict(RoomInfo | address == address))),
  (squareFeet   = sum(roomSize, restrict(RoomInfo | address == address))))
```

External derived relations are what users care about. `OpenOffers` shows current bids with no decision yet. `PropertyForWebSite` shows unsold properties for the website. `CommissionDue` shows each agent's total commission:

```frp
CommissionDue = project(
  summarize(SalesCommissions, project(SalesCommissions, agent),
    totalCommission = sum(commission)),
  agent, totalCommission)
```

Because these are derived rather than stored, the infrastructure maintains them automatically. There is no cache to invalidate, no trigger to debug, no materialized view to keep in sync.

Illustrates: [[data-independence]], [[relational-model]]

### Seven Integrity Constraints — Rules That Cannot Be Violated

Constraints are boolean expressions that must always evaluate to true. The infrastructure checks them on every state change and rejects anything that would break a rule.

Standard constraints define keys and foreign keys:

```frp
candidate key Property = (address)
candidate key Offer = (address, offerDate, bidderName, bidderAddress)
foreign key Offer (address) in Property
foreign key Decision (address, offerDate, bidderName, bidderAddress) in Offer
```

Domain-specific constraints express business rules declaratively. No bidder may offer on their own property:

```frp
count(restrict(Offer | bidderAddress == address)) == 0
```

No offers may be placed after a sale is agreed:

```frp
count(restrict(join(Offer, project(Acceptance, address, decisionDate))
  | offerDate > decisionDate)) == 0
```

Max 10 offers per bidder per property:

```frp
count(restrict(summarize(Offer,
  project(Offer, address, bidderName, bidderAddress),
  numberOfOffers = count())
  | numberOfOffers > 10)) == 0
```

Critically, constraints cannot interact. Each is evaluated independently, so constraint complexity grows linearly, not quadratically. This is the declarative advantage: state a rule once, and the infrastructure enforces it everywhere, forever.

Illustrates: [[integrity-constraints]]

### Feeders and Observers — The Boundary

The relational core knows nothing of the outside world. Feeders convert user input into relational assignments. Observers watch derived relations and produce output.

```frp
Property := Property ∪ {new property tuple}
```

The infrastructure validates every assignment against all constraints before applying it. If a assignment would violate any constraint — say, accepting an offer on a property that already has a sale — the entire transaction is rejected. The database is never left in an invalid state.

Illustrates: [[accidental-state]]

### Pure Functions — No Hidden State

Three user-defined functions compute derived values: `priceBandForPrice`, `areaCodeForAddress`, `datesToSpeedBand`. Each is purely functional — given the same inputs, they always return the same output, with no access to any state.

```frp
priceBandForPrice(250000) → PREMIUM
areaCodeForAddress("123 Main St") → CITY
datesToSpeedBand(registered, sold) → FAST
```

Because these functions are pure, they can be composed freely in derived relation definitions without concern for ordering or hidden dependencies. They are independently testable: test once, trust everywhere.

Illustrates: [[referential-transparency]]

## Source

- [[out-of-the-tar-pit-s09]] — Functional Relational Programming overview
- [[out-of-the-tar-pit-s10]] — Estate Agency system in detail
