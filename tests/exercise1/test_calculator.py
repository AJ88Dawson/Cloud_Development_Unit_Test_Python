"""EXERCISE 1: testing existing code.

WHAT THIS IS
    The first exercise. `Calculator` in src/exercise1/calculator.py already works. You
    are not writing it and you are not changing it. You are writing the tests
    that prove it does what it claims, which is the skill this module is
    about.

WHAT YOU DO HERE
    Cover all four methods, add(), subtract(), multiply() and divide(), with
    at least three test cases each: at least one normal input combination,
    and the borderline values at the edges of what a Python float can hold.
    What are the largest numbers you can add? What about the smallest?

THE TWO PARTS, AND PART 1 IS NOT OPTIONAL
    Part 1: write the test plan FIRST. Copy tasks/TEST_PLAN_TEMPLATE.md,
        rename your copy (test-plan.md will do), and fill in a row per case:
        ID, method, description, inputs, expected output, actual output. The
        plan is the exercise. Deciding what "correct" means before you can
        see what the code returns is the whole point.
    Part 2: turn each row of that plan into a test down here, then fill in
        the Actual output column from what you saw. Where actual differs from
        expected you have either found a defect or mis-stated your
        expectation, and both are worth writing down.

HOW THE TODOs WORK
    Every test still to be written carries @unittest.skip, so the suite is
    green on a fresh clone and the skip count is your progress bar. To do one:
    delete the @unittest.skip line above it, then replace `pass` with your
    arrange / act / assert. JUnit spells that marker @Disabled("reason").

HOW TO RUN
    From the repository root, the whole suite:
        python -m unittest discover
    Just this file:
        python -m unittest tests.exercise1.test_calculator
    One test by name:
        python -m unittest tests.exercise1.test_calculator.CalculatorTest.test_add_returns_the_sum_of_two_small_numbers
    Add -v to any of those to see one line per test with the skip reasons.

THE FULL BRIEF
    tasks/01_testing_existing_code.md

THE FRAMEWORK
    unittest, from the Python standard library. It is the closest thing
    Python has to JUnit: a TestCase class holding test methods, setUp instead
    of @BeforeEach, and assertEqual / assertTrue / assertRaises instead of the
    JUnit assertions. There is nothing to install.
"""

import unittest

from exercise1.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    """The JUnit CalculatorTest class, in Python.

    Every method whose name starts with `test_` is a test. JUnit finds tests
    by the @Test annotation; unittest finds them by that name prefix, so
    there is nothing to import and nothing to forget. Tests run in
    alphabetical order and each one gets its own fresh instance of this
    class, so nothing you set in one test can leak into another.

    Name your own tests the way these are named:
    test_method_scenario_expectedresult.
    """

    def setUp(self):
        """THE FIXTURE. Runs before EVERY test method in this class.

        This is exactly JUnit's @BeforeEach, same job and same timing, and
        unittest's tearDown is JUnit's @AfterEach (nothing here needs one).
        Build the object under test here and hang it on `self`, so every test
        starts from an identical, clean object and no test can be affected by
        one that ran before it.

        Calculator holds no state between calls, so a fresh one is not
        strictly needed here, but building the object under test in the
        fixture is the habit to get into: exercise 2's UserService does hold
        state, and there it is what stops the tests interfering.
        """
        self.calculator = Calculator()

    # -----------------------------------------------------------------
    # add()
    # -----------------------------------------------------------------

    def test_add_returns_the_sum_of_two_small_numbers(self):
        """WORKED EXAMPLE - this is test case 1 from the guide's test plan.

        Row 1 reads: add(num1, num2), adding two small numbers, num1=10 and
        num2=30, expected output 40. Copy this shape for the rest. Notice the
        three labelled steps and the name, method_scenario_expectedresult.
        """
        # Arrange: set up the inputs and the answer we expect.
        num1 = 10
        num2 = 30

        # Act: call the one method under test, once.
        result = self.calculator.add(num1, num2)

        # Assert. JUnit's assertEquals(expected, actual) is strict about the
        # order. unittest's assertEqual(first, second) is not: it has no
        # expected or actual, and the failure message reads "first != second"
        # whichever way round you put them. Pick one order and stay with it.
        self.assertEqual(result, 40)

    @unittest.skip("TODO - delete this line and write the test")
    def test_add_returns_a_negative_total_when_both_numbers_are_negative(self):
        # The normal-input case for negatives. Arrange two negative numbers,
        # say num1=-10 and num2=-30, act, and assert the result is -40, the
        # negative total. Nothing should be raised.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_add_overflows_to_infinity_at_the_largest_float(self):
        # The borderline case at the top end: what are the highest values you
        # can add? Arrange sys.float_info.max (Java's Double.MAX_VALUE) as
        # both operands, act, and assert the result is math.inf. Python floats
        # overflow to infinity rather than raising, exactly as Java doubles
        # do. You will need `import math` and `import sys` at the top.
        pass

    # -----------------------------------------------------------------
    # subtract()
    # -----------------------------------------------------------------

    @unittest.skip("TODO - delete this line and write the test")
    def test_subtract_returns_the_difference_of_two_small_numbers(self):
        # The normal-input case for subtract(). Take a larger number minus a
        # smaller one, say 30 - 10, and assert the positive difference 20.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_subtract_returns_zero_when_both_numbers_are_the_same(self):
        # A borderline case: the result sits exactly on zero. Subtract a
        # number from itself, say 30 - 30, and assert the result is 0. This
        # one is worth having because zero is the value most likely to be
        # mishandled elsewhere in a system.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_subtract_returns_a_negative_result_when_the_second_number_is_larger(self):
        # The crossing-below-zero case. Assert that 10 - 30 gives -20, so a
        # result that goes negative is returned rather than clamped at zero.
        pass

    # -----------------------------------------------------------------
    # multiply()
    # -----------------------------------------------------------------

    @unittest.skip("TODO - delete this line and write the test")
    def test_multiply_returns_the_product_of_two_small_numbers(self):
        # The normal-input case for multiply(): 6 * 7, expected 42.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_multiply_returns_zero_when_either_number_is_zero(self):
        # The borderline case where one operand is 0. Assert that multiplying
        # by zero gives 0, and prove it both ways round: zero as the first
        # operand and zero as the second.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_multiply_returns_a_close_enough_answer_for_decimal_numbers(self):
        # The precision case. Assert 0.1 * 0.3 using self.assertAlmostEqual,
        # NOT assertEqual, because binary floating point cannot represent
        # those values exactly and the exact comparison fails. In JUnit this
        # is the three-argument assertEquals(0.03, actual, 0.0001) with a
        # delta; assertAlmostEqual is the same idea with the tolerance
        # already chosen for you.
        pass

    # -----------------------------------------------------------------
    # divide()
    # -----------------------------------------------------------------

    @unittest.skip("TODO - delete this line and write the test")
    def test_divide_returns_the_quotient_of_two_small_numbers(self):
        # The normal-input case for divide(): 30 / 10, expected 3. Note that
        # Python's `/` never truncates, so the Java surprise where 1/2 is 0
        # does not happen here.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_divide_returns_a_fraction_when_the_divisor_is_larger(self):
        # Assert that 1 / 4 gives 0.25, so dividing by something bigger
        # returns a real fraction rather than rounding to zero.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_divide_raises_value_error_when_the_divisor_is_zero(self):
        # The exception case, and the one borderline value divide() actually
        # rejects. Assert that divide(30, 0) raises ValueError AND that the
        # message is exactly "Division by zero: divisor must not be 0".
        # Use the context manager form:
        #     with self.assertRaises(ValueError) as context:
        #         self.calculator.divide(30, 0)
        #     self.assertEqual(str(context.exception), "Division by zero: ...")
        # That is unittest's spelling of JUnit's
        # assertThrows(IllegalArgumentException.class, () -> c.divide(30, 0));
        # a context manager rather than a lambda, and str(context.exception)
        # where Java calls getMessage() on what assertThrows returned.
        pass


if __name__ == "__main__":
    # Lets you run this one file with `python -m tests.exercise1.test_calculator`.
    unittest.main()
