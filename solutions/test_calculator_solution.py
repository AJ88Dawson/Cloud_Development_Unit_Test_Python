"""Exercise 1 - model answers.

Run with:  pytest solutions
"""

import math
import sys

import pytest

from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


# ---------------------------------------------------------------------------
# add()
# ---------------------------------------------------------------------------


def test_add_returns_the_sum_of_two_small_numbers(calculator):
    # Arrange
    num1 = 10
    num2 = 30

    # Act
    result = calculator.add(num1, num2)

    # Assert
    assert result == 40


def test_add_returns_a_negative_total_when_both_numbers_are_negative(calculator):
    # Arrange
    num1 = -10
    num2 = -30

    # Act
    result = calculator.add(num1, num2)

    # Assert
    assert result == -40


def test_add_returns_a_close_enough_total_for_decimal_numbers(calculator):
    # Arrange - 0.1 + 0.2 is famously not exactly 0.3 in binary floating
    # point, so compare with pytest.approx rather than ==.
    num1 = 0.1
    num2 = 0.2

    # Act
    result = calculator.add(num1, num2)

    # Assert
    assert result == pytest.approx(0.3)


def test_add_overflows_to_infinity_at_the_largest_float(calculator):
    # Arrange - the borderline case. sys.float_info.max is the largest
    # finite float, the same value as Java's Double.MAX_VALUE.
    num1 = sys.float_info.max
    num2 = sys.float_info.max

    # Act
    result = calculator.add(num1, num2)

    # Assert
    assert result == math.inf


def test_add_keeps_the_smallest_positive_float_when_zero_is_added(calculator):
    # Arrange - the other borderline.
    num1 = sys.float_info.min
    num2 = 0.0

    # Act
    result = calculator.add(num1, num2)

    # Assert
    assert result == sys.float_info.min


# ---------------------------------------------------------------------------
# subtract()
# ---------------------------------------------------------------------------


def test_subtract_returns_the_difference_of_two_small_numbers(calculator):
    # Arrange
    num1 = 30
    num2 = 10

    # Act
    result = calculator.subtract(num1, num2)

    # Assert
    assert result == 20


def test_subtract_returns_zero_when_both_numbers_are_the_same(calculator):
    # Arrange
    num1 = 42.5
    num2 = 42.5

    # Act
    result = calculator.subtract(num1, num2)

    # Assert
    assert result == 0


def test_subtract_returns_a_negative_result_when_the_second_number_is_larger(calculator):
    # Arrange
    num1 = 10
    num2 = 30

    # Act
    result = calculator.subtract(num1, num2)

    # Assert
    assert result == -20


def test_subtract_overflows_to_negative_infinity_at_the_float_limits(calculator):
    # Arrange
    num1 = -sys.float_info.max
    num2 = sys.float_info.max

    # Act
    result = calculator.subtract(num1, num2)

    # Assert
    assert result == -math.inf


# ---------------------------------------------------------------------------
# multiply()
# ---------------------------------------------------------------------------


def test_multiply_returns_the_product_of_two_small_numbers(calculator):
    # Arrange
    num1 = 6
    num2 = 7

    # Act
    result = calculator.multiply(num1, num2)

    # Assert
    assert result == 42


def test_multiply_returns_zero_when_either_number_is_zero(calculator):
    # Arrange
    num1 = 12345.678
    num2 = 0

    # Act
    result = calculator.multiply(num1, num2)

    # Assert
    assert result == 0


def test_multiply_returns_a_close_enough_answer_for_decimal_numbers(calculator):
    # Arrange
    num1 = 0.1
    num2 = 0.3

    # Act
    result = calculator.multiply(num1, num2)

    # Assert
    assert result == pytest.approx(0.03)


def test_multiply_overflows_to_infinity_at_the_largest_float(calculator):
    # Arrange
    num1 = sys.float_info.max
    num2 = 2

    # Act
    result = calculator.multiply(num1, num2)

    # Assert
    assert result == math.inf


def test_multiply_underflows_to_zero_at_the_smallest_float(calculator):
    # Arrange - two tiny numbers multiply to something too small to hold.
    num1 = sys.float_info.min
    num2 = sys.float_info.min

    # Act
    result = calculator.multiply(num1, num2)

    # Assert
    assert result == 0


# ---------------------------------------------------------------------------
# divide()
# ---------------------------------------------------------------------------


def test_divide_returns_the_quotient_of_two_small_numbers(calculator):
    # Arrange
    num1 = 30
    num2 = 10

    # Act
    result = calculator.divide(num1, num2)

    # Assert
    assert result == 3


def test_divide_returns_a_fraction_when_the_divisor_is_larger(calculator):
    # Arrange
    num1 = 1
    num2 = 4

    # Act
    result = calculator.divide(num1, num2)

    # Assert
    assert result == 0.25


def test_divide_returns_a_negative_quotient_for_mixed_signs(calculator):
    # Arrange
    num1 = -30
    num2 = 10

    # Act
    result = calculator.divide(num1, num2)

    # Assert
    assert result == -3


def test_divide_raises_value_error_when_the_divisor_is_zero(calculator):
    # Arrange
    num1 = 30
    num2 = 0

    # Act and Assert
    with pytest.raises(ValueError) as exception_info:
        calculator.divide(num1, num2)

    assert str(exception_info.value) == "Division by zero: divisor must not be 0"


def test_divide_raises_value_error_for_negative_zero(calculator):
    # Arrange - a borderline case that is easy to miss. In both Java and
    # Python -0.0 == 0, so the guard catches it.
    num1 = 30
    num2 = -0.0

    # Act and Assert
    with pytest.raises(ValueError):
        calculator.divide(num1, num2)
