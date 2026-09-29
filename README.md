# Unit testing exercises (Python)

## What this is

Four exercises in writing unit tests, for **SDL3 Module 5: Testing**. You
write the tests; the code under test is already here.

This repository is the Python version of **002 - SDL3M5 - Testing Exercise
Guide**. The guide is written for Java and JUnit, and this is a faithful
translation of it: the same exercises, the same parts, the same test plan
tables, the same classes doing the same things and raising equivalent
exceptions.

**The exercise brief lives in [`tasks/`](tasks/README.md). Start there.**
This repository is self-contained: you do not need the PDF exercise guide
and you do not need the original Java repository.

| | Exercise | Class under test | The file you edit |
| - | -------- | ---------------- | ----------------- |
| 1 | [Testing existing code](tasks/01_testing_existing_code.md) | `Calculator` | `tests/exercise1/test_calculator.py` |
| 2 | [Testing exceptions](tasks/02_testing_exceptions.md) | `UserService` | `tests/exercise2/test_user_service.py` |
| 3 | [Mocking](tasks/03_mocking.md) | `UserController` | `tests/exercise3/test_user_controller.py` |
| 4 | [TDD (stretch)](tasks/04_stretch_tdd_repository.md) | you write the class | `tests/exercise3/test_concrete_user_repository.py` |

## Prerequisites and setup

You need **Python 3.10 or newer**. Built and verified on **3.12.10**. Check
what you have:

```
python --version
```

Create and activate a virtual environment in the repository root (the folder
this README is in).

Windows (PowerShell):

```
python -m venv venv
venv\Scripts\Activate.ps1
```

macOS and Linux:

```
python3 -m venv venv
source venv/bin/activate
```

**There is nothing to `pip install`.** The test framework is `unittest`,
which is part of the Python standard library, and the mocking library is
`unittest.mock`, which is part of `unittest`. Both arrive with Python
itself. `requirements.txt` is present, and says exactly that. You do not
strictly need a virtual environment either, but making one is the right
habit and costs you two commands.

## How to run the tests

From the repository root:

```
python -m unittest discover
```

On a fresh clone that is green. It looks like this, and this is the real
output:

```
ss.ssssssssssssssssssssssssssssssssssss.ssssssssssssssss.s
----------------------------------------------------------------------
Ran 58 tests in 0.001s

OK (skipped=55)
```

Read that last line carefully, because **the skip count is your progress
bar**. There are 58 tests. Three of them are the worked examples for
exercises 1 to 3, already written, and they pass: that is what the three
dots are. The other 55 are the ones you are about to write, and until you
write them they *skip* rather than fail, which is why a fresh clone says
`OK`.

The stretch file is the odd one out. Every test in it skips, including its
worked example, because the class it tests does not exist until you write
it. Deleting a skip there makes the test go **red** first, and that is the
exercise.

Every test you complete moves one test from the skipped column into the
passed column. When you are finished, the line reads `OK` with no skips at
all.

Useful variations:

```
python -m unittest discover -v          one line per test, with skip reasons
python -m unittest tests.exercise1.test_calculator        a single file
python -m unittest tests.exercise1.test_calculator.CalculatorTest.test_add_returns_the_sum_of_two_small_numbers
```

The `-v` form is worth running at least once. It names every test and
prints the reason beside each skip:

```
test_add_returns_the_sum_of_two_small_numbers (tests.exercise1.test_calculator.CalculatorTest.test_add_returns_the_sum_of_two_small_numbers)
WORKED EXAMPLE - this is test case 1 from the guide's test plan. ... ok
test_divide_raises_value_error_when_the_divisor_is_zero (tests.exercise1.test_calculator.CalculatorTest.test_divide_raises_value_error_when_the_divisor_is_zero) ... skipped 'TODO - delete this line and write the test'
```

A test with a docstring gets its first line printed underneath the test
name, which is why the first one takes two lines. That is a good reason to
give your own tests a one-line docstring.

> `tests/__init__.py` is what makes `from exercise1.calculator import Calculator`
> work: it puts `src/` on the import path. You do not need to change it.

## How to do one TODO

Every test you have to write looks like this:

```python
@unittest.skip("TODO - delete this line and write the test")
def test_divide_raises_value_error_when_the_divisor_is_zero(self):
    # Should use `with self.assertRaises(ValueError) as context:` and
    # check the message is "Division by zero: divisor must not be 0".
    pass
```

Two steps:

1. **Delete the `@unittest.skip(...)` line.** That is the whole of the
   first step. The test now runs instead of skipping.
2. **Replace `pass`** with your arrange / act / assert. The comment above
   `pass` tells you what the test should assert. Delete it once you have
   written the test, or keep it, as you prefer.

So the example above becomes:

```python
def test_divide_raises_value_error_when_the_divisor_is_zero(self):
    # Arrange
    num1 = 30
    num2 = 0

    # Act and Assert
    with self.assertRaises(ValueError) as context:
        self.calculator.divide(num1, num2)

    self.assertEqual(str(context.exception), "Division by zero: divisor must not be 0")
```

Run the suite again. The skip count drops by one and the pass count rises
by one.

Write extra tests of your own whenever your test plan calls for one. Add
another method to the same class, name it after what it asserts the way
these are named, and it will be picked up automatically: `unittest` runs
every method whose name starts with `test_`.

## The code you are working with

All of it is in `src/`, grouped one folder per exercise. **Do not change
anything in `src/`.** Your job is to test it as it stands. The folder names
are lowercase `exercise1`, `exercise2` and `exercise3` here, in the Java
repository and in the C# one, so the three stay directly comparable.

### `src/exercise1/calculator.py` - exercise 1

```python
class Calculator:
    def add(self, num1: float, num2: float) -> float
    def subtract(self, num1: float, num2: float) -> float
    def multiply(self, num1: float, num2: float) -> float
    def divide(self, num1: float, num2: float) -> float
```

No state is kept between calls. `divide` raises
`ValueError("Division by zero: divisor must not be 0")` when `num2` is `0`.
The type hints say `float`, but nothing enforces them: `add(1, 2)` returns
the integer `3`.

### `src/exercise2/user_service.py` - exercise 2

```python
class UserService:
    def __init__(self)
    def register(self, username, password) -> str
    def login(self, username, password) -> str
```

Registered users are held in memory in a `dict` keyed by username.
`register` validates the username and password, stores them, and returns the
**trimmed** username. `login` returns the trimmed username when the
credentials match. Both raise `ValueError` for broken rules;
`login` raises `RuntimeError("Invalid username supplied")` for a user that
was never registered. The exact messages are listed in
[`tasks/02_testing_exceptions.md`](tasks/02_testing_exceptions.md), and
asserting the exact message is the point of the exercise.

### `src/exercise3/user.py` - exercise 3

```python
@dataclass
class User:
    id: int = 0
    username: str = ""
    password: str = ""
```

A data object. `@dataclass` generates the constructor, `__eq__` and
`__repr__`, so `User(id=1, username="bobby", password="Codes123")` works and
two Users with the same three values compare equal. Construct one with
keyword arguments, as in that example.

### `src/exercise3/user_repository.py` - exercise 3

```python
class UserRepository(Protocol):
    def exists(self, trimmed_username: str) -> bool
    def register(self, user: User) -> User
    def login(self, user: User) -> User
```

The Java interface, as a `typing.Protocol`. Nothing implements it in this
repository: in exercise 3 you replace it with a mock, and in the stretch
task you write a real class that satisfies it.

### `src/exercise3/user_controller.py` - exercise 3

```python
class UserController:
    def __init__(self, user_repository)
    def register(self, user: User) -> User
    def login(self, user: User) -> User
```

The class under test in exercise 3. It takes its repository as a
constructor argument, which is exactly what lets you hand it a mock. Its
`register` runs the same validation rules as `UserService.register`, but
asks `repository.exists(trimmed_username)` about uniqueness and then calls
`repository.register(user)`. Its `login` checks only that the user,
username and password are present, then hands the whole `User` to
`repository.login(user)`.

## The framework: unittest

`unittest` is Python's standard-library test framework. It is a direct
descendant of JUnit, which is why it looks so familiar. Nothing here needs
installing.

These are the exact names you will type:

| You write | What it is for |
| --------- | -------------- |
| `import unittest` | the only import the framework needs |
| `class CalculatorTest(unittest.TestCase)` | the test class. Every method on it whose name starts with `test_` is a test, and each test gets its own fresh instance of the class, so nothing leaks between tests. |
| `def setUp(self)` | runs before **every** test method. Build the object under test here and hang it on `self`. |
| `def tearDown(self)` | runs after every test method, even when the test fails. For closing anything you opened. None of these exercises need it. |
| `self.assertEqual(a, b)` | fails unless `a == b`. Your main assertion. |
| `self.assertTrue(x)` / `self.assertFalse(x)` | fails unless the value is truthy / falsy. |
| `with self.assertRaises(ValueError) as context:` | the block must raise that exception, or the test fails. Afterwards `context.exception` is the exception object, so `str(context.exception)` gives you the message to assert on. |
| `self.assertAlmostEqual(a, b)` | equality for decimals. `0.1 + 0.2` is not exactly `0.3` in binary floating point, so `assertEqual` on that would fail. |
| `@unittest.skip("reason")` | skips the test and prints the reason. This is what marks each TODO. |
| `from unittest.mock import MagicMock` | a stand-in object that answers to any attribute or method. Exercise 3's fake repository. |
| `mock.method.return_value = x` | make a mocked method return `x`. |
| `mock.method.side_effect = ValueError("...")` | make a mocked method raise instead of return. |
| `mock.method.assert_called_once_with(a)` | fails unless that method was called exactly once, with exactly that argument. |
| `mock.method.assert_not_called()` | fails if it was called at all. Use it to prove that failed validation never reached the repository. |
| `from unittest.mock import patch` | replaces something **where it is used**, as a decorator or a `with` block. You do not need it here, because `UserController` takes its repository as a constructor argument. Reach for it when a dependency is imported or constructed inside the code under test and cannot be injected. |

## Java to Python: the differences

You have just done these exercises in Java with JUnit. You are doing them
again in Python with unittest, and the code under test behaves the same
way, so **you do not need any of this table to finish the work.** Carrying
what you already know across is the whole point, and `unittest` was chosen
over the alternatives precisely because it mirrors JUnit so closely.

The table is here for a different reason. Seeing one exercise in two
languages shows you which parts of what you know are about **testing** and
which parts were only ever about **Java**. A test class, a fixture method,
an assertion, an expected exception and a mocked collaborator are ideas.
`@BeforeEach` and `assertThrows` are spellings. That distinction is the
thing you gain here, and it is what makes the third language cheap.

| Java / JUnit / Mockito | Python / unittest | Notes |
| ---------------------- | ----------------- | ----- |
| `class CalculatorTest` with `@Test` methods | `class CalculatorTest(unittest.TestCase)` with `test_` methods | Same idea, different marker. JUnit finds tests by the annotation; unittest finds them by the method name prefix, so there is nothing to import and nothing to forget. |
| `assertEquals(expected, actual)` | `self.assertEqual(first, second)` | **Watch the argument order.** JUnit is strict: expected first. unittest has no expected and no actual, and the failure message reads `first != second` whichever way round you put them. Pick an order and be consistent. |
| `assertThrows(IllegalArgumentException.class, () -> c.divide(1, 0))` | `with self.assertRaises(ValueError): c.divide(1, 0)` | A **context manager**, not a lambda. Add `as context` and `str(context.exception)` is the message, the equivalent of calling `getMessage()` on what `assertThrows` returned. |
| `assertTrue` / `assertFalse` | `self.assertTrue` / `self.assertFalse` | The same, with `self.` in front. |
| `@BeforeEach void setUp()` | `def setUp(self)` | Same job, same timing: before every test. JUnit also gives you `@AfterEach`; that is `tearDown`. |
| `@Disabled("reason")` | `@unittest.skip("reason")` | Same job. Every TODO in this repository carries one, which is why a fresh clone is green. |
| `IllegalArgumentException` | `ValueError` | The standard Python exception for an argument of the right type with an unacceptable value. That is what `IllegalArgumentException` means. |
| `RuntimeException` | `RuntimeError` | The closest built-in equivalent. |
| Checked exceptions and `throws` clauses | nothing | Python has no checked exceptions. What a method can raise is documented in its docstring and enforced only by your tests, which raises the stakes on your test plan. |
| Mockito | `unittest.mock` | Standard library. No dependency to add, no annotation processor, no runner extension. |
| `@Mock UserRepository repository` | `repository = MagicMock()` | A `MagicMock` answers to any attribute you ask for, so it needs to know nothing about `UserRepository`. |
| `@InjectMocks UserController controller` | `controller = UserController(repository)` | Constructor injection, written out by hand. No annotation, and nothing magic. |
| `when(repo.exists("bob")).thenReturn(true)` | `repository.exists.return_value = True` | Stubbing is an assignment, not a call chain. |
| `when(repo.login(u)).thenThrow(new RuntimeException())` | `repository.login.side_effect = RuntimeError(...)` | `side_effect` is how a mock raises instead of returning. |
| `verify(repo).register(user)` | `repository.register.assert_called_once_with(user)` | Verification happens **after** the act, in both. `assert_called_with` checks the most recent call; `assert_called_once_with` also checks that there was exactly one. |
| `verify(repo, never()).register(user)` | `repository.register.assert_not_called()` | Proving nothing happened is as much a test as proving something did. |
| `interface UserRepository` | `class UserRepository(Protocol)` | A `Protocol` is **structural**: anything with matching methods satisfies it, with no `implements` and no subclassing. That is exactly why a `MagicMock` can be passed straight in. |
| JavaBean: private fields, getters, setters, `equals`, `hashCode`, `toString` | `@dataclass` | The dataclass generates the constructor, `__eq__` and `__repr__`. Attributes are public, so getters and setters add nothing. |
| `HashMap`, unspecified iteration order | `dict`, insertion ordered | Nothing here depends on ordering, but do not write a test that does, or the two language versions will disagree. |
| `String.matches()` | `re.fullmatch()` | Both match the **whole** string. `re.match()` only anchors at the start, which is a different question. |
| `int` and `double` are different types; `1/2` is `0` | one number type in practice; `1/2` is `0.5` | Python has no integer division on `/`, so the classic Java surprise where `1/2` is `0` does not happen. `//` is the one that truncates. `add(1, 2)` returns the int `3`, not `3.0`, and `Calculator` takes whatever you hand it. |
| `Double.MAX_VALUE`, `Double.MIN_VALUE` | `sys.float_info.max`, `sys.float_info.min` | The borderline values exercise 1 asks for. Overflow gives `math.inf`, as it does in Java. |
| `assertEquals(0.3, actual, 0.0001)` | `self.assertAlmostEqual(actual, 0.3)` | Both exist because binary floating point cannot represent `0.1` exactly, in either language. |
| Static types on parameters, checked by the compiler | type hints, checked by nothing | A hint is documentation. Nothing stops a caller passing the wrong type, so a Java compile error becomes a Python test case. |

## Layout

```
python/
  README.md                 this file
  CODE_CORRECTIONS.md       two defects in the original Java code, and what changed
  requirements.txt          nothing to install, and it says so
  tasks/                    the exercise briefs. Start here.
    README.md               contents page and running order
    01_testing_existing_code.md
    02_testing_exceptions.md
    03_mocking.md
    04_stretch_tdd_repository.md
    TEST_PLAN_TEMPLATE.md   the test plan tables to fill in
  src/                      the code under test. Do not change it.
    exercise1/
      __init__.py
      calculator.py         exercise 1
    exercise2/
      __init__.py
      user_service.py       exercise 2
    exercise3/
      __init__.py
      user.py               exercise 3, a dataclass
      user_repository.py    exercise 3, a typing.Protocol
      user_controller.py    exercise 3, the class you will mock around
  tests/                    your work goes here
    __init__.py             puts src/ on the import path. Leave it alone.
    exercise1/
      __init__.py           needed, or discovery skips the folder
      test_calculator.py
    exercise2/
      __init__.py
      test_user_service.py
    exercise3/
      __init__.py
      test_user_controller.py
      test_concrete_user_repository.py   exercise 3 stretch, written test first
```

Model answers are not in this repository. Your trainer has them. Finish a
test, then ask.
