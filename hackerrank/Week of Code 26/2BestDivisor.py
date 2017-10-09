from math import sqrt

def divgen(n):
    d = 1
    while d < sqrt(n):
        if n % d == 0:
            yield d
            yield n // d
        d += 1

def sumdig(n):
    s = 0
    for c in str(n):
        s += int(c)
    return s

n = int(input().strip())
m = 0
b = 1
for d in list(divgen(n)):
    r = sumdig(d)
    if r > m or (r == m and d < b):
        m, b = r, d
print(b)
