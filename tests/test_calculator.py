"""Exercise 1 - testing existing code.

Write the test plan first (copy tasks/TEST_PLAN_TEMPLATE.md), then fill in the
tests below. You need at least three test cases per Calculator method:
borderline values as well as one normal combination.

HOW TO USE THIS FILE
  * One test is already written for you, as a worked example.
  * Every other test is a TODO. They currently SKIP rather than fail, so
    running the suite shows you how far you have got.
  * To do a TODO: delete the @unittest.skip line above it and replace the
    body with your arrange / act / assert.

THE FRAMEWORK
  unittest, from the Python standard library. It is the closest thing Python
  has to JUnit: a TestCase class holding test methods, setUp instead of
  @BeforeEach, and assertEqual / assertTrue / assertRaises instead of the
  JUnit assertions.
"""

import unittest

from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    """The JUnit CalculatorTest class, in Python.

    Every method whose name starts with `test_` is a test. They run in
    alphabetical order and each one gets its own fresh instance of this
    class, so nothing you set in one test can leak into another.
    """

    def setUp(self):
        """Runs before every test method, like JUnit's @BeforeEach.

        Calculator holds no state, so a fresh one is not strictly needed,
        but building the object under test here is the habit to get into.
        """
        self.calculator = Calculator()

    # -----------------------------------------------------------------
    # add()
    # -----------------------------------------------------------------

    def test_add_returns_the_sum_of_two_small_numbers(self):
        """WORKED EXAMPLE - this is test case 1 from the guide's test plan."""
        # Arrange
        num1 = 10
        num2 = 30

        # Act
        result = self.calculator.add(num1, num2)

        # Assert. JUnit's assertEquals(expected, actual) is strict about the
        # order. unittest's assertEqual(first, second) is not: it has no
        # expected or actual, and the failure message reads "first != second"
        # whichever way round you put them. Pick one order and stay with it.
        self.assertEqual(result, 40)

    @unittest.skip("TODO - delete this line and write the test")
    def test_add_returns_a_negative_total_when_both_numbers_are_negative(self):
        # Should assert that adding two negative numbers gives a negative total.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_add_overflows_to_infinity_at_the_largest_float(self):
        # Should assert that adding sys.float_info.max to itself gives
        # math.inf. Python floats behave like Java doubles here.
        pass

    # -----------------------------------------------------------------
    # subtract()
    # -----------------------------------------------------------------

    @unittest.skip("TODO - delete this line and write the test")
    def test_subtract_returns_the_difference_of_two_small_numbers(self):
        # Should assert that subtracting a smaller number from a larger one
        # gives the expected positive difference.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_subtract_returns_zero_when_both_numbers_are_the_same(self):
        # Should assert the borderline case where the result is exactly 0.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_subtract_returns_a_negative_result_when_the_second_number_is_larger(self):
        # Should assert that 10 - 30 gives -20.
        pass

    # -----------------------------------------------------------------
    # multiply()
    # -----------------------------------------------------------------

    @unittest.skip("TODO - delete this line and write the test")
    def test_multiply_returns_the_product_of_two_small_numbers(self):
        # Should assert a normal case such as 6 * 7 giving 42.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_multiply_returns_zero_when_either_number_is_zero(self):
        # Should assert the borderline case where one operand is 0.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_multiply_returns_a_close_enough_answer_for_decimal_numbers(self):
        # Should assert 0.1 * 0.3 using self.assertAlmostEqual, because
        # binary floating point cannot represent those values exactly.
        pass

    # -----------------------------------------------------------------
    # divide()
    # -----------------------------------------------------------------

    @unittest.skip("TODO - delete this line and write the test")
    def test_divide_returns_the_quotient_of_two_small_numbers(self):
        # Should assert a normal case such as 30 / 10 giving 3.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_divide_returns_a_fraction_when_the_divisor_is_larger(self):
        # Should assert that 1 / 4 gives 0.25.
        pass

    @unittest.skip("TODO - delete this line and write the test")
    def test_divide_raises_value_error_when_the_divisor_is_zero(self):
        # Should use `with self.assertRaises(ValueError) as context:` and
        # check the message is "Division by zero: divisor must not be 0".
        pass


if __name__ == "__main__":
    # Lets you run this one file with `python -m tests.test_calculator`.
    unittest.main()
