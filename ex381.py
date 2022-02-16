# Project Euler 381 - (prime-k) factorial, solved in  35.43 seconds runtime.
# Exercise: https://projecteuler.net/problem=381
# Synopsis: https://dannythedev.myportfolio.com/project-euler-exercise-381

import timeit
start = timeit.default_timer()

def primes_list(n):
    l = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            l+=[p]
            for i in range(p, n+1, p):
                sieve[i] = False
    return l

def ex381():
    lim = 10 ** 8
    p = primes_list(lim)[2:]
    sum=0
    for x in range(0,len(p)):
        a = pow((-24), -1, p[x])
        sum+=(a*9)%p[x]
    return sum

print(ex381())

stop = timeit.default_timer()
print('Time: ', stop - start,"seconds.")
