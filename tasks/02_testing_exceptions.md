# Exercise 2 - Testing exceptions

This exercise uses the `UserService` class. In the Java guide it lives in
the `exercise2` package; here it is **`src/exercise2/user_service.py`**, in a
folder of the same name. No clone, no Eclipse import: activate the virtual environment described in
[`README.md`](README.md) and you are ready.

Source: `src/exercise2/user_service.py`
Your tests: `tests/exercise2/test_user_service.py`

## Part 1 - Create a test plan

In this exercise, you are required to create a test plan which consists of
test cases for the `UserService` class's two methods. Use the following
template for creating your test cases:

| ID | Method | Description | Inputs | Expected output | Actual output |
| -- | ------ | ----------- | ------ | --------------- | ------------- |
| 1 | `login(username, password)` | Register a valid user, login successfully with said valid user. | Register: username="bobby", password="Codes123". Login: username="bobby", password="Codes123" | "bobby" | |
| 2 | `register(username, password)` | Register a user with an invalid password due to missing number. | Register: username="bobby", password="Codes" | ValueError("Password must contain at least 1 number character") | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

Two example test cases have been created for you. It is expected that you
produce a test case for every possible exception that could be thrown.

> **Footnote on row 2, and it matters.** Run it early, because it does not
> do what the row says. `"Codes"` is **five** characters, so the
> six-character length rule fires **before** the number rule and you get
> `ValueError("Password must contain at least 6 characters")` instead.
>
> This is a mistake in the worksheet, not in the code. The validation rules
> run in a fixed order, and only the first one to fail produces a message,
> so a test plan has to know that order. If you want the "missing number"
> message, use a six-character password with no digit, such as `"Codess"`.
> That is what the worked example in `tests/exercise2/test_user_service.py` does.

Row 1 behaves exactly as written.

The Python translation raises `ValueError` where the Java original raises
`IllegalArgumentException`, and `RuntimeError` where it raises
`RuntimeException`. Write the Python names in your plan.

The table is also in [`TEST_PLAN_TEMPLATE.md`](TEST_PLAN_TEMPLATE.md).

## Part 2 - Implement your test plan

The `UserService` class has already been created. Use your test plan to
guide the development of tests for the methods of this class.

Open **`tests/exercise2/test_user_service.py`**. One test is written for you as a
worked example; the rest are stubs that skip until you write them. The
pattern is:

```python
with self.assertRaises(ValueError) as context:
    self.service.register("bob", "Codes123")

self.assertEqual(str(context.exception), "Username must contain at least 4 characters")
```

**Assert the exact message, not just the exception type.** Several rules
raise the same `ValueError`, so a test that only checks the type cannot
tell you which rule fired, and a wrong message is a defect in its own
right.

Run your tests from the repository root:

```
python -m unittest tests.exercise2.test_user_service
```

## Every exception you need a case for

`register()` raises `ValueError` for: a null username, a whitespace-only
username, a null password, a whitespace-only password, a username under 4
characters, a username that already exists, a password under 6 characters,
a password with no uppercase character, a password with no lowercase
character, and a password with no number character.

`login()` raises `ValueError` for a null username or password, and for an
empty username or password. It raises `RuntimeError("Invalid username
supplied")` when no such user is registered, and
`ValueError("Invalid password supplied")` when the password does not match
the one stored.

Do not forget the happy paths: `register()` returns the **trimmed**
username, and so does `login()`.

## Done looks like

Every stub in `tests/exercise2/test_user_service.py` has gone from skipped to
passing:

```
python -m unittest tests.exercise2.test_user_service
```

Your plan's **Actual output** column is filled in, including the honest
answer for row 2.
