# Project Euler 145 - How many reversible numbers are there below one-billion?, solved in  57.67 seconds runtime.
# Exercise: https://projecteuler.net/problem=145

import math
import timeit
start = timeit.default_timer()

def is_odd_digits(x):
    while(x>0):
        if (x%10)%2==0:
            return False
        x//=10
    return True

def ex145(lim):
    c=0
    n=12
    while(n<lim):
        if n%10!=0:
            y = int(str(n)[::-1])
            if is_odd_digits(n+y):
                c+=2
        else:
            if (int(math.log(n,10))+1) % 4 == 1:
                n*=10
        n+=2
    return c

print(ex145(10**9))

stop = timeit.default_timer()
print('Time: ', stop - start,"seconds.")
