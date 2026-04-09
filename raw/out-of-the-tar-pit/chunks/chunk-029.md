# 10 Example of an FRP system

10 Example of an FRP system
We now examine a simple example FRP system. The system is designed
to support an estate agency (real estate) business. It will keep track of
properties which are being sold, o↵ers which are made on the properties,
53

---
Page 54
---

decisions made on the o↵ers by the owners, and commission fees earnt by
the individual agency employees from their successful sales. The example
should serve to highlight the declarative nature of the components of an
FRP system.
To keep things simple, this system operates under some restrictions:
1. Sales only — no rentals / lettings
2. Peopleonlyhaveonehome,andtheownersresideatthepropertythey
are selling
3. Rooms are perfectly rectangular
4. O↵er acceptance is binding (ie an accepted o↵er constitutes a sale)
The example will use syntax from a hypothetical FRP infrastructure
(whichsupportsnotonlytherelationalalgebrabutalsosomeofthecommon
extensions from section 8.5) — typewriter font is used for this.
