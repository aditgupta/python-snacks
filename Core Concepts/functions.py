""" Some basic examples of playing with functions """

# A higher-order function

# --------------------------------------------


def calculate(func, x, y):  # A simple example of a higher-order function
    return func(x, y)


def add(x, y):
    return x+y


print(calculate(add, 2, 3))  # prints 5

# --------------------------------------------
# An inner function


def outer(name):  # This is an outer function
    def inner(intro):   # This is an inner function that remembers the scope of the outer function
        print(f"Hello {name}, {intro}")
        pass
    return inner


person = outer("John")
person("I am a developer")

# --------------------------------------------
# A simple calculator using inner functions


def calculator():
    def add(x, y):
        return x+y

    def subtact(x, y):
        return x-y

    def multiply(x,y):
        return x*y

    def divide(x,y):
        return x/y

    while True:
        print("Select an operation: ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            break

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == "1":
            print(f"The sum is {add(num1, num2)}")
        elif choice == "2":
            print(f"The difference is {subtact(num1, num2)}")
        elif choice == "3":
            print(f"The product is {multiply(num1, num2)}")
        elif choice == "4":
            print(f"The quotient is {divide(num1, num2)}")
        else:
            print("Invalid choice")


calculator()

# --------------------------------------------
# An example of an inner function modifying the scope of the outer function
# If the inner function modifies a variable that is defined in the enclosing scope without using the nonlocal keyword,
# it will create a new variable in the inner function's scope


def outer_func():
    x = 2
    print("x is ", x , "from the outer function")

    def inner_func():
        nonlocal x  # With nonlocal, you can modify the scope of the outer function
        x = 5
    inner_func()
    print("x is now ", x, "from the  modified value of inner function")


outer_func()

# --------------------------------------------

# A simple example of a decorator

def decorator(func):
    def wrapper(*args, **kwargs):
        print('The function decorated is ', func.__name__)
        return func(*args, **kwargs)
    return wrapper


@decorator
def add(x,y):
    return x+y


print(add(2,3))

# --------------------------------------------

# A simple example of recursion

def sum_natual_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_natual_numbers(n-1)


print(sum_natual_numbers(10))