---
title: "Ch 9: Better Together Or Better Apart?"
tags: [chapter, software-design, modules, decomposition]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Ch 9: Better Together Or Better Apart?

Part of [[a-philosophy-of-software-design]]

The fundamental design question: should two pieces of functionality be together or apart? Subdividing creates complexity — more components, more interfaces, separation that hides related code, and duplication. The goal: pick the structure that produces the best [[information-hiding]], fewest dependencies, and deepest interfaces.

Code should be brought [[together-or-apart|together]] when it shares information, is used together bidirectionally, overlaps conceptually, or can't be understood independently. Specific reasons: eliminate shared information (HTTP read + parse), simplify interfaces (Java I/O), or eliminate duplication.

Code should be separated when general-purpose and special-purpose code are mixed, or when code is truly independent. The cursor and selection example shows separation working — a combined object was awkward, while separate Position objects simplified both usage and implementation. The error logging example shows joining working — separate logging methods were [[shallow-modules|shallow]] and only called once; inline logging was simpler.

Method splitting: length alone is rarely a good reason. Split only for cleaner abstractions — factoring out a self-contained subtask, or splitting into independent methods with simpler interfaces. Methods of hundreds of lines are fine if they have simple signatures and are readable. [[deep-modules|Depth]] matters more than length. Ousterhout explicitly disagrees with Robert Martin's extreme "functions should be tiny" approach — over-splitting creates shallow, conjoined methods.

New [[red-flags]]: Repetition (same code over and over), Special-General Mixture (general mechanism contaminated with special-purpose code), Conjoined Methods (can't understand one without reading the other).

## Related
- [[together-or-apart]] — the decision framework
- [[information-hiding]] — the primary criterion
- [[deep-modules]] — the goal
- [[shallow-modules]] — what over-splitting produces
- [[a-philosophy-of-software-design-ch05]] — information hiding
