# Project Euler 40 - Champernowne's constant. Solved in 0.091535 seconds runtime.
# Exercise: https://projecteuler.net/problem=40

def concatenate_positive_integers(lim):
    s,i='',1
    while(True):
        s+=str(i)
        if len(s)+1>lim: return s[:lim]
        i+=1

def ex40():
    d=concatenate_positive_integers(1000000)
    return int(d[0])*int(d[9])*int(d[99])*int(d[999])*int(d[9999])*int(d[99999])*int(d[999999])
