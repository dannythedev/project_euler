# Project Euler 125 - Palindromic sums, solved in  4.605 seconds runtime.
# Exercise: https://projecteuler.net/problem=125
# Synopsis: https://dannythedev.myportfolio.com/project-euler-exercise-125

import timeit
start = timeit.default_timer()

def palindrome_list(lim):
    pol = 0
    x=1
    l=[1,2,3,4,5,6,7,8,9]
    while pol<=lim:
        s = str(x)
        pol = int(s + s[::-1])
        x+=1
        l.append(pol)
        if pol*10<=lim:
            for d in range(0,10):
                pol = int(s +str(d)+ s[::-1])
                l.append(pol)
    return l

def sqaured_list(lim):
    l=[0]
    a=1
    while(a*a <= lim):
        l.append(a*a)
        a+=1
    return l

def consecutive_pow(lim):
    s = sqaured_list(lim)
    c = []
    a_lim = int(lim**0.5)
    for x in range(1,a_lim):
        sum=0
        for y in range(x,a_lim):
            sum+=s[y]
            if sum>lim:
                continue
            #t.update(x,y,sum)
            c.append(sum)
    return set(c).difference(s)

def ex125():
    lim = 10**8
    a = set(palindrome_list(lim))
    b = set(consecutive_pow(lim))
    s = a.intersection(b)
    sum=0
    for x in s:
        sum+=x
    return sum

print(ex125())

stop = timeit.default_timer()
print('Time: ', stop - start,"seconds.")
