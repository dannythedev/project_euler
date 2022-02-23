# Project Euler 35, Circular primes. Solved in 2.757 seconds runtime.
# Exercise: https://projecteuler.net/problem=35

def isPrime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True

def rotation(s):
    l=[s]
    for i in range(1,len(s)):
        s2 = ''
        for j in range(0,len(s)):
            s2+=s[(i+j)%(len(s))]
        l.append(s2)
    return l

def is_circular_prime(n):
    l=rotation(str(n))
    for x in l:
        if not isPrime(int(x)):
            return False
    return True

def ex35():
    pl = prime_list(1000000)
    c=0
    for x in pl:
        if is_circular_prime(x):
            c+=1
    return c

print(ex35())
