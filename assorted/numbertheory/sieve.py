def sieve():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for d in D[q]:
                D.setdefault(q+d, [])
                D[q+d].append(d)
        q += 1

def verify(n):
    for q in range(2, int(n**0.5) + 1):
        if n % q == 0:
            return False
    return True

eratos = sieve()
print([next(eratos) for _ in range(100)])
print(all(map(verify, [next(eratos) for _ in range(10000)])))
