# Project Euler 14, Longest Collatz sequence. Solved in 15.3693 seconds runtime.
# Exercise: https://projecteuler.net/problem=14

def collatz_sequence(n):
    c=1
    while (n!=1):
        if n%2==0: n/=2
        else: n = 3*n+1
        c+=1
    return c

def ex14():
    max_n,max=0,0
    for n in range(1,1000000,2):
        #We can iterate only over odd numbers since even numbers produce smaller chains.
        m = collatz_sequence(n)
        if m > max:
            max_n,max=n,m
    return max_n

print(ex14())
