# Unit testing exercises (Python)

SDL3 Module 5: Testing. Three exercises in writing unit tests with pytest,
plus a test-driven development stretch task.

This is a Python translation of the Java exercise repository. The classes do
the same things and raise equivalent exceptions, so the exercise guide still
applies. Where Python genuinely cannot mirror Java, the source says so in a
comment. See **Differences from the Java version** below.

**Start with [`tasks/README.md`](tasks/README.md)**, which holds the full
exercise brief. This repository is self-contained: you do not need the PDF
exercise guide or the original Java repository.

## Setting up

You need Python 3.10 or newer. Built and verified on 3.12.10.

Windows (PowerShell):

```
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS and Linux:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the tests

From the project root (the folder containing `pytest.ini`):

```
pytest
```

On a fresh clone this passes. The tests you have not written yet are marked
as skipped rather than failed, so the summary line shows how far you have
got:

```
3 passed, 43 skipped
```

Useful variations:

```
pytest -v                         # one line per test
pytest tests/test_calculator.py   # a single file
pytest -k divide                  # tests whose name contains "divide"
pytest solutions                  # the model answers, all passing
```

## Layout

```
python/
  README.md                 this file
  CODE_CORRECTIONS.md       what was wrong in the original and what changed
  tasks/                    the exercise briefs, start here
    README.md               contents page and running order
    01_testing_existing_code.md
    02_testing_exceptions.md
    03_mocking.md
    04_stretch_tdd_repository.md
    TEST_PLAN_TEMPLATE.md   the test plan tables to fill in
  requirements.txt          pytest, and nothing else
  pytest.ini                puts src/ on the import path
  src/                      the code under test. Do not change it.
    calculator.py           exercise 1
    user_service.py         exercise 2
    user.py                 exercise 3, a dataclass
    user_repository.py      exercise 3, a typing.Protocol
    user_controller.py      exercise 3, the class you will mock around
  tests/                    your work goes here
    test_calculator.py
    test_user_service.py
    test_user_controller.py
  solutions/                model answers, run with "pytest solutions"
```

## How the skeletons work

Each test file contains:

* one fully worked example, so you can see the shape of a pytest test;
* a TODO stub for every remaining test, each with a one-line comment saying
  what it should assert.

Every stub carries a marker:

```python
@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_divide_raises_value_error_when_the_divisor_is_zero(calculator):
    pass
```

To do one: delete the `@pytest.mark.skip` line and replace `pass` with your
arrange / act / assert. Name your own extra tests after what they assert,
the same way these are named.

## The exercises

The full brief for each exercise, with the guide's own test plan tables, is
in [`tasks/`](tasks/README.md). What follows is the Python-specific summary.

### Exercise 1 - testing existing code (`src/calculator.py`)

**Part 1.** Write a test plan for all four `Calculator` methods. At least
three cases per method. Cover borderline values (what is the largest number
you can add? the smallest?) as well as one normal combination.

**Part 2.** Implement the plan in `tests/test_calculator.py`.

Python notes: `Calculator.divide` raises `ValueError` where the Java version
raised `IllegalArgumentException`. Use `pytest.raises(ValueError)` to assert
it. For decimal arithmetic use `pytest.approx`, because `0.1 + 0.2` is not
exactly `0.3` in binary floating point. `sys.float_info.max` and
`sys.float_info.min` are the equivalents of `Double.MAX_VALUE` and
`Double.MIN_VALUE`.

### Exercise 2 - testing exceptions (`src/user_service.py`)

**Part 1.** Write a test plan for `register()` and `login()`, with a case for
every exception either can raise.

**Part 2.** Implement it in `tests/test_user_service.py`.

The pattern is:

```python
with pytest.raises(ValueError) as exception_info:
    service.register("bob", "Codes123")

assert str(exception_info.value) == "Username must contain at least 4 characters"
```

Every test asked for here can pass. When one goes red, read the message
before assuming your test is wrong: the order the validation rules run in
decides which message you get, and one row of the exercise guide's own test
plan gets that wrong. `CODE_CORRECTIONS.md` has the detail.

### Exercise 3 - mocking (`src/user_controller.py`)

**Part 1.** Adapt the exercise 2 plan for `UserController`. Add a Class
column. `register()` gains an exception decided by the repository;
`login()` loses most of its exceptions because the repository handles them.

**Part 2.** Implement it in `tests/test_user_controller.py` with the
repository **mocked**.

The guide names Mockito. Mockito is a Java library, so in Python we use
`unittest.mock` from the standard library. There is nothing to install.

| Mockito | unittest.mock |
| ------- | ------------- |
| `@Mock UserRepository repository` | `repository = MagicMock()` |
| `@InjectMocks UserController controller` | `controller = UserController(repository)` |
| `when(repo.exists("bob")).thenReturn(true)` | `repository.exists.return_value = True` |
| `when(repo.login(u)).thenThrow(...)` | `repository.login.side_effect = ValueError(...)` |
| `verify(repo).register(user)` | `repository.register.assert_called_once_with(user)` |
| `verify(repo, never()).register(user)` | `repository.register.assert_not_called()` |

`@patch` is the other half of `unittest.mock`. You do not need it here,
because `UserController` takes its repository as a constructor argument, so
you can simply hand it a `MagicMock`. Reach for `@patch` when a dependency is
imported or constructed inside the code under test and you cannot inject it.

**Part 3 (stretch) - test-driven development.** Write a test plan for the
three `UserRepository` methods, then build a `ConcreteUserRepository` that
implements the protocol, storing users in a list. Work test first: write one
failing test, write just enough code to pass it, repeat. Put the class in
`src/concrete_user_repository.py` and the tests in
`tests/test_concrete_user_repository.py`. See
[`tasks/04_stretch_tdd_repository.md`](tasks/04_stretch_tdd_repository.md).

## Differences from the Java version

| Java | Python | Why |
| ---- | ------ | --- |
| `IllegalArgumentException` | `ValueError` | The standard Python exception for an argument of the right type but an unacceptable value. |
| `RuntimeException` | `RuntimeError` | Closest built-in equivalent. |
| Checked exceptions, `throws` clauses | nothing | Python has no checked exceptions. What a function can raise is documented in its docstring and enforced only by your tests. |
| Static types on parameters | type hints | Hints are documentation. Nothing stops a caller passing the wrong type, so a Java compiler error becomes a Python test case. |
| `interface UserRepository` | `typing.Protocol` | Structural, so a `MagicMock` satisfies it with no subclassing. An ABC would be stricter but would get in the way of mocking. |
| JavaBean with getters, setters, `equals`, `hashCode`, `toString` | `@dataclass` | The dataclass generates the constructor, equality and repr. Attributes are public, so getters and setters add nothing. |
| `HashMap`, unspecified iteration order | `dict`, insertion ordered | Nothing here depends on ordering, but do not write a test that does. |
| `String.matches()` | `re.fullmatch()` | Both match the whole string. `re.match()` would only anchor at the start and would change the behaviour. |
| `matches(".*[A-Z].*")` in the password rules | `re.search(r"[A-Z]", ...)` | Both ask "does it contain one", which is what the rule says. The original used a whole-string match, which asked a different question and named the wrong rule. See `CODE_CORRECTIONS.md`. |
| `double` everywhere | one `float` type | `add(1, 2)` returns the int `3`, not `3.0`. Compare decimals with `pytest.approx`. |
| Mockito `@Mock` / `@InjectMocks` | `unittest.mock.MagicMock` | Standard library, no annotations, no test runner extension. |
| JUnit `assertThrows` | `pytest.raises` | Used as a context manager. |
| JUnit `@BeforeEach` | a pytest fixture | Fixtures are requested by name as test arguments. |
