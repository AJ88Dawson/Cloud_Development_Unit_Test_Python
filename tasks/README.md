# SDL3 Module 5: Testing - Exercise Guide

This folder is the exercise guide. It is a faithful Python rendering of
**002 - SDL3M5 - Testing Exercise Guide**: the same exercises, the same
parts, the same test plan tables. You do not need the PDF, and you do not
need the original Java repository. Everything the guide points at lives in
this repository.

## Before you start

Set up the environment once, from the repository root (the folder holding
`pytest.ini`).

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

Check it works:

```
pytest
```

You should see `3 passed, 43 skipped`. The three that pass are the worked
examples. The skips are the tests you are about to write.

## The exercises

Do them in order. Each has a **Part 1**, write a test plan, and a **Part 2**,
implement it. Do not skip Part 1: the plan is the exercise.

| | Exercise | Class under test | You edit | Roughly |
| - | -------- | ---------------- | -------- | ------- |
| 1 | [Testing existing code](01_testing_existing_code.md) | `src/calculator.py` | `tests/test_calculator.py` | 45 min |
| 2 | [Testing exceptions](02_testing_exceptions.md) | `src/user_service.py` | `tests/test_user_service.py` | 45 min |
| 3 | [Mocking in a unit test](03_mocking.md) | `src/user_controller.py` | `tests/test_user_controller.py` | 60 min |
| 4 | [Test-driven development (stretch)](04_stretch_tdd_repository.md) | you write it | `tests/test_concrete_user_repository.py` | 45 min |

## The test plan template

The tables you fill in for Part 1 of every exercise are in
[`TEST_PLAN_TEMPLATE.md`](TEST_PLAN_TEMPLATE.md). Copy it, rename your copy
(for example `test-plan.md`), and fill it in before you write any test code.

## Where the source and the solutions live

The guide links to two GitHub repositories, one for the exercise source and
one for the solutions. **This repository replaces both.**

| The guide says | In this repository |
| -------------- | ------------------ |
| Clone the exercises repository | you already have it, this is it |
| the `exercise1` package | `src/calculator.py` |
| the `exercise2` package | `src/user_service.py` |
| the `exercise3` package | `src/user.py`, `src/user_repository.py`, `src/user_controller.py` |
| the solutions repository | `solutions/`, run with `pytest solutions` |

Do not open `solutions/` until you have had a proper go yourself.

## A note for trainers

Two defects in the original Java code have been fixed here, and the fixes
are explained in the source at the point of the change.
[`../CODE_CORRECTIONS.md`](../CODE_CORRECTIONS.md) records what was wrong,
what changed and what to draw students' attention to. One error in the
guide's own worksheet is **not** fixed, because it is in the worksheet and
not in the code. It is flagged in exercise 2 below.
