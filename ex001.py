# Project Euler 1 - Multiples of 3 or 5. Solved in 8.7e-05 seconds runtime.
# Exercise: https://projecteuler.net/problem=1

def ex1():
    return sum([x for x in range(0, 1000, 3)] +\
               [x for x in range(0, 1000, 5) if not x % 3 == 0])

print(ex1())
