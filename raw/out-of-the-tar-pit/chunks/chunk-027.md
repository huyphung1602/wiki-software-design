# 9.2 Benefits of this approach

9.2 Benefits of this approach
FRP follows the guidelines of avoid and separate as recommended in sec-
tion 7 and hence gains all the benefits which derive from that. We now
examine how FRP helps to avoid complexity from the common causes.
9.2.1 Benefits for State
The architecture is explicitly designed to avoid useless accidental state, and
to avoid even the possibility of an FRP system ever getting into a “bad
state”.
Specifically derived state is not normally stored (is not treated as essen-
tial state). In normal circumstances26 hybrid feeders/observers never feed
back in the exact same data which they observed — they only ever feed in
some externally generated input or response. So long as this principle is
observed errors in the logic of the system can never cause it to get into a
“bad state” — the only thing required to fix such errors27 is to correct the
logic, there is no need to perform an exhaustive search through and correc-
tion of the essential state. This also means that (aside from errors in the
infrastructure) the system can never require “restarting” / “rebooting” etc.
When it comes to separation, the architecture clearly exhibits both the
logic / state split and the accidental / essential split recommended in sec-
tion 7. An example of what this means is that you do not have to think
about any accidental state when concentrating on the logic of your system.
In fact, you do not really have to think about the essential state as being
state either — from the point of view of the logic, the essential state is seen
as constant.
Furthermore, the functional component (of the logic) has no access to
any state at all (even the essential state) — it is totally referentially trans-
The e↵ort involved in this is insignificant when compared to the hundreds of man-years
often involved in large systems.
26The exception might be in the kind of highly interactive scenario considered in sec-
tions 7.2.2 and 7.3.1
27We’re talking here solely about fixing the system itself — of course FRP can’t guar-
antee that errors in the logic won’t escape and a↵ect the real world via observers!
50

---
Page 51
---

parent, can only access what is supplied in the function arguments, and
hence o↵ers hugely better prospects for testing (as mentioned earlier in sec-
tion 4.1.1).
Additionally, there are major advantages gained from adopting a re-
lational representation of data — specifically, there is no introduction of
subjective bias into the data, no concern with data access paths. This is in
contrast with approaches such as OOP or XML (as we saw in section 8.1.2).
Finally, integrity constraints provide big benefits for maintaining consis-
tency of state in a declarative manner:
The fact that we can impose the integrity constraints of our sys-
tem in a purely declarative manner (without requiring triggers
or worse, methods / procedures) is one of the key benefits of the
FRP approach. It means that the addition of new constraints
increases the complexity of the system only linearly because the
constraints do not — indeed cannot — interact in any way at
all. (Constraints can make use of user-defined functions — but
they have no way of referring to other constraints). This is in
stark contrast with more imperative approaches such as object
oriented programming where interaction between methods causes
the complexity to grow at a far greater rate.
Furthermore, the declarative nature of the integrity constraints opens
the door to the possibility of a suitably sophisticated infrastructure making
use of them for performance reasons (to give a trivial example, there is no
needtocomputetherelationalintersectionoftworelvarsatallifitcanbe
establishedthattheirintegrityconstraintsaremutuallyexclusive—because
then the result is guaranteed to be empty). This type of optimisation is just
not possible if the integrity is maintained in an imperative way.
9.2.2 Benefits for Control
Control is avoided completely in the relational component which constitutes
the top level of the essential logic. In FRP this logic consists simply of a set
of equations (equating derived relvars with the relations calculated by their
expressions) which have no intrinsic ordering or control flow at all.
FRP also avoids any explicit parallelism in the essential components but
provides for the possibility of separated accidental control should that be
required.
An infrastructure which supports FRP may well make use of implicit
parallelism to improve its performance — but this shouldn’t be the concern
51

---
Page 52
---

of anyone other than the implementor of the infrastructure — certainly it is
not the concern of someone developing an FRP system.
A final advantage (which isn’t particularly related to control) is that the
uniformnatureoftherepresentationofdataasrelationsmakesitmucheasier
to create distributed implementations of an FRP infrastructure should that
be required (e.g. there are no pointers or other access paths to maintain).
9.2.3 Benefits for Code Volume
FRP addresses this in two ways. The first is that a sharp focus on true
essentials and avoiding useless accidental complexity inevitably leads to less
code.
The second way is that the FRP approach reduces the harm that large
volumes of code cause through its use of separation (see section 4.3).
9.2.4 Benefits for Data Abstraction
Data Abstraction is something which we have only mentioned in passing (in
section 4.4) so far. By data abstraction we basically mean the creation of
compound data types and the use of the corresponding compound values
(whose internal contents are hidden).
We believe that in many cases, un-needed data abstraction actually rep-
resents another common (and serious) cause of complexity. This is for two
reasons:
Subjectivity Firstly the grouping of data items together into larger com-
pound data abstractions is an inherently subjective business (Ungar
and Smith discuss this problem in the context of Self in [SU96]).
Groupingswhichmakesenseforonepurposewillinevitablydi↵erfrom
thosemostnaturalforotheruses, yetthepresenceofpre-existingdata
abstractions all too easily leads to inappropriate reuse.
Data Hiding Secondly, large and heavily structured data abstractions can
seriously erode the benefits of referential transparency (section 5.2.1)
inexactlythemanneroftheextremeexamplediscussedinsection5.2.3.
This problem occurs both because data abstractions will often cause
un-needed, irrelevant data to be supplied to a function, and because
the data which does get used (and hence influences the result of a
function) is hidden at the function call site. This hidden and excessive
dataleadstoproblemsfortestingaswellasinformalreasoninginways
very similar to state (see section 4.1).
52

---
Page 53
---

One of the primary strengths of the relational model (inherited by FRP)
is that it involves only minimal commitment to any subjective groupings
(basically just the structure chosen for the base relations), and this commit-
ment has only minimal impact on the rest of the system. Derived relvars
o↵er a straightforward way for di↵erent (application-specific) groupings to
be used alongside the base groupings. The benefits in terms of subjectivity
arecloselyrelatedtothebenefitsofaccesspathindependence(section8.1.2).
FRPalsoo↵ersbenefitsintheareaofdatahiding,simplybydiscouraging
it. Specifically, FRP o↵ers no support for nested relations or for creating
product types (as we shall see in section 9.3).
9.2.5 Other Benefits
The previous sections considered the benefits o↵ered by FRP for minimiz-
ing complexity. Other potential benefits include performance (as mentioned
brieflyundersection9.2.1)andthepossibilitythatdevelopmentteamsthem-
selves could be organised around the di↵erent components — for example
one team could focus on the accidental aspects of the system, one on the
essential aspects, one on the interfacing, and another on providing the in-
frastructure.
