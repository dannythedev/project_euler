# Project Euler 4 - Largest palindrome product. Solved in 0.079 seconds runtime.
# Exercise: https://projecteuler.net/problem=4

def palindrome(min, max, l=[]):
    ran = range(min,max)
    digit = [str(d) for d in range(0, 10)]+['']
    for x in ran:
        s = str(x)
        l += [int(s + d + s[::-1]) for d in digit]
    return l

def prod(min,max):
    return set([p1*p2 for p1 in range(min,max) for p2 in range(min, p1)])

def ex4():
    t_min, t_max = 100, 1000
    return max(prod(t_min,t_max).intersection(palindrome(t_min, t_max)))
