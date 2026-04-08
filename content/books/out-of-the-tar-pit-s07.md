---
title: "Out of the Tar Pit — S7: Recommended General Approach"
tags: [complexity, separation, state, control-flow, accidental-complexity]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Out of the Tar Pit — S7: Recommended General Approach

This is the theoretical core of the paper. The authors' two recommendations are: **avoid** complexity where possible, and **separate** it where not.

**The ideal world.** Even in the ideal world, some state is essential -- specifically, input data that the system may need to refer to in the future. All derived data (whether immutable or mutable) corresponds to [[accidental-state]] and can be omitted by re-deriving it on demand. Control is entirely accidental: the informal requirements never mention ordering, so developers should not have to specify it. The ideal approach is pure [[declarative-programming]]: specify what is required, not how.

**Real-world limitations.** Performance concerns may require some accidental state (e.g., caching derived data) and control (e.g., parallelism). In rare cases, accidental state offers the most natural way to express logic (e.g., game AI position tracking). But these should be the exception, not the rule.

**Separation.** The system should be cleanly divided into three components with restricted relationships:
1. **Essential State** -- the foundation, specified in complete isolation. Changes here may cascade to the other components, but nothing can change it.
2. **Essential Logic** -- what must be true, expressed in terms of the state. It references essential state but never accidental components. Changes in the accidental specification can never require changes here.
3. **Accidental State and Control** -- performance hints and optimizations. Changes here never affect the other components.

Each component should use a different, restricted language tailored to its purpose. The weaker each language, the easier it is to reason about. This is the "power corrupts" principle applied to architecture: restricting expressive power enables understanding.

The authors warn emphatically against designing for performance upfront: "there can be no comparison between the difficulty of improving the performance of a slow system designed for simplicity and that of removing complexity from a complex system designed to be fast." This reinforces Ousterhout's similar argument in [[designing-for-performance]].

Part of [[out-of-the-tar-pit]]

## Related
- [[essential-vs-accidental-complexity]] — the classification enabling this approach
- [[accidental-state]] — state that can be eliminated or separated
- [[declarative-programming]] — the ideal-world paradigm
- [[designing-for-performance]] — Ousterhout's compatible advice
- [[out-of-the-tar-pit-s06]] — Accidents and Essence
- [[out-of-the-tar-pit-s09]] — Functional Relational Programming
