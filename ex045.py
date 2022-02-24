# Project Euler 45 - Triangular, pentagonal, and hexagonal. Solved in 0.05842 seconds runtime.
# Exercise: https://projecteuler.net/problem=45

def ex45():
    t,p,h=set(),set(),set()
    for n in range(1,60000):
        tn,pn,hn= n*(n+1)/2, n*(3*n-1)/2, n*(2*n-1)
        t.add(tn)
        p.add(pn)
        h.add(hn)
    return list(t.intersection(p.intersection(h)))[-1]
