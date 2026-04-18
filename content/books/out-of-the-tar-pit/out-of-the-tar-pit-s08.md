---
title: "S8: The Relational Model"
tags: [relational-model, data-independence, integrity-constraints]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# S8: The Relational Model

The [[relational-model]] has nothing intrinsically to do with databases. It is an elegant approach to structuring data, manipulating it, maintaining integrity, and enforcing a clear separation between logical and physical layers. These features are applicable to state and data in any context.

The model has four aspects. **Structure** uses relations (homogeneous sets of uniquely-named records) as the sole data representation. Relations contain no duplicates and have no ordering, unlike SQL tables. The key benefit is access path independence: no subjective, up-front decisions about navigation between data instances are needed. The authors note "disturbing similarities" between OOP/XML data structuring and the older hierarchical/network models that the relational model superseded.

**Manipulation** uses the relational algebra: restrict, project, product, union, intersection, difference, join, and divide. The algebra has the property of closure -- all operands and results are relations -- enabling arbitrary nesting.

**Integrity** is maintained through [[integrity-constraints]] specified in a purely declarative way. Constraints may be arbitrarily complex, but they cannot interact with each other, so their complexity grows only linearly. Imperative mechanisms like triggers are not part of the relational model because they introduce control-flow concerns.

**Data independence** -- the [[data-independence]] principle -- separates the logical model from physical storage representation. This is a close parallel to the accidental/essential split recommended in section 7, and is one of the key motivations for adopting the relational model in FRP.

The authors warn that SQL is not an accurate reflection of the relational model and should not be equated with it. Common extensions to the algebra include arithmetic, aggregate operators, grouping, and renaming capabilities.

Part of [[out-of-the-tar-pit]]

## Related
- [[relational-model]] — the data foundation of FRP
- [[data-independence]] — logical/physical separation
- [[integrity-constraints]] — declarative consistency enforcement
- [[out-of-the-tar-pit-s07]] — Recommended General Approach
- [[out-of-the-tar-pit-s09]] — Functional Relational Programming
