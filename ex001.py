# Project Euler 1 - Multiples of 3 or 5. Solved in 0.0001 seconds runtime.
# Exercise: https://projecteuler.net/problem=1

def ex1():
    sum, x = 0, 1
    a3, a5 = 0, 0
    while a3 < 1000:
        if a5 < 1000 and not a5 % 3 == 0:
            sum += a5
        sum += a3
        a3, a5 = x * 3, x * 5
        x += 1
    return sum

print(ex1())
