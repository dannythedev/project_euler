# Project Euler 39 - Integer right triangles, solved in 0.162483 seconds runtime.
# Exercise: https://projecteuler.net/problem=39
# Synopsis: https://dannythedev.myportfolio.com/project-euler-exercise-39

def find_solutions_right_triangle_by_perimeter(p):
    c,l=0,[]
    for a in range(1,p):
        b = p*(p-2*a)/(2*(p-a))
        if b%1==0 and b>0:
            if (b,a) not in l:
                l.append((a,b))
                c+=1
    return c

def ex39():
    max_p,max=0,0
    for p in range(1,1000):
        s=find_solutions_right_triangle_by_perimeter(p)
        if s>max:
            max_p,max=p,s
    return max_p

print(ex39())
