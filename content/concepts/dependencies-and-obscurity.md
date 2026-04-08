---
title: Dependencies and Obscurity
aliases: [dependency complexity, obscurity]
tags: [root-cause, complexity, design]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Dependencies and Obscurity

Ousterhout identifies two root causes of [[complexity]]. All three symptoms ([[change-amplification]], [[cognitive-load]], [[unknown-unknowns]]) trace back to these two factors.

## Dependencies

A dependency exists when code cannot be understood and modified in isolation — it relates to other code that must also be considered or modified. Examples: method signatures create dependencies between callers and implementations; network protocols create dependencies between sender and receiver code.

Dependencies are fundamental to software and cannot be completely eliminated — we intentionally create them as part of design (every class API is a dependency). The goal is to **reduce the number of dependencies** and **make remaining dependencies as simple and obvious as possible**. A good dependency is one where a developer can easily find all affected code, and compilers/tools can help manage it.

Dependencies cause [[change-amplification]] (scattered code must be modified) and [[cognitive-load]] (must understand related code).

## Obscurity

Obscurity occurs when important information is not obvious. Examples: a variable name so generic it carries no information (e.g., `time`), missing unit documentation, inconsistency (same name for different purposes), hidden dependencies.

Obscurity is not just a documentation problem — it is a **design problem**. If a system has a clean and obvious design, it needs less documentation. The need for extensive documentation is often a [[red-flags|red flag]] that the design isn't right.

Obscurity creates [[unknown-unknowns]] (the worst symptom) and contributes to [[cognitive-load]].

## The Relationship

Together, dependencies and obscurity account for all three symptoms of complexity. Design techniques that minimize dependencies and obscurity will reduce complexity. This is the theoretical foundation for every principle in the rest of the book.

## Related
- [[complexity]] — what these two factors cause
- [[change-amplification]] — caused by dependencies
- [[cognitive-load]] — caused by both
- [[unknown-unknowns]] — caused by obscurity
- [[a-philosophy-of-software-design-ch02]] — where these are defined
