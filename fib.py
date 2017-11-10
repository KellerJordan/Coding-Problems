import numpy as np

# fast fibonacci - returns nth number
def f(n):
    if n < 1: return None
    if n == 1: return 0
    n -= 2
    M = np.array([[1,1],[1,0]], dtype=np.uint64)
    P = [M] # list of 2^ith power
    for _ in range(int(np.log2(n+1))):
        M = M @ M
        P.append(M)
    res = np.eye(2, dtype=np.uint64)
    powers = [i for i, p in enumerate(bin(n)[:1:-1]) if p == '1']
    for i in powers:
        res = res @ P[i]
    return res[0][0]

print(f(84))
