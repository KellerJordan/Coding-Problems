def segsieve(N):
    P = [True]*(N+1)
    q = 2
    while q <= N:
        if P[q]:
            yield q
            d = q+q
            while d <= N:
                P[d] = False
                d += q
        q += 1

def verify(n):
    for q in range(2, int(n**0.5) + 1):
        if n % q == 0:
            return False
    return True

eratos = segsieve(100)
print(list(eratos))
print(all(map(verify, list(eratos))))
