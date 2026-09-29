# Test plan template

Copy this file, rename it (for example `test-plan.md`), and fill in the
tables before you write any test code. Every exercise starts with the plan.

Fill in the **Actual output** column only after you have run the test. Where
it differs from **Expected output**, you have either found a defect or
mis-stated your expectation. Both are worth writing down.

---

## Exercise 1 - Calculator

At least three test cases per method. Test borderline input values (what are
the largest and smallest numbers you can add?) as well as normal ones.

| ID | Method | Description | Inputs | Expected output | Actual output |
| -- | ------ | ----------- | ------ | --------------- | ------------- |
| 1 | `add(num1, num2)` | Adding two small numbers | num1=10, num2=30 | 40 | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

---

## Exercise 2 - UserService

One test case for every exception that can be raised, plus the happy paths.

| ID | Method | Description | Inputs | Expected output | Actual output |
| -- | ------ | ----------- | ------ | --------------- | ------------- |
| 1 | `login(username, password)` | Register a valid user, then log in successfully with that user | Register: username="bobby", password="Codes123". Login: username="bobby", password="Codes123" | "bobby" | |
| 2 | `register(username, password)` | Register a user with an invalid password because it has no number | username="bobby", password="Codes" | ValueError("Password must contain at least 1 number character") | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

Both rows above come straight from the exercise guide. Run them early. Row 1
behaves exactly as written. Row 2 does **not**: `"Codes"` is five
characters, so the length rule fires first and you get
`ValueError("Password must contain at least 6 characters")`. That is a
mistake in the worksheet, not in the code, and it is a good illustration of
why the order of the validation rules matters to a test plan.

The Python translation raises `ValueError` where the Java original raises
`IllegalArgumentException`, and `RuntimeError` where it raises
`RuntimeException`. Write the Python names in your plan.

---

## Exercise 3 - UserController with a mocked repository

Reuse and adapt the exercise 2 plan. A **Class** column is added because
more than one class is now involved. Add a column of your own for what the
mock is stubbed to do and what you verify on it.

| ID | Class | Method | Description | Inputs | Mock setup / verification | Expected output | Actual output |
| -- | ----- | ------ | ----------- | ------ | ------------------------- | --------------- | ------------- |
| 1 | `UserController` | `register(user)` | Register a valid user | User(1, "bobby", "Codes123") | `exists` returns False; verify `register` called once with the user | the same User | |
| 2 | | | | | | | |
| 3 | | | | | | | |

Remember:

* `register()` gains one exception that `UserService` did not have in the
  same form: "Username already exists", now decided by the repository.
* `login()` loses most of its exceptions, because the repository is expected
  to deal with unknown usernames and wrong passwords.

---

## Exercise 3 stretch - ConcreteUserRepository

Plan the three repository methods before you write them, then build the
class test first.

| ID | Method | Description | Inputs | Expected output | Actual output |
| -- | ------ | ----------- | ------ | --------------- | ------------- |
| 1 | `exists(username)` | No user stored yet | "bobby" | False | |
| 2 | | | | | |
| 3 | | | | | |
