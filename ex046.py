# Project Euler 46 - Goldbach's other conjecture. Solved in 0.67324 seconds runtime.
# Exercise: https://projecteuler.net/problem=46

def prime_and_composite_list(n):
    sieve = [True] * (n+1)
    p=2
    pri, com = [],[]
    while (p*p <=n):
        if (sieve[p]):
            for i in range(p*p, n+1, p):
                sieve[i] = False
        p+=1
    sieve[0],sieve[1]=False,False
    for p in range(2,n+1):
        if sieve[p]:
            pri.append(p)
        else:
            com.append(p)
    return (pri,com)

def ex46():
    l,lim=[],6000
    primes_list = prime_and_composite_list(lim)[0][1:] #since a=p+2*(n^2) must be odd, then so does p. 2 is removed from the list of primes.
    odd_composites_list = set(prime_and_composite_list(lim)[1]).intersection(set(range(3,lim,2))) #1 is not a composite number.
    for p in primes_list:
        for n in range(1, p):
            l.append(p+2*(n * n))
    return min(odd_composites_list.difference(set(l)))

print(ex46())
