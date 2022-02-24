# Project Euler 42 - Coded triangle numbers. Solved in 0.008558 seconds runtime.
# Exercise: https://projecteuler.net/problem=42

def read_words():
    f = open("words.txt", "r")
    a = f.readlines()
    a[0]=a[0].replace('"','')
    a=a[0].split(',')
    f.close()
    return a

def is_in_triangle_sequence(tn):
    a=0.5*(-math.sqrt((8*tn+1))-1)
    b=0.5*(math.sqrt((8*tn+1))-1)
    if (a%1==0 and a>0) or (b%1==0 and b>0):
        return True
    return False

def word_to_num_sum(w,sum=0):
    for x in w:
        sum+=ord(x)-64
    return sum

def ex42():
    c=0
    w=read_words()
    for x in w:
        if is_in_triangle_sequence(word_to_num_sum(x)):
            c+=1
    return c

print(ex42())
