"""
Write a function to find the first missing positive integer in a list of integers.

The function should return the smallest positive integer that is missing from the list. If all positive integers are
present, it should return the next positive integer. If the input list is empty or contains only negative integers,
the function should return 1.

Input: [-1, 1, 0]
Output: 2

Input: [2, 3, -1, -2]
Output: 1

Input: [6, 7, 8, 10, 11]
Output: 1

Input: [1, 2, 3, 4, 5]
Output: 6

Input: [-1, -2, -3, -4, -5]
Output: 1

"""

def missing_positive_integer(numbers):
    # return 1 if the list is empty
    if not numbers:
        return 1

    length_list = len(numbers)
    i = 0

    # arrange positive numbers sequentially - check if it's positive and at the right index
    # If not at right index, position it at the right index sequentially

    while i < length_list:
        if 0 < numbers[i] <= length_list and numbers[i] != numbers[numbers[i] - 1]:  # check if it's positive and at the right index
            numbers[numbers[i] - 1], numbers[i] = numbers[i], numbers[numbers[i] - 1]  # parallel assignment / tuple unpacking - swap
        else:
            i += 1

        # find the first missing positive integer
    for i in range(length_list):
        if numbers[i] != i+1:  # if list is [-1, 1, 3, 4] then 2 is missing
            return i+1  # return the missing number

    return length_list + 1


list_numbers = [-1, 1, 0]
print(missing_positive_integer(list_numbers))

list_numbers = [2, 3, -1, -2]
print(missing_positive_integer(list_numbers))

list_numbers = [6, 7, 8, 10, 11]
print(missing_positive_integer(list_numbers))

list_numbers = [1, 2, 3, 4, 5]
print(missing_positive_integer(list_numbers))

list_numbers = [-1, -2, -3, -4, -5]
print(missing_positive_integer(list_numbers))







