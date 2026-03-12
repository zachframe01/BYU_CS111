# Q1
def echo_twice(s, n):
    """
    Prints all possible strings formed by repeating s exactly
    n times, where at each step you may add either 'A' or 'B'.
    >>> echo_twice("hello", 2)
    helloAA
    helloAB
    helloBA
    helloBB
    >>> echo_twice("cat", 1)
    catA
    catB
    >>> echo_twice("dog", 0)
    dog
    """
    if n == 0:
        print(s)
    else:
        echo_twice(s+"A", n-1) 
        echo_twice(s+"B",n-1)



# Q2
def ways_to_climb(n):
    """
    Returns the number of distinct ways to reach the top by taking either 1 or 2 steps each step.
    >>> ways_to_climb(4)
    5
    >>> ways_to_climb(0)
    1
    >>> ways_to_climb(1)
    1
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return ways_to_climb(n-2) + ways_to_climb(n-1)


# # Q3
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)
    
print(paths(5,7))
print(paths(1,155))


# # Q4
# def phone_keypad(digits, prefix=""):
#     """
#     Prints all letter combinations represented by a phone keypad.
#     >>> phone_keypad('23')
#     AD
#     AE
#     AF
#     BD
#     BE
#     BF
#     CD
#     CE
#     CF
#     >>> phone_keypad('159')
#     1JW
#     1JX
#     1JY
#     1JZ
#     1KW
#     1KX
#     1KY
#     1KZ
#     1LW
#     1LX
#     1LY
#     1LZ
#     >>> phone_keypad('7')
#     P
#     Q
#     R
#     S
#     """
#     """*** YOUR CODE HERE ***"""
