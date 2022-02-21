# Project Euler 21, Amicable numbers. Solved in 0.298 seconds runtime.
# Exercise: https://projecteuler.net/problem=21

def sum_of_divisors(n):
    lim = int(n ** 0.5) + 1
    return sum([n,1]+[f for d in range(2,lim) for f in (d,n/d) if (n%d==0)])

def has_amicable_pair(n):
    d1 = sum_of_divisors(n)-n #Not including n itself.
    d2 = sum_of_divisors(d1)-d1 #Not including d1 itself.
    return d2==n and n!=d1

def ex21():
    sum=0
    for x in range(1,10000):
        if has_amicable_pair(x):
            sum+=x
    return sum

print(ex21())
