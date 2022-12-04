f = open("input41.txt", "r")
total = 0
for line in f:
    # print(line)
    pairs = line.split(",")
    num1, num2 = pairs[0].split("-")
    num3, num4 = pairs[1].split("-")
    num1, num2, num3, num4 = int(num1), int(num2), int(num3), int(num4)
    # print(num1, num2, num3, num4)
    if num1 > num4 or num3 > num2:
        continue
    else:
        total += 1
print(total)
