# 12 Conclusions

12 Conclusions
We have argued that complexity causes more problems in large software
systems than anything else. We have also argued that it can be tamed
— but only through a concerted e↵ort to avoid it where possible, and to
separate itwherenot. Specificallywehavearguedthatasystemcanusefully
be separated into three main parts: the essential state, the essential logic,
and the accidental state and control.
We believe that taking these principles and applying them to the top
level of a system design — e↵ectively using di↵erent specialised languages
for the di↵erent components — can o↵er more in terms simplicity than can
the unstructured adoption of any single general language (be it imperative,
logicorfunctional). Inmakingthisargumentwebrieflysurveyedeachofthe
common programming paradigms, paying some attention to the weaknesses
of object-orientation as a particular example of an imperative approach.
In cases (such as existing large systems) where this separation cannot be
directly applied we believe the focus should be on avoiding state, avoiding
explicit control where possible, and striving at all costs to get rid of code.
So, what is the way out of the tar pit? What is the silver bullet? ...it
may not be FRP, but we believe there can be no doubt that it is simplicity.
References
[Bac78] John W. Backus. Can programming be liberated from the von
Neumann style? a functional style and its algebra of programs.
Commun. ACM, 21(8):613–641, 1978.
[Bak93] Henry G. Baker. Equal rights for functional objects or, the more
things change, the more they are the same. Journal of Object-
Oriented Programming, 4(4):2–27, October 1993.
[Boo91] G. Booch. Object Oriented Design with Applications. Ben-
jamin/Cummings, 1991.
[Bro86] Frederick P. Brooks, Jr. No silver bullet: Essence and accidents of
software engineering. Information Processing 1986, Proceedings of
the Tenth World Computing Conference, H.-J. Kugler, ed.: 1069–
76. Reprinted in IEEE Computer, 20(4):10-19, April 1987, and in
Brooks, The Mythical Man-Month: Essays on Software Engineer-
ing, Anniversary Edition, Chapter 16, Addison-Wesley, 1995.
64

---
Page 65
---

[Che76] P. P. Chen. “The Entity-Relationship Model”. ACM Trans. on
Database Systems (TODS), 1:9–36, 1976.
[Cod70] E.F.Codd. Arelationalmodelofdataforlargeshareddatabanks.
Comm. ACM, 13(6):377–387, June 1970.
[Cod79] E. F. Codd. Extending the database relational model to capture
more meaning. ACM Trans. on Database Sys., 4(4):397, December
1979.
[Cod90] E. F. Codd. The Relational Model for Database Management, Ver-
sion 2. Addison-Wesley, 1990.
[Cor91] Fernando J. Corbat´o. On building systems that will fail. Commun.
ACM, 34(9):72–81, 1991.
[Dat04] C. J. Date. An Introduction to Database Systems. Addison Wesley,
8th edition, 2004.
[DD00] Hugh Darwen and C. J. Date. Foundation for Future Database
Systems: The Third Manifesto. Addison-Wesley, 2nd edition, 2000.
[Dij71] Edsger W. Dijkstra. On the reliability of programs. circulated
privately, 1971.
[Dij72] Edsger W. Dijkstra. The humble programmer. Commun. ACM,
15(10):859–866, 1972.
[Dij97] Dijkstra. The tide, not the waves. In Peter J. Denning and
Robert M. Metcalfe, editors, Beyond Calculation: The Next Fifty
Years of Computing, Copernicus, 1997. 1997.
[Eco04] Managing complexity. The Economist, 373(8403):89–91, 2004.
[EH97] Conal Elliott and Paul Hudak. Functional reactive animation. In
Proceedings of the ACM SIGPLAN International Conference on
Functional Programming (ICFP-97), volume 32,8 of ACM SIG-
PLAN Notices, pages 263–273, New York, June 9–11 1997. ACM
Press.
[HJ89] I. Hayes and C. Jones. Specifications are not (necessarily) exe-
cutable. IEE Software Engineering Journal, 4(6):330–338, Novem-
ber 1989.
