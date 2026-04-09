# 7.1 Ideal World

7.1 Ideal World
In the ideal world we are not concerned with performance, and our language
and infrastructure provide all the general support we desire. It is against
thisbackgroundthatwearegoingtoexaminestate andcontrol. Specifically,
we are going to identify state as accidental state if we can omit it in this
ideal world, and the same applies to control.
Even in the ideal world we need to start somewhere, and it seems rea-
sonable to assume that we need to start with a set of informal requirements
from the prospective users.
Our next observation is that because we ultimately need something to
happen — i.e. we are going to need to have our system processed mechan-
ically (on a computer) — we are going to need formality. We are going to
need to derive formal requirements from the informal ones.
So, taken together, this means that even in the ideal world we have:
Informal requirements Formal requirements
!
Note that given that we’re aiming for simplicity, it is crucial that the
formalisation be done without adding any accidental aspects at all. Specifi-
cally this means that in the ideal world, formalisation must be done with no
view to execution whatsoever. The sole concern when producing the formal
requirements must be to ensure that there is no relevant6 ambiguity in the
informal requirements (i.e. that it has no omissions).
So, having produced the formalised requirements, what should the next
stepbe? Giventhatweareconsideringtheidealworld,itisnotunreasonable
6Weincludetheword“relevant”herebecauseinmanycasestheremaybemanypossible
acceptable solutions — and in such cases the requirements can be ambiguous in that
regard, however that is not considered to be a “relevant” ambiguity, i.e. it does not
correspond to an erroneous omission from the requirements.
23

---
Page 24
---

to assume that the next step is simply to execute these formal requirements
directly on our underlying general purpose infrastructure.7
Thisstateofa↵airsisabsolute simplicity—itdoesnotseemconceivable
that we can do any better than this even in an ideal world.
It is interesting to note that e↵ectively what we have just described is in
fact the very essence of declarative programming — i.e. that you need only
specify what you require, not how it must be achieved.
We now consider the implications of this “ideal” approach for the causes
of complexity discussed above.
7.1.1 State in the ideal world
Our main aim for state in the ideal world is to get rid of it — i.e. we are
hoping that most state will turn out to be accidental state.
Westartfromtheperspectiveoftheusers’informalrequirements. These
will mention data of various kinds — some of which can give rise to state
— and it is these kinds which we now classify.
Alldatawilleitherbeprovideddirectlytothesystem(input)orderived.
Additionally, derived data is either immutable (if the data is intended only
for display) or mutable (if explicit reference is made within the requirements
to the ability of users to update that data).
All data mentioned in the users’ informal requirements is of concern to
the users, and is as such essential. The fact that all such data is essential
does not however mean that it will all unavoidably correspond to essential
state. It may well be possible to avoid storing some such data, instead
dealing with it in some other essential aspect of the system (such as the
logic) — this is the case with derived data, as we shall see. In cases where
this is possible the data corresponds to accidental state.
Input Data
Data which is provided directly (input) will have to have been included
in the informal requirements and as such is deemed essential. There are
basically two cases:
There is (according to the requirements) a possibility that the system
•
may be required to refer to the data in the future.
There is no such possibility.
•
7In the presence of irrelevant ambiguities this will mean that the infrastructure must
choose one of the possibilities, or perhaps even provide all possible solutions
24

---
Page 25
---

In the first case, even in the ideal world, the system must retain the data
and as such it corresponds to essential state.
In the second case (which will most often happen when the input is
designed simply to cause some side-e↵ect) the data need not be maintained
at all.
Essential Derived Data — Immutable
Data of this kind can always be re-derived (from the input data — i.e. from
the essential state) whenever required. As a result we do not need to store
it in the ideal world (we just re-derive it when it is required) and it is clearly
accidental state.
Essential Derived Data — Mutable
As with immutable essential derived data, this can be excluded (and the
data re-derived on demand) and hence corresponds to accidental state.
Mutability of derived data makes sense only where the function (logic)
used to derive the data has an inverse (otherwise — given its mutability
— the data cannot be considered derived on an ongoing basis, and it is
e↵ectively input). An inverse often exists where the derived data represents
simplerestructuringsoftheinputdata. Inthissituationmodificationstothe
data can simply be treated identically to the corresponding modifications to
the existing essential state.
Accidental Derived Data
State which is derived but not in the users’ requirements is also accidental
state. Consider the following imperative pseudo-code:
procedure int doCalculation(int y)
// ’subsidaryCalcCache’ is declared and initialized
// elsewhere in the code
if (subsidaryCalcCache.contains(y) == false) {
subsidaryCalcCache.y := slowSubsidaryCalculation(y)
}
return 3 * (4 + subsidaryCalcCache.y)
The above use of state in the doCalculation procedure seems to be
unnecessary (in the ideal world), and hence of the accidental variety. We
25

---
Page 26
---

Data Essentiality Data Type Data Mutability Classification
Essential Input - Essential State
Essential Derived Immutable Accidental State
Essential Derived Mutable Accidental State
Accidental Derived - Accidental State
Table 1: Data and State
cannot actually be sure without knowing whether and how the subsidary-
CalcCache is used elsewhere in the program, but for this example we shall
assume that there are no other uses aside from initialization. The above
procedure is thus equivalent to:
procedure int doCalculation(int y)
return 3 * (4 + slowSubsidaryCalculation(y))
It is almost certain that this use of state would not have been part of
the users’ informal requirements. It is also derived. Hence, it is quite clear
that we can eliminate it completely from our ideal world, and that hence it
is accidental.
Summary — State in the ideal world
For our ideal approach to state, we largely follow the example of functional
programming which shows how mutable state can be avoided. We need to
remember though that:
1. even in the ideal world we are going to have some essential state —
as we have just established
2. pure functional programs can e↵ectively simulate accidental state in
the same way that they can simulate essential state (using techniques
such as the one discussed above in section 5.2.3) — we obviously want
to avoid this in the ideal world.
The data type classifications are summarized in Table 1. Wherever the
table shows data as corresponding to accidental state it means that it can
be excluded from the ideal world (by re-deriving the data as required).
The obvious implication of the above is that there are large amounts of
accidental state in typical systems. In fact, it is our belief that the vast
majority of state (as encountered in typical contemporary systems) simply
26
[Image: page-026-fig-01.png]


---
Page 27
---

isn’t needed (in this ideal world). Because of this, and the huge complexity
whichstatecancause, theidealworldremovesall non-essentialstate. There
is no other state at all. No caches, no stores of derived calculations of any
kind. One e↵ect of this is that all the state in the system is visible to the
user of (or person testing) the system (because inputs can reasonably be
expected to be visible in ways which internal cached state normally is not).
7.1.2 Control in the ideal world
Whereas we have seen that some state is essential, control generally can be
completely omitted from the ideal world and as such is considered entirely
accidental. It typically won’t be mentioned in the informal requirements
and hence should not appear in the formal requirements (because these are
derived with no view to execution).
What do we mean by this? Clearly if the program is ever to run, some
control will be needed somewhere because things will have to happen in
some order — but this should no more be our concern than the fact that the
chancesaresomeelectricitywillbeneededsomewhere. Theimportantthing
is that we (as developers of the system) should not have to worry about the
control flow in the system. Specifically the results of the system should be
independent of the actual control mechanism which is finally used.
These are precisely the lessons which logic programming teaches us, and
because of this we would like to take the lead for our ideal approach to
control from logic programming which shows that control can be separated
completely.
It is worth noting that because typically the informal requirements will
not mention concurrency, that too is normally of an accidental nature. In
an ideal world we can assume that finite (stateless) computations take zero
time8 andassuchitisimmaterialtoauserwhethertheyhappeninsequence
or in parallel.
7.1.3 Summary
In the ideal world we have been able to avoid large amounts of complexity
— both state and control. As a result, it is clear that a lot of complexity
is accidental. This gives us hope that it may be possible to significantly
reduce the complexity of real large systems. The question is — how close is
it possible to get to the ideal world in the real one?
8this assumption is generally known as the “synchrony hypothesis”
27

---
Page 28
---
