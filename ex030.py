# Project Euler 30, Digit fifth powers. Solved in 0.957 seconds runtime.
# Exercise: https://projecteuler.net/problem=30

def sum_of_power_of_digits(n,pow,sum=0):
    l=list(str(n))
    for x in l:
        sum+=(int(x)**pow)
        if sum>n: return False
    return sum==n

def ex30():
    sum=0
    for x in range(2,250000): #1 doesn't count.
        if sum_of_power_of_digits(x,5):
            sum+=x
    return sum
