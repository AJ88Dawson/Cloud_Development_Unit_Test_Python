"""EXERCISE 3 STRETCH: test-driven development.

Do this only once exercise 3 is complete.

WHAT THIS IS
    The only exercise where the code under test does not exist yet. There is
    no src/exercise3/concrete_user_repository.py in this repository, and
    there is not meant to be. YOU write it, and you write it TEST FIRST: the
    test comes before the class, which is the entire point of the exercise.

    So your first job is to create
    src/exercise3/concrete_user_repository.py, beside
    src/exercise3/user_repository.py, holding a class called
    ConcreteUserRepository. The "Concrete" in the name says it is a class,
    not an interface or an abstract class. Start it empty, add a method only when a test you have
    already watched fail demands it. Store the users in a plain list
    attribute set in __init__: the guide asks for a List<User>, and a list is
    the Python spelling of that. A dict keyed by username would be faster,
    but the exercise is about the tests, not the data structure.

    There is no `implements` keyword in Python, and UserRepository is a
    typing.Protocol rather than a Java interface, so your class inherits from
    nothing. It satisfies the protocol simply by having the three methods.
    The Java version would be
    `public class ConcreteUserRepository implements UserRepository`.

    There are NO MOCKS here. This is the real implementation, so these are
    ordinary state-based tests: do something to the repository, then look at
    what it now holds or returns.

RED, GREEN, REFACTOR, AND WHY EVERY TEST BELOW SKIPS
    Every test in this file carries @unittest.skip, including the worked
    example. That is not the same as the other three files. There the worked
    example passes; here it CANNOT, because the class it imports does not
    exist. That is correct and expected. Delete the skip on one test, run it,
    and watch it go red. Then write just enough of ConcreteUserRepository to
    turn it green. Then the next one. A test that has never been seen to fail
    has not been shown to test anything.

    Because the import sits inside setUp rather than at the top of the file,
    a skipped test never runs it, so a fresh clone stays green until you
    start work. Move that import to the top before the class exists and the
    whole suite will error on collection.

THE TWO PARTS, AND PART 1 IS NOT OPTIONAL
    Part 1: write the test plan FIRST, for the three methods of
        src/exercise3/user_repository.py. Copy tasks/TEST_PLAN_TEMPLATE.md.
            exists(trimmed_username)  True if that username is already stored
            register(user)            stores the user, returns the stored one
            login(user)               returns the stored user if it matches
        The protocol does NOT say what should happen when you register a
        username that already exists, or log in with credentials matching
        nothing. That is YOUR decision, and the exercise is that you make it
        in the plan rather than discovering it halfway through coding. Write
        the decision and its exact exception message into the plan, then make
        the tests below match what you decided.
    Part 2: work down the tests one at a time, red then green.

HOW TO RUN
    From the repository root, this file alone, which is what you will run
    over and over while doing this:
        python -m unittest tests.exercise3.test_concrete_user_repository
    One test by name:
        python -m unittest tests.exercise3.test_concrete_user_repository.ConcreteUserRepositoryTest.test_exists_returns_false_when_the_repository_is_empty
    The whole suite:
        python -m unittest discover
    Done looks like: no skips and no failures anywhere, and
    src/exercise3/concrete_user_repository.py contains nothing that was not
    demanded by
    a test you had already watched fail.

THE FULL BRIEF
    tasks/04_stretch_tdd_repository.md
"""

import unittest

from exercise3.user import User


class ConcreteUserRepositoryTest(unittest.TestCase):
    """The Java guide calls this class UserRepositoryTest. The unittest
    equivalent is a TestCase named after the concrete class it tests, with
    every test as a method named test_*.
    """

    def setUp(self):
        """THE FIXTURE. Runs before EVERY test method, like JUnit's
        @BeforeEach, and skipped tests never reach it.

        A fresh, empty repository per test. This fixture matters more here
        than anywhere else in the repository: the repository holds its users
        in a list on the instance, so without a new one per test a user
        registered in an earlier test would still be sitting there and your
        "empty repository" cases would pass or fail at random depending on
        the alphabetical order the tests happen to run in.

        The import is INSIDE this method on purpose. src/exercise3/ has no
        concrete_user_repository.py until you write it, and a top-level
        import of a missing module would break the whole suite for everybody
        before you had written a line. Once your class exists you may move
        this import up to the top of the file beside
        `from exercise3.user import User`, which is where it would normally
        live.
        """
        from exercise3.concrete_user_repository import ConcreteUserRepository

        self.repository = ConcreteUserRepository()
        self.bobby = User(id=1, username="bobby", password="Codes123")

    # -----------------------------------------------------------------
    # exists()
    # -----------------------------------------------------------------

    @unittest.skip("TODO - delete this line, watch it go RED, then write the class")
    def test_exists_returns_false_when_the_repository_is_empty(self):
        """WORKED EXAMPLE - row 1 of the guide's plan, and your first red test.

        Row 1 reads: exists(username), no user stored yet, input "bobby",
        expected output False. It is written out in full below so you can see
        the shape, but it still skips, and when you delete the skip it will
        FAIL rather than pass, because ConcreteUserRepository does not exist
        yet. That failure is the first step of the exercise, not a problem to
        work around. Read the error, create
        src/exercise3/concrete_user_repository.py
        with a class holding an empty users list and an exists() that returns
        False, run again, and watch it go green. Then move to the next test
        and repeat.
        """
        # Arrange: setUp already gave us an empty repository.

        # Act
        result = self.repository.exists("bobby")

        # Assert
        self.assertFalse(result)

    @unittest.skip("TODO - delete this line and write the test")
    def test_exists_returns_true_after_the_user_is_registered(self):
        # Arrange by registering self.bobby, act by calling exists("bobby"),
        # assert True with self.assertTrue. This is the test that forces
        # exists() to look in the list rather than just returning False, so
        # write it straight after the worked example.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_exists_returns_false_for_a_different_username(self):
        # Register self.bobby, then ask exists("alice"). Assert False. Without
        # this one, an exists() that returns True whenever the list is
        # non-empty would still pass every test you have.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_exists_is_case_sensitive(self):
        # Register self.bobby, then ask exists("BOBBY"). Assert False, if
        # case-sensitive matching is what your plan decided. This is a
        # borderline case and a decision, not a fact: if your plan says
        # usernames are case-insensitive, assert True here instead and make
        # the implementation match. Either is defensible. Silence is not.
        pass

    # -----------------------------------------------------------------
    # register()
    # -----------------------------------------------------------------

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_returns_the_user_it_was_given(self):
        # Act with self.repository.register(self.bobby), assert the returned
        # value equals self.bobby. User is a dataclass, so two Users with the
        # same three field values compare equal: no need for a hand-written
        # equals() as Java would require.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_stores_the_user_in_the_list(self):
        # Register self.bobby, then assert the repository's list attribute
        # equals [self.bobby]. Returning the user is not the same as storing
        # it, so this is a separate case from the one above: it is the test
        # that forces the append.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_stores_several_different_users(self):
        # Arrange a second user, for example
        # User(id=2, username="alice", password="Codes456"), register both,
        # and assert the list now has a length of 2. This stops an
        # implementation that overwrites a single slot rather than appending.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_register_raises_value_error_for_a_duplicate_username(self):
        # The decision the protocol leaves to you, and the one your plan has
        # to answer before you write it. If you decided duplicates are
        # refused: register self.bobby, then try to register a DIFFERENT User
        # object carrying the same username, and assert ValueError with
        # whatever message your plan chose. Also assert the list still has
        # exactly one entry, so a rejected registration leaves no trace.
        # If your plan instead decided the second registration silently wins
        # or is ignored, write that test instead. Just do not leave the
        # behaviour untested.
        pass

    # -----------------------------------------------------------------
    # login()
    # -----------------------------------------------------------------

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_returns_the_stored_user_when_the_credentials_match(self):
        # The happy path. Register self.bobby, then log in with a SEPARATE
        # User object carrying the same username and password, for example
        # User(id=0, username="bobby", password="Codes123"), and assert the
        # STORED user comes back. Using a different object with a different id
        # is deliberate: it proves login looked the user up rather than
        # handing your argument straight back.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_password_is_wrong(self):
        # Register self.bobby, then log in as "bobby" with a different
        # password such as "Wrong123". Assert ValueError, and assert the exact
        # message your plan chose. A matching username with a wrong password
        # must not be treated as a match.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_username_is_unknown(self):
        # Register self.bobby, then log in as "alice" with any password.
        # Assert the same failure as the wrong-password case, if your plan
        # decided to use one message for both. Telling an attacker which of
        # the two was wrong is a real design choice, so make it deliberately.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_login_raises_value_error_when_the_repository_is_empty(self):
        # The borderline case at the empty end: log in without registering
        # anything first and assert it fails rather than crashing on an empty
        # list. Cheap to write and the one most likely to catch a loop that
        # assumes at least one stored user.
        pass


if __name__ == "__main__":
    # Lets you run this one file with
    # `python -m tests.exercise3.test_concrete_user_repository`.
    unittest.main()
