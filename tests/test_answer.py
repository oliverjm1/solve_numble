import pytest

from solve_numble.source import solve_numble

def test_correct_answer():
    # Check today's numble
    target = 504
    inputs = [4, 7, 8, 10, 25, 75]

    solved = solve_numble(target, inputs)
    assert eval(solved) == target