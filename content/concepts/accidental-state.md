---
title: Accidental State
aliases: [derived state, cached state, unnecessary state]
tags: [core-concept, state, complexity, software-design]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Accidental State

Accidental state is state that exists not because the problem domain requires it, but because of implementation choices. Caches, derived data, denormalized aggregates, precomputed values, and redundant storage are all forms of accidental state. Moseley and Marks argue that the ideal system eliminates accidental state entirely, computing derived values from essential state on demand rather than storing them.

## The Problem with Accidental State

Every piece of state adds to the system's configuration space. If a customer's "total spending" is stored as a separate field rather than computed from their transactions, the system now has an additional state variable that must be kept consistent with the source data. If the two ever diverge — due to a bug, a race condition, or an incomplete update — the system produces incorrect results. The [[state-and-complexity|complexity introduced by state]] applies equally to accidental and essential state, but accidental state is particularly damaging because it is unnecessary.

Cache invalidation is the canonical example. A cached value is accidental state — it duplicates information available elsewhere. Keeping the cache consistent with its source requires invalidation logic that is notoriously difficult to get right. The cache adds complexity without adding expressive power.

## Essential vs Accidental State

In the [[essential-vs-accidental-complexity]] framework, essential state is what the problem domain demands: account balances, inventory counts, user profiles. Accidental state is everything else the implementation adds: lookup tables, memoized results, precomputed aggregations, session data.

The distinction is not always obvious. A shopping cart's contents might seem essential, but if they can be derived from the user's session and the product catalog, the cart itself is derived state. The essential state is the user's selections; the cart is a presentation convenience.

## The Functional Relational Approach

[[functional-relational-programming]] addresses accidental state by making it a rule: do not store what can be computed. Derived values are calculated by [[referential-transparency|pure functions]] over essential state. There is no cache to invalidate because there is no cache. The computation is deterministic and cheap enough to repeat.

When performance demands caching, the cache is treated as an accidental component — managed by the infrastructure layer, invisible to the essential logic. The cache is a performance optimization, not a design feature. Its correctness is verified by comparing its output to the pure function it accelerates.

## Cases
- [[estate-agency-frp]] — the Estate Agency system distinguishes essential state (Property, Offer stored as relations) from accidental state (caches, performance hints managed by infrastructure). Feeders/observers ensure derived data never masquerades as essential state (from Out of the Tar Pit)

## Related
- [[essential-state]] — the counterpart: state that must be retained because the problem requires it
- [[essential-vs-accidental-complexity]] — the framework for distinguishing necessary from unnecessary
- [[state-and-complexity]] — why all state, including accidental state, causes complexity
- [[functional-relational-programming]] — the architecture that eliminates accidental state
