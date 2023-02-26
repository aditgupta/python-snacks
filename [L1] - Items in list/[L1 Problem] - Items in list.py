"""
Write a program to return the occurrence of items in a list as a dictionary without using Counter()

"""


def items_in_list(target_list) -> dict:
    result = {}
    for item in target_list:
        result[item] = result.get(item, 0) + 1
    return result


new_list = ['a', 'b', 'c', 'a', 'a', 'b', 'a', 'b', 'c', 'a']
print(items_in_list(new_list))


# Using Counter
from collections import Counter
print(Counter(new_list))
