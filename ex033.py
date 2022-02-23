# Project Euler 33 - Digit cancelling fractions. Solved in 0.056185 seconds runtime.
# Exercise: https://projecteuler.net/problem=33

def is_curious_fraction(n,d):
    if n==d: return False
    if n%10==0 or d%10==0: return False
    n2,d2=str(n),str(d)
    l=[]
    for x in range(0,len(n2)):
        for y in range(0,len(d2)):
            if n2[x]==d2[y]:
                l.append((x,y))
    if len(l)==0: return False
    for c in l:
        n2 = n2[:c[0]] + n2[c[0] + 1:]
        d2 = d2[:c[1]] + d2[c[1] + 1:]
    if n2=='' or d2=='': return False
    return int(n2)/int(d2)==n/d

#gets fraction n/d, returns the simplified fraction.
def simplify(n,d):
    i=2
    m = min(n,d)+1
    while (i < m):
        if n%i==0 and d%i==0:
            n//=i
            d//=i
        else:
            i+=1
    return (n,d)

def ex33():
    c,prod_n,prod_d=0,1,1
    for n in range(10,100):
        for d in range(n,100):

            if is_curious_fraction(n,d):
                c+=1
                prod_n*=n
                prod_d*=d
            if c==4:
                return simplify(prod_n,prod_d)[1]

print(ex33())
