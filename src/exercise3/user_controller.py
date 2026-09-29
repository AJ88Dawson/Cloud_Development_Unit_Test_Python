"""Exercise 3 - the class under test, with its repository to be mocked.

Python port of the Java UserController. The validation rules are the same as
UserService.register(), except that uniqueness is delegated to the repository
and login() does far less work because the repository is expected to handle
invalid credentials.

The password patterns are imported from user_service so that the two
exercises cannot drift apart. See CODE_CORRECTIONS.md for what those rules
used to look like and why they were changed.
"""

import re

from exercise2.user_service import _HAS_LOWERCASE, _HAS_NUMBER, _HAS_UPPERCASE


class UserController:
    def __init__(self, user_repository):
        # In Java the constructor parameter is typed UserRepository and the
        # compiler enforces it. Here any object with the right methods will
        # do, which is what lets a MagicMock be passed straight in with no
        # subclassing and no framework.
        self.repository = user_repository

    def register(self, user):
        """Validate the user then hand it to the repository.

        Raises ValueError if any validation rule is broken.
        """
        # user must not be None
        if user is None:
            raise ValueError("User must not be null")

        username = user.username
        password = user.password

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

        # username must be unique - this is one of the calls you will mock
        if self.repository.exists(trimmed_username):
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

        # add the user to the database
        return self.repository.register(user)

    def login(self, user):
        """Validate the bare minimum then hand the user to the repository.

        Raises ValueError for a missing user, username or password.
        """
        # user must not be None
        if user is None:
            raise ValueError("User must not be null")

        username = user.username
        password = user.password

        # username and password must not be None
        if username is None or password is None:
            raise ValueError("Username and password must not be null")

        # username and password must not be empty. Note that the Java
        # original calls isEmpty() here WITHOUT trimming first, so a
        # whitespace-only username reaches the repository. Ported as is.
        if username == "" or password == "":
            raise ValueError("Username and password must not be empty")

        return self.repository.login(user)
