total = []
temp = 0
with open("input1.txt") as f:
    for line in f:
        if line != "\n":
            temp += int(line)
        else:
            total.append(temp)
            temp = 0
print(max(total))
