---
title: Consistency
aliases:
  - convention
  - uniformity
tags:
  - core-concept
  - coding-style
  - design-principle
sources:
  - a-philosophy-of-software-design
created: 2026-04-08
updated: 2026-04-08
---

# Consistency

Consistency means that similar things are done in similar ways throughout a system, and dissimilar things are done in different ways. It is a powerful tool for reducing [[complexity]] because it creates cognitive leverage: once you learn how something works in one place, that knowledge transfers to every other place that follows the same pattern. Without consistency, every situation must be learned independently.

## Why Consistency Matters

Consistency reduces both effort and errors. When patterns are uniform, developers can make safe assumptions about unfamiliar code based on familiar-looking patterns. If the system is inconsistent, two situations may appear identical when they actually differ, leading to incorrect assumptions and bugs. Consistency also makes code more [[obvious-code|obvious]] -- readers can recognize patterns and draw conclusions without detailed analysis.

## Levels of Consistency

Consistency applies at multiple scales in a software system:
- **Names**: Using [[choosing-names|consistent naming conventions]] so that related variables, methods, and classes follow the same patterns
- **Coding style**: Following style guides for indentation, brace placement, declaration order, and commenting
- **Interfaces**: When multiple implementations share an interface, learning one teaches the others
- **Design patterns**: Using established patterns so readers bring prior knowledge
- **Invariants**: Properties that are always true reduce the special cases developers must consider

## Maintaining Consistency

Consistency is hard to maintain over time, especially with large teams. Three practices help: document conventions where developers will find them; enforce conventions with automated tools (linters, pre-commit hooks) so violations cannot slip in; and follow the "when in Rome" rule -- match existing patterns in each area of the codebase. Resist changing established conventions unless you have significant new justification and will update all existing uses. Overzealous consistency is also a danger: forcing dissimilar things into the same pattern creates confusion rather than clarity.

## Related
- [[obvious-code]] -- consistency makes code easier to understand at a glance
- [[choosing-names|consistent naming]] -- consistent naming is a primary form of consistency
- [[abstractions]] -- consistent interfaces multiply the value of learning each one
- [[continuous-design]] -- consistency as an ongoing investment in code quality
- [[complexity]] -- what consistency reduces
- [[a-philosophy-of-software-design-ch17]] -- the source chapter
