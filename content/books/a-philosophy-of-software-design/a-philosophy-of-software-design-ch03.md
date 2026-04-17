---
title: "A Philosophy of Software Design — Ch 3: Working Code Isn't Enough"
tags: [chapter, mindset, investment]
sources: [a-philosophy-of-software-design]
created: 2026-04-08
updated: 2026-04-08
---

# A Philosophy of Software Design — Ch 3: Working Code Isn't Enough

Part of [[a-philosophy-of-software-design]]

## Summary

The most important element of good design is your mindset. [[tactical-programming|Tactical programming]] — focused on getting features working ASAP — makes good design nearly impossible. [[strategic-programming|Strategic programming]] treats a great design (that also works) as the primary goal.

### Tactical Programming

Short-sighted: finish tasks as quickly as possible, add small complexities as "reasonable compromises." Each task contributes complexity. Before long, you're patching patches and the code is a mess. The [[tactical-tornado]] archetype embodies this — fast output, but leaves destruction for others to clean up.

### Strategic Programming

Invest time in both proactive improvements (finding simpler designs, writing docs) and reactive ones (fixing design problems when discovered). Continually make small improvements — the opposite of tactical programming's continual accumulation of [[complexity]].

### The Investment Argument

Spend **10-20% of development time** on [[design-investment]]. Initial projects take 10-20% longer, but benefits compound within months. Payback period: 6-18 months. Eventually, investments become free — past benefits cover future costs.

### Technical Debt

[[technical-debt|Tactical programming borrows time from the future]]. Unlike financial debt, most technical debt is never fully repaid — you keep paying forever. Once a code base turns to spaghetti, it's nearly impossible to fix.

### Real-World Examples

Facebook ("Move fast and break things" → eventually "Move fast with solid infrastructure") vs. Google/VMware (strategic from the start, attracted top talent). Both can succeed, but strategic is more sustainable.

## Related
- [[strategic-vs-tactical-programming]] — the core dichotomy this chapter explores
- [[tactical-tornado]] — the extreme tactical programmer
- [[design-investment]] — the 10-20% rule
- [[technical-debt]] — the cost of tactical programming
- [[complexity]] — what tactical programming accumulates
