def answer(xs):
    # if there is only one element, return it
    if len(xs) == 1:
        return str(xs[0])

    nonzero = [x for x in xs if x != 0]

    # if there are non nonzero elements or just one negative then return 0
    if len(nonzero) == 0 or (len(nonzero) == 1 and nonzero[0] < 1):
        return str(0)

    product = 1
    for x in nonzero:
        product *= x

    # if the product is positive, return it
    if product > 0:
        return str(product)
    # if the product is negative, divide by largest negative number
    else:
        max_neg = max([x for x in nonzero if x < 0])
        return str(product // max_neg)


xs = [0, -1000, 1, 0, 0]
print(answer(xs))
