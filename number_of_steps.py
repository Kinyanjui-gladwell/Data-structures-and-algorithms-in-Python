"""This solves the number of steps needed to reduce to zero."""
"""Implemention with classes coming soon."""
def reduce(number):
    steps = 0
    while (number > 0):
        if number % 2 == 0:
            steps += 1
            number = number / 2
        else:
            steps += 1
            number = number - 1
    print(f"Output: {steps}")

reduce(8)