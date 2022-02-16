# Project Euler 387 - Harshad Numbers, solved in 9.8469988 seconds runtime.
# Exercise: https://projecteuler.net/problem=387
# Synopsis: https://dannythedev.myportfolio.com/project-euler-exercise-387

import timeit
start = timeit.default_timer()

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False
    return True

def sumOfDigits(n):
    s = 0
    while n>0:
        s += n % 10
        n//=10
    return s

def isHarshad(n):
    return n%sumOfDigits(n)==0

def isStrongHarshad(n):
    sum=sumOfDigits(n)
    if n%sum==0:
        return isPrime(n/sum)
    return False

def rightTrunctableHarshadList(l,n,lim):
    if n > lim:
        return l
    if isHarshad(n):
        return [n]+rightTrunctableHarshadList(l,n*10 + 0,lim) + rightTrunctableHarshadList(l,n*10 + 1,lim) + \
               rightTrunctableHarshadList(l, n * 10 + 2, lim) + rightTrunctableHarshadList(l, n * 10 + 3, lim) +\
        rightTrunctableHarshadList(l,n*10 + 4,lim) + rightTrunctableHarshadList(l,n*10 + 5,lim) + \
        rightTrunctableHarshadList(l, n * 10 + 6, lim) + rightTrunctableHarshadList(l, n * 10 + 7, lim) + \
        rightTrunctableHarshadList(l, n * 10 + 8, lim) + rightTrunctableHarshadList(l, n * 10 + 9, lim)
    return l

def RightTrunctubleList(lim):
    #All digits.
    l = rightTrunctableHarshadList([],1,lim)+rightTrunctableHarshadList([],2,lim)+\
                           rightTrunctableHarshadList([],3,lim)+rightTrunctableHarshadList([],4,lim)+\
                           rightTrunctableHarshadList([],5,lim)+rightTrunctableHarshadList([],6,lim)+\
                           rightTrunctableHarshadList([],7,lim)+rightTrunctableHarshadList([],8,lim)+\
                           rightTrunctableHarshadList([],9,lim)
    return l

def ex367():
    l = RightTrunctubleList(10**13)

    sum = 0
    d = [1,3,7,9]  #Anything that ends with any even-digit or 5 is surely divisible.
    for x in l:
        if not isStrongHarshad(x):
            continue
        for n in d:
            a = x*10 + n
            if isPrime(a):
                sum+=a
    return sum

print(ex367())

stop = timeit.default_timer()
print('Time: ', stop - start,"seconds.")
