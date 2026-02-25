# first-order function 
def cube(k):
    return k ** 3

# higher-order function
def summation(n, term):
    """Sum the first N terms of a sequence. TERM is a function
       that takes a single argument and returns a result.
    >>> summation(5, cube)
    225
    """
    total = 0
    k = 1
    while k <= n:
        total = total + term(k)
        k = k + 1
    return total

print(summation(5,cube))

# using a lambda function instead of a def'd function
def summation(n, term):
    """Sum the first N terms of a sequence. TERM is a function
       that takes a single argument and returns a result.
    >>> summation(5, cube)
    225
    """
    total = 0
    k = 1
    while k <= n:
        total = total + term(k)
        k = k + 1
    return total

print(summation(5,lambda k: k ** 3))

# now print the result of summation replacing 0 with your own lambda expression
print(summation(5,lambda k: 2/k **2))


# locally defined function - adder
def make_adder(n):
    """Return a function that takes one argument k
       and returns k + n.
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

add_three = make_adder(3)
print(add_three(4))
print(make_adder(3)(4))

# now try writing a higher order funtion that takes a first string as a parameter
# and returns a function that when called with a second string, returns a string
# consisting of the second string with the first string concatenated to the front and back,
# e.g., first_string = '**', second_string = 'Note', returned_string = '**Note**'