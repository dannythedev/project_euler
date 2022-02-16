# Project Euler 119 - Investigating multiple reflections of a laser beam, solved in  0.3842008 seconds runtime.
# Exercise: https://projecteuler.net/problem=119
# Synopsis: https://dannythedev.myportfolio.com/project-euler-exercise-119

import math
import timeit
start = timeit.default_timer()

def sum_of_digits(n):
    sum = 0
    while (n > 0):
        sum += n % 10
        n //= 10
    return sum

def digit_power_sum(n):
    sum = sum_of_digits(n)
    if sum == 1:
        return False
    if (n+sum)%2==1:
        return False
    if n%sum!=0:
        return False
    m = 2
    while(sum**m <= n):
        if sum**m == n:
            return True
        m+=1
    return False

def list_of_a_pow(a,lim):
    l = []
    x=1
    b=x**a
    while(lim>b):
        x+=1
        b = x**a
        l+=[b]
    return l

def union_of_pow_from_ran(lim,b,c):
    uni = set()
    for a in range(b,c+1):
        uni = uni.union(set(list_of_a_pow(a,lim)))
    return sorted(uni)

def ex119():
    lim = 10**15
    uni = union_of_pow_from_ran(lim,3,7)
    c=1
    for n in uni:
        if digit_power_sum(n):
            if c==30:
                return n
            c+=1

print(ex119())

stop = timeit.default_timer()
print('Time: ', stop - start,"seconds.")
