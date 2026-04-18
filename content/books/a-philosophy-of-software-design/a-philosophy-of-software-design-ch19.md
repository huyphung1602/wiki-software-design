---
title: "Chapter 19 - Software Trends"
tags: [software-design, trends, patterns, testing]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Chapter 19 - Software Trends

Part of [[a-philosophy-of-software-design]]

This chapter evaluates several popular software development trends through the lens of [[complexity]] reduction, using the book's principles to assess whether each trend provides genuine leverage.

## Object-Oriented Programming and Inheritance

OOP mechanisms like private methods support [[information-hiding]] and can reduce complexity. Interface inheritance is beneficial -- the more implementations an interface has, the deeper it becomes. Implementation inheritance is riskier: it creates dependencies between parent and child classes, leading to [[information-leakage]] across the hierarchy. Prefer composition over implementation inheritance when possible, and separate state managed by parent classes from state managed by subclasses.

## Agile Development

Agile's incremental approach aligns with the book's advocacy for [[continuous-design|iterative development]]. However, agile risks encouraging [[tactical-programming|tactical programming]] by focusing on features rather than abstractions. The fix: develop in increments of abstractions, not features. When an abstraction is needed, invest in designing it cleanly rather than building it piecemeal.

## Unit Tests and Test-Driven Development

Unit tests facilitate refactoring by catching regressions, enabling the structural improvements the book advocates. Test-driven development, however, is criticized as tactical programming: it focuses on getting specific features working rather than finding the best design. Write tests first when fixing bugs (to verify the fix), but design abstractions holistically before testing.

## Design Patterns and Getters/Setters

Design patterns solve common problems well, but over-application -- forcing problems into patterns that do not fit -- creates complexity. Getters and setters are a cautionary example: they are [[shallow-modules|shallow methods]] that expose implementation data, violating [[information-hiding]]. The pattern has been overused because developers assume all established patterns are universally good.

## Related
- [[information-hiding]] -- OOP mechanisms support it when used correctly
- [[information-leakage]] -- implementation inheritance creates it
- [[shallow-modules]] -- getters and setters as a shallow pattern
- [[strategic-vs-tactical-programming]] -- agile and TDD can encourage tactical approaches
- [[continuous-design]] -- incremental development done right
- [[complexity]] -- the lens for evaluating all trends
