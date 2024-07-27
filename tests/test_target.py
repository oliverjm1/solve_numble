import pytest

from solve_numble.source import solve_numble

def test_target_int_error_using_float():
    target = 10.5
    inputs = [1, 2, 3, 4, 5, 6]
    with pytest.raises(TypeError):
        solve_numble(target, inputs)

def test_target_int_error_using_string():
    target = '10'
    inputs = [1, 2, 3, 4, 5, 6]
    with pytest.raises(TypeError):
        solve_numble(target, inputs)        
