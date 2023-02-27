"""
Using Merge Sort to sort a list of numbers. This is more efficient and has a worst case of O(n log n)
"""


def sort_numbers(numbers) -> list:
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]
    left_sorted = sort_numbers(left_half)
    right_sorted = sort_numbers(right_half)
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list += left[i:]
    sorted_list += right[j:]
    return sorted_list

list_numbers = [20, 2, 5, 1, 3, 4, 6, 7, 8, 9, 10]
print(sort_numbers(list_numbers))
