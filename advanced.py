import random

grid = {}
for row in range(1,5):
    for column in range(1,5):
        grid[(row, column)] = 0



beginner_visit = []
advanced_visit = []


def beginner(grid):
    global beginner_visit
    global advanced_visit
    # print(len(count_two_in_rows_player(grid)))
    # print(len(count_two_in_rows_opponent(grid)))
    if len(count_two_in_rows_player(grid)) != 0:
        return random.choice(count_two_in_rows_player(grid))
    elif len(count_two_in_rows_opponent(grid)) != 0:
        return random.choice(count_two_in_rows_opponent(grid))
    else:
        for row in range(1, 5):
            for col in range(1, 5):
                if grid[(row, col)] == 0:
                    return [row, col]


def count_two_in_rows_player(grid):
    global beginner_visit
    global advanced_visit
    count = 0
    open_two_in_row_position = []
    for [row, col] in beginner_visit:
        for [r, c] in [row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1,
                                                                                                               col - 1], [
                                  row + 1, col], [row + 1, col + 1]:
            if 1 <= r <= 4 and 1 <= c <= 4:
                if [r, c] in beginner_visit:
                    if r == row - 1 and c == col - 1:
                        if 1 <= r - 1 <= 4 and 1 <= c - 1 <= 4 and grid[(r - 1, c - 1)] == 0:
                            open_two_in_row_position.append([r - 1, c - 1])
                    if r == row - 1 and c == col:
                        if 1 <= r - 1 <= 4 and 1 <= c <= 4 and grid[(r - 1, c)] == 0:
                            open_two_in_row_position.append([r - 1, c])
                    if r == row - 1 and c == col + 1:
                        if 1 <= r - 1 <= 4 and 1 <= c + 1 <= 4 and grid[(r - 1, c + 1)] == 0:
                            open_two_in_row_position.append([r - 1, c + 1])
                    if r == row and c == col - 1:
                        if 1 <= r <= 4 and 1 <= c - 1 <= 4 and grid[(r, c - 1)] == 0:
                            open_two_in_row_position.append([r, c - 1])
                    if r == row and c == col + 1:
                        if 1 <= r <= 4 and 1 <= c + 1 <= 4 and grid[(r, c + 1)] == 0:
                            open_two_in_row_position.append([r, c + 1])
                    if r == row + 1 and c == col - 1:
                        if 1 <= r + 1 <= 4 and 1 <= c - 1 <= 4 and grid[(r + 1, c - 1)] == 0:
                            open_two_in_row_position.append([r + 1, c - 1])
                    if r == row + 1 and c == col:
                        if 1 <= r + 1 <= 4 and 1 <= c <= 4 and grid[(r + 1, c)] == 0:
                            open_two_in_row_position.append([r + 1, c])
                    if r == row + 1 and c == col + 1:
                        if 1 <= r + 1 <= 4 and 1 <= c + 1 <= 4 and grid[(r + 1, c + 1)] == 0:
                            open_two_in_row_position.append([r + 1, c + 1])
    return open_two_in_row_position


def count_two_in_rows_opponent(grid):
    global beginner_visit
    global advanced_visit
    open_two_in_row_position = []
    for [row, col] in advanced_visit:
        for [r, c] in [row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1,
                                                                                                               col - 1], [
                                  row + 1, col], [row + 1, col + 1]:
            if 1 <= r <= 4 and 1 <= c <= 4:
                if [r, c] in advanced_visit:
                    if r == row - 1 and c == col - 1:
                        if 1 <= r - 1 <= 4 and 1 <= c - 1 <= 4 and grid[(r - 1, c - 1)] == 0:
                            open_two_in_row_position.append([r - 1, c - 1])
                    if r == row - 1 and c == col:
                        if 1 <= r - 1 <= 4 and 1 <= c <= 4 and grid[(r - 1, c)] == 0:
                            open_two_in_row_position.append([r - 1, c])
                    if r == row - 1 and c == col + 1:
                        if 1 <= r - 1 <= 4 and 1 <= c + 1 <= 4 and grid[(r - 1, c + 1)] == 0:
                            open_two_in_row_position.append([r - 1, c + 1])
                    if r == row and c == col - 1:
                        if 1 <= r <= 4 and 1 <= c - 1 <= 4 and grid[(r, c - 1)] == 0:
                            open_two_in_row_position.append([r, c - 1])
                    if r == row and c == col + 1:
                        if 1 <= r <= 4 and 1 <= c + 1 <= 4 and grid[(r, c + 1)] == 0:
                            open_two_in_row_position.append([r, c + 1])
                    if r == row + 1 and c == col - 1:
                        if 1 <= r + 1 <= 4 and 1 <= c - 1 <= 4 and grid[(r + 1, c - 1)] == 0:
                            open_two_in_row_position.append([r + 1, c - 1])
                    if r == row + 1 and c == col:
                        if 1 <= r + 1 <= 4 and 1 <= c <= 4 and grid[(r + 1, c)] == 0:
                            open_two_in_row_position.append([r + 1, c])
                    if r == row + 1 and c == col + 1:
                        if 1 <= r + 1 <= 4 and 1 <= c + 1 <= 4 and grid[(r + 1, c + 1)] == 0:
                            open_two_in_row_position.append([r + 1, c + 1])
    return open_two_in_row_position


def check_win(grid):
    global beginner_visit
    global advanced_visit

    for [row, col] in advanced_visit:
        for [r, c] in [row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1,
                                                                                                               col - 1], [
                                  row + 1, col], [row + 1, col + 1]:
            if 1 <= r <= 4 and 1 <= c <= 4:
                if [r, c] in advanced_visit:
                    if r == row - 1 and c == col - 1:
                        if 1 <= r - 1 <= 4 and 1 <= c - 1 <= 4 and grid[(r - 1, c - 1)] == -1:
                            return -1
                    if r == row - 1 and c == col:
                        if 1 <= r - 1 <= 4 and 1 <= c <= 4 and grid[(r - 1, c)] == -1:
                            return -1
                    if r == row - 1 and c == col + 1:
                        if 1 <= r - 1 <= 4 and 1 <= c + 1 <= 4 and grid[(r - 1, c + 1)] == -1:
                            return -1
                    if r == row and c == col - 1:
                        if 1 <= r <= 4 and 1 <= c - 1 <= 4 and grid[(r, c - 1)] == -1:
                            return -1
                    if r == row and c == col + 1:
                        if 1 <= r <= 4 and 1 <= c + 1 <= 4 and grid[(r, c + 1)] == -1:
                            return -1
                    if r == row + 1 and c == col - 1:
                        if 1 <= r + 1 <= 4 and 1 <= c - 1 <= 4 and grid[(r + 1, c - 1)] == -1:
                            return -1
                    if r == row + 1 and c == col:
                        if 1 <= r + 1 <= 4 and 1 <= c <= 4 and grid[(r + 1, c)] == -1:
                            return -1
                    if r == row + 1 and c == col + 1:
                        if 1 <= r + 1 <= 4 and 1 <= c + 1 <= 4 and grid[(r + 1, c + 1)] == -1:
                            return -1
    for [row, col] in beginner_visit:
        for [r, c] in [row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1,
                                                                                                               col - 1], [
                                  row + 1, col], [row + 1, col + 1]:
            if 1 <= r <= 4 and 1 <= c <= 4:
                if [r, c] in beginner_visit:
                    if r == row - 1 and c == col - 1:
                        if 1 <= r - 1 <= 4 and 1 <= c - 1 <= 4 and grid[(r - 1, c - 1)] == 1:
                            return 1
                    if r == row - 1 and c == col:
                        if 1 <= r - 1 <= 4 and 1 <= c <= 4 and grid[(r - 1, c)] == 1:
                            return 1
                    if r == row - 1 and c == col + 1:
                        if 1 <= r - 1 <= 4 and 1 <= c + 1 <= 4 and grid[(r - 1, c + 1)] == 1:
                            return 1
                    if r == row and c == col - 1:
                        if 1 <= r <= 4 and 1 <= c - 1 <= 4 and grid[(r, c - 1)] == 1:
                            return 1
                    if r == row and c == col + 1:
                        if 1 <= r <= 4 and 1 <= c + 1 <= 4 and grid[(r, c + 1)] == 1:
                            return 1
                    if r == row + 1 and c == col - 1:
                        if 1 <= r + 1 <= 4 and 1 <= c - 1 <= 4 and grid[(r + 1, c - 1)] == 1:
                            return 1
                    if r == row + 1 and c == col:
                        if 1 <= r + 1 <= 4 and 1 <= c <= 4 and grid[(r + 1, c)] == 1:
                            return 1
                    if r == row + 1 and c == col + 1:
                        if 1 <= r + 1 <= 4 and 1 <= c + 1 <= 4 and grid[(r + 1, c + 1)] == 1:
                            return 1
    return 0




def minimum_value(list):
    for i in range(len(list) - 1):
        if list[i] <= list[i + 1]:
            min = list[i]
            return min

def maximum_value(list):
    for i in range(len(list) - 1):
        if list[i][2] > list[i + 1][2]:
            max = list[i]
            return max

max_node1 = []
count = 0

def advanced(grid):
    global advanced_visit
    global beginner_visit
    global max_node1
    global count
    max_value = -10000
    #for max part
    for row in range(1, 5):
        for col in range(1, 5):
            if grid[(row, col)] == 0:
                grid[(row, col)] = -1
                advanced_visit.append([row, col])
                if check_win(grid) != 1:
                #for min
                    min_value = 10000
                    for r in range(1, 5):
                        for c in range(1, 5):
                            if grid[(r, c)] == 0:
                                grid[(r, c)] = -1
                                beginner_visit.append([r, c])
                                if check_win(grid) != 1:
                                    count += 1
                                    h = (len(count_two_in_rows_opponent(grid)) - len(count_two_in_rows_player(grid)))
                                    min_value = min(h, min_value)
                                else:
                                    min_value = -10000
                                # print [r, c, min_value]
                                grid[(r, c)] = 0
                                beginner_visit.pop()
                    # print([row, col])
                    if min_value >= max_value:
                        max_value = min_value
                        # print([row, col])
                        max_node1 = [row, col]
                    count += 1
                else:
                    max_value = 10000
                    max_node1 = [row, col]
                # print "@@@@@@@@@",[max_node1[0], max_node1[1], max_value]
                grid[(row, col)] = 0
                advanced_visit.pop()

    return max_value


def beginner_vs_advanced(grid):
    global advanced_visit
    global beginner_visit
    while check_win(grid) == 0:
        [row, col] = beginner(grid)
        print "beginner:", (row, col)
        grid[(row, col)] = 1
        beginner_visit.append([row, col])
        if check_win(grid) == 1:
            print "beginner wins"
            return
        else:
            advanced(grid)
            print "advanced:", (max_node1[0], max_node1[1])
            advanced_visit.append([max_node1[0], max_node1[1]])
            grid[(max_node1[0], max_node1[1])] = -1
            if check_win(grid) == -1:
                print "opponent wins"
                return



beginner_vs_advanced(grid)

print "the number of expand node is:", count

