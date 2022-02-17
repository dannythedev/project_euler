# Project Euler 4 - Largest palindrome product. Solved in 0.169 seconds runtime.
# Exercise: https://projecteuler.net/problem=4

def palindrome_list(lim):
    pol,x = 0,1
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while pol <= lim:
        s = str(x)
        pol = int(s + s[::-1])
        x += 1
        l.append(pol)
        if pol * 10 <= lim:
            for d in range(0, 10):
                pol = int(s + str(d) + s[::-1])
                l.append(pol)
    return set(l)

def product_of_two():
    return set([p1*p2 for p1 in range(100,1000) for p2 in range(100,1000) if p1!=p2])
def ex4():
    return max(product_of_two().intersection(palindrome_list(1000**2)))
