# create a dictioary starting with "a":1 and ending with "z":26
dict = {}
for i in range(1, 27):
    dict[chr(i + 96)] = i
for i in range(28, 53):
    dict[chr(i + 38)] = i
# print(dict)

total = 0
f = open("input3.txt", "r")
# read 3 lines at a time and strip the newline character
for line in zip(f, f, f):
    string0 = line[0].strip()
    string1 = line[1].strip()
    string2 = line[2].strip()
    a = set(string1) & set(string2) & set(string0)
    for i in a:
        # print(i)
        total += dict[i]
        # print(dict[i])
print(total)
