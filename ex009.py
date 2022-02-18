# Project Euler 9 Special Pythagorean triplet. Solved in 0.08883 seconds runtime.
# Exercise: https://projecteuler.net/problem=9
import math

def ex9():
    for a in range(1,1000):
        for b in range(1,1000):
            c = math.sqrt(a*a + b*b)
            if a + b + c == 1000:
                return a*b*c
print(ex9())
