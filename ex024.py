# Project Euler 24, Lexicographic permutations. Solved in 611.067 seconds runtime.
# Exercise: https://projecteuler.net/problem=24

def permute(s, i = 0,w=[]):
    if i == len(s):
        w+=["".join(s)]
    for j in range(i, len(s)):
        l = [c for c in s]
        l[i], l[j] = l[j], l[i]
        permute(l, i + 1,w)
    return w

def ex24():
    return sorted(permute("0123456789"))[999999]

print(ex24())
