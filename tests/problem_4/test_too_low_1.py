# ASSIGNMENT: Activity 05 (Control)
# PROBLEM NUMBER: 4

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output, assert_python3

FILENAME = 'guessinggame.py'
POINTS = 1

def test_python3():
    assert_python3()

def test_too_low_1():
    return _test_output(FILENAME,
                        r"""too low""",
                        input_values=['0', ''])


