---
title: Integrity Constraints
aliases: [declarative constraints, data integrity, invariants]
tags: [core-concept, data-integrity, declarative, software-design]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Integrity Constraints

Integrity constraints are declarative specifications of rules that must always hold true within a system. In the [[relational-model]], they take the form of conditions over relations: primary key uniqueness, foreign key validity, check constraints, and arbitrary predicates. In [[functional-relational-programming]], they are the primary mechanism for expressing essential business logic.

## The Declarative Advantage

The traditional approach to data validation scatters imperative checks throughout the codebase: validate input in the UI layer, check again in the service layer, perhaps add assertions in the data layer. Each check must be maintained independently, and it is easy to miss one. When a new code path is added, the developer must remember to include all relevant validations.

[[Declarative-programming|Declarative integrity constraints]] solve this by defining each rule once. The constraint "account balance must not go below zero" is stated as a condition on the accounts relation. The system enforces it automatically, regardless of which code path modifies the account. Adding a new transaction type cannot bypass the constraint because the constraint is not in the code path — it is a property of the data.

## Types of Constraints

**Type constraints** define the domain of each attribute — an account number is an integer, a status is one of {active, suspended, closed}. These are the most basic form of integrity.

**Uniqueness constraints** ensure that no two tuples in a relation share the same key. This is the relational analog of identity.

**Referential constraints** (foreign keys) ensure that references between relations are valid — every order references an existing customer.

**Arbitrary constraints** express business rules: "an employee's salary must not exceed their manager's," "a transfer must have matching source and destination amounts." These are the most powerful and the most commonly neglected in traditional architectures.

## Constraints and State

Integrity constraints directly address [[state-and-complexity|the complexity caused by mutable state]]. Without constraints, any part of the system can put state into any configuration, and every consumer must handle all possible configurations — including invalid ones. With constraints, the state space is narrowed to valid configurations only. Every consumer can assume the invariants hold, reducing the defensive code they must write.

## Related
- [[relational-model]] — the framework where integrity constraints are most naturally expressed
- [[declarative-programming]] — the paradigm that makes constraints concise
- [[functional-relational-programming]] — the architecture that uses constraints as primary business logic
- [[state-and-complexity]] — constraints reduce the state space that causes complexity
