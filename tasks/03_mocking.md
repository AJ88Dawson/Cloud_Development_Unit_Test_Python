# Exercise 3 - Mocking in a unit test

This exercise relies on the `User` and `UserController` classes and the
`UserRepository` interface. In the Java guide they live in the `exercise3`
package; here they are:

| The guide says | In this repository |
| -------------- | ------------------ |
| `User` | `src/exercise3/user.py`, a `@dataclass` |
| `UserRepository` interface | `src/exercise3/user_repository.py`, a `typing.Protocol` |
| `UserController` | `src/exercise3/user_controller.py` |

Your tests: `tests/exercise3/test_user_controller.py`

## Part 1 - Update the test plan from exercise 2

The test plan from exercise 2 can be reused for this example. Modify the
test plan to accommodate the changes to the `login` and `register` methods
present in the `UserController` class.

As we are now dealing with multiple classes, it is also recommended to add
a **Class** column to the test table.

* There is a **new exception** that could be thrown in the `register`
  method: `"Username already exists"`, now decided by the repository rather
  than by an in-memory map.
* Some exceptions have been **removed** from the `login` method, as it is
  expected that the repository implementation would handle those cases in
  this example, i.e., invalid usernames or passwords.

| ID | Class | Method | Description | Inputs | Mock setup / verification | Expected output | Actual output |
| -- | ----- | ------ | ----------- | ------ | ------------------------- | --------------- | ------------- |
| 1 | `UserController` | `register(user)` | Register a valid user | User(1, "bobby", "Codes123") | `exists` returns False; verify `register` called once with the user | the same User | |
| 2 | | | | | | | |
| 3 | | | | | | | |

The table is also in [`TEST_PLAN_TEMPLATE.md`](TEST_PLAN_TEMPLATE.md).

## Part 2 - Implement the tests

Implement your unit test plan, as done with the previous examples.

Be careful when writing your tests for the `login` and `register` methods.
The guide expects you to use the **Mockito** framework to mock interactions
with the repository, and to inject the mock into the controller with the
`@Mock` and `@InjectMocks` annotations.

**Mockito is a Java library and does not exist in Python.** Use
`unittest.mock` from the standard library instead. It is already installed:
it ships with Python, so there is nothing to add to `requirements.txt`. The
ideas map across one for one:

| Mockito | unittest.mock |
| ------- | ------------- |
| `@Mock UserRepository repository` | `repository = MagicMock()` |
| `@InjectMocks UserController controller` | `controller = UserController(repository)` |
| `when(repo.exists("bob")).thenReturn(true)` | `repository.exists.return_value = True` |
| `when(repo.login(u)).thenThrow(...)` | `repository.login.side_effect = ValueError(...)` |
| `verify(repo).register(user)` | `repository.register.assert_called_once_with(user)` |
| `verify(repo, never()).register(user)` | `repository.register.assert_not_called()` |
| `@BeforeEach` building both | `setUp`, building both onto `self` |

There is no annotation processor and no test runner extension. A
`MagicMock` is just an object that answers to any attribute, and because
`UserRepository` is a `typing.Protocol` rather than a Java interface, no
subclassing is needed: you hand the mock straight to the constructor.

`@patch` is the other half of `unittest.mock`. You do not need it here,
because `UserController` takes its repository as a constructor argument.
Reach for `@patch` when a dependency is imported or constructed inside the
code under test and you cannot inject it.

The repository methods being mocked are `UserRepository.exists()`,
`UserRepository.register()` and `UserRepository.login()`.

Open **`tests/exercise3/test_user_controller.py`**. One test is written for you as a
worked example; the rest are stubs that skip until you write them. Run
them from the repository root:

```
python -m unittest tests.exercise3.test_user_controller
```

## What to verify, not just assert

Mocking lets you test the **interaction**, not only the return value. For
each case, ask both questions:

* what did the controller return or raise?
* and what did it call on the repository, with what arguments, how many
  times, or did it correctly call nothing at all?

For example, when validation fails the repository must never be touched:
`repository.register.assert_not_called()`.

## Done looks like

Every stub in `tests/exercise3/test_user_controller.py` has gone from skipped to
passing:

```
python -m unittest tests.exercise3.test_user_controller
```

Then move on to [the stretch task](04_stretch_tdd_repository.md).
