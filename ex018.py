# Project Euler 18, Maximum path sum I. Solved in 0.024758 seconds runtime.
# Exercise: https://projecteuler.net/problem=18

def str_to_grid(d):
    g = d.split("\n")
    for x in range(0,len(g)):
        g[x]=g[x].split(" ")
    for x in range(0,len(g)):
        for y in range(0,len(g[x])):
            g[x][y] = int(g[x][y])
    return g

#pyramid as input, outputs list of sums all possible routes.
def adj(l,g,x,y,sum):
    if x==len(g)-1: return [sum]
    return adj(l,g,x+1,y,sum+g[x+1][y]) + adj(l,g,x+1,y+1,sum+g[x+1][y+1])

def ex18():
    d = "75\n" +\
         "95 64\n" +\
         "17 47 82\n" +\
         "18 35 87 10\n" +\
         "20 04 82 47 65\n" +\
         "19 01 23 75 03 34\n" +\
         "88 02 77 73 07 63 67\n" +\
         "99 65 04 28 06 16 70 92\n" +\
         "41 41 26 56 83 40 80 70 33\n" +\
         "41 48 72 33 47 32 37 16 94 29\n" +\
         "53 71 44 65 25 43 91 52 97 51 14\n" +\
         "70 11 33 28 77 73 17 78 39 68 17 57\n" +\
         "91 71 52 38 17 14 91 43 58 50 27 29 48\n" +\
         "63 66 04 68 89 53 67 30 73 16 69 87 40 31\n" +\
         "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
    g = str_to_grid(d)
    return max(adj([],g,0,0,g[0][0]))

print(ex18())
