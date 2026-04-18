---
title: "S3: Approaches to Understanding"
tags: [testing, reasoning, simplicity]
sources: [out-of-the-tar-pit]
created: 2026-04-08
updated: 2026-04-08
---

# S3: Approaches to Understanding

There are two widely-used approaches to understanding software systems: testing and informal reasoning. Testing examines a system from the outside as a "black box," drawing conclusions from observations in specific situations. Informal reasoning examines a system from the inside, using extra structural information to build understanding.

Of the two, informal reasoning is far more important. Testing has inherent limits: a test using one set of inputs tells you nothing about behavior with different inputs. As Dijkstra observed, testing "can be used very effectively to show the presence of bugs but never to show their absence." Moreover, informal reasoning is always used as part of development, and improvements in reasoning prevent errors from being created in the first place, whereas testing can only detect more errors after the fact.

The authors quote Dijkstra: "Those who want really reliable software will discover that they must find means of avoiding the majority of bugs to start with." And O'Keefe: "Our response to mistakes should be to look for ways that we can avoid making them, not to blame the nature of things."

This does not mean testing is useless. All approaches to understanding have limitations -- informal reasoning is limited in scope and imprecise, and formal reasoning depends on specification accuracy. Employing both testing and reasoning together is prudent.

But because every approach has limits, [[complexity]] becomes the critical variable. Simplicity is more important than either testing or reasoning. Given a choice between investing in testing and investing in simplicity, the latter is often the better choice because it facilitates all future attempts to understand the system -- of any kind. This creates a framework for evaluating [[testing-vs-reasoning]]: the value of any technique depends on how much complexity it must overcome.

Part of [[out-of-the-tar-pit]]

## Related
- [[testing-vs-reasoning]] — why reasoning trumps testing
- [[complexity]] — the enemy of all understanding approaches
- [[out-of-the-tar-pit-s02]] — Complexity
- [[out-of-the-tar-pit-s04]] — Causes of Complexity
