# Implementing dunder methods
from math import gcd
class Rational:
    def __init__(self, numerator, denominator):
        g = gcd(numerator, denominator)
        self.numer = numerator // g
        self.denom = denominator // g
    def __str__(self):
        return f"{self.numer}/{self.denom}"
    def __repr__(self):
        return f"Rational({self.numer}, {self.denom})"
    def __add__(self, other):

# what will this print? 
        print(Rational(1, 2) + Rational(3, 4))
# what do we have to do to add and print the correct result?

# Generic function
def sum_em(items, initial_value):
    """Returns the sum of ITEMS,
    starting with a value of INITIAL_VALUE."""
    sum = initial_value
    for item in items:
        sum += item
    return sum

print(sum_em(range(4),0))
print(sum_em(["a", "b", "c"],""))

# Type dispatching
def is_valid_month(month):
    if isinstance(month, str):
        if len(month) == 1:
            return month in ["J", "F", "M", "A", "S", "O", "N", "D"]
        else:
            return month in ["January", "February", "March", "April",
                "May", "June", "July", "August", "September",
                "October", "November", "December"]
    if isinstance(month, int):
        return month >= 1 and month <= 12
    return False

print(is_valid_month("N"))
print(is_valid_month("July"))
print(is_valid_month(13))

# Type Coercion
def sum_numbers(nums):
    """Returns the sum of nums"""
    sum = Rational(0, 1)
    for num in nums:
        if isinstance(num, int):
            num = Rational(num, 1)
        sum += num
    return sum

print(sum_numbers([1,Rational(5,2),3]))
