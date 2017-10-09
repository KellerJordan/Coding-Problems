def answer(n):
    # decorator to enable memoization
    def dyn_dec(f):
        R = {} # results
        def dyn_wrap(*args):
            sarg = str(args)
            if sarg not in R:
                R[sarg] = f(*args)
            return R[sarg]
        return dyn_wrap

    # r: remaining bricks left, l: length of remaining sequence
    @dyn_dec
    def combos(r, l):
        if l == 1:
            return 1
        count = 0
        v = 0 # the first value of the remainder of the sequence
        while v*l <= r:
            # since all further values must be greater than or equal to v,
            # subtract v times length
            count += combos(r-v*l, l-1)
            v += 1
        return count

    count = 0
    # 20 is the highest possible length for staircases of 200 or fewer bricks
    for l in range(2, 20):
        # by subtracting the staircase made of increasing each height by 1,
        # the problem is transformed into finding a sequence which either increases
        # or stays the same. easier to work with
        r = n - l*(l+1)//2
        count += combos(r, l)

    return count

N = 200
print(answer(N))
