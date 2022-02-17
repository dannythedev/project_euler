# Project Euler 6 - Sum square difference. Solved in 4.799999999999943e-05 seconds runtime.
# Exercise: https://projecteuler.net/problem=6

def ex6():
    lim, sum, squared_sum = 100, 0, 0
    for x in range(1,lim+1):
        sum+=x
        squared_sum+=(x*x)
    return (sum*sum)-squared_sum

print(ex6())
