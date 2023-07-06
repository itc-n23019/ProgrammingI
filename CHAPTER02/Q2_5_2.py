result =  ""
for i in range(4):
    for j in range(4):
        if i == j:
                result += "⚪"
        else:
                result += "⚫"
    result += "\n"
print(result)
