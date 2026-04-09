---
title: Declarative Programming
aliases: [declarative specification, what not how, declarative approach]
tags: [core-concept, programming-paradigm, software-design]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Declarative Programming

Declarative programming specifies WHAT a system should do, not HOW it should do it. A declarative specification describes the desired result — the properties the output must satisfy, the relationships that must hold — without prescribing the sequence of steps to achieve it. This stands in contrast to imperative programming, which specifies a particular control flow and thereby introduces [[control-flow-complexity|ordering constraints]] that are often accidental.

## Eliminating Control Flow

The key benefit of declarative programming is the elimination of unnecessary ordering. When you write `SELECT name FROM employees WHERE department = 'Engineering'`, you do not specify whether the database should scan the table, use an index, or filter first. You describe the result you want, and the system determines the optimal execution plan. The ordering is accidental — it is managed by the infrastructure, not specified by the developer.

This principle applies far beyond database queries. [[integrity-constraints]] are declarative: they state conditions that must always hold without specifying when or how to check them. Derivation rules in [[functional-relational-programming]] are declarative: they define how to compute derived values from essential state without specifying evaluation order.

## Declarative vs Imperative

Imperative code says "do A, then do B, then do C." This forces the reader to understand why A must come before B, what state A produces that B consumes, and what happens if the ordering is wrong. Declarative code says "the result must satisfy properties P, Q, and R." The reader focuses on what is true, not on the mechanics of how it became true.

The imperative approach introduces [[accidental-complexity|accidental complexity]] because the ordering is often not inherent to the problem. The problem domain says "customers must have unique email addresses" — it does not say "check for duplicates before inserting." The declarative version — a uniqueness constraint — expresses the rule directly and lets the system enforce it.

## Limits of Declarative Programming

Not everything can be expressed declaratively. User interaction, real-time processing, and hardware control often require explicit sequencing. Moseley and Marks acknowledge this: their [[functional-relational-programming]] architecture isolates the accidental (imperative) components in a thin outer layer, while the essential logic and state remain declarative.

## Related
- [[control-flow-complexity]] — the problem that declarative programming eliminates
- [[functional-relational-programming]] — an architecture that maximizes declarative specification
- [[complexity]] — what declarative programming reduces
- [[accidental-complexity]] — most control flow ordering is accidental
- [[integrity-constraints]] — a key form of declarative specification
