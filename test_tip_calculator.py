"""
Your test suite for Lab 2. One sample test is provided to get you started.

Requirements (see the Lab 2 assignment):
  - at least 8 test functions total
  - at least one fixture
  - at least one @pytest.mark.parametrize
  - at least 2 error/edge-case tests (e.g., negative bill, zero people)
  - >= 80% branch coverage

Practice TDD on at least 2 of the three functions:
  write the failing test FIRST, commit, then write the code, commit.
"""
import pytest
from tip_calculator import calculate_tip, calculate_total, split_bill


@pytest.fixture
def sample_bill():
    return 100


def test_calculate_tip(sample_bill):
    assert calculate_tip(sample_bill, 20) == 20.0


@pytest.mark.parametrize("bill, tip_pct, expected", [
    (100, 15, 15.0),
    (50, 20, 10.0),
    (80, 10, 8.0),
])
def test_calculate_tip_parametrize(bill, tip_pct, expected):
    assert calculate_tip(bill, tip_pct) == expected


def test_calculate_total():
    assert calculate_total(100, 20) == 120.0


def test_calculate_total_zero_tip():
    assert calculate_total(100, 0) == 100.0


def test_split_bill():
    assert split_bill(120, 4) == 30.0


def test_split_bill_rounding():
    assert split_bill(100, 3) == 33.33


def test_negative_bill():
    with pytest.raises(ValueError):
        calculate_tip(-100, 20)


def test_zero_people():
    with pytest.raises(ValueError):
        split_bill(100, 0)