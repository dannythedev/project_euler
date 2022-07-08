#Work in progress.

def s(n,c=0):
    i=290797
    yield i
    while (c<n):
        i = (i ** 2) % 50515093
        c+=1
        yield i

def size(n):
    return sum([x for x in range(0,n)])

def m(n):
    a = list(s(n-1))
    for i in range(n):
        for j in range(i + 1, n):
            yield a[i]*a[j]

def ex793(n):
    a = sorted(m(n))
    return next(itertools.islice(a, int(size(n)/2), None))
