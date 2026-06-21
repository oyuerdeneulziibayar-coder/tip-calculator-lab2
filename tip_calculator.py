"""
tip_calculator.py  —  Lab 2 (ENGR403)

Build these three functions using Test-Driven Development.
Write a FAILING test first, then write just enough code here to pass.

Delete the `raise NotImplementedError` lines as you implement each one.
"""

def calculate_tip(bill, tip_pct):
    if bill < 0 or tip_pct < 0:
        raise ValueError("Bill or tip cannot be negative")
    return round(bill * (tip_pct / 100), 2)


def calculate_total(bill, tip_pct):
    return round(bill + calculate_tip(bill, tip_pct), 2)


def split_bill(total, people):
    if people <= 0:
        raise ValueError("People must be greater than 0")
    return round(total / people, 2)

