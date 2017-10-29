from random import randint

def isprime(n, k=5):
    if n == 2:
        return True
    for _ in range(k):
        d = randint(2, n-1)
        if d**(n-1) % n != 1:
            return False
    return True

def verify(n):
    for q in range(2, int(n**0.5) + 1):
        if n % q == 0:
            return False
    return True

def accuracy(n, k):
    return sum(verify(n) == isprime(n, k=k) for _ in range(1000)) / 1000


# print(list(map(isprime, range(2, 100))))

print('Accuracy of prime test based on fermat\'s little theorem on 2821 with various values of k')
for k in range(1, 15):
    print('k=%d:'%k, accuracy(2821, k))
