# ASSIGNMENT: Activity 05 (Control)
# PROBLEM NUMBER: 1

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output

FILENAME = 'temperatures.py'
POINTS = 4

def test_range():
    return _test_output(FILENAME,
                        r"""\s*60.1 F\s+288.8 K
\s*78.3 F\s+298.9 K
\s*98.8 F\s+310.3 K
\s*97.1 F\s+309.3 K
\s*101.3 F\s+311.6 K
\s*110.0 F\s+316.5 K
""",
                        input_values=None)


