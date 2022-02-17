# Project Euler 3 - Largest Prime Factor. Solved in 0.374 seconds runtime.
# Exercise: https://projecteuler.net/problem=3

def isPrime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True

def ex3():
    n = 600851475143
    lim = int(n ** 0.5) + 1
    return max([f for d in range(2, lim) for f in (d, int(n / d)) if n % d == 0 and isPrime(f)])

print(ex3())
