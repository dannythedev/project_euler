# Project Euler 36 - Double-base palindromes. Solved in 0.0244 seconds runtime.
# Exercise: https://projecteuler.net/problem=36

#gets base 10 number, convers to base b and returns as str.
def int_to_base(n,b):
    if n==0:
        return 0
    digits=''
    s=''
    while n>0:
        s+=str(int(n%b))
        n//=b
    return s[::-1]

def palindrome_set(lim):
    pol,x = 0,1
    l = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    while pol <= lim:
        s = str(x)
        pol = int(s + s[::-1])
        x += 1
        l.add(pol)
        if pol * 10 <= lim:
            for d in range(0, 10):
                pol = int(s + str(d) + s[::-1])
                l.add(pol)
    return set(l)

def is_palindrome(n):
    n=str(n)
    for x in range(0,int(len(n)/2)):
        if n[x]!=n[len(n)-x-1]:
            return False
    return True

def ex36():
    p=palindrome_set(1000000)
    sum=0
    for x in p:
        if is_palindrome(int_to_base(x,2)):
            sum+=x
    return sum

print(ex36())
