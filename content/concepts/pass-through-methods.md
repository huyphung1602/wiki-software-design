---
title: Pass-Through Methods
aliases: [delegation methods, wrapper methods]
tags: [anti-pattern, modules, design, red-flag]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# Pass-Through Methods

A pass-through method does little except invoke another method with the same or similar signature. It adds interface complexity without contributing functionality. This is a [[red-flags|red flag]] indicating confused division of responsibility between classes.

Example: a `TextDocument` class where 13 of 15 public methods just delegate to `TextArea` with identical signatures. The class increases complexity (more interfaces to learn, signature changes propagate) but provides almost no value.

Pass-through methods make classes [[shallow-modules|shallower]]: they increase interface complexity of the class but don't increase total system functionality. They also create dependencies — if the underlying method's signature changes, the pass-through must change too.

Solutions:
1. **Expose the lower class directly** — Remove responsibility for the feature from the higher-level class
2. **Redistribute functionality** — Move methods between classes so each has distinct, coherent responsibility
3. **Merge the classes** — If they can't be disentangled, combine them

Exception: dispatchers and interface implementations. A dispatcher selects among several methods to invoke — same signatures but it provides the useful functionality of *choosing*. Multiple implementations of the same interface (like disk drivers) are fine because each provides different functionality.

Decorators (wrappers) are a related pattern that often produces pass-through methods. They introduce boilerplate for a small amount of new functionality, creating [[shallow-modules|shallow classes]]. Before creating a decorator, consider adding functionality to the underlying class, merging with the use case, or implementing as a stand-alone class.

## Related
- [[red-flags]] — pass-through method is a recognized red flag
- [[shallow-modules]] — what pass-through methods create
- [[classitis]] — the decorator anti-pattern produces pass-throughs
- [[pass-through-variables]] — the variable analogue
- [[a-philosophy-of-software-design-ch07]] — where this is analyzed
