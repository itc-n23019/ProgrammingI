many_numbers = list(range(1,100))
s = ''
for i in many_numbers:
    s += "{:2d},".format(i)
    if i % 10 == 0:
        s += "\n"  
print(s)

