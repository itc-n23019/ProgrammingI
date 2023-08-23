import random

random.seed(1)
msgs = ["Hi", "Hello", "Good morning", "Good night", "See you later", "How are you", "Have a good day"]

with open("some.txt", "w") as f:
	for i in range(1000000):
		f.write("{},{}\n".format(i, random.choice(msgs)))

f = open('some.text')
c = 0
for l in f:
	print(l, end = '')
	if c == 2:
		break
	c += 1
f.close

%%time
r = open('some.txt')
c = 0
for l in f:
	print(l, end = '')
	if c == 2:
		break
	c += 1
f.close	
