"""EXERCISE 3: mocking in a unit test.

WHAT THIS IS
    The third exercise. `UserController` in src/user_controller.py runs the
    same validation rules as exercise 2's UserService, but it no longer keeps
    users itself: it asks a UserRepository whether a username exists and hands
    the user over to be stored. You test the controller ALONE, with a fake
    repository in place of a real one, so a failure here can only be the
    controller's fault.

WHAT YOU DO HERE
    For every case, ask both questions the guide asks:
      * what did the controller return or raise?
      * and what did it call on the repository, with what arguments, how many
        times, or did it correctly call nothing at all?
    When validation fails the repository must never be touched, and proving
    that is as much a test as proving something happened.

THE TWO PARTS, AND PART 1 IS NOT OPTIONAL
    Part 1: update the exercise 2 test plan rather than starting again. Copy
        tasks/TEST_PLAN_TEMPLATE.md if you want the fuller table: it adds a
        Class column and a Mock setup / verification column, both of which
        you now need. Two changes to carry in: register() has a NEW exception,
        "Username already exists", now decided by the repository rather than
        by an in-memory map; and login() has LOST exceptions, because the
        repository is expected to handle bad credentials.
    Part 2: turn each row into a test down here, stubbing the mock in Arrange
        and verifying it in Assert.

HOW THE TODOs WORK
    Every test still to be written carries @unittest.skip, so the suite is
    green on a fresh clone and the skip count is your progress bar. To do one:
    delete the @unittest.skip line above it, then replace `pass` with your
    arrange / act / assert. JUnit spells that marker @Disabled("reason").

HOW TO RUN
    From the repository root, the whole suite:
        python -m unittest discover
    Just this file:
        python -m unittest tests.test_user_controller
    One test by name:
        python -m unittest tests.test_user_controller.UserControllerTest.test_register_saves_a_valid_user_through_the_repository
    Add -v for one line per test with the skip reasons.

THE FULL BRIEF
    tasks/03_mocking.md. The stretch task that follows it is
    tasks/04_stretch_tdd_repository.md, and its test file already exists at
    tests/test_concrete_user_repository.py.

MOCKITO DOES NOT EXIST IN PYTHON
    The guide says to use Mockito. Mockito is a Java library, so we use
    unittest.mock from the standard library instead. It ships with Python, so
    there is nothing to install. The ideas map across one for one:

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
    is just an object that answers to any attribute, and because
    UserRepository is a typing.Protocol rather than a Java interface, no
    subclassing is needed. Stubbing is an assignment, not a call chain, and
    verification happens AFTER the act in both languages.
"""

import unittest
from unittest.mock import MagicMock

from user import User
from user_controller import UserController


class UserControllerTest(unittest.TestCase):
    """The JUnit UserControllerTest class, in Python. Methods named test_* run."""

    def setUp(self):
        """THE FIXTURE. Runs before EVERY test method, like JUnit's
        @BeforeEach. In the Java version this same method carries @BeforeEach
        and builds both objects, or the @Mock and @InjectMocks annotations do
        it for you; here it is two plain lines of Python.

        Build a fake repository and inject it into the controller. A fresh
        mock per test matters even more than a fresh object: a mock REMEMBERS
        every call made to it, and assert_called_once_with counts calls over
        the mock's whole life, so a mock shared between tests would make those
        assertions lie.

        Every method on a MagicMock returns another MagicMock until you tell
        it otherwise with return_value or side_effect. That is why
        `repository.exists(...)` is truthy by default, and why any test about
        a username NOT existing has to stub exists to False explicitly.
        """
        self.repository = MagicMock()
        self.controller = UserController(self.repository)

    # -----------------------------------------------------------------
    # register()
    # -----------------------------------------------------------------

    def test_register_saves_a_valid_user_through_the_repository(self):
        """WORKED EXAMPLE - row 1 of the guide's exercise 3 test plan.

        Register a valid user: User(1, "bobby", "Codes123"), exists stubbed to
        return False, verify register was called once with that user, expected
        output the same User back. Stub the repository, act, then verify the
        interaction.
        """
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
        # Call register(None). Assert ValueError with the message "User must
        # not be null", AND that the repository was never touched, with
        # self.repository.exists.assert_not_called(). That second assertion is
        # Mockito's verify(repo, never()).exists(...) and is the half of the
        # test that mocking buys you.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_username_is_none(self):
        # Build a User whose username is None, act, assert ValueError with the
        # message "Username must not be null". Verify the repository was never
        # called: validation fails before it is reached.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_username_is_whitespace_only(self):
        # A User whose username is spaces only, such as "   ". Assert
        # ValueError, message "Username must not be whitespace only", and no
        # repository call.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_is_none(self):
        # A valid username with a None password. Assert ValueError, message
        # "Password must not be null", and no repository call.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_is_whitespace_only(self):
        # A valid username with a password of spaces only. Assert ValueError,
        # message "Password must not be whitespace only", and no repository
        # call.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_username_is_too_short(self):
        # A three character username such as "bob". Assert ValueError, message
        # "Username must contain at least 4 characters". This rule runs BEFORE
        # the repository is asked about uniqueness, so exists must still never
        # be called. Four characters is the borderline that is accepted.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_repository_says_the_username_exists(self):
        # The exception that is NEW in exercise 3, and the only one that
        # depends on the mock's answer rather than on the input. Arrange with
        # self.repository.exists.return_value = True, act with an otherwise
        # perfectly valid user, and assert ValueError with the message
        # "Username already exists". Then assert
        # self.repository.register.assert_not_called(): the user must not be
        # stored. This is the test the whole exercise exists for, because
        # there is no real repository to put a duplicate into.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_is_too_short(self):
        # Stub exists to return False first, or the default truthy MagicMock
        # will trip the uniqueness rule and you will get the wrong message.
        # Then a five character password such as "Cod1e", and assert
        # ValueError, message "Password must contain at least 6 characters".
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_has_no_uppercase(self):
        # exists stubbed to False, password "codes123". Assert ValueError,
        # message "Password must contain at least 1 uppercase character", and
        # that register was never called.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_has_no_lowercase(self):
        # exists stubbed to False, password "CODES123". Assert ValueError,
        # message "Password must contain at least 1 lowercase character". The
        # uppercase rule runs first, so the password must contain a capital.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_has_no_number(self):
        # exists stubbed to False, password "Codess": six characters, a
        # capital, lowercase, no digit. Assert ValueError, message "Password
        # must contain at least 1 number character". Same corrected password
        # as the exercise 2 worked example, and for the same reason.
        pass

    # -----------------------------------------------------------------
    # login()
    # -----------------------------------------------------------------

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_returns_the_user_the_repository_gives_back(self):
        # The happy path, and the one place login() delegates. Arrange a valid
        # User and stub self.repository.login.return_value to it, act, then
        # assert the controller returned that same user and called
        # repository.login exactly once with the whole User object:
        # self.repository.login.assert_called_once_with(user). Note it passes
        # the User itself, not the username and password separately.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_user_is_none(self):
        # login(None). Assert ValueError, message "User must not be null", and
        # self.repository.login.assert_not_called().
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_username_is_none(self):
        # A User whose username is None. Assert ValueError with the message
        # "Username and password must not be null", one shared message for
        # both fields, and no repository call. Worth a second test with a None
        # password reaching the same message.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_password_is_empty(self):
        # A User with a valid username and password set to "". Assert
        # ValueError, message "Username and password must not be empty", and
        # no repository call. Careful: this check does NOT trim first, so a
        # whitespace-only password is NOT empty and does reach the repository.
        # That behaviour is ported from the Java original deliberately, so if
        # you want a test for it, assert the delegation rather than a raise.
        pass


if __name__ == "__main__":
    # Lets you run this one file with `python -m tests.test_user_controller`.
    unittest.main()
