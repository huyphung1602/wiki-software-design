# 10.4 Accidental State and Control

10.4 Accidental State and Control
Theaccidentalstateandcontrol componentofanFRPsystemconsistssolely
of a set of declarations which represent performance hints for the infrastruc-
ture (see section 9.1.3). In this example the accidental state and control is
a set of three hint declarations.
declare store PropertyInfo
This declaration is simply a hint to the infrastructure to request that
the PropertyInfo derived relation is actually stored (ie cached) rather than
continually recalculated.
62

---
Page 63
---

declare store shared Room Floor
Thishintinstructstheinfrastructuretodenormalize theRoomandFloor
relations into a single shared storage structure. (Note that because we are
able to express this as part of the accidental state and control we have not
beenforcedtocompromisetheessential partsofoursystemwhichstilltreat
Room and Floor separately).
declare store separate Property (photo)
This hint instructs the infrastructure to store the photo attribute of
the Property relation separately from its other attributes (because it is not
frequently used).
These three hints have all focused on state (PropertyInfo is accidental
state, and the other two declarations are concerned with accidental aspects
of state). Larger systems would probably also include accidental control
specifications for performance reasons.
