---
title: "Out of the Tar Pit — S4: Causes of Complexity"
tags: [complexity, state, control-flow, code-volume]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Out of the Tar Pit — S4: Causes of Complexity

This section identifies three primary causes of complexity in software systems.

**State.** [[state-and-complexity|Mutable state]] is the single biggest cause. Anyone who has been told to "restart the program" or "reboot your computer" has experienced the consequences. State makes testing nearly useless -- a test in one state tells you nothing about behavior in another state, and the number of possible states grows exponentially with each bit of added state. State also undermines informal reasoning through contamination: a stateless procedure that calls a stateful one (even indirectly) becomes contaminated and can only be understood in the context of state. "When you let the nose of the camel into the tent, the rest of him tends to follow."

**Control.** [[Control-flow-complexity|Control flow]] arises from forcing developers to specify the order in which things happen. Most languages impose textual ordering as execution ordering, which means programmers must over-specify their intent. Even when ordering is irrelevant (as in three independent assignments), the language semantics force the reader to determine that the ordering does not matter -- duplicating the compiler's work and introducing risk of subtle bugs. Concurrency makes everything worse: with shared-state concurrency, repeating the same test with the same inputs and state tells you nothing about the next run.

**Code Volume.** Sheer [[cognitive-load|code volume]] is a secondary effect -- much code exists to manage state or specify control. Brooks noted that complexity increases nonlinearly with size, and the authors agree this is true in most current systems. However, following Dijkstra, they argue that with effective management of state and control, complexity need not grow more than proportionally to program length.

Three meta-principles govern all other causes: complexity breeds complexity, simplicity is hard, and power corrupts (the more a language permits, the harder it is to understand systems built with it).

Part of [[out-of-the-tar-pit]]

## Related
- [[state-and-complexity]] — state as the primary complexity cause
- [[control-flow-complexity]] — control as a complexity cause
- [[complexity]] — the overarching problem
- [[out-of-the-tar-pit-s03]] — Approaches to Understanding
- [[out-of-the-tar-pit-s05]] — Classical Approaches
