# Project Euler 38 - Pandigital multiples. Solved in 0.03891 seconds runtime.
# Exercise: https://projecteuler.net/problem=38

def is_1to9_pandigital(n):
    s,c,p='',1,1
    while(int(s+str(n*c))<=987654321):
        prod=n*c
        s+=str(prod)
        c+=1
    if sorted(list(s))==['1','2','3','4','5','6','7','8','9']:
        return int(s)
    return -1

def ex38():
    max=0
    for x in range(1,9999):
        a=is_1to9_pandigital(x)
        if a>max:
            max=a
    return max

print(ex38())
