# Project Euler 48 - Self powers, solved in 0.00977 seconds runtime.
# Exercise: https://projecteuler.net/problem=48

def ex48():
    n=0
    for x in range(1,1000):
        n+=x**x
    return str(n)[-10:]

print(ex48())
