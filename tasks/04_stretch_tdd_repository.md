# Part 3 (stretch) - Test-driven development

Do this only once [exercise 3](03_mocking.md) is complete.

If you complete the above task, create a test plan for the methods of the
`UserRepository` interface (`src/user_repository.py`, a `typing.Protocol`
here rather than a Java interface).

Once a suitable plan is created, create your tests, and implement the
interface as a class. Call it **`ConcreteUserRepository`**. The *Concrete*
in the name indicates that it is a class and not an interface or an
abstract class.

Store the instances of `User` in a `List<User>` instance variable on the
concrete repository class. In Python that is a plain `list` attribute set in
`__init__`.

You write: `src/concrete_user_repository.py`
Your tests: `tests/test_concrete_user_repository.py`

There are no mocks in this exercise. This is the real implementation, so
the tests are ordinary state-based tests.

## Part 1 - The plan

Three methods to plan, from `src/user_repository.py`:

| Method | Does |
| ------ | ---- |
| `exists(trimmed_username)` | returns True if a user with this username is already stored |
| `register(user)` | stores the user and returns the stored instance |
| `login(user)` | returns the stored user if the credentials match |

The protocol does not say what should happen when you register a username
that already exists, or log in with credentials that match nothing. **That
is your decision to make and to write into your plan before you code.**
Deciding it in the plan, rather than discovering it while coding, is the
whole point.

| ID | Method | Description | Inputs | Expected output | Actual output |
| -- | ------ | ----------- | ------ | --------------- | ------------- |
| 1 | `exists(username)` | No user stored yet | "bobby" | False | |
| 2 | | | | | |
| 3 | | | | | |

The table is also in [`TEST_PLAN_TEMPLATE.md`](TEST_PLAN_TEMPLATE.md).

## Advice

The guide's own steps, in order:

1. After creating the plan, create the concrete repository class and
   implement the `UserRepository` interface. In Python there is no
   `implements` keyword and `UserRepository` is a `Protocol`, so you simply
   write a class with the three methods. Nothing inherits from anything.
2. Add the empty method stubs.
3. The test class is already stubbed for you. The Java guide calls it
   `UserRepositoryTest`; the unittest equivalent is the
   `class ConcreteUserRepositoryTest(unittest.TestCase)` waiting in
   `tests/test_concrete_user_repository.py`, which builds the repository in
   `setUp`. Every test in it skips, including its worked example, because
   the class does not exist yet.
4. Start creating the `register` tests.
5. Create the implementation of `ConcreteUserRepository.register()` **as you
   write the test**. Write one failing test, write just enough code to pass
   it, then repeat.
6. Repeat steps 4 and 5 for the `login` and `exists` methods.

Red, green, refactor. Run the suite after every single step:

```
python -m unittest tests.test_concrete_user_repository
```

A test that has never been seen to fail has not been shown to test
anything, so watch each one go red before you make it green.

## Done looks like

`tests/test_concrete_user_repository.py` exists, every test in it passes,
and `src/concrete_user_repository.py` contains nothing that was not
demanded by a test you had already watched fail.

```
python -m unittest discover
```

reports no skips and no failures.
