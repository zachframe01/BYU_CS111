def categorize(n):
    """
    >>> categorize(5)
    ['Normal', 'Normal', 'Fizz', 'Normal', 'Normal']
    """
    # Try to use a single list comprehension here!
    # Hint: You can use an 'if-else' inside the Map Expression (the start of the comprehension)
    return ['fizz' if i % 3 == 0 else 'normal' for i in range(1, n + 1) ]

#if the number is a factor of 3 then print fizz

print(categorize(12))

def is_odd(n):
    """
    Docstring for is_odd
    >>> categorize(3)
    ['odd', 'even', 'odd']
    """
    return [['odd', i] if i % 2 != 0 else ['even', i] for i in range(1, n+1)]

print(is_odd(8))


