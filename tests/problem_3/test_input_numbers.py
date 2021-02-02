# ASSIGNMENT: Activity 05 (Control)
# PROBLEM NUMBER: 3

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable_with_input

FILENAME = 'alternatesum.py'
POINTS = 6

def test_input_numbers():
    return _test_variable_with_input("numbers",
                                     [1, 1, 1, 1, 2, 1, 1, ''],
                                     [1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0],
                                     FILENAME, check_type=False)
