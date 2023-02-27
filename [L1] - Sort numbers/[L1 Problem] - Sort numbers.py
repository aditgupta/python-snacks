"""
A simple program to sort numbers in ascending order without using the sort() method
"""

# Inefficient way to sort numbers. Worst case is O(n^2)
def sort_numbers(numbers) -> list:
    sorted_list = []
    while numbers:
        min_number = numbers[0]
        for num in numbers:
            if num < min_number:
               min_number = num
        sorted_list.append(min_number)
        numbers.remove(min_number)
    return sorted_list


list_numbers = [20, 2, 5, 1, 3, 4, 6, 7, 8, 9, 10]
print(sort_numbers(list_numbers))

# Easy way out. Worst case is O(n log n)
another_list_numbers = [30, 25, 20, 15, 10, 5, 1]
another_list_numbers.sort()
print(another_list_numbers)

