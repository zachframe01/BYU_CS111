def square(x):
    """ returns the square of x for any value.
    >>> square(10)
    100
    >>> square(3.1415)
    9.86902225
    """
    return x * x

from math import * 
def square_root(x):
    """ returns the square root of any x, but raises a ValueError if x is negative
    >>> square_root(16)
    4.0
    >>> square_root(6.25)
    2.5
    """
    if x < 0:
        raise ValueError("Negative numbers not allowed")
    return sqrt(x)

def add_floats(x,y):
    """ adds two floating point numbers
    >>> add_floats(0.2 , 0.2)
    0.4
    >>> add_floats(0.1, 0.1)
    0.2
    """
    return x + y

def div_floats(x,y):

    """ returns the float sum of two floats. 
    >>> div_floats(6.0,2.0)
    3.0
    """
    # your docstring and code here
    return x/y

if __name__ == '__main__':
    float1 = float(input('Please input a floating point number: '))
    float2 = float(input('Please input another floating point number: '))
    print(f'The square of the first floating point number is {square(float1)}')
    print(f'The square root of the second floating point number is {square_root(float2)}')
    print(f'The sum of the two floating point numbers is {add_floats(float1,float2)}')
    print(f'The first floating point number divided by the second is {div_floats(float1,float2)}')
