# Requirements
import random

# Want a function that returns a method of solving Numble
# 2 inputs (an integer, and a list of integers).
# 1st input corresponds to the target, 2nd input is list containing 6 the integer numbers to use
# 1 ouput: A string of a valid equation that reaches the target.

def solve_numble(target, inputs):
    """Function to return the solved numble equation

    Args:
        target (int): Target number to reach
        inputs (list): List of 6 input integers

    Returns:
        string: A valid equation that would reach the target
    """

    # First would be checking that inputs are of correct form (all integers)

    solved = False
    
    # keep going until solved or had 100000 goes
    attempts = 0

    while solved == False and attempts < 100000:

        # One method would simply be to pick random number, random operator, random number etc...
        operators = ['+', '-', '*', '/']
        numbers = [str(i) for i in inputs]

        # Pick number to start
        eq = ""
        start_num = str(random.choice(numbers))
        eq += start_num
        numbers.remove(start_num) # remove number when chosen

        stored_val = start_num

        # Pick operator then number, then evaluate and check
        while len(numbers) > 0:
            operator = random.choice(operators)
            num = str(random.choice(numbers))
            numbers.remove(num)

            # update stored val
            stored_val = str(eval(stored_val + operator + num))

            # Add brackets if needed
            if eval(eq + operator + num) != float(stored_val):
                eq = '(' + eq + ')'
            
            # Add to equation
            eq = eq + operator + num

            if float(stored_val) == target:
                solved = True
                break

        attempts += 1

    if solved:
        solved_eq = eq
        return solved_eq
    else:
        return(f'No solution found in {attempts} attempts')
