# Project Euler 2 - Even Fibonacci numbers. Solved in 4.22e-05 seconds runtime.
# Exercise: https://projecteuler.net/problem=2

# 08/07/22 - current solution, Solved in 4.22e-05 seconds runtime. If lim=10*10000 then runtime becomes 0.550152 seconds.
def fib(lim=4000000):
    n1,n2=0,1
    yield n1
    yield n2
    yield n1+n2
    while (n1+n2<lim):
        n1, n2 = n2, n1+n2
        yield n1+n2 if (n1+n2)%2==0 else 0

def ex2():
    a = fib()
    return sum(a)

print(ex2())

# 17/02/22 - old solution, Solved in 6.06e-05 seconds runtime. If lim=10*410000 then runtime becomes 7.97301623 seconds.
def ex2(lim=4000000):
    l=[0,1,2]
    n,p,sum = 0,3,2
    while (n<lim):
        n=l[p-1]+l[p-2]
        l.append(n)
        if n%2==0:
            sum+=n
        p+=1
    return sum

print(ex2())
