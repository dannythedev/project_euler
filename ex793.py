#Work in progress.

def s(n,c=0):
    i=290797
    yield i
    while (c<n):
        i = (i ** 2) % 50515093
        c+=1
        yield i

def m_seq(lim):
    a = list(s(lim))
    return [(a[i]*a[j], i, j) for i in range(0, lim) for j in range(i + 1, lim)]


# def size(n):
#     return sum([x for x in range(0, n)])

def ex793(n):
    m = m_seq(n)
    return sorted(m, key=lambda tup: tup[0])[len(m)//2]

print(ex793(103))
