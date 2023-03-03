"""
Write a function to find the maximum value in a list. The function should not use the built-in max() function.
"""

# The worst-case complexity of this program is O(n)
def max_number(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


list_numbers = [-2, 10, 5, 1, 3, 4, 6, 7, 8, 9]
print(max_number(list_numbers))
