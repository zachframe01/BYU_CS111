# ZeroDivisionError
def div_numbers(dividend, divisor):
    return dividend/divisor

try:
    quot1 = div_numbers(10, 2)
    quot2 = div_numbers(10, 1)
    quot3 = div_numbers(10, 0) 
    quot4 = div_numbers(10, -1)
except ZeroDivisionError as e:
    print(f'Tried to divide by 0: {e}')