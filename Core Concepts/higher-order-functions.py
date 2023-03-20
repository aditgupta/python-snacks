"""
A simpl example to demonstrate the concept of higher order functions.
"""

def compose(f,g):
    def composed_function(x):
        return f(g(x))
    return composed_function

def square(x):
    return x*x

def double(x):
    return x*2

def main():
    numbers = [1,2,3,4,5]
    square_double = compose(square, double)
    double_square = compose(double, square)

    squared_and_doubled = list(map(square_double, numbers))
    doubled_and_squared = list(map(double_square, numbers))

    print('Numbers: ', numbers)
    print('Squared and Doubled: ', squared_and_doubled)
    print('Doubled and Squared: ', doubled_and_squared)

if __name__ == '__main__':
    main()
                                `