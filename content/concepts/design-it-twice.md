---
title: Design it Twice
aliases: [consider alternatives, multiple designs]
tags: [core-concept, design-process, alternatives]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Design it Twice

Your first design idea will rarely be the best. The principle: for every major design decision, consider multiple radically different approaches before choosing. Compare their pros and cons, then pick the best or combine elements into a new hybrid.

The text class example: consider a line-oriented interface, a character-oriented interface, and a string/range-oriented interface. Each has different trade-offs for higher-level code. Comparing them reveals that neither lines nor single characters match the actual operations in higher-level code — leading to the range-oriented API that handles them naturally.

Pick approaches that are radically different from each other. Even if you're certain there's only one reasonable approach, force yourself to sketch a second design. Analyzing its weaknesses is instructive.

When comparing alternatives, consider:
- Which has the simplest interface?
- Which is more general-purpose?
- Which enables a more efficient implementation?
- Which is easiest to use for higher-level code?

If none of the alternatives is attractive, use their problems to drive a new design. The weaknesses you identify point toward a better solution.

The principle applies at every level: module interfaces, implementations, system decomposition, even UI features. For a class, exploring alternatives might take an hour or two — a small investment against days or weeks of implementation.

Smart people often resist this principle because their first quick idea always seemed sufficient growing up. But software design problems are hard enough that no one gets them right on the first try. Designing it twice not only produces better designs but also improves design skills over time, as the process teaches what makes designs better or worse.

## Related
- [[problem-decomposition]] — the skill this practice develops
- [[continuous-design]] — design as an ongoing process
- [[strategic-programming]] — the mindset that enables investing in multiple designs
- [[a-philosophy-of-software-design-ch11]] — where this principle is introduced
- [[decide-what-matters]] — designing twice reveals what truly matters
