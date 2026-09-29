"""Exercise 3 - the repository abstraction that UserController depends on.

The Java original is an interface. Python's nearest equivalents are an
abstract base class (ABC) or a typing.Protocol. We use a Protocol because
it is structural: any object with matching methods satisfies it, including
a unittest.mock.MagicMock, which is exactly what exercise 3 needs.

Java differences worth noting:
  * There is no `implements` keyword and nothing is checked at runtime, so
    unlike Java a class can forget a method and still be accepted right up
    until that method is called. An ABC would fail earlier, at construction,
    but would also stop a MagicMock being used in its place.
  * The return types below are hints only. They are not enforced.
"""

from typing import Protocol

from exercise3.user import User


class UserRepository(Protocol):
    def exists(self, trimmed_username: str) -> bool:
        """Return True if a user with this username is already stored."""
        ...

    def register(self, user: User) -> User:
        """Store the user and return the stored instance."""
        ...

    def login(self, user: User) -> User:
        """Return the stored user if the credentials match."""
        ...
