def answer(l):
    # using insertion sort
    # could rewrite using merge/quicksort but focus seems
    # to be on version comparison rather than efficiency

    # helper function to compare versions
    def lessthan(v1, v2):
        v1, v2 = [int(v) for v in v1.split('.')], [int(v) for v in v2.split('.')]
        if v1[0] != v2[0]:
            return v1[0] < v2[0]
        if len(v1) >= 2 and len(v2) >= 2:
            if v1[1] != v2[1]:
                return v1[1] < v2[1]
        else:
            return len(v1) < len(v2)
        if len(v1) == 3 and len(v2) == 3:
            # if they are equal will just return v2 as greater.
            return v1[2] < v2[2]
        else:
            return len(v1) < len(v2)

    # insertion sort using lessthan comparison function
    N = len(l)
    for i in range(N):
        min_v, min_i = l[i], i
        for j in range(i+1, N):
            if lessthan(l[j], min_v):
                min_v, min_i = l[j], j
        l[j], l[min_i] = l[min_i], l[i]

    return l
