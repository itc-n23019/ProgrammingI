import random

numbers = [str(i) for i in range(10)]
num4 = ''.join(random.sample(numbers, k=4))

while input() != num4:
    print('NG')

print('OK')

