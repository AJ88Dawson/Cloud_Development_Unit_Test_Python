"""EXERCISE 2: testing exceptions.

WHAT THIS IS
    The second exercise. `UserService` in src/user_service.py validates a
    username and a password and keeps registered users in memory. Almost
    everything it does wrong, it does by raising. Testing that behaviour is
    the exercise.

WHAT YOU DO HERE
    Write a test case for EVERY exception register() and login() can raise,
    and assert the exact message each time, not just the exception type.
    Several different rules raise the same ValueError, so a test that checks
    only the type cannot tell you which rule fired, and a wrong message is a
    defect in its own right. Do not forget the happy paths either: both
    register() and login() return the TRIMMED username.

THE TWO PARTS, AND PART 1 IS NOT OPTIONAL
    Part 1: write the test plan FIRST. Copy tasks/TEST_PLAN_TEMPLATE.md and
        fill in a row per case: ID, method, description, inputs, expected
        output, actual output. For this exercise the Expected output column
        holds the exception and its message, for example
        ValueError("Username must contain at least 4 characters").
    Part 2: turn each row into a test down here, then fill in the Actual
        output column honestly, including for row 2 of the guide's table.

HOW THE TODOs WORK
    Every test still to be written carries @unittest.skip, so the suite is
    green on a fresh clone and the skip count is your progress bar. To do one:
    delete the @unittest.skip line above it, then replace `pass` with your
    arrange / act / assert. JUnit spells that marker @Disabled("reason").

HOW TO RUN
    From the repository root, the whole suite:
        python -m unittest discover
    Just this file:
        python -m unittest tests.test_user_service
    One test by name:
        python -m unittest tests.test_user_service.UserServiceTest.test_register_rejects_a_password_with_no_number
    Add -v for one line per test with the skip reasons.

THE FULL BRIEF
    tasks/02_testing_exceptions.md, which lists every rule and its message.

A NOTE BEFORE YOU START
    Every test below can pass against the code as it stands. When one fails,
    read the failure message carefully: the order the validation rules run in
    decides which message you get, and that is easy to get wrong in a plan.
    One row of the exercise guide's own test plan has exactly that mistake in
    it. See CODE_CORRECTIONS.md, and the worked example below.
"""

import unittest

from user_service import UserService


class UserServiceTest(unittest.TestCase):
    """The JUnit UserServiceTest class, in Python. Methods named test_* run."""

    def setUp(self):
        """THE FIXTURE. Runs before EVERY test method, like JUnit's
        @BeforeEach (and tearDown is @AfterEach, unused here).

        This one earns its keep. UserService keeps its registered users in a
        dict on the instance, so it DOES hold state between calls. Building a
        brand new service here means a user registered in one test cannot
        leak into the next and turn a passing test into a mysterious
        "Username already exists". Any test that needs an existing user must
        register it for itself, in its own Arrange step.
        """
        self.service = UserService()

    # -----------------------------------------------------------------
    # register()
    # -----------------------------------------------------------------

    def test_register_rejects_a_password_with_no_number(self):
        """WORKED EXAMPLE - test case 2 from the guide's test plan, corrected.

        The guide uses the password "Codes". That is only five characters, so
        the length rule fires first and you get "Password must contain at
        least 6 characters" instead. "Codess" is six characters with no
        digit, which is what the test case was actually trying to express.
        """
        # Arrange
        username = "bobby"
        password = "Codess"

        # Act and Assert. assertRaises used as a context manager is the
        # unittest equivalent of JUnit's assertThrows: a `with` block rather
        # than a lambda. The exception it caught is on context.exception, so
        # str(context.exception) gives you the message, where Java would call
        # getMessage() on the value assertThrows returned.
        with self.assertRaises(ValueError) as context:
            self.service.register(username, password)

        self.assertEqual(
            str(context.exception), "Password must contain at least 1 number character"
        )

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_returns_the_trimmed_username_for_a_valid_user(self):
        # The happy path. Assert that register("  bobby  ", "Codes123")
        # returns "bobby", with the surrounding whitespace stripped. Nothing
        # is raised. This is the case that proves the trimming, so pass a
        # username with spaces at both ends deliberately.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_username_is_none(self):
        # Assert ValueError with the exact message "Username must not be
        # null" for register(None, "Codes123"). None is Python's null.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_username_is_whitespace_only(self):
        # Assert ValueError, message "Username must not be whitespace only",
        # for a username that is spaces and nothing else, such as "   ".
        # Note this fires BEFORE the 4-character rule, even though "   " is
        # three characters, because the emptiness check runs first.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_is_none(self):
        # Assert ValueError, message "Password must not be null", for
        # register("bobby", None).
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_is_whitespace_only(self):
        # Assert ValueError, message "Password must not be whitespace only",
        # for a password of spaces only, such as "      ". Six spaces is long
        # enough to clear the length rule, so this really is the rule under
        # test.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_username_is_too_short(self):
        # Assert ValueError, message "Username must contain at least 4
        # characters", for a three character username such as "bob".
        # This is a borderline value: four characters is the shortest name
        # that must be ACCEPTED, so it is worth adding a second test proving
        # a 4-character username registers fine.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_username_is_already_taken(self):
        # Arrange by registering "bobby" / "Codes123" successfully, then act
        # by registering the same username again (any valid password), and
        # assert ValueError with the message "Username already exists". This
        # is the one test that depends on state built up earlier in the same
        # test, which is why setUp hands you a fresh service.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_is_too_short(self):
        # Assert ValueError, message "Password must contain at least 6
        # characters", for a five character password such as "Cod1e". Note
        # that "Cod1e" satisfies every other password rule, so length is the
        # only reason it can fail. Six characters is the borderline that must
        # be accepted.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_has_no_uppercase(self):
        # Assert ValueError, message "Password must contain at least 1
        # uppercase character", for a password such as "codes123": long
        # enough, has lowercase, has a digit, no capital letter.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_when_the_password_has_no_lowercase(self):
        # Assert ValueError, message "Password must contain at least 1
        # lowercase character", for a password such as "CODES123". Remember
        # the uppercase rule runs first, so the password must contain a
        # capital or you will get the other message.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_accepts_a_password_whose_only_digit_is_zero(self):
        # A borderline happy path. Assert that register("bobby", "Codes0")
        # returns "bobby", because "Codes0" does contain a number: zero is a
        # number. Six characters, one capital, lowercase letters, one digit.
        # This is the kind of case a naive "is it truthy" check gets wrong.
        pass

    # -----------------------------------------------------------------
    # login()
    # -----------------------------------------------------------------

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_returns_the_username_after_a_successful_registration(self):
        # Test case 1 from the guide's test plan, and it behaves exactly as
        # written. Arrange by registering "bobby" / "Codes123", act by
        # logging in with the same pair, assert "bobby" comes back.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_username_is_none(self):
        # Assert ValueError, message "Username and password must not be
        # null". Note login() uses one shared message for both arguments,
        # unlike register(), which names whichever one is missing.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_password_is_none(self):
        # Assert the same message, "Username and password must not be null",
        # this time with a valid username and a None password. Two separate
        # inputs reaching one message is worth two separate test cases.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_username_is_whitespace_only(self):
        # Assert ValueError with the message "Username and password must not
        # be empty" for a whitespace-only username.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_runtime_error_when_the_user_was_never_registered(self):
        # The one case in this file that is NOT a ValueError. Log in as a
        # user who was never registered and assert RuntimeError with the
        # message "Invalid username supplied". RuntimeError is the Python
        # stand-in for Java's RuntimeException. Get the expected type wrong
        # and assertRaises will not catch it, so the test errors rather than
        # failing, which looks different in the output.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_password_is_wrong(self):
        # Arrange by registering "bobby" / "Codes123", then log in as "bobby"
        # with a different valid-looking password such as "Wrong123", and
        # assert ValueError with the message "Invalid password supplied".
        # Note the pair: an unknown user gives RuntimeError, a known user
        # with the wrong password gives ValueError. Two messages, two types,
        # two test cases.
        pass


if __name__ == "__main__":
    # Lets you run this one file with `python -m tests.test_user_service`.
    unittest.main()
