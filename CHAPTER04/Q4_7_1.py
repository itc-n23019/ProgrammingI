def make_add():
    def add(x, y):
        return x + y
    return add

adder = make_add()
answer = adder(1, 10)
print(answer)
