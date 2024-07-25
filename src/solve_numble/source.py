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
    
    # keep going until solved or had 100 goes
    attempts = 0

    while solved == False and attempts < 1000:

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

            # Add to equation
            eq += (" " + operator)
            eq += (" " + num)

            if float(stored_val) == target:
                solved = True
                break

        attempts += 1

        print(f"attempt {attempts}: {eq}")
    
    print("Solved! (Or done 100 attempts)")
    print("Attempts ", attempts)

    solved_eq = eq
    return solved_eq

print(solve_numble(756, [3, 4, 6, 8, 75, 100]))