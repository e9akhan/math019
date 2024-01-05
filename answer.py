"""
    Module name :- answer
    Method(s) :- answer()
"""

import datetime
from solver import solver


def answer():
    """
    Find the num of times the given weekday comes on 1st of month in 20th century.

    Args:-
        from_date(datetime) :- Starting date.
        to_date(datetime) :- Ending date.

    Return
        Num of times the given weekday comes on 1st of month in 20th century.
    """
    start_date = datetime.datetime.strptime("01-01-1901", "%d-%m-%Y")
    end_date = datetime.datetime.strptime("31-12-2000", "%d-%m-%Y")
    return solver(start_date, end_date, "SUNDAY")


if __name__ == "__main__":
    print(f"answer() = {answer()}")
