def cascade(n):
    """ prints shrinking and then growing numbers of digits of N """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

cascade(123)


def inverse_cascade(n):
    """ prints growing and then shrinking numbers of digits of N """
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

inverse_cascade(1234)


def virfib(n):
    """Compute the nth Virahanka-Fibonacci number, for N >= 1.
    >>> virfib(2)
    1
    >>> virfib(6)
    8
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return virfib(n-2) + virfib(n-1)
    
print(virfib(5))

# insert the correct expression where the string 'put an expression here' occurs in the code below
def all_binary_strings(n):
    """
    Generate all binary strings of length n.
    Each binary string consists only of the characters '0' and '1'.
    The order of the returned strings does not matter.

    Parameters:
        n (int): The length of each binary string. Assumes n >= 0.
    Returns:
        list[str]: A list containing all binary strings of length n.

    >>> all_binary_strings(0)
    ['']
    >>> all_binary_strings(2)
    ['00', '01', '10', '11']
    """
    if n == 0:
        return ['']
    else:
        return ['0' + b  for b in all_binary_strings(n-1)] \
               + ['1' + b for b in all_binary_strings(n-1)]

print(all_binary_strings(3))

