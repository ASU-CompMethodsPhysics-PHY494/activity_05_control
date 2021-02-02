# ASSIGNMENT: Activity 05 (Control)
# PROBLEM NUMBER: 4

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output

FILENAME = 'guessinggame.py'
POINTS = 2

def test_goldilocks():
    return _test_output(FILENAME,
                        r"""guessed the number""",
                        input_values=['42', ''])


