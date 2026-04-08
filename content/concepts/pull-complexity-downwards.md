---
title: Pull Complexity Downwards
aliases: [complexity absorption, hide complexity internally]
tags: [core-concept, modules, design, encapsulation]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Pull Complexity Downwards

When a module has unavoidable [[complexity]], handle it internally rather than exposing it to users. Most modules have more users than developers, so developer suffering is preferable to user suffering. A simple interface is more important than a simple implementation.

The temptation is to do the opposite: solve easy problems internally and punt hard ones upward. Throw an exception instead of handling it. Export a configuration parameter instead of determining good behavior automatically. These approaches amplify complexity — many people must deal with the problem instead of one.

Configuration parameters are a common example of pushing complexity upward. Rather than deciding behavior internally, the class exports parameters for users to tune. While sometimes justified (when users truly know their domain better), they're often an excuse to avoid hard decisions. A network protocol that exports a "retry interval" parameter could instead measure response times and compute the interval dynamically. This pulls complexity down and produces a better result that adapts to changing conditions.

Three criteria for when pulling complexity down makes sense:
1. The complexity is closely related to the class's existing functionality
2. Pulling it down results in simplifications elsewhere in the application
3. Pulling it down simplifies the class's interface

The text class example illustrates all three: a character-oriented API (vs. line-oriented) pulls line-splitting complexity into the text class, where it belongs. The UI becomes simpler, the text interface is simpler, and line management relates to the text class's core purpose. But pulling UI-specific knowledge (like backspace behavior) into the text class fails the first criterion — it creates [[information-leakage]], not simplification.

This principle is another path to [[deep-modules]]: more complexity in the implementation, less in the interface.

## Related
- [[deep-modules]] — what pulling complexity downwards produces
- [[information-hiding]] — the mechanism for keeping complexity internal
- [[complexity]] — what this principle manages
- [[a-philosophy-of-software-design-ch08]] — where this principle is introduced
