# ASSIGNMENT: Activity 05 (Control)
# PROBLEM NUMBER: 4

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output

FILENAME = 'guessinggame.py'
POINTS = 1

def test_too_high_2():
    return _test_output(FILENAME,
                        r"""too high""",
                        input_values=['100', ''])


