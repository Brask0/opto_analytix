# Test du module analysis.basic
from analysis import basic

def test_passthrough():
    assert basic.passthrough(42) == 42
    assert basic.passthrough(-1) == -1
    assert basic.passthrough(0) == 0
