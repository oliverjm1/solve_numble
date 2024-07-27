import pytest

from solve_numble.source import solve_numble, InputLengthError

def test_inputs_length():
    target = 10

    with pytest.raises(InputLengthError):
        inputs = [1, 2, 3, 4, 5]
        solve_numble(target, inputs)
    
    with pytest.raises(InputLengthError):
        inputs = [1, 2, 3, 4, 5, 6, 7]
        solve_numble(target, inputs)