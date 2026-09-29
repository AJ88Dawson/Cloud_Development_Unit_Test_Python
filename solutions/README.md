# Solutions

Model answers. Do not look at these until you have had a proper go at the
exercises yourself.

Run them from the project root (the folder containing `pytest.ini`):

```
pytest solutions
```

A bare `pytest` deliberately does **not** pick this folder up, so you cannot
run the answers by accident: `testpaths = tests` in `pytest.ini` limits the
default run to the student skeletons.

Expected result: everything passes, with nothing skipped and nothing
`xfailed`.

Two defects carried over from the Java original have been fixed in `src/`,
so the tests that assert the exercise guide's own worked examples now pass
on their own terms. `../CODE_CORRECTIONS.md` records what was wrong, what
changed and what to point out to students.

`concrete_user_repository.py` lives here rather than in `src/` because
building it is the stretch task. Students write their own in
`src/concrete_user_repository.py`.
