def sum_squares(start, end):
    """
    Sum the squares of the values from start to end inclusive
    """
    counter = start
    total = 0
    while counter <= end:
       total += pow(counter, 2)
       counter += 1 
    return total

value = sum_squares(1, 20)
print("The sum is", value)