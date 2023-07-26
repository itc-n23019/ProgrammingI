import random
def generate_stud_data(num_stud = 10):
    stud_data = []
    for i in range(num_stud):
        name = "n" + str(random.randint(10,50))
        height = random.randint(150,190)
        weight = random.randint(50,80)
        stud_data.append((name, height, weight))
        if i == 0: print('1', name, height, weight)
        if i < 2 or i == num_stud - 1:
            print("i,name, height, weight")
        elif i == 2:
            print("...")
    return stud_data
stud_data = generate_stud_data(10)
stud_hei = sorted(stud_data, key = lambda s: s[1])
stud_wei = sorted(stud_data, key = lambda s: s[2])

print("\nSort by height")
for stud in stud_hei:
    print(stud)

print("\nSort by weight")
for stud in stud_wei:
    print(stud)
