# a tracing function
def trace1(f):
    """Return a function that takes a single argument, x, prints it,
    computes and prints F(x), and returns the computed value.
    >>> square = lambda x: x * x
    >>> trace1(square)(3)
    -> 3
    <- 9
    9
    """
    def traced(x):
        print("->", x)
        r = f(x) # calls the function that was passed to trace1()
        print("<-", r)
        return r
    return traced

# we can use trace1() like this to trace the input and output
# of square() any time it is called:
def square(x):
    return x * x
square = trace1(square) # rebinds the name "square" to the the traced() function
print(square(3)) # really calls an instance of traced() that contains square()

# this code is equivalent, but it doesn't rebind the name "square" to the traced() function
# instead, the traced() function returned from trace1(square) is called immediately with (3)
def square(x):
    return x * x
print(trace1(square)(3))

# the code below does exactly what the code above does, including rebinding the name square to traced()
# @trace1 means that whatever function follows it is being "decorated" with the trace1() function,
# so trace1() is a decorator function!
# this is a decorator. 
@trace1
def square(x):
    return x * x
print(square(3))

# now write your own decorator called debugger that prints out a message when the function it is
# decorating is called saying "Entering a function" and also any parameters passed to that function.
# the decorator should also print out a message after the decorated function returns saying
# "Returning from the function" and any return values other than None.
def debugger(f):
    def debug(x):
        print("entering a function")
        r = f(x)  # calls the function that was passed to trace1()
        print("exiting Function")
        if r != None:
            print(r)
        return r
    return debug
    
@debugger
def repeat_hello_world(x):

    return 'hello world' * x

print(repeat_hello_world(6))


