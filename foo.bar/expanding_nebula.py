def answer(g):
    # convert to integers representing grid as bits
    bcols = [int(''.join(map(str, map(int, col))), 2) for col in zip(*g)]

    # bitwise test that tcol results from time step on [pcol, ncol]
    mask = (1<<len(g)) - 1
    def valid(pcol, ncol, tcol):
        cxor, cand = pcol ^ ncol, pcol & ncol
        res = ((cxor&mask) ^ (cxor>>1)) & ~((cand&mask) | (cand>>1))
        return res == tcol

    # iterate over columns generating every possibility, sum over prev possibilities
    maxcol = 1<<(len(g)+1) # 100...00 (len(g) 0s)
    pcols = {col: 1 for col in range(maxcol)}
    for tcol in bcols:
        ncols = {
            ncol: sum(pcols[pcol] for pcol in pcols if valid(pcol, ncol, tcol))
            for ncol in range(maxcol)}
        pcols = {col: ncols[col] for col in ncols if ncols[col] > 0}

    # return the sum of ways to arrive at each last column
    return sum(pcols.values())

# inpt = [
# [1,0,1],
# [0,1,0],
# [1,0,1]]
# inpt = [
# [1,0,1,0,0,1,1,1],
# [1,0,1,0,0,0,1,0],
# [1,1,1,0,0,0,1,0],
# [1,0,1,0,0,0,1,0],
# [1,0,1,0,0,1,1,1]]
inpt = [
[1,1,0,1,0,1,0,1,1,0],
[1,1,0,0,0,0,1,1,1,0],
[1,1,0,0,0,0,0,0,0,1],
[0,1,0,0,0,0,1,1,0,0]]
print(answer(inpt))
