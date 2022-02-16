# Project Euler 357 - Prime generating integers, solved in  55.75 seconds runtime.
# Exercise: https://projecteuler.net/problem=357
# Synopsis: https://dannythedev.myportfolio.com/project-euler-exercise-357

import timeit
start = timeit.default_timer()

def range_of_search_siege_primes(n):
    sieve = [True] * (n+1)
    p=2
    ran1 = set()
    ran2 = set()
    while (p*p <=n): #Sieve to rule-out composite numbers.
        if (sieve[p]):
            for i in range(p*p, n+1, p):
                sieve[i] = False
        p+=1
    sieve[0]=False
    sieve[1]=False

    for p in range(n+1):
        if sieve[p]:
            if 2 * p - 4 <= n:
                ran1.add(2 * p - 4)
            ran2.add(p - 1)
    return sorted(ran1.intersection(ran2))

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    lim = int(n**0.5)+1
    for i in range(3, lim, 2):
        if n%i==0:
            return False
    return True

def divisors_of_n_prime(n):
    lim= int(n**0.5)+1
    for d in range(3,lim):
        if n%d==0:
            if not isPrime(d + (n/d)):
                return False
    return True

def ex357():
    sum=1
    pl = range_of_search_siege_primes(10**8)
    for n in pl:
        if divisors_of_n_prime(n):
            sum+=n
    return sum

print(ex357())

stop = timeit.default_timer()
print('Time: ', stop - start,"seconds.")
