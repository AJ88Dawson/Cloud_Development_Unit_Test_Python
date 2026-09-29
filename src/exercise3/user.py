"""Exercise 3 - the User data object.

The Java original was a classic JavaBean: private fields, a no-argument
constructor, a full constructor, getters and setters, and hand-written
equals(), hashCode() and toString(). In Python a dataclass gives you all of
that for free, so the idiomatic translation is much shorter. @dataclass
generates __init__, __eq__ and __repr__ for you, and the Java getters and
setters are unnecessary because Python attributes are public and can be
turned into properties later without changing any caller.

One difference worth knowing: the Java equals() rejects objects of a
different class outright, whereas a dataclass __eq__ returns NotImplemented
for a different class, which Python then turns into False. The observable
result is the same.
"""

from dataclasses import dataclass


@dataclass
class User:
    # Defaults are supplied so that User() works, mirroring the Java
    # no-argument constructor that left the fields at 0 and null.
    id: int = 0
    username: str = ""
    password: str = ""
