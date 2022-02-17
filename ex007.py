# Project Euler 7 - 10001st prime. Solved in 0.0178 seconds runtime.
# Exercise: https://projecteuler.net/problem=7

def ex7():
    # Prime number theorem suggests that number of primes below x, (lim) equals to n/ln(n),
    # then we isolate n and we get -W(1/-lim)*lim. W is for Lambert's W function.
    # For lim=10001, n = -W(1/-10001)*10001 equals approximately 116683.
    lim,n = 10001,116683 
    sieve = [True] * (n+1)
    p=2
    ran = set()
    while (p*p <=n): #Sieve to rule-out composite numbers.
        if (sieve[p]):
            for i in range(p*p, n+1, p):
                sieve[i] = False
        p+=1
    sieve[0],sieve[1]=False,False
    c=0
    for p in range(n+1):
        if sieve[p]:
            ran.add(p)
            c+=1
            if c >= lim:
                return p
    return -1

print(ex7())
