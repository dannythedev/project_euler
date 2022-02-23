# Project Euler 20 - Factorial digit sum. Solved in 0.0002926 seconds runtime.
# Exercise: https://projecteuler.net/problem=20

def factorial(n):
    if n<=1: return 1
    if n==2: return n
    return n*factorial(n-1)

def sum_of_digits(n):
    s = 0
    while n>0:
        s += n % 10
        n//=10
    return s

def ex20():
    return sum_of_digits(factorial(100))

print(ex20())
