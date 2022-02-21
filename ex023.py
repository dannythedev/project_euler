# Project Euler 23, Non-abundant sums. Solved in 6.384 seconds runtime.
# Exercise: https://projecteuler.net/problem=23

#true if sum of proper divisors for n is above n.
def is_abudant_number(n):
    lim = int(n ** 0.5) + 1
    return n<sum(set([1]+[f for d in range(2,lim) for f in (d,n/d) if (n%d==0)]))

def list_of_abudant_numbers():
    l=[]
    for x in range(1,28123): #upper lim given in exercise.
        if is_abudant_number(x):
            l.append(x)
    return l

def ex23():
    l=list_of_abudant_numbers()
    s=set() #set of all abudant numbers.
    for x in l:
        for y in l:
            s.add(x+y)
    u=set(range(1,28123)) #u is set of all numbers below lim given in exercise.
    return sum(u.difference(s)) #return difference.

print(ex23())
