import sys
import numpy as np


def merge(arr):
    if len(arr) <= 1: return arr
    m = len(arr)//2
    left = merge(arr[:m])
    right = merge(arr[m:])
    i = j = 0
    new = []
    while i < m or j < len(right):
        if (i < m and j < len(right) and left[i] > right[j]) or i == m:
            new.append(right[j])
            j += 1
        else:
            new.append(left[i])
            i += 1
    return new

def quick(arr):
    def partition(a, b):
        if b-a <= 1: return
        pi, pv = a, arr[b-1]
        for i in range(a, b):
            if arr[i] <= pv:
                arr[i], arr[pi] = arr[pi], arr[i]
                pi += 1
        partition(a, pi-1)
        partition(pi, b)

    partition(0, len(arr))
    return arr

def insertion(arr):
    for i in range(len(arr)):
        mini, minv = i, arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < minv:
                mini, minv = j, arr[j]
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr

def bubble(arr):
    for _ in range(len(arr)-1):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('options: merge, quick, insertion, bubble')
    else:
        arr = list(np.random.randint(10, size=(10,)))
        print(arr)
        arr = globals()[sys.argv[1]](arr)
        print(arr)
