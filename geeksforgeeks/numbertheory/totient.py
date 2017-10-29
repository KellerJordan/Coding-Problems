from math import gcd, sqrt, ceil

def simple(n):
    return sum(gcd(n, i) == 1 for i in range(1, n+1))

def totient(n):
    res = n
    p = 2
    while p*p <= n:
        if n % p == 0:
            res *= 1.0 - 1.0/p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        res *= 1.0 - 1.0/n
    return int(res)

print(list(map(totient, range(1, 10))))
