# ZeroDivisionError
def div_numbers(dividend, divisor):
    return dividend/divisor

quot1 = div_numbers(10, 2)
quot2 = div_numbers(10, 1)
quot3 = div_numbers(10, 0) 
quot4 = div_numbers(10, -1)

# NoneTypeError
def sum(a, b):
    print(a + b)
total = sum( sum(30, 45), sum(10, 15) )

# UnboundLocalError
def sum_nums(x, y):
    sum += x + y 
    return sum
    
sum_nums(4, 5)