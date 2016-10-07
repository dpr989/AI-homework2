import random

grid = {}
for row in range(1,5):
    for column in range(1,5):
        grid[(row, column)] = 0


advanced_visit = []
master_visit = []

def count_two_in_rows_advanced(grid):
    global advanced_visit
    global master_visit
    count = 0
    open_two_in_row_position = []
    for [row, col] in advanced_visit:
        for [r, c] in [row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1, col - 1], [row + 1, col], [row + 1, col + 1]:
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


def count_two_in_rows_master(grid):
    global advanced_visit
    global master_visit
    open_two_in_row_position = []
    for [row, col] in master_visit:
        for [r, c] in [row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1,
                                                                                                               col - 1], [
                                  row + 1, col], [row + 1, col + 1]:
            if 1 <= r <= 4 and 1 <= c <= 4:
                if [r, c] in master_visit:
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
    global advanced_visit
    global master_visit

    for [row, col] in master_visit:
        for [r, c] in [row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1,
                                                                                                               col - 1], [
                                  row + 1, col], [row + 1, col + 1]:
            if 1 <= r <= 4 and 1 <= c <= 4:
                if [r, c] in master_visit:
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
    for [row, col] in advanced_visit:
        for [r, c] in [row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1,
                                                                                                               col - 1], [
                                  row + 1, col], [row + 1, col + 1]:
            if 1 <= r <= 4 and 1 <= c <= 4:
                if [r, c] in advanced_visit:
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





# def minimum_value(list):
#     min = list[0]
#     for i in range(len(list)):
#         if list[i] <= min:
#             min = list[i]
#
#     print(min)
#     return min

def minimum_value(list):
    min = list[0]
    for i in range(len(list)):
        if list[i][2] <= min[2]:
            min = list[i]
    return min


def maximum_value(list):
    max = list[0]
    for i in range(len(list)):
        if list[i][2] >= max[2]:
            max = list[i]
    return max



max_node1 = []

def advanced(grid):
    global advanced_visit
    global master_visit
    global max_node1
    max_value = -10000
    #for max
    for row in range(1, 5):
        for col in range(1, 5):
            if grid[(row, col)] == 0:
                grid[(row, col)] = 1
                advanced_visit.append([row, col])
                if check_win(grid) != 1:
                #for min
                    min_value = 10000
                    for r in range(1, 5):
                        for c in range(1, 5):
                            if grid[(r, c)] == 0:
                                grid[(r, c)] = -1
                                master_visit.append([r, c])
                                if check_win(grid) != -1:
                                    h = (len(count_two_in_rows_advanced(grid)) - len(count_two_in_rows_master(grid)))
                                    min_value = min(h, min_value)
                                else:
                                    min_value = -10000

                                grid[(r, c)] = 0
                                master_visit.pop()

                    if min_value >= max_value:
                        max_value = min_value
                        max_node1 = [row, col]
                else:
                    max_value = 10000
                    max_node1 = [row, col]
                grid[(row, col)] = 0
                advanced_visit.pop()

    return max_value

# def advanced(grid):
#     global advanced_visit
#     global master_visit
#     max_list = []
#     #for max
#     for row in range(1, 5):
#         for col in range(1, 5):
#             if grid[(row, col)] == 0:
#                 grid[(row, col)] = 1
#                 advanced_visit.append([row, col])
#                 min_list = []
#                 #for min
#                 for r in range(1, 5):
#                     for c in range(1, 5):
#                         if grid[(r, c)] == 0:
#                             grid[(r, c)] = -1
#                             master_visit.append([r, c])
#                             h = (len(count_two_in_rows_player(grid)) - len(count_two_in_rows_opponent(grid)))
#                             # print([r, c, h])
#                             min_list.append([r, c, h])
#                             grid[(r, c)] = 0
#                             master_visit.pop()
#                 min = minimum_value(min_list)
#                 # print "minimum", minimum_value(min_list)
#                 max_list.append([row, col, min[2]])
#                 grid[(row, col)] = 0
#                 advanced_visit.pop()
#     max = maximum_value(max_list)
#     # print "!!!!!!!!!!!!!!!***************", max
#     return max



max_node = []

def master(grid, depth):
    global advanced_visit
    global master_visit
    global max_node
    if depth == 0:
        return len(count_two_in_rows_master(grid)) - len(count_two_in_rows_advanced(grid))
    else:
        max_value = -10000
        for row in range(1, 5):
            for col in range(1, 5):
                if grid[(row, col)] == 0:
                    grid[(row, col)] = -1
                    master_visit.append([row, col])

                    if check_win(grid) != -1:
                        min_value = 10000
                        #for min
                        for r in range(1, 5):
                            for c in range(1, 5):
                                if grid[(r, c)] == 0:
                                    grid[(r, c)] = 1
                                    advanced_visit.append([r, c])
                                    if check_win(grid) != 1:
                                        h = master(grid, depth - 1)
                                        # print([r, c, h])

                                        min_value = min(h, min_value)
                                    else:
                                        min_value = -10000
                                    # if depth == 1:
                                        # print
                                    grid[(r, c)] = 0
                                    advanced_visit.pop()


                        if min_value >= max_value:
                            max_value = min_value
                            # if depth == 2:
                            max_node = [row, col]
                        # if depth == 2:
                            # print [max_node[0], max_node[1], max_value]
                    else:
                        max_value = 10000
                        max_node = [row, col]
                    grid[(row, col)] = 0
                    master_visit.pop()
    return max_value




# def master(grid):
#     global advanced_visit
#     global master_visit
#     max_list1 = []
#
#     for row in range(1, 5):
#         for col in range(1, 5):
#             if grid[(row, col)] == 0:
#                 grid[(row, col)] = -1
#                 master_visit.append([row, col])
#                 min_list1 = []
#                 #for min
#                 for r in range(1, 5):
#                     for c in range(1, 5):
#                         if grid[(r, c)] == 0:
#                             grid[(r, c)] = 1
#                             advanced_visit.append([r, c])
#                             max_list2 = []
#
#                             for x in range(1, 5):
#                                 for y in range(1, 5):
#                                     if grid[(x, y)] == 0:
#                                         grid[(x, y)] = -1
#                                         master_visit.append([x, y])
#                                         min_list2 = []
#
#                                         for a in range(1, 5):
#                                             for b in range(1, 5):
#                                                 if grid[(a, b)] == 0:
#                                                     grid[(a, b)] = 1
#                                                     advanced_visit.append([a, b])
#                                                     h = (len(count_two_in_rows_opponent(grid)) - len(count_two_in_rows_player(grid)))
#                                                     # print([a, b, h])
#                                                     min_list2.append([a, b, h])
#                                                     grid[(a, b)] = 0
#                                                     advanced_visit.pop()
#
#
#                                         min = minimum_value(min_list2)
#                                         # print "@@@@@@@@@@", min
#                                         max_list2.append([x, y, min[2]])
#                                         grid[(x, y)] = 0
#                                         master_visit.pop()
#
#                             max = maximum_value(max_list2)
#                             # print "!!!!!!!!!!!!!!!!!", max
#                             min_list1.append([r, c, max[2]])
#                             grid[(r, c)] = 0
#                             advanced_visit.pop()
#
#                 min = minimum_value(min_list1)
#                 max_list1.append([row, col, min[2]])
#                 grid[(row, col)] = 0
#                 master_visit.pop()
#
#                 # print "*******************"
#
#         max = maximum_value(max_list1)
#     # if len(max_list) != 0:
#     #     max_list.pop()
#     # print "%%%%%%%%", max
#     return max


def advanced_vs_master(grid):
    global advanced_visit
    global master_visit

    while check_win(grid) == 0:
        advanced(grid)
        # print advanced(grid)
        print "advanced:", (max_node1[0], max_node1[1])
        grid[(max_node1[0], max_node1[1])] = 1
        advanced_visit.append([max_node1[0], max_node1[1]])
        if check_win(grid) == 1:
            print "advanced wins"
            return
        else:
            master(grid,2)
            print "master:", (max_node[0], max_node[1])
            master_visit.append([max_node[0], max_node[1]])
            grid[(max_node[0], max_node[1])] = -1
            if check_win(grid) == -1:
                print "master wins"
                return



def master_vs_advanced(grid):
    global advanced_visit
    global master_visit

    while check_win(grid) == 0:
        master(grid, 2)
        print "master:", (max_node[0], max_node[1])
        master_visit.append([max_node[0], max_node[1]])
        grid[(max_node[0], max_node[1])] = -1
        if check_win(grid) == -1:
            print "master wins"
            return
        else:
            advanced(grid)
            # print advanced(grid)
            print "advanced:", (max_node1[0], max_node1[1])
            grid[(max_node1[0], max_node1[1])] = 1
            advanced_visit.append([max_node1[0], max_node1[1]])
            if check_win(grid) == 1:
                print "advanced wins"
                return


advanced_vs_master(grid)
#master_vs_advanced(grid)