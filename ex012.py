# Project Euler 12, Highly divisible triangular number. Solved in 3.46412 seconds runtime.
# Exercise: https://projecteuler.net/problem=12

def num_of_divisors(n):
    lim = int(n ** 0.5) + 1
    sum=2 #n and 1
    for d in range(2,lim):
        if n%d==0:
            if d == n/d: sum+=1
            else: sum+=2
    return sum

def ex12():
    c,tri=0,0
    while(num_of_divisors(tri)<500):
        tri+=c
        c+=1
    return tri

print(ex12())
