# ASSIGNMENT: Activity 05 (Control)
# PROBLEM NUMBER: 3

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable_with_input

FILENAME = 'alternatesum.py'
POINTS = 2

def test_alternating_sum_negative():
    return _test_variable_with_input("asum",
                                     [-2.5, 1.5, 3, -1, -2, -1, 1, ''],
                                     0.0,
                                     FILENAME, check_type=False)
