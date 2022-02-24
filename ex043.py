# Project Euler 43 - Sub-string divisibility. Solved in 19.0983 seconds runtime.
# Exercise: https://projecteuler.net/problem=43

def is_sub_string_divisibility(n):
    d = list(str(n))
    p = [2,3,5,7,11,13,17]
    for x in range(0,len(d)-3):
        if (int(d[x+1]+d[x+2]+d[x+3]))%p[x]:
            return False
    return True

def ex43():
    sum=0
    p = permute("0123456789")
    for x in p:
        if is_sub_string_divisibility(x):
            sum+=int(x)
    return sum

print(ex43())
