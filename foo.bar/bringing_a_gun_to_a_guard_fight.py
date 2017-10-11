def answer(dimensions, captain_position, badguy_position, distance):
    # things that could make this faster if I had more time:
    # * iterative over a circle in reflection-space rather than square
    # * check in order of distance to avoid having to do min(D[b], l)
    # * maybe some linear algebra method to get a closed formula ....

    from fractions import gcd
    w, h, cx, cy = dimensions+captain_position

    # insbearing():
    # 1. compute bearing b to reflection-space ij, position P
    # 2. check if within distance, if not do nothing
    # 3. set D[b] to the new least number of repetitions of b to reach position P
    def insbearing(ij, P, D):
        i, j, px, py = ij + P
        x = w*i + (w - px if i%2 else px) - cx
        y = h*j + (h - py if j%2 else py) - cy
        norm2 = x**2 + y**2
        if 0 < norm2 and norm2 <= distance**2:
            l = abs(gcd(x, y))
            b = (x//l, y//l) # bearing (tuple in order to use as index)
            D[b] = min(D[b], l) if b in D else l

    B, C = {}, {} # bearings to hit badguy, captain
    xmax, ymax = distance//w + 2, distance//h + 2
    for i in range(-xmax, xmax):
        for j in range(-ymax, ymax):
            insbearing([i, j], badguy_position, B)
            insbearing([i, j], captain_position, C)

    # return total number of ways to reach badguy that dont hit captain first
    return sum(bv not in C or B[bv] < C[bv] for bv in B)

# inpt = [[3, 2], [1, 1], [2, 1], 4]
inpt = [[300, 275], [150, 150], [185, 100], 500]

print(answer(*inpt))
