# Project Euler 5 - Smallest multiple. Solved in 24.942207 seconds runtime.
# Exercise: https://projecteuler.net/problem=5

def is_evenly_divisible(n,l):
    for x in l:
        if n%x!=0: return False
    return True

def ex5():
    c,lim=20,20
    ran = range(int(lim/2),lim+1) #If n is divided by the latter half of range, it is divided by the former as-well.
    while(True):
        if is_evenly_divisible(c,ran): return c
        c+=2
    return 0

print(ex5())
