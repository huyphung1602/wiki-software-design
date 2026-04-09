---
title: Testing
aliases: [software testing, black-box testing, test coverage, validation through testing]
tags: [core-concept, testing, software-quality, validation]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# Testing

Testing is the approach to understanding a software system from the outside — as a "black box." Conclusions are drawn from observing how the system behaves with specific inputs in specific situations. Testing can demonstrate the presence of bugs but never their absence.

## In Out of the Tar Pit

Moseley and Marks identify a fundamental limitation of testing: a test using one particular set of inputs tells you nothing about the system's behavior with a different set of inputs. The state space of any non-trivial system is too large to test exhaustively, so test suites can only sample from it.

[[State-and-complexity|Mutable state]] makes testing exponentially harder. Each state variable doubles the number of possible configurations. A system with 30 boolean state variables has over a billion possible states — most of which will never be tested. The common approach of testing in a "clean" initial state simply sweeps the problem under the carpet.

Concurrency compounds the problem further: running the same test with the same inputs and the same starting state may produce different results on different runs. This is as bad as it gets — testing cannot even guarantee result consistency.

[[referential-transparency]] dramatically improves testing effectiveness by eliminating the state problem. When a function depends only on its arguments, testing it requires only providing inputs and checking outputs — no state setup or teardown. This is one of the strongest practical arguments for functional programming.

Despite its limitations, testing remains useful as a supplementary validation mechanism. The key insight is that [[reasoning]] about code is more important than testing — and both degrade as [[complexity]] increases.

## Related
- [[reasoning]] — the more powerful but more fragile approach
- [[testing-vs-reasoning]] — how the two approaches compare and why reasoning is prioritized
- [[complexity]] — the force that degrades testing effectiveness
- [[referential-transparency]] — the property that makes testing tractable
- [[state-and-complexity]] — the primary factor making testing infeasible
- [[out-of-the-tar-pit-s03]] — where testing limitations are analyzed
