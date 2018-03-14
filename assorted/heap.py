# simple binary min-heap implementation in python

import numpy as np

class MinHeap:

    def __init__(self, arr=None):
        if arr is not None:
            self.arr = list(arr)
            self.size = len(self.arr)
            i = self.size//2
            while i >= 0:
                self.percdown(i)
                i -= 1
        else:
            self.arr = []
            self.size = 0

    def insert(self, val):
        self.arr.append(val)
        self.size += 1
        self.percup(self.size-1)

    def percup(self, i):
        v = self.arr[i]
        while v < self.arr[(i+1)//2-1] and i > 0:
            j = (i+1)//2-1
            self.arr[i], self.arr[j] = self.arr[j], v
            i = j

    def percdown(self, i):
        v = self.arr[i]
        j = 0
        while i*2 < self.size:
            j = 2*i+1
            if j+1 < self.size:
                j = j+1 if self.arr[j+1] < self.arr[j] else j
            if j < self.size and v > self.arr[j]:
                self.arr[i], self.arr[j] = self.arr[j], v
            else:
                break
            i = j

    def deltop(self):
        ret = self.arr[0]
        self.size -= 1
        if self.size > 1:
            self.arr[0] = self.arr.pop(-1)
            self.percdown(0)
        return ret

    def __repr__(self):
        return repr(self.arr)


## method one
mheap = MinHeap()
for i in np.random.randint(15, size=15):
    mheap.insert(i)
## method two
# mheap = MinHeap(np.random.randint(15, size=15))

print(mheap)

arr = []
while mheap.size:
    arr.append(mheap.deltop())
print(arr)
