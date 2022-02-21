# Project Euler 22, Highly divisible triangular number. Solved in 0.15628 seconds runtime.
# Exercise: https://projecteuler.net/problem=22

#Reads names.txt in the same directory, returns sorted list of said names.
def read_names():
    f = open("names.txt", "r")
    a = f.readlines()
    a[0]=a[0].replace('"','')
    a=sorted(a[0].split(','))
    f.close()
    return a

def ex22():
    s=read_names()
    total,sum=0,0
    for x in range(0,len(s)):
        sum=0
        for y in s[x]:
            sum+=ord(y)-64
        print(s[x],sum,x+1)
        total+=sum*(x+1)
    return total

print(ex22())
