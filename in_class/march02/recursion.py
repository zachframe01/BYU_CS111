# def sum_digits(n):
#     """Returns the sum of the digits of positive integer N.
#     >>> sum_digits(6)
#     6
#     >>> sum_digits(2023)
#     7
#     """
#     if n < 10:       # base case
#         return n
#     else:            # recursive case
#         last = n % 10
#         all_but_last = n // 10
#         return sum_digits(all_but_last) + last

# print(sum_digits(6))
# print(sum_digits(2023))

# def fact(n):
#     """Returns the factorial of N.
#     >>> fact(0)
#     1
#     >>> fact(3)
#     6
#     """
#     if n == 0:              # base case
#         return 1
#     else:                   # recursive case
#         return n*fact(n-1)

# print(fact(7))

# # now with print statments to help understanding
# def fact(n):
#     """Returns the factorial of N.
#     >>> fact(0)
#     1
#     >>> fact(3)
#     6
#     """
#     if n == 0:              # base case
#         print('n=0')
#         return 1
#     else:                   # recursive case
#         print(f'n={n} and n-1={n-1}')
#         factorial = n*fact(n-1)
#         print(f'value of n*n-1={factorial}')
#         return factorial

# print(fact(7))


# For you to try to code recursively
def sum_nums(nums):
    """Returns the sum of the numbers in nums.
    >>> sum_nums([2,3,4])
    9
    >>> sum_nums([6, 24, 1984])
    2014
    >>> sum_nums([-32, 0, 32])
    0
    """
    if not nums:       # base case
        return 0
    return nums[0] + sum_nums(nums[1:])
nums_list = [2,3,4]
print(sum_nums(nums_list))
# print(sum_nums([2,3,4]))

# For you to try to code recursively
def sum_up_to(n):
    """Returns the sum of positive numbers from 1 
    up to n (inclusive).
    >>> sum_up_to(5)
    15
    """
    pass

# print(sum_up_to(5))
