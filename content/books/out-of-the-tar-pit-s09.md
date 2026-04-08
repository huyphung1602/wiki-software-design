---
title: "Out of the Tar Pit — S9: Functional Relational Programming"
tags: [frp, functional-programming, relational-model, architecture]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Out of the Tar Pit — S9: Functional Relational Programming

[[Functional-relational-programming]] (FRP) is the concrete architecture the authors propose for applying the avoid-and-separate principles. FRP is currently hypothetical but grounded in widely-proven ideas from functional programming and the relational model. All essential state takes the form of relations, and all essential logic is expressed using relational algebra extended with pure user-defined functions.

An FRP system has four components. **Essential State** specifies the base relvars (names and types only). Data is treated as essential state only when it has been directly input by a user. **Essential Logic** defines derived relations, [[integrity-constraints]], and pure functions. No consideration of performance is allowed here -- concepts like "denormalization for performance" make no sense because physical storage is handled separately. **Accidental State and Control** consists of isolated, declarative performance hints: which derived relvars to store, what physical storage mechanisms to use, parallelism recommendations. Hints cannot refer to each other. **Other** handles interfacing with the outside world through feeders (converting input into relational assignments) and observers (generating output from derived-relation changes).

The separation yields powerful benefits. For state, the system can never enter a "bad state" from logic errors -- fixing the logic is sufficient, with no need to scan and correct stored data. The functional component has no access to state at all, is fully [[referential-transparent]], and offers excellent testing prospects. Integrity constraints, being declarative and non-interacting, grow only linearly in complexity. For control, the relational component has no ordering at all -- it is simply a set of equations. For code volume, the focus on essentials and separation reduces both the amount of code and the harm from what remains.

The authors also argue against unnecessary data abstraction: subjective grouping of data and hidden internal structure erode referential transparency much like state does. The relational model's flat structure and access path independence avoid both problems.

Part of [[out-of-the-tar-pit]]

## Related
- [[functional-relational-programming]] — the proposed architecture
- [[referential-transparency]] — guaranteed for the functional component
- [[integrity-constraints]] — declarative, non-interacting consistency rules
- [[declarative-programming]] — the paradigm underlying FRP
- [[out-of-the-tar-pit-s08]] — The Relational Model
- [[out-of-the-tar-pit-s10]] — Example of an FRP System
