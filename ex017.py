# Project Euler 17 - Number letter counts. Solved in 0.00403 seconds runtime.
# Exercise: https://projecteuler.net/problem=17

def num_to_words(n):
    word,c,s = "",str(n),0
    u = {0: "",1: "one",2: "two",3: "three",4: "four", 5:"five",6: "six",7: "seven",8: "eight",9: "nine"}
    e = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    t = {0: "", 1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    while len(s)>0:
        if len(s)==1: word+=u[int(s[c])]
        elif len(s)==2:
            if n>100 and str(n)[-2:]!="00":
                word+="and"
            if s[0]=="1" and s[1]!="0":
                word+=e[int(s)]
                break
            else:
                word += t[int(s[c])]
        elif len(s)==3: word+=u[int(s[c])]+"hundred"
        elif len(s)==4: word+=u[int(s[c])]+"thousand"
        s = s[1:]
        if s.count('0')==len(s):
            break
    return word

def ex17():
    sum=0
    for x in range(1,1001):
        sum+=len(num_to_words(x))
    return sum

print(ex17())
