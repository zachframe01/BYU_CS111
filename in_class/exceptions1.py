def invert(x):
    inverse = 1/x # Causes a ZeroDivisionError if x is 0
    print('Never printed if x is 0')
    return inverse

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('Handled in invert_safe', e)
        return 0

print(invert_safe(0))

try:
    print(invert_safe(0))
except ZeroDivisionError as e:
    print('Handled outside of invert_safe!')

# try this again using assert or raise
    
def invert(x):
    # Use "assert" if you know this should not happen in your code:
    # assert x != 0, "Should never devide by zero!"  
    # Use "raise" if this could result from user input - defensive programming
    if x == 0: 
        raise ZeroDivisionError("User is trying to divide by 0")
    inverse = 1/x 
    print('Never printed if x is 0')
    return inverse

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print(e)
        return 0
    except AssertionError as e:
        print(e)
        return 0

# Either my code set x to 0 somewhere, in which case I assert this should not happen, 
# or a user entered data causing x to be 0, in which case I raise an exception
x = 0
invert_safe(x)

