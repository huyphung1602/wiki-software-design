---
title: Together or Apart
aliases: [combine or separate, cohesion vs separation]
tags: [core-concept, modules, design, decomposition]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Together or Apart

The fundamental question in software design: should two pieces of functionality be implemented together or separately? This applies at every level — functions, methods, classes, services.

Subdividing always creates additional complexity: more components to track, more interfaces, separation that makes related code harder to see together, and potential duplication. The goal is to pick the structure that results in the best [[information-hiding]], fewest dependencies, and [[deep-modules|deepest interfaces]].

**Bring together if code is related:** code shares information, is used together bidirectionally, overlaps conceptually, or can't be understood independently.

**Bring together to:**
- Eliminate shared information across modules (HTTP read + parse into one class)
- Simplify the interface (Java I/O: combine FileInputStream and BufferedInputStream)
- Eliminate duplication (same code pattern repeated = wrong abstractions)

**Separate when:**
- General-purpose and special-purpose code are mixed (text class shouldn't contain UI operations)
- Code is truly independent (hash tables can be used without disk caches)

The cursor/selection example: combined object was awkward — higher-level code still treated them as distinct entities, implementation was more complex. Separating them into `Position` objects simplified both. The error logging example: separate logging methods were [[shallow-modules|shallow]] (one line of code, only called once, required understanding invocation site). Putting log statements inline was simpler.

**Method splitting:** Length alone is rarely a good reason to split. Split only if it produces cleaner abstractions — factoring out a self-contained subtask, or splitting into two independent methods with simpler interfaces. Methods of hundreds of lines are fine if they have simple signatures and are readable. Depth matters more than length. Ousterhout explicitly disagrees with Robert Martin's "functions should be tiny" approach — over-splitting creates shallow methods and conjoined functions that must be read together.

## Related
- [[information-hiding]] — the primary criterion for together/apart decisions
- [[deep-modules]] — the goal of good decomposition
- [[shallow-modules]] — what over-splitting produces
- [[classitis]] — the cultural bias toward splitting
- [[generality]] — making modules general-purpose
- [[specialization]] — keeping specialized code separate
- [[a-philosophy-of-software-design-ch09]] — where this framework is developed
