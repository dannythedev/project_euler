# Project Euler 44 - Pentagon numbers. Solved in 10.504 seconds runtime.
# Exercise: https://projecteuler.net/problem=44

def pentagonal_list(lim,l=[]):
    for x in range(1,lim):
        l.append(pentagonal_sequence(x))
    return l

def is_pentagonal(t):
    a,b=(1-(24*t+1)**0.5)/6, (1+(24*t+1)**0.5)/6
    return (a>0 and a%1==0) or (b>0 and b%1==0)

def pentagonal_pair_difference_and_sum(pj,pk):
    s=pj+pk
    d=abs(pj-pk)
    if is_pentagonal(s) and is_pentagonal(d):
        return d
    return -1

def ex44():
    p = pentagonal_list(10000)
    for pj in range(0,len(p)):
        for pk in range(pj+1,len(p)):
            a=pentagonal_pair_difference_and_sum(p[pj],p[pk])
            if a!=-1:
                return int(a)
    return -1

print(ex44())
