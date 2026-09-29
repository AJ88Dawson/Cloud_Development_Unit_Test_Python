"""Exercise 1 - testing existing code.

Write the test plan first (copy tasks/TEST_PLAN_TEMPLATE.md), then fill in the
tests below. You need at least three test cases per Calculator method:
borderline values as well as one normal combination.

HOW TO USE THIS FILE
  * One test is already written for you, as a worked example.
  * Every other test is a TODO. They currently SKIP rather than fail, so
    running pytest shows you how far you have got.
  * To do a TODO: delete the @pytest.mark.skip line above it and replace
    the body with your arrange / act / assert.
"""

import pytest

from calculator import Calculator


@pytest.fixture
def calculator():
    """A fresh Calculator for each test. Calculator holds no state, but a
    fixture is still the habit to get into."""
    return Calculator()


# ---------------------------------------------------------------------------
# add()
# ---------------------------------------------------------------------------


def test_add_returns_the_sum_of_two_small_numbers(calculator):
    """WORKED EXAMPLE - this is test case 1 from the guide's test plan."""
    # Arrange
    num1 = 10
    num2 = 30

    # Act
    result = calculator.add(num1, num2)

    # Assert
    assert result == 40


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_add_returns_a_negative_total_when_both_numbers_are_negative(calculator):
    # Should assert that adding two negative numbers gives a negative total.
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_add_overflows_to_infinity_at_the_largest_float(calculator):
    # Should assert that adding sys.float_info.max to itself gives
    # math.inf. Python floats behave like Java doubles here.
    pass


# ---------------------------------------------------------------------------
# subtract()
# ---------------------------------------------------------------------------


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_subtract_returns_the_difference_of_two_small_numbers(calculator):
    # Should assert that subtracting a smaller number from a larger one
    # gives the expected positive difference.
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_subtract_returns_zero_when_both_numbers_are_the_same(calculator):
    # Should assert the borderline case where the result is exactly 0.
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_subtract_returns_a_negative_result_when_the_second_number_is_larger(calculator):
    # Should assert that 10 - 30 gives -20.
    pass


# ---------------------------------------------------------------------------
# multiply()
# ---------------------------------------------------------------------------


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_multiply_returns_the_product_of_two_small_numbers(calculator):
    # Should assert a normal case such as 6 * 7 giving 42.
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_multiply_returns_zero_when_either_number_is_zero(calculator):
    # Should assert the borderline case where one operand is 0.
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_multiply_returns_a_close_enough_answer_for_decimal_numbers(calculator):
    # Should assert 0.1 * 0.3 using pytest.approx, because binary floating
    # point cannot represent those values exactly.
    pass


# ---------------------------------------------------------------------------
# divide()
# ---------------------------------------------------------------------------


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_divide_returns_the_quotient_of_two_small_numbers(calculator):
    # Should assert a normal case such as 30 / 10 giving 3.
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_divide_returns_a_fraction_when_the_divisor_is_larger(calculator):
    # Should assert that 1 / 4 gives 0.25.
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_divide_raises_value_error_when_the_divisor_is_zero(calculator):
    # Should use pytest.raises(ValueError) and check the message is
    # "Division by zero: divisor must not be 0".
    pass
