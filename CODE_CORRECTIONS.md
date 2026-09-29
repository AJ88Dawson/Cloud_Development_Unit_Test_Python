# What was wrong in the original, and what was changed

This project is a Python translation of the Java exercise repository. The
Java originals contained two real defects. They were ported faithfully at
first, and have now been **fixed**, because a student's first encounter with
unit testing should not be a fight with code that cannot pass its own
worked example.

This file is the record: what the original code did, why it was wrong, what
it does now, and what to notice. The source carries a short comment at each
fix, so reading `src/` alone still shows you why it is written that way.

The Java, C# and Python ports of these exercises all carry the same two
fixes and behave identically.

Everything here is fixed except the third entry, which is a mistake in the
exercise worksheet rather than in the code. That one is still live, and
exercise 2 warns you about it.

---

## Fixed 1 - `UserService.login()` looked users up by password

**Where:** `src/exercise2/user_service.py`, in `login()`.

The original, ported verbatim from the Java:

```python
saved_password = self.users.get(trimmed_password)   # wrong key
...
return username                                     # untrimmed
```

`register()` stores users as `self.users[username] = password`, so the
dictionary is keyed by username. `login()` then looked the entry up using
the **password** as the key. For any normally registered user that lookup
returned `None` and login failed with `"Invalid username supplied"`.

It is now:

```python
saved_password = self.users.get(trimmed_username)
...
return trimmed_username
```

The return value is trimmed too, so `login()` agrees with `register()`
about what a username is.

**Why it matters.** This is **test case 1 from the guide's own test plan**:
register `bobby` / `Codes123`, then log in with the same pair. Against the
original code that case could not pass.

**What a student should notice:**

* Login used to succeed only when a user's username and password were the
  same string, which is the one case the wrong key accidentally gets right.
  A test suite that only ever used such a user would have looked green.
* The `"Invalid password supplied"` branch used to be all but unreachable.
  Reaching it needed some *other* user registered under a username equal to
  the password being supplied. It is now reached the obvious way, by a user
  mistyping their own password. **Unreachable code is a smell worth hunting
  for in a review**, and a coverage report would have shown it.

`UserController.login()` was never affected: it delegates to the
repository and holds no map of its own.

**Now pinned by** four of the model answers for exercise 2, which your
trainer holds: the successful-registration-then-login case, the trimmed
username, the wrong password and the user who was never registered. Three
of them are TODOs in `tests/exercise2/test_user_service.py`, so you will write them
yourself.

---

## Fixed 2 - the password character rules used `[A-Z|a-z|1-9]`

**Where:** `src/exercise2/user_service.py`, the three module-level patterns, which
`src/exercise3/user_controller.py` imports so both classes share them.

The original:

```python
_HAS_UPPERCASE = r"[A-Z|a-z|1-9]*[A-Z]+[A-Z|a-z|1-9]*"
_HAS_LOWERCASE = r"[A-Z|a-z|1-9]*[a-z]+[A-Z|a-z|1-9]*"
_HAS_NUMBER    = r"[A-Z|a-z|1-9]*[1-9]+[A-Z|a-z|1-9]*"
```

used with `re.fullmatch`, which matches the whole string, exactly as Java's
`String.matches()` does. Three things went wrong, in Java and in Python
alike:

1. Inside a character class, `|` is a **literal pipe character**, not
   alternation. So a pipe was quietly accepted as a password character
   while every other symbol was rejected.
2. The digit range was `1-9`, not `0-9`. **The digit zero was not in the
   class at all.**
3. Because the match was whole-string, any character the class did not list
   failed **all three** patterns, starting with the uppercase one. A user
   with a perfectly valid password such as `Codes0` was told their password
   had no capital letter.

It is now one plain "contains" search per rule, in the same order and with
the messages unchanged:

```python
_HAS_UPPERCASE = r"[A-Z]"
_HAS_LOWERCASE = r"[a-z]"
_HAS_NUMBER    = r"[0-9]"
...
if not re.search(_HAS_UPPERCASE, trimmed_password): ...
```

**What a student should notice:**

* The rule as stated is "contains at least one uppercase character". A
  whole-string match answers a **different question**, "is the whole
  password made only of these characters", and there was no stated rule
  saying that. Testing the rule you were given is not the same as testing
  the rule the code implements.
* The message was actively misleading. `Codes0` starts with a capital C and
  was still told it had no uppercase character. A wrong error message is a
  defect in its own right, and only a test that asserts the **exact
  message** catches it. Asserting "some ValueError was raised" would have
  passed.
* If the intention really was to restrict the allowed alphabet, that is a
  separate rule and needs its own check and its own message, for example
  `re.fullmatch(r"[A-Za-z0-9]+", trimmed_password)`.

**Now pinned by** five of the model answers for exercise 2, and the
matching five for exercise 3: a password whose only digit is zero, a
password containing a symbol, and one per rule checking that the message
names the rule that actually failed.
`test_register_accepts_a_password_whose_only_digit_is_zero` is a TODO in
`tests/exercise2/test_user_service.py`, so you will write that one yourself.

---

## Still live - a mistake in the exercise guide, not in the code

The guide's test case 2 for exercise 2 says that registering
`username="bobby"`, `password="Codes"` should give
`"Password must contain at least 1 number character"`.

It does not, and it never did. `"Codes"` is **five** characters, so the
six-character length rule fires first:

```
E   ValueError: Password must contain at least 6 characters
```

This one is **not fixed**, because there is nothing wrong with the code.
The worksheet is wrong, and the order in which validation rules run is a
genuine thing a test plan has to get right.

The worked example in `tests/exercise2/test_user_service.py` therefore uses `"Codess"`
(six characters, no digit), which produces the message the guide intended.
A model answer pins the guide's original input so the discrepancy is on the
record, and `tasks/02_testing_exceptions.md` reproduces the guide's table
with a footnote.

It is a good illustration of why the order of validation checks matters to
a test plan. Only the first rule to fail produces a message, so a plan that
does not know the order will predict the wrong one.
