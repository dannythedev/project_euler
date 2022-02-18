# Project Euler 15, Lattice paths. Solved in 0.000148 seconds runtime.
# Exercise: https://projecteuler.net/problem=15

def factorial(n):
    if n<=2:
        return n
    return n*factorial(n-1)

def ex15():
    dim=20
    #The number of routes for a square grid (n×n) is the central binomial coefficient, which is (2n)!/(n!)**2.
    return factorial(dim*2)/(factorial(dim)**2)

print(ex15())
