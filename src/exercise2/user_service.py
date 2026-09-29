"""Exercise 2 - registering and logging in users, used for "testing exceptions".

Python port of the Java UserService class.

Translation notes:
  * Java's IllegalArgumentException becomes ValueError. ValueError is what
    Python raises when an argument has the right type but an unacceptable
    value, which is exactly what IllegalArgumentException means.
  * Java's RuntimeException becomes RuntimeError, the closest built-in.
  * Java's HashMap becomes a plain dict. Java makes no promise about HashMap
    iteration order; Python dicts remember insertion order. Nothing here
    depends on ordering, but do not write a test that relies on it if you
    want the Java and Python suites to agree.
  * Java has checked exceptions and a `throws` clause. Python has neither,
    so the exceptions a method can raise are documented in comments only.
  * Java's String.matches() matches the WHOLE string. The password rules
    below want "contains one of these", so they use re.search rather than
    re.fullmatch.
"""

import re

# one pattern per password rule. Each names only the character the rule is
# about, and is used with re.search, so it asks "does the password contain
# one of these?" and nothing more.
_HAS_UPPERCASE = r"[A-Z]"
_HAS_LOWERCASE = r"[a-z]"
_HAS_NUMBER = r"[0-9]"


class UserService:
    """Holds registered users in memory as {username: password}."""

    def __init__(self):
        self.users = {}

    def register(self, username, password):
        """Register a new user and return the trimmed username.

        Raises ValueError if any validation rule is broken.
        """
        # username must not be None or empty
        if username is None:
            raise ValueError("Username must not be null")
        trimmed_username = username.strip()
        if trimmed_username == "":
            raise ValueError("Username must not be whitespace only")

        # password must not be None or empty
        if password is None:
            raise ValueError("Password must not be null")
        trimmed_password = password.strip()
        if trimmed_password == "":
            raise ValueError("Password must not be whitespace only")

        # username must be at least 4 characters
        if len(trimmed_username) < 4:
            raise ValueError("Username must contain at least 4 characters")

        # username must be unique
        if self.users.get(trimmed_username) is not None:
            raise ValueError("Username already exists")

        # password must be at least 6 characters
        if len(trimmed_password) < 6:
            raise ValueError("Password must contain at least 6 characters")

        # password must contain at least 1 uppercase character. A "contains"
        # check, not a whole-string match: a whole-string match fails on any
        # character the class does not list, so a single unexpected symbol
        # would report the wrong rule.
        if not re.search(_HAS_UPPERCASE, trimmed_password):
            raise ValueError("Password must contain at least 1 uppercase character")

        # password must contain at least 1 lowercase character
        if not re.search(_HAS_LOWERCASE, trimmed_password):
            raise ValueError("Password must contain at least 1 lowercase character")

        # password must contain at least 1 number
        if not re.search(_HAS_NUMBER, trimmed_password):
            raise ValueError("Password must contain at least 1 number character")

        # add user to the map
        self.users[trimmed_username] = trimmed_password

        return trimmed_username

    def login(self, username, password):
        """Return the username supplied if the credentials are valid.

        Raises ValueError for missing or empty arguments, and RuntimeError
        when no matching user is found.
        """
        # username and password must not be None
        if username is None or password is None:
            raise ValueError("Username and password must not be null")
        trimmed_username = username.strip()
        trimmed_password = password.strip()

        # username and password must not be empty
        if trimmed_username == "" or trimmed_password == "":
            raise ValueError("Username and password must not be empty")

        # look the user up by their username, then check the password they
        # supplied against the one we stored. Keying the map by password
        # would only ever match a user whose name happened to equal their
        # own password.
        saved_password = self.users.get(trimmed_username)
        if saved_password is None:
            raise RuntimeError("Invalid username supplied")

        if trimmed_password != saved_password:
            raise ValueError("Invalid password supplied")

        # return the trimmed username, to match what register() returns
        return trimmed_username
