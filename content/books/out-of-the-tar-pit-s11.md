---
title: "Out of the Tar Pit — S11: Related Work"
tags: [frp, related-work]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Out of the Tar Pit — S11: Related Work

The authors briefly situate [[functional-relational-programming]] relative to prior work. FRP draws some influence from Darwen and Date's "Foundation for Future Database Systems: The Third Manifesto," but differs in aiming at general-purpose large-scale application programming rather than database-specific concerns. FRP also uses a separate functional sub-language and has different ideas about types, while its accidental component covers a broader range than traditional DBMS physical/logical mapping.

There are similarities to Backus' Applicative State Transition systems from his 1978 Turing Award lecture, which argued for liberating programming from the von Neumann style. The Aldat project at McGill also investigated general-purpose applications of relational algebra.

The section is brief, and the authors acknowledge that FRP is a synthesis of existing ideas -- functional programming, the relational model, and logic programming -- applied in a novel combination to general application development. The novelty lies not in any single component but in the strict separation of concerns and the insistence that each component use the most restricted language possible.

This modest positioning is consistent with the paper's overall argument: the individual ideas are well-proven, and the contribution is in how they are combined to attack complexity through avoidance and separation rather than management.

Part of [[out-of-the-tar-pit]]

## Related
- [[functional-relational-programming]] — the synthesized architecture
- [[out-of-the-tar-pit-s09]] — Functional Relational Programming
- [[out-of-the-tar-pit-s12]] — Conclusions
