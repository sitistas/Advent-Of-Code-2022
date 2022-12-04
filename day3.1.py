# create a dictioary starting with "a":1 and ending with "z":26
dict = {}
for i in range(1, 27):
    dict[chr(i + 96)] = i
for i in range(28, 53):
    dict[chr(i + 38)] = i
# print(dict)

total = 0
f = open("input3.txt", "r")
for line in f:
    # split string in half
    string1, string2 = line[: len(line) // 2], line[len(line) // 2 :]
    # print(string1, string2)
    a = set(string1) & set(string2)
    for i in a:
        # print(i)
        total += dict[i]
        # print(dict[i])
print(total)
