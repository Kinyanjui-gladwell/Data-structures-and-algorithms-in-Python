"""This function details the number of steps taken to reduce a number to zero."""
"""Implementation with classes coming soon."""
def reduce(number):
    steps = 0
    while (number > 0):
        if number % 2 == 0:
            steps += 1
            quotient = number/2
            number = quotient
        else:
            new_number = number - 1
            steps += 1
            number = new_number
    print (f"Output: {steps}")
reduce(8)
