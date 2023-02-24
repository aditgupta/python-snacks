""" Some basic examples of playing with functions """

# A higher-order function


def calculate(func, x, y):  # A simple example of a higher-order function
    return func(x, y)


def add(x, y):
    return x+y


print(calculate(add, 2, 3))  # prints 5

