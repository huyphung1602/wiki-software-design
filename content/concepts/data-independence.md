---
title: Data Independence
aliases: [logical-physical separation, access path independence]
tags: [core-concept, data-modeling, software-design]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Data Independence

Data independence is the separation of the logical view of data from its physical storage and representation. Users and application code interact with data through its logical structure — relations with named attributes — without knowing or caring how that data is stored on disk, indexed, or distributed across machines. The concept originates with the [[relational-model]] and is one of its most powerful properties.

## Why It Matters

Without data independence, application code becomes tightly coupled to physical storage decisions. If a system stores customer data in a hash table keyed by ID, every piece of code that accesses customers must know about the hash table — its size, its collision strategy, its resizing behavior. Changing the storage format requires changes throughout the codebase. This is the data analog of violating [[information-hiding]]: physical details that should be hidden inside a module are instead spread across the system.

With data independence, the logical structure (a "customers" relation with columns for name, email, and address) is stable. The physical structure (B-tree, hash index, columnar storage, distributed across servers) can change without affecting any code that uses the logical view. Adding an index improves performance without changing behavior. Migrating to a different storage engine requires no changes to business logic.

## Access Path Independence

A specific and powerful form of data independence is access path independence. In navigational data models (hierarchical or network databases), the developer specifies how to traverse from one record to another — follow this pointer, then that one. The access path is hardcoded, and changing it requires rewriting queries.

In the relational model, there are no access paths. Any relation can be joined with any other relation on any condition. The query optimizer chooses the best execution plan. This is [[declarative-programming]] applied to data access: specify what you want, not how to get it.

## Relation to Information Hiding

Data independence is [[information-hiding]] applied specifically to data structures. The same principle applies: hide details that users do not need to know, expose only the logical interface. [[abstractions]] in the code sense and data independence in the storage sense are two expressions of the same idea — separation of what matters from what does not.

## In Functional Relational Programming

[[functional-relational-programming]] relies on data independence to maintain its separation of essential state from accidental components. Essential state is defined as relations with logical structure. The physical storage — whether in-memory data structures, files, or a database — is an accidental detail handled by the infrastructure layer.

## Cases
- [[estate-agency-frp]] — the Estate Agency system uses the relational model to achieve data independence: the accidental component specifies physical storage separately from the logical model, and derived relvars are maintained automatically by the infrastructure (from Out of the Tar Pit)

## Related
- [[relational-model]] — the framework that provides data independence
- [[information-hiding]] — the broader principle that data independence instantiates
- [[functional-relational-programming]] — an architecture that depends on data independence
- [[abstractions]] — the general concept of hiding irrelevant details
