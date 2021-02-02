# ASSIGNMENT: Activity 05 (Control)
# PROBLEM NUMBER: 3

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable_with_input

FILENAME = 'alternatesum.py'
POINTS = 4

def test_alternating_sum():
    return _test_variable_with_input("asum",
                                     [1, 1, 1, 1, 2, 1, 1, ''],
                                     2.0,
                                     FILENAME, check_type=False)
