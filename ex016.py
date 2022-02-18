# Project Euler 16, Power digit sum. Solved in 0.000148 seconds runtime.
# Exercise: https://projecteuler.net/problem=16

def ex16():
    l=list(str(2**1000))
    sum=0
    for x in l:
        sum+=int(x)
    return sum

print(ex16())
