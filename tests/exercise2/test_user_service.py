"""EXERCISE 2: testing exceptions.

WHAT THIS IS
    The second exercise. `UserService` in src/exercise2/user_service.py validates a
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
        python -m unittest tests.exercise2.test_user_service
    One test by name:
        python -m unittest tests.exercise2.test_user_service.UserServiceTest.test_register_rejects_a_password_with_no_number
    Add -v for one line per test with the skip reasons.

THE FULL BRIEF
    tasks/02_testing_exceptions.md, which lists every rule and its message.

A NOTE BEFORE YOU START
    Every test below can pass against the code as it stands. When one fails,
    read the failure message carefully: the order the validation rules run in
    decides which message you get, and that is easy to get wrong in a plan.
    One row of the exercise guide's own test plan has exactly that mistake in
    it. See the worked example below.
"""

import unittest

from exercise2.user_service import UserService


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

    def test_register_returns_the_trimmed_username_for_a_valid_user(self):
        # Arrange
        username = "  bobby  "
        password = "Codes123"

        # Act
        result = self.service.register(username, password)

        # Assert
        self.assertEqual(result, "bobby")

    def test_register_raises_value_error_when_the_username_is_none(self):
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.service.register(None, "Codes123")

        self.assertEqual(str(context.exception), "Username must not be null")

    def test_register_raises_value_error_when_the_username_is_whitespace_only(self):
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.service.register("   ", "Codes123")

        self.assertEqual(str(context.exception), "Username must not be whitespace only")

    def test_register_raises_value_error_when_the_password_is_none(self):
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.service.register("bobby", None)

        self.assertEqual(str(context.exception), "Password must not be null")

    def test_register_raises_value_error_when_the_password_is_whitespace_only(self):
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.service.register("bobby", "      ")

        self.assertEqual(str(context.exception), "Password must not be whitespace only")

    def test_register_raises_value_error_when_the_username_is_too_short(self):
        # Act and Assert. "bob" is three characters; four is the borderline
        # that must be accepted.
        with self.assertRaises(ValueError) as context:
            self.service.register("bob", "Codes123")

        self.assertEqual(str(context.exception), "Username must contain at least 4 characters")

    def test_register_raises_value_error_when_the_username_is_already_taken(self):
        # Arrange
        self.service.register("bobby", "Codes123")

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.service.register("bobby", "Codes456")

        self.assertEqual(str(context.exception), "Username already exists")

    def test_register_raises_value_error_when_the_password_is_too_short(self):
        # Act and Assert. "Cod1e" is five characters; six is the borderline
        # that must be accepted.
        with self.assertRaises(ValueError) as context:
            self.service.register("bobby", "Cod1e")

        self.assertEqual(str(context.exception), "Password must contain at least 6 characters")

    def test_register_raises_value_error_when_the_password_has_no_uppercase(self):
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.service.register("bobby", "codes123")

        self.assertEqual(
            str(context.exception), "Password must contain at least 1 uppercase character"
        )

    def test_register_raises_value_error_when_the_password_has_no_lowercase(self):
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.service.register("bobby", "CODES123")

        self.assertEqual(
            str(context.exception), "Password must contain at least 1 lowercase character"
        )

    def test_register_accepts_a_password_whose_only_digit_is_zero(self):
        # Act and Assert. "Codes0" does contain a number - zero is a number.
        result = self.service.register("bobby", "Codes0")

        self.assertEqual(result, "bobby")

    # -----------------------------------------------------------------
    # login()
    # -----------------------------------------------------------------

    def test_login_returns_the_username_after_a_successful_registration(self):
        # Arrange
        self.service.register("bobby", "Codes123")

        # Act
        result = self.service.login("bobby", "Codes123")

        # Assert
        self.assertEqual(result, "bobby")

    def test_login_raises_value_error_when_the_username_is_none(self):
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.service.login(None, "Codes123")

        self.assertEqual(str(context.exception), "Username and password must not be null")

    def test_login_raises_value_error_when_the_password_is_none(self):
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.service.login("bobby", None)

        self.assertEqual(str(context.exception), "Username and password must not be null")

    def test_login_raises_value_error_when_the_username_is_whitespace_only(self):
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.service.login("   ", "Codes123")

        self.assertEqual(str(context.exception), "Username and password must not be empty")

    def test_login_raises_runtime_error_when_the_user_was_never_registered(self):
        # Act and Assert
        with self.assertRaises(RuntimeError) as context:
            self.service.login("ghost", "Codes123")

        self.assertEqual(str(context.exception), "Invalid username supplied")

    def test_login_raises_value_error_when_the_password_is_wrong(self):
        # Arrange
        self.service.register("bobby", "Codes123")

        # Act and Assert
        with self.assertRaises(ValueError) as context:
            self.service.login("bobby", "Wrong123")

        self.assertEqual(str(context.exception), "Invalid password supplied")


if __name__ == "__main__":
    # Lets you run this one file with `python -m tests.exercise2.test_user_service`.
    unittest.main()
