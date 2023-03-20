"""
Write a Python function to find the maximum product of two integers in an array.

Input:
numbers = [10, 5, 2, 6, 8, 4, 7]
Output:
80

Input:
[-8, -10, 2, 5, 8, 4, 7]
Output:
80

"""

def maximum_product(numbers):
    sorted_list = sorted(numbers)
    # we will take the product of the first and last two integers so that we account for both negative and positive integers
    return max(sorted_list[-1] * sorted_list[-2], sorted_list[0] * sorted_list[1])


numbers = [-8, -10, 2, 5, 8, 4, 7]
print(maximum_product(numbers))

another_list = [0, 2, 5, 1, 3, 4, 2, 2, 9, 1]
print(maximum_product(another_list))
