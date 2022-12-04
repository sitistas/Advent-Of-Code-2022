total = []
temp = 0
with open("input1.txt") as f:
    for line in f:
        if line != "\n":
            temp += int(line)
        else:
            total.append(temp)
            temp = 0
# sort the list
# total.sort(reverse=1)
# print(total)
temp = 0
for i in range(3):
    # pop max of total
    max_val = max(total)
    print(max_val)
    temp += max_val
    total.remove(max_val)
print(temp)
