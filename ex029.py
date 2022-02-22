# Project Euler 29, Distinct powers. Solved in 0.033845 seconds runtime.
# Exercise: https://projecteuler.net/problem=29

def power_combinations(i,s,l=[]):
    for a in range(i,s+1):
        for b in range(i,s+1):
            l.append(a**b)
            l.append(b**a)
    return len(set(l))

def ex29():
    return power_combinations(2,100)

print(ex29())
