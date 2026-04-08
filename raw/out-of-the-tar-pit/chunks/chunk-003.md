# 3 Approaches to Understanding

3 Approaches to Understanding
Wearguedabovethatthedangerofcomplexitycamefromitsimpactonour
attempts to understand a system. Because of this, it is helpful to consider
the mechanisms that are commonly used to try to understand systems. We
can then later consider the impact that potential causes of complexity have
on these approaches. There are two widely-used approaches to understand-
ing systems (or components of systems):
Testing This is attempting to understand a system from the outside — as
a “black box”. Conclusions about the system are drawn on the basis
of observations about how it behaves in certain specific situations.
Testingmaybeperformedeitherbyhumanorbymachine. Theformer
is more common for whole-system testing, the latter more common for
individual component testing.
Informal Reasoning This is attempting to understand the system by ex-
amining it from the inside. The hope is that by using the extra infor-
mation available, a more accurate understanding can be gained.
Of the two informal reasoning is the most important by far. This is
because — as we shall see below — there are inherent limits to what can
be achieved by testing, and because informal reasoning (by virtue of being
an inherent part of the development process) is always used. The other
justification is that improvements in informal reasoning will lead to less
errors being created whilst all that improvements in testing can do is to lead
to more errors being detected. As Dijkstra said in his Turing award speech
[Dij72, EWD340]:
4

---
Page 5
---

“Those who want really reliable software will discover that they
must find means of avoiding the majority of bugs to start with.”
andasO’Keefe(whoalsostressedtheimportanceof“understandingyour
problem” and that “Elegance is not optional”) said [O’K90]:
“Our response to mistakes should be to look for ways that we
can avoid making them, not to blame the nature of things.”
The key problem with testing is that a test (of any kind) that uses one
particular set of inputs tells you nothing at all about the behaviour of the
system or component when it is given a di↵erent set of inputs. The huge
numberofdi↵erentpossibleinputsusuallyrulesoutthepossibilityoftesting
them all, hence the unavoidable concern with testing will always be — have
you performed the right tests?. The only certain answer you will ever get
to this question is an answer in the negative — when the system breaks.
Again, as Dijkstra observed [Dij71, EWD303]:
“testing is hopelessly inadequate....(it) can be used very e↵ec-
tively to show the presence of bugs but never to show their ab-
sence.”
We agree with Dijkstra. Rely on testing at your peril.
This is not to say that testing has no use. The bottom line is that all
ways of attempting to understand a system have their limitations (and this
includesbothinformal reasoning —whichislimitedinscope, impreciseand
hence prone to error — as well as formal reasoning — which is dependent
upon the accuracy of a specification). Because of these limitations it may
often be prudent to employ both testing and reasoning together.
It is precisely because of the limitations of all these approaches that
simplicity isvital. Whenconsiderednexttotestingandreasoning,simplicity
is more important than either. Given a stark choice between investment
in testing and investment in simplicity, the latter may often be the better
choicebecauseitwillfacilitateall futureattemptstounderstandthesystem
— attempts of any kind.
