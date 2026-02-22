from random import randrange, seed, random
from math import sqrt

def calc_pi(n):
    """Calculate pi using random numbers. N is the number
    to random numbers to generate. Larger N give better
    values of pi.  This is in no way the most efficent way
    to caclulate pi; just a demo of using random numbers to
    do it.
    """
    count = 0
    for i in range(n):
        x = random()
        y = random()
        if sqrt(x * x + y * y) <= 1.0:
            count += 1
    print(f"With n={n:9}, pi = {4 * count / n}")

if __name__ == "__main__":
    # Genrate 10 random numbers using different seeds
    # The first seed is duplicated to see that resetting the
    #   seed to the same number results in the same sequence.
    for s in [1,1,2,3]:
        seed(s)
        print(f"seed = {s}:", end=" ")
        for i in range(10):
            print(randrange(1, 100), end=" ")
        print()
    print()

    # calculate pi with different n ranging from 10 to 1 billion
    for i in range(1, 9):
        calc_pi(10 ** i)