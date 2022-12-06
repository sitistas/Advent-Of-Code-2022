# read file input6.txt
f = open("input6.txt", "r")
text = f.read()
text = [*text]
# print(text)

last4 = []
counter = 0
for i in range(len(text)):
    if text[i] in last4:
        # find position of text[i] in last4
        pos = last4.index(text[i])
        for j in range(pos + 1):
            del last4[0]
        last4.append(text[i])
    else:
        last4.append(text[i])
    counter += 1
    if len(last4) == 4:
        print(last4)
        print(counter)
        break
