# a lambda expression is a simple function definition that evaluates to a function
# syntax:
# lambda <parameters>: <expression>

# is there a difference between:
def square(x):
    return x * x
print(square(4))
# and:
square = lambda x: x * x
print(square(4))
# ?

# conditional expressions: if predicate is True, value is consequent, else value is alternative
# syntax:
# <consequent> if <predicate> else <alternative>

# is there a difference between:
def not_negative(x):
    if x >= 0:
        return x
    else:
        return -x
print(not_negative(5),not_negative(-5))
# and:
not_negative = lambda x: x if x >= 0 else -x
print(not_negative(5),not_negative(-5))
# ?


# lambda expression with a conditional expression
result1 = lambda x: "x is greater than 10" if x > 10 else "x is less than or equal to 10"
print(result1(12))  # Output: x is greater than 10
print(result1(8))   # Output: x is less than or equal to 10

# lambda expression with nested conditional expressions
result2 = lambda x: "x is greater than 10" if x > 10 else ("x is less than 10" if x < 10 else "x is equal to 10")
print(result2(12))  # Output: x is greater than 10
print(result2(8))   # Output: x is less than 10
print(result2(10))  # Output: x is equal to 10

# Now write a lambda expression that is assigned to "result" that produces the output in the comments below
result = lambda x : "Stop!" if x == "red" else ("Go!" if x == "green" else "Proceed with caution!")
print(result("red"))    # Output: Stop!
print(result("green"))  # Output: Go!
print(result("yellow")) # Output: Proceed with caution!
