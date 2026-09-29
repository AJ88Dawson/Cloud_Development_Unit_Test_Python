"""Exercise 3 stretch task - model answer for the concrete repository.

Built test first: see test_concrete_user_repository_solution.py. Users are
held in a plain list, as the guide asks.

Because UserRepository is a typing.Protocol rather than a Java interface,
this class does not inherit from it and there is no `implements` keyword.
It satisfies the protocol simply by having the three methods.
"""

from user import User


class ConcreteUserRepository:
    def __init__(self):
        # The guide asks for a List<User>, so a plain list it is. A dict
        # keyed by username would be faster, but the exercise is about the
        # tests, not the data structure.
        self.users = []

    def exists(self, trimmed_username: str) -> bool:
        return any(user.username == trimmed_username for user in self.users)

    def register(self, user: User) -> User:
        # The interface says nothing about duplicates, so this
        # implementation refuses them rather than storing two users with
        # the same name. Decide this yourself and write it into your plan.
        if self.exists(user.username):
            raise ValueError("Username already exists")
        self.users.append(user)
        return user

    def login(self, user: User) -> User:
        for stored in self.users:
            if stored.username == user.username and stored.password == user.password:
                return stored
        raise ValueError("Invalid username or password")
