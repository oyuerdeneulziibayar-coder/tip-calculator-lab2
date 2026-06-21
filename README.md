# Lab 2 — TDD Tip Calculator (Starter)

You'll build three small functions **test-first**. Don't worry about a blank
page — the function stubs and one sample test are already here.

## What's in this folder
- `tip_calculator.py` — three empty functions for you to implement
- `test_tip_calculator.py` — one sample test to copy the pattern from
- `requirements.txt` — the packages you need

## Step 1 — Set it up (one time)
```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Step 2 — See the starting point
```bash
pytest
```
The sample test will FAIL — that's correct. The functions aren't written yet.

## Step 3 — Do TDD on at least 2 functions
For each of two functions, repeat this loop:
1. **Red** — write a failing test, run `pytest`, then `git commit`
2. **Green** — write just enough code to pass, run `pytest`, then `git commit`

That gives ~4 commits that show the test-first pattern.

## Step 4 — Finish the suite
You need, in total:
- at least **8 test functions**
- at least **one** `@pytest.fixture`
- at least **one** `@pytest.mark.parametrize`
- at least **2** error/edge tests (e.g. negative bill, zero people)

## Step 5 — Check coverage (aim for ≥80%)
```bash
pytest --cov=tip_calculator --cov-report=term-missing
```
The "Missing" column tells you exactly which lines still need a test.

## Step 6 — Submit
Push to GitHub, then submit: **repo link + a screenshot of the coverage report (≥80%)**.

### Troubleshooting
- *"no tests ran"* → test files and functions must start with `test_`.
- *coverage stuck* → write one test per line listed under "Missing".
