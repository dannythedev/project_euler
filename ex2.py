# Project Euler 2 - Multiples of 3 or 5. Solved in 6.989999999999774e-05 seconds runtime.
# Exercise: https://projecteuler.net/problem=2

import timeit
start = timeit.default_timer()

def ex2():
    l=[0,1,2]
    n,p,sum = 0,3,2
    while (True):
        n=l[p-1]+l[p-2]
        if (n<4000000):
            l.append(n)
            if n%2==0:
                sum+=n
        else:
            return sum
        p+=1
    return 0

print(ex2())
stop = timeit.default_timer()
print('Time: ', stop - start,"seconds.")