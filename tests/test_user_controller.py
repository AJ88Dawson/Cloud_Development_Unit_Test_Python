"""Exercise 3 - mocking in a unit test.

The guide says to use Mockito. Mockito is a Java library and does not exist
in Python, so we use unittest.mock from the standard library instead. It
ships with Python, so there is nothing to install. The ideas map across one
for one:

    Mockito                             unittest.mock
    ---------------------------------   ---------------------------------
    @Mock UserRepository repository     repository = MagicMock()
    @InjectMocks UserController c       c = UserController(repository)
    when(repo.exists("bob")).           repository.exists.return_value =
        thenReturn(true)                    True
    when(repo.login(u)).thenThrow(e)    repository.login.side_effect = e
    verify(repo).register(user)         repository.register.assert_called_once_with(user)
    verify(repo, never()).register()    repository.register.assert_not_called()

There is no annotation processor and no test runner extension: a MagicMock
is just an object that answers to any attribute, and because UserRepository
is a typing.Protocol rather than a Java interface, no subclassing is needed.

HOW TO USE THIS FILE
  * One test is written for you as a worked example.
  * Every other test is a TODO that SKIPs until you write it.
"""

import unittest
from unittest.mock import MagicMock

from user import User
from user_controller import UserController


class UserControllerTest(unittest.TestCase):
    def setUp(self):
        """Build a fake repository and inject it into the controller.

        Every method on a MagicMock returns another MagicMock until you tell
        it otherwise with return_value or side_effect.
        """
        self.repository = MagicMock()
        self.controller = UserController(self.repository)

    # -----------------------------------------------------------------
    # register()
    # -----------------------------------------------------------------

    def test_register_saves_a_valid_user_through_the_repository(self):
        """WORKED EXAMPLE - stub the repository, then verify the interaction."""
        # Arrange
        user = User(id=1, username="bobby", password="Codes123")
        self.repository.exists.return_value = False
        self.repository.register.return_value = user

        # Act
        result = self.controller.register(user)

        # Assert - both the returned value and the calls that were made
        self.assertEqual(result, user)
        self.repository.exists.assert_called_once_with("bobby")
        self.repository.register.assert_called_once_with(user)

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_user_is_none(self):
        # Should assert "User must not be null" and that the repository was
        # never touched (self.repository.exists.assert_not_called()).
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_username_is_none(self):
        # Should assert "Username must not be null".
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_username_is_whitespace_only(self):
        # Should assert "Username must not be whitespace only".
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_is_none(self):
        # Should assert "Password must not be null".
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_is_whitespace_only(self):
        # Should assert "Password must not be whitespace only".
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_username_is_too_short(self):
        # Should assert "Username must contain at least 4 characters".
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_repository_says_the_username_exists(self):
        # This is the exception that is NEW in exercise 3. Stub
        # self.repository.exists to return True, then assert the message
        # "Username already exists" and that register was never called.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_is_too_short(self):
        # Should stub exists to False, then assert
        # "Password must contain at least 6 characters".
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_has_no_uppercase(self):
        # Should assert "Password must contain at least 1 uppercase character".
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_has_no_lowercase(self):
        # Should assert "Password must contain at least 1 lowercase character".
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_has_no_number(self):
        # Should assert "Password must contain at least 1 number character".
        pass

    # -----------------------------------------------------------------
    # login()
    # -----------------------------------------------------------------

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_returns_the_user_the_repository_gives_back(self):
        # Should stub self.repository.login to return the user, then assert
        # the controller returns it and called repository.login exactly once.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_user_is_none(self):
        # Should assert "User must not be null" and that the repository was
        # never called.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_username_is_none(self):
        # Should assert "Username and password must not be null".
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_password_is_empty(self):
        # Should assert "Username and password must not be empty".
        pass


# ---------------------------------------------------------------------------
# Stretch task - test-driven development
# ---------------------------------------------------------------------------
# Write a test plan for the three UserRepository methods, then build
# ConcreteUserRepository test first: write one failing test, write just
# enough implementation to pass it, repeat. Store the users in a plain list
# on the instance. Put the class in src/concrete_user_repository.py and its
# tests in tests/test_concrete_user_repository.py, as another
# unittest.TestCase class.
#
# No mocks here: this is the real implementation, so the tests are ordinary
# state-based tests.


if __name__ == "__main__":
    unittest.main()
