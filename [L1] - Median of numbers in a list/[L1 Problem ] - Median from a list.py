"""
Write a function that takes a list of integers and returns a new list with the median of every three adjacent numbers.
"""


# The program has a worst-case complexity of O(n)
def median(numbers):
    median_list = []
    numbers_count = len(numbers)
    for i in range(1, numbers_count - 1):
        median_formula = (numbers[i-1] + numbers[i] + numbers[i+1]) / 3
        median_list.append(median_formula)
    return median_list


list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(median(list_numbers))
