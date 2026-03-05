import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from calculator import Calculator

calc = Calculator()

def test_addition():
    assert calc.add(5, 3) == 8