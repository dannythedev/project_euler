# Project Euler 1 - Multiples of 3 or 5. Solved in 0.00014 seconds runtime.
# Exercise: https://projecteuler.net/problem=1

def ex1():
    return sum([x for x in range(1,10**7) if x%3==0 or x%5==0])

print(ex1())
