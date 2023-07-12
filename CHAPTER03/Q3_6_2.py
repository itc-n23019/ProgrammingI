import random

num4 = ''.join(random.choices('0123456789', k=4))

while (val := input()) != num4:
    if len(val) != 4:
        print('input 4 numbers.')
        continue
    answer = ''.join([x if x == y else 'X' for x, y in zip(val, num4)])
    print('-> ' + answer)

