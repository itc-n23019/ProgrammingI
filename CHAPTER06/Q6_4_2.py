def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generator():
    n = 2
    while True:
        if prime(n):
            yield n
        n += 1

gen = generator()
for _ in range(10):
    print(next(gen))

