---
title: Exception Handling
aliases: [error handling, exception management]
tags: [core-concept, complexity, errors, design]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Exception Handling

Exception handling is one of the worst sources of [[complexity]]. Code dealing with special conditions is harder to write than normal-case code, developers often define exceptions without considering handling, and exception handling code itself creates opportunities for more exceptions. A study found over 90% of catastrophic failures in distributed systems came from incorrect error handling.

The overall goal: **reduce the number of places where exceptions must be handled.** Four techniques:

1. **Define errors out of existence** — Redesign APIs so the normal case handles all situations. Tcl's `unset` should "ensure variable doesn't exist" (no error if already gone) rather than "delete variable" (error if missing). Unix file deletion succeeds even if the file is open (marks for deletion, removes later). Java's `substring` should auto-clamp indices rather than throwing `IndexOutOfBoundsException`. Defining errors out of existence simplifies APIs and makes methods [[deep-modules|deeper]].

2. **Mask exceptions** — Handle exceptional conditions at a low level so higher-level code never sees them. TCP resends lost packets transparently. NFS retries file operations silently when a server is down. Masking is a form of [[pull-complexity-downwards|pulling complexity down]].

3. **Aggregate exceptions** — Handle many exceptions with a single piece of code. A Web server's top-level dispatcher catches all parameter errors and generates error responses, rather than wrapping each `getParameter` call in a separate handler. RAMCloud promotes small errors (corrupted object) into larger ones (server crash) to use a single recovery mechanism.

4. **Just crash** — For errors that are difficult to handle and don't occur often, abort with a diagnostic. Out-of-memory errors are the classic example: there's nothing useful the application can do. Crashing immediately is better than propagating errors through every allocation site.

Exceptions are part of a class's interface. Classes with many exceptions have complex interfaces and are shallower. Throwing exceptions is easy; handling them is hard. The complexity comes from the handling code, so minimize where handling is needed.

## Related
- [[complexity]] — what exception handling adds
- [[deep-modules]] — defining errors away makes modules deeper
- [[pull-complexity-downwards]] — masking exceptions as pulling complexity down
- [[a-philosophy-of-software-design-ch10]] — where these techniques are developed
- [[decide-what-matters]] — minimizing what matters includes handling exceptions at the lowest level
