import random

# Q1
def add_one(number):
    """
    Returns the input number plus one.
    """
    return number + 1

def add_one_exception_handler():
    """ 
    This function catches the error from add_one and prints "Can't add 1 to that."
    instead of having the program crash.
    """
    try:
        add_one("apple")
        print("You added 1.")
    except ValueError:
        print("Can't add 1 to that.")


# Q2
def validate_input(user_input):
    input_list = user_input.split()
    if input_list[0].isdigit():
        if input_list[0] != "1" or input_list[0] != "2":
            print(ValueError("The options are 1, 2, or 'exit'"))
        if input_list[0] == "1" and len(input_list) != 2:
            print(ValueError("Option 1 requires one adiitional parameter"))
        if input_list[0] == "2" and len(input_list) != 1:
            print(ValueError("Option 2 takes no additional parameters"))
    else:
        if user_input == "exit":
            print(ValueError("The options are 1, 2, or 'exit'"))


# Q3
def exception_maker():
    raise TypeError

def exception_handler():
    """ Write a function that uses a try-except block to handle an exception.
    If an exception is thrown/raised, then print out something like:
    "Exception caught! Exception type: <<put the type of the exception here>>"
    """
    """*** YOUR CODE HERE ***"""


# Q4
def in_range1(n):
    """ Write a function that checks to see if n is
    within the range of 1-100 and have it return False if not
    >>> in_range1(9)
    True
    >>> in_range1(-4)
    False
    >>> in_range1(103)
    False
    """
    """*** YOUR CODE HERE ***"""

def in_range2(n):
    """ Redo in_range1, but instead of returning False, raise a ValueError
    if n is outside the range of 1-100.
    """
    """*** YOUR CODE HERE ***"""

def main():
    """ Write code in the main function that generates 1000
    random numbers between 1 and 101 and calls both in_range1
    and in_range2 function to validate the numbers generated using
    both functions.
    """
    """*** YOUR CODE HERE ***"""


# Q5
def bound_checker(x_dimension, y_dimension, x, y):
    """ If given an x and a y dimension which represent the maximum values on a grid
    (think of a square with dimensions x = 10, y = 12, for example),
    write a function that returns True if the x and y are within the grid,
    and throws an IndexError if they are out of bounds.
    >>> bound_checker(10, 12, 2, 3)
    True
    >>> bound_checker(10, 12, 59, 3)
    Traceback (most recent call last):
        ...
    IndexError
    """
    """*** YOUR CODE HERE ***"""