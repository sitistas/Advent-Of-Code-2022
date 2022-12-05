# read file input5.txt
stack = [[""], [""], [""], [""], [""], [""], [""], [""], [""]]
with open("input5.txt") as f:
    for line in f:
        reps = 0
        origin = 0
        dest = 0
        temp = []
        if line == "\n":
            for i in range(9):
                stack[i].pop()
        elif line[0] == "m":
            line = line.split(" ")
            # print(line)
            reps = int(line[1])
            origin = int(line[3]) - 1
            dest = int(line[5].split("\\")[0]) - 1
            print(reps, origin, dest)
            for i in range(reps):
                temp.append(stack[origin].pop())
            for i in range(reps):
                stack[dest].append(temp.pop())
            # print("reps: ", reps, "origin: ", origin, "dest: ", dest)
        else:
            if line[1] != " ":
                stack[0].insert(0, line[1])
            for i in range(1, 9):
                try:
                    if line[4 * i + 1] != " ":
                        stack[i].insert(0, line[4 * i + 1])
                except:
                    continue
for i in range(9):
    print(stack[i])
