---
title: "Chapter 11 - Design it Twice"
tags: [chapter, software-design, process]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Chapter 11 - Design it Twice

Part of [[a-philosophy-of-software-design]]

For every major design decision, consider multiple radically different approaches before choosing. First ideas are rarely best. The text class example: comparing line-oriented, character-oriented, and range-oriented interfaces reveals that the range-oriented approach best matches higher-level operations.

Pick approaches that are radically different. Even when you think there's only one reasonable approach, force a second design. Comparing weaknesses is instructive. Evaluate on: simplest interface? Most general-purpose? Most efficient? Easiest to use?

If no alternative is attractive, use their problems to drive a new, better design. The weaknesses you identify point toward the solution.

The principle applies at every level: interfaces, implementations, system decomposition, UI features. For a class, exploring alternatives takes an hour or two — small against days of implementation. The investment pays off in better design and improved design skills over time.

Smart people sometimes resist this because their first idea always seemed sufficient growing up. But software design is hard enough that no one gets it right the first try. Designing it twice not only improves the current design but teaches what makes designs good or bad, honing judgment for future work.

## Related
- [[design-it-twice]] — the core principle
- [[problem-decomposition]] — the skill this practice develops
- [[strategic-programming]] — the mindset that enables investing time in design
