# Project Euler 28, Number spiral diagonals. Solved in 0.01495 seconds runtime.
# Exercise: https://projecteuler.net/problem=28

#returns the amount of cells in a n×n spiral. n is odd.
def spiral(n,sum=0):
    if n==1: return 1
    return (n)*2+(n-2)*2+spiral(n-2,sum)

def ex28():
    n=1001
    lim=spiral(n)
    c,sum,x,c2= 0,1,1,4
    while(x<lim):
        if c2%4==0:
            c+=2
        x+=c
        sum+=x
        c2+=1
    return sum

print(ex28())
