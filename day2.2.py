# read file input.txt
# A = Rock = X
# B = Paper = Y
# C = Scissors = Z


def calc_points(line):
    points = 0
    opp, strat = line.split(" ")[0], line.split(" ")[1].strip()
    if strat == "X":
        if opp == "A":
            points = 3
        elif opp == "B":
            points = 1
        elif opp == "C":
            points = 2
    elif strat == "Y":
        if opp == "A":
            points = 4
        elif opp == "B":
            points = 5
        elif opp == "C":
            points = 6
    else:
        if opp == "A":
            points = 8
        elif opp == "B":
            points = 9
        elif opp == "C":
            points = 7
    return points


total = 0
with open("input2.txt") as f:
    # read file line by line
    for line in f:
        total += calc_points(line)
print(total)
