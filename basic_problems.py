# A simple program to return the occurrence of items in a list as a dictionary

def count_items(sequence) -> dict:
    result = {}
    for item in sequence:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

list_alphabets = ['a', 'b', 'c', 'a', 'b', 'a']
print(count_items(list_alphabets))


def count_items_another(sequence) -> dict:
    result = {}
    for item in sequence:
        result[item] = result.get(item, 0) + 1  # get the value of the key, if not present, return 0 and add 1
    return result


list_another_alphabets = ['a', 'b', 'c', 'a', 'b', 'a']
print(count_items_another(list_another_alphabets))

# We can achieve the same result using Counter


from collections import Counter
print(Counter(list_another_alphabets))
