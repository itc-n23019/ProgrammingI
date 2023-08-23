import my_math2
x, y, exp = 2, 5, 32
ans = my_math2.my_pow(x, y)
print("Test my_pow({},{}) -> {}, exp: {} ---- ".format(x, y, ans, exp), end = '')
if ans == exp:
    print("Test OK")
else:
    print("Test Fall")
