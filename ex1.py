# Project Euler 1 - Multiples of 3 or 5.
# Exercise: https://projecteuler.net/problem=1

import timeit
start = timeit.default_timer()

def ex1():
    sum=0
    for x in range(1,1000):
        if x%3==0 or x%5==0:
            sum+=x
    return sum
print(ex1())

stop = timeit.default_timer()
print('Time: ', stop - start,"seconds.")
