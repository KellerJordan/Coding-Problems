def answer(num_buns, num_required):
    # give each combination of num_buns-num_required+1 bunnies a unique key
    # that way if you miss even one combination by selecting num_required-1,
    # you will miss that key

    bunarr = [[] for _ in range(num_buns)]
    currkey = 0
    # using itertools feels almost like cheating!
    from itertools import combinations
    for combo in combinations(list(range(num_buns)), num_buns-num_required+1):
        for i in combo:
            bunarr[i].append(currkey)
        currkey += 1
    return bunarr

inpt = [5, 3]
print(answer(*inpt))
