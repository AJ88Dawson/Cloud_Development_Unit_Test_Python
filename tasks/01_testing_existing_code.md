# Exercise 1 - Testing existing code

This exercise uses the `Calculator` class. In the Java guide it lives in the
`exercise1` package; here it is **`src/exercise1/calculator.py`**, in a folder
of the same name. There is nothing to clone and no project to import into
Eclipse: activate the virtual
environment described in [`README.md`](README.md) and you are ready.

Source: `src/exercise1/calculator.py`
Your tests: `tests/exercise1/test_calculator.py`

## Part 1 - Create a test plan

In this exercise, you are required to create a test plan which consists of
test cases for the `Calculator` class's four methods. Use the following
template for creating your test cases:

| ID | Method | Description | Inputs | Expected output | Actual output |
| -- | ------ | ----------- | ------ | --------------- | ------------- |
| 1 | `add(num1, num2)` | Adding two small numbers | num1=10, num2=30 | 40 | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

One test case has been created for you as an example. It is expected that
you produce at least three test cases per method:

* Test borderline input values, i.e., what are the highest values you can
  add? What about the smallest?
* Test at least one normal input combination.

The table is also in [`TEST_PLAN_TEMPLATE.md`](TEST_PLAN_TEMPLATE.md). Copy
that file and fill your copy in.

## Part 2 - Implement your test plan

The `Calculator` class has already been created. Use your test plan to guide
the development of tests for the methods of this class.

Open **`tests/exercise1/test_calculator.py`**. One test is written for you as a worked
example. Every other test is a stub that skips until you write it:

```python
@unittest.skip("TODO - delete this line and write the test")
def test_divide_raises_value_error_when_the_divisor_is_zero(self):
    pass
```

Delete the `@unittest.skip` line and replace `pass` with your arrange /
act / assert. Name any extra tests of your own after what they assert, the
same way these are named, and add them as further methods on the same
`CalculatorTest` class.

Run your tests from the repository root:

```
python -m unittest discover
```

or just this file:

```
python -m unittest tests.exercise1.test_calculator
```

## Python notes

* `Calculator.divide` raises `ValueError` where the Java version raised
  `IllegalArgumentException`. Assert it with `self.assertRaises(ValueError)`
  used as a context manager, which is the unittest equivalent of JUnit's
  `assertThrows`.
* For decimal arithmetic use `self.assertAlmostEqual`, because `0.1 + 0.2`
  is not exactly `0.3` in binary floating point.
* `sys.float_info.max` and `sys.float_info.min` are the equivalents of
  `Double.MAX_VALUE` and `Double.MIN_VALUE`.
* There is one `float` type rather than `double`, so `add(1, 2)` returns the
  int `3`, not `3.0`.

## Done looks like

Every stub in `tests/exercise1/test_calculator.py` has gone from skipped to passing,
and the summary line no longer reports any skips from that file:

```
python -m unittest tests.exercise1.test_calculator
```

Your plan's **Actual output** column is filled in. Where it differs from
**Expected output**, you have either found a defect or mis-stated your
expectation. Both are worth writing down.
