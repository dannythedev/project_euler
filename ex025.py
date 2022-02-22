# Project Euler 25 - 1000-digit Fibonacci number. Solved in 0.0518 seconds runtime.
# Exercise: https://projecteuler.net/problem=25

#returns the first fibonacci number with 1000-digits.
def ex25():
    l=[0,1,2]
    n,p,sum = 0,3,2
    while (True):
        n=l[p-1]+l[p-2]
        l.append(n)
        if (len(str(n)) == 1000):
            return p+1
        p+=1
    return -1

print(ex25())
