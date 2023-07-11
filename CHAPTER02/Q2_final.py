import random

word = "t"

while True:
    ranchar = random.choice([chr(i) for i in range(97, 97+26)])
    print(ranchar)
    
    if ranchar == "t":
        break

