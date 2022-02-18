# Project Euler 10, Summation of primes. Solved in 0.3604757 seconds runtime.
# Exercise: https://projecteuler.net/problem=10

def ex10():
    sum,p,n=0,2,2000000
    sieve = [True] * (n+1)
    while (p*p <=n):
        if (sieve[p]):
            for i in range(p*p, n+1, p):
                sieve[i] = False
        p+=1
    sieve[0],sieve[1]=False,False
    for p in range(n+1):
        if sieve[p]:
            sum+=p
    return sum

print(ex10())
