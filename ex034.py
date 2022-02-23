# Project Euler 34 - Digit factorials. Solved in 0.191 seconds runtime.
# Exercise: https://projecteuler.net/problem=34

def factorial(n):
    if n<=1: return 1
    if n==2: return n
    return n*factorial(n-1)

def is_curious_number(n,sum=0):
    l=list(str(n))
    for x in l:
        sum+=factorial(int(x))
        if sum>n: return False
    return sum==n

def ex34():
    sum=0
    for x in range(10,50000):
        if is_curious_number(x):
            sum+=x
    return sum

print(ex34())
