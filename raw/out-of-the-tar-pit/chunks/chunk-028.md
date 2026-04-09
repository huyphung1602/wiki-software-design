# 9.3 Types

9.3 Types
A final comment is that — in addition to a fairly typical set of standard
types — FRP provides a limited ability to define new user types for use in
the essential state and essential logic components.
Specifically it permits the creation of disjoint union types (sometimes
known as “enumeration” types) but does not permit the creation of new
product types (types with multiple subsidiary components). This is because
(as mentioned above) we have a strong desire to avoid any unnecessary data
abstraction.
Finally, it probably makes sense for infrastructures to provide type in-
ference for the essential logic. Interesting work in this area has been carried
out in the Machiavelli system [OB88].
