def answer(M, F):
    # if m>f, the only preceding step is m-f, f. if f>m, then m, f-m.
    # the only step preceding m=f is 0, f or m, 0 -- both are impossible.
    # without loss of generality, if m>f then necessarily there preceded
    # only mach bomb generating steps until 0<m<f. this included
    # (m-1)//f steps, and results in m=(m-1)%f + 1.
    m, f = int(M), int(F)
    steps = 0
    while m > 1 or f > 1:
        if m > f:
            steps += (m-1) // f
            m = (m-1) % f + 1
        elif f > m:
            steps += (f-1) // m
            f = (f-1) % m + 1
        else:
            return "impossible"
    return str(steps)

print(answer(100, 1))
print(answer(7, 4))
print(answer(12, 2))
