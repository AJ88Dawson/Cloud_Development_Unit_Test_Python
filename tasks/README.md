# SDL3 Module 5: Testing - Exercise Guide

This folder is the exercise guide. It is a faithful Python rendering of
**002 - SDL3M5 - Testing Exercise Guide**: the same exercises, the same
parts, the same test plan tables. You do not need the PDF, and you do not
need the original Java repository. Everything the guide points at lives in
this repository.

## Before you start

Set up the environment once, from the repository root (the folder holding
this repository's own `README.md`). You need Python 3.10 or newer; this was
built and verified on 3.12.10.

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

There is nothing to install. The tests use `unittest` and `unittest.mock`,
both of which are part of the Python standard library.

Check it works:

```
python -m unittest discover
```

You should see `Ran 46 tests` and `OK (skipped=43)`. The three that pass
are the worked examples. The 43 skips are the tests you are about to write,
and that count is your progress bar. The repository's
[`README.md`](../README.md) has the full setup and running notes.

## The exercises

Do them in order. Each has a **Part 1**, write a test plan, and a **Part 2**,
implement it. Do not skip Part 1: the plan is the exercise.

| | Exercise | Class under test | You edit |
| - | -------- | ---------------- | -------- |
| 1 | [Testing existing code](01_testing_existing_code.md) | `src/calculator.py` | `tests/test_calculator.py` |
| 2 | [Testing exceptions](02_testing_exceptions.md) | `src/user_service.py` | `tests/test_user_service.py` |
| 3 | [Mocking in a unit test](03_mocking.md) | `src/user_controller.py` | `tests/test_user_controller.py` |
| 4 | [Test-driven development (stretch)](04_stretch_tdd_repository.md) | you write it | `tests/test_concrete_user_repository.py` |

## The test plan template

The tables you fill in for Part 1 of every exercise are in
[`TEST_PLAN_TEMPLATE.md`](TEST_PLAN_TEMPLATE.md). Copy it, rename your copy
(for example `test-plan.md`), and fill it in before you write any test code.

## Where the source lives

The guide links to two GitHub repositories, one for the exercise source and
one for the solutions. **This repository replaces the first.**

| The guide says | In this repository |
| -------------- | ------------------ |
| Clone the exercises repository | you already have it, this is it |
| the `exercise1` package | `src/calculator.py` |
| the `exercise2` package | `src/user_service.py` |
| the `exercise3` package | `src/user.py`, `src/user_repository.py`, `src/user_controller.py` |

The model answers are not in this repository, and there is nothing to clone
for them. Your trainer has them. Have a proper go at an exercise first,
then ask.

## Two fixes to the original code

Two defects in the original Java code have been fixed here, and the fixes
are explained in the source at the point of the change.
[`../CODE_CORRECTIONS.md`](../CODE_CORRECTIONS.md) records what was wrong
and what changed. It is worth reading: both defects are the kind a test
suite is supposed to catch.

One error in the guide's own worksheet is **not** fixed, because it is in
the worksheet and not in the code. It is flagged in exercise 2.
