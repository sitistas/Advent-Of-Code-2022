def find_visible_trees(matrix):
    counter = 0

    for row in range(len(matrix)):
        # check if first or last row
        if row == 0 or row == len(matrix) - 1:
            # add all the trees in the counter
            for col in range(len(matrix[row])):
                counter += 1
        else:
            # if first or last column, add the tree to the counter
            if matrix[row][0] > -1 or matrix[row][len(matrix[row]) - 1] > -1:
                counter += 1
    return counter


with open("input8.txt", "r", encoding="utf-8") as f:
    counter1 = 0
    counter2 = 0
    matrix = [[0] * 99] * 99
    for line in f:
        line = line.strip()
        # print(line)
        for pos in range(len(line)):
            matrix[counter1][counter2] = int(line[pos])
            counter2 += 1
        counter1 += 1
        counter2 = 0
    print(find_visible_trees(matrix))
