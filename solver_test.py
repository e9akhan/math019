import solver
import datetime


def is_solved():
    assert solver.solver(datetime.date.today(), datetime.datetime.strptime('01-11-2025', '%d-%m-%Y'), 'MONDAY')


def test_solver():
    assert solver.solver(datetime.date.today(), datetime.datetime.strptime('01-11-2025', '%d-%m-%Y'), 'MONDAY') == 2
