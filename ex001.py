# Project Euler 1 - Multiples of 3 or 5. Solved in 0.00020090000000000385 seconds runtime.
# Exercise: https://projecteuler.net/problem=1

def ex1():
    sum=0
    for x in range(1,1000):
        if x%3==0 or x%5==0:
            sum+=x
    return sum
print(ex1())
