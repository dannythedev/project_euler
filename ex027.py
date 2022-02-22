# Project Euler 27 - Quadratic primes. Solved in 0.95865 seconds runtime.
# Exercise: https://projecteuler.net/problem=27

# sieve of erathostenes, returns list of all primes under n.
def prime_list(n):
    sieve = [True] * (n+1)
    p=2
    ran = set()
    while (p*p <=n):
        if (sieve[p]):
            for i in range(p*p, n+1, p):
                sieve[i] = False
        p+=1
    sieve[0],sieve[1]=False,False
    for p in range(n+1):
        if sieve[p]:
            ran.add(p)
    return sorted(ran)

# returns true if prime, else false.
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    lim = int(n**0.5)+1
    for i in range(3, lim, 2):   # only odd numbers
        if n%i==0: return False
    return True

# b must be a positive integer and a prime number since for each n=0 there must be n^2+n+b = b = prime.
def ex27():
    max_c,max = 0,0
    pl=prime_list(1000) #since be must be >1000.
    for a in range(-1000,1000):
        for b in pl:
            n=0
            while (isPrime(n**2+a*n+b)):
                    n+=1
            if max < n:
                max = n
                max_c = a * b
    return (max_c)

print(ex27())
