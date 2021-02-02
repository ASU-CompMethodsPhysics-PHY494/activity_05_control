# ASSIGNMENT: Activity 05 (Control)
# PROBLEM NUMBER: 1

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'temperatures.py'
POINTS = 4

def test_create_list():
    return _test_variable("temp_Kelvin", [288.76111111111106, 298.8722222222222, 310.26111111111106, 309.31666666666666, 311.65, 316.4833333333333],
                          FILENAME,
                          check_type=False)
