# simple python hash table implementation with linkedlist collision resolution

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None]*capacity

    def insert(self, key, val):
        pos = hash(key) % self.capacity
        node = Node(key, val)
        curr = self.arr[pos]
        if curr is None:
            self.arr[pos] = node
        else:
            while curr.next:
                curr = curr.next
            curr.next = node
        self.size += 1

    def remove(self, key):
        pos = hash(key) % self.capacity
        curr = self.arr[pos]
        if curr.key == key:
            self.arr[pos] = curr.next
        else:
            prev = None
            while curr.key != key:
                prev = curr
                curr = curr.next
        self.size -= 1

    def get(self, key):
        pos = hash(key) % self.capacity
        curr = self.arr[pos]
        while curr.key != key:
            curr = curr.next
        return curr.val

    def length(self):
        return self.size


htable = HashTable()
htable.insert('abc', 'def')
print(htable.get('abc'))
htable.insert('zyx', '123')
print(htable.get('zyx'))
print(htable.length())
htable.remove('abc')
print(htable.get('zyx'))
print(htable.length())
