---
title: Essential State
aliases: [essential data, user input state]
tags: [core-concept, state, functional-programming, software-design]
sources: [out-of-the-tar-pit]
created: 2026-04-09
updated: 2026-04-09
---

# Essential State

Essential state is the state that a system must retain because the problem domain requires it — data that users directly input and that the system must remember for future reference. Moseley and Marks draw a sharp line: if the team could produce a correct system without retaining this data, it is not essential. The "have to" is the test.

## What Makes State Essential

Essential state falls into two categories:

**Input data** — data provided directly by users or external systems. If the requirements say the system may need to refer to this data in the future, it must be retained. Example: a property listing's address and price. The system must remember these because future decisions (offers, sales, commissions) depend on them.

**Derived data that cannot be re-derived** — some mutable derived data cannot be recomputed from inputs alone because it depends on previous values. The canonical example is a game opponent's position in an interactive game — while theoretically derivable from all prior moves, the derivation would be impractical.

The key discriminator is whether the data could be omitted in the ideal world (no performance concerns, perfect language and infrastructure). If it could be re-derived on demand, it is accidental, not essential.

## Essential State in FRP

In Functional Relational Programming, essential state is the foundation of the system. All essential state takes the form of relations — flat tables with named, typed attributes. The decision to use relations is deliberate: relations provide [[access-path-independence]], [[data-independence]], and a natural home for [[integrity-constraints]].

The essential state specification is completely self-contained. It makes no reference to the logic layer or the accidental layer. Changes to the essential state specification may require changes to the logic, but changes to the logic can never require changes to the essential state specification. This one-way dependency is what enables reasoning about each layer independently.

In the Estate Agency example, Property, Offer, Decision, Room, Floor, and Commission are all essential state. They are what the users care about — what was listed, what was offered, what was decided.

## Essential vs Accidental State

The distinction matters because only essential state must be maintained by the core system. Accidental state — caches, derived data stored for performance, materialized aggregates — can be recomputed or delegated to the infrastructure layer.

A common mistake is treating accidental state as essential. If a system stores "customer total spending" as a separate field that could be computed from the transaction history, that field is accidental state. The essential state is the transactions; the total is derived. Keeping the total in sync with the transactions is unnecessary work that introduces complexity and potential for inconsistency.

The practical test: if the stored value could be recomputed from other stored values with no loss of information to the user, it is likely accidental.

## Cases

- [[estate-agency-frp]] — the Estate Agency system's base relvars (Property, Offer, Decision, Room, Floor, Commission) are all essential state: data directly input by users that must be retained and reasoned about (from Out of the Tar Pit)

## Related

- [[accidental-state]] — the counterpart: state that exists for implementation convenience, not problem requirements
- [[functional-relational-programming]] — the architecture that isolates essential state in the relational layer
- [[state-and-complexity]] — why state (essential or accidental) causes complexity
- [[integrity-constraints]] — rules that essential state must satisfy
- [[relational-model]] — the data structure used to represent essential state in FRP
