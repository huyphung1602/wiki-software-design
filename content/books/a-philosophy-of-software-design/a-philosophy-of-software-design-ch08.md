---
title: "Chapter 8 - Pull Complexity Downwards"
tags: [chapter, software-design, modules]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Chapter 8 - Pull Complexity Downwards

Part of [[a-philosophy-of-software-design]]

This chapter introduces a simple principle: when a module has unavoidable [[complexity]], handle it internally rather than exposing it to users. A module should have a simpler interface than implementation. Most modules have more users than developers, so developer suffering is preferable to user suffering.

The opposite temptation is to push complexity upward: throw exceptions instead of handling them, export configuration parameters instead of determining good defaults, leave policy decisions to callers. These approaches amplify complexity because many people must deal with each problem instead of one.

Configuration parameters are a common form of upward complexity push. While sometimes justified when users know their domain better, they're often an excuse to avoid hard design decisions. A network protocol could export a retry interval parameter — or it could measure response times and compute the interval dynamically, adapting automatically. Auto-computed values are better than static configuration because they adjust to changing conditions.

[[pull-complexity-downwards|Pulling complexity down]] works best when three criteria are met: the complexity relates to the class's existing functionality, it simplifies code elsewhere, and it simplifies the class's interface. The text class example: a character-oriented API pulls line-splitting logic into the class, producing a simpler interface and simpler UI code. But pulling UI knowledge (backspace behavior) into the text class fails — it creates [[information-leakage]] rather than simplification.

The principle is another path to [[deep-modules|deep modules]]: more complexity in the implementation, less exposed in the interface.

## Related
- [[pull-complexity-downwards]] — the core principle
- [[deep-modules]] — what pulling complexity produces
- [[information-hiding]] — the mechanism
- [[a-philosophy-of-software-design-ch06]] — general-purpose interfaces pull complexity down
