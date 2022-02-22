# Project Euler 32 - Pandigital products. Solved in 1.680288 seconds runtime.
# Exercise: https://projecteuler.net/problem=32

def permute(s, i = 0,w=[]):
    if i == len(s):
        w+=["".join(s)]
    for j in range(i, len(s)):
        l = [c for c in s]
        l[i], l[j] = l[j], l[i]
        permute(l, i + 1,w)
    return w

def ex32():
    l=permute("123456789")
    s=set()
    for x in l:
        a,b,c,d,e=int(x[:2]),int(x[2:5]),int(x[5:]),int(x[:1]),int(x[1:5])
        if a*b==c:
            s.add(c)
        if d*e==c:
            s.add(c)
    return sum(s)

print(ex32())
