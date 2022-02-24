# Project Euler 47 - Distinct primes factors, solved in 3.61926 seconds runtime.
# Exercise: https://projecteuler.net/problem=47

def distinct_primes(n,p):
    lim=(n**(2/3))+5
    c=0
    for x in p:
        if n%x==0:
            c+=1
        if x>lim:
            return c

def ex47():
    lim=999999
    p=prime_list(lim)
    c,temp=0,0
    for x in range(1,lim):
        n=distinct_primes(x,p)
        if n==4 and temp==4:
            c+=1
            if c == 3:
                return x-3
        else:
            c=0
        temp=n
        
print(ex47())
