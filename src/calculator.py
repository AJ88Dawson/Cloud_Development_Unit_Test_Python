"""Exercise 1 - a small calculator, used for "testing existing code".

Python port of the Java Calculator class. The Java version used `double`
for every parameter and return value. Python has one built-in float type
and no static typing, so the type hints below are documentation only:
nothing stops a caller passing an int, and `add(1, 2)` returns the int 3
rather than 3.0. That is a genuine difference from Java and your tests
should be written with it in mind (use assertAlmostEqual for float
maths).
"""


class Calculator:
    """Four arithmetic operations. No state is kept between calls."""

    def add(self, num1: float, num2: float) -> float:
        return num1 + num2

    def subtract(self, num1: float, num2: float) -> float:
        return num1 - num2

    def multiply(self, num1: float, num2: float) -> float:
        return num1 * num2

    def divide(self, num1: float, num2: float) -> float:
        # The Java original throws IllegalArgumentException here.
        # Python has no IllegalArgumentException. ValueError is the
        # standard exception for "right type of argument, wrong value",
        # so that is the faithful translation.
        if num2 == 0:
            raise ValueError("Division by zero: divisor must not be 0")
        return num1 / num2
