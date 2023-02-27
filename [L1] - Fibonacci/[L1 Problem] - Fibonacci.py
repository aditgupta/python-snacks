"""
A super simple Fibonacci sequence generator
"""

def fibs(n):
    k = [0, 1]
    for i in range(n-2):  # n-2 because we already have 2 numbers in the list
        k.append(k[-1] + k[-2])
    return k

print(fibs(10))