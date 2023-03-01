""" A basic palindrome checker
 It can't get simpler than this!
 """

# Using basic function. Complexity is O(n)
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


print(is_palindrome('level'))
print(is_palindrome('hello'))


# Using lambda. Complexity is O(n)
palindrome = lambda word: True if word == word[::-1] else False

print(palindrome('level'))