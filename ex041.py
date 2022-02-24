# Project Euler 41 - Pandigital prime. Solved in 4.5208 seconds runtime.
# Exercise: https://projecteuler.net/problem=41

def is_pandigital(n,l=[]):
    for x in range(1,len(str(n))+1):
        l+=[str(x)]
    return sorted(list(str(n)))==l

def ex41():
    max=0
    p = prime_list(10000000)
    for x in p:
        if is_pandigital(x):
            if x>max:
                max=x
    return max

print(ex41())
