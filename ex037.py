# Project Euler 37 - Truncatable primes. Solved in 0.38 seconds runtime.
# Exercise: https://projecteuler.net/problem=37

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

def is_trunctable_prime(n):
    s=str(n)
    k=len(s)-1
    s_right=s
    s_left=s
    #left
    for x in range(0,k):
        s_left,s_right = s_left[:-1], s_right[1:]
        if not (isPrime(int(s_left)) and isPrime(int(s_right))):
            return False
    return True

def ex37():
    sum=-(2+3+5+7) #single-digit primes don't count.
    p=prime_list(1000000)
    for x in p:
        if is_trunctable_prime(x):
            sum+=x
    return sum

print(ex37())
