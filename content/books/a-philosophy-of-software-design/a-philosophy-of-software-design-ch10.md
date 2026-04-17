---
title: "Ch 10: Define Errors Out Of Existence"
tags: [chapter, software-design, errors, exceptions]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Ch 10: Define Errors Out Of Existence

Part of [[a-philosophy-of-software-design]]

[[exception-handling|Exception handling]] is one of the worst sources of [[complexity]]. Over 90% of catastrophic failures in distributed systems come from incorrect error handling. The key lesson: reduce the number of places where exceptions must be handled. Four techniques:

**Define errors out of existence** — Redesign APIs so normal behavior handles all situations. Tcl's `unset` should "ensure variable doesn't exist" rather than "delete variable." Unix file deletion succeeds even for open files (marks for deletion, removes later). Java's `substring` should auto-clamp indices. Defining errors away simplifies APIs and makes modules [[deep-modules|deeper]].

**Mask exceptions** — Handle conditions at a low level so higher code is unaware. TCP resends lost packets. NFS retries silently when a server is down. Masking is [[pull-complexity-downwards|pulling complexity down]].

**Aggregate exceptions** — Handle many exceptions with one handler. A Web server's top-level dispatcher catches all parameter errors rather than wrapping each call separately. RAMCloud promotes small errors into server crashes to use a single recovery mechanism.

**Just crash** — For rare, unhandleable errors (out of memory, internal inconsistency), abort with a diagnostic. Crashing immediately is better than propagating through every call site.

Exceptions are part of a class's interface. Many exceptions = complex interface = shallow module. The goal is to minimize where handling is needed — define away, mask, aggregate, or crash.

## Related
- [[exception-handling]] — the core concept with all four techniques
- [[complexity]] — what exceptions add
- [[deep-modules]] — defining errors away produces depth
