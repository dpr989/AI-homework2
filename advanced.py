import random

grid = {}
for row in range(1,5):
    for column in range(1,5):
        print(row, column)
        grid[(row, column)] = 0



min_visit = []
max_visit = []


def beginner(grid):
    global min_visit
    global opponent_visit
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
    global min_visit
    global opponent_visit
    count = 0
    open_two_in_row_position = []
    for [row, col] in min_visit:
        for [r, c] in [row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1,
                                                                                                               col - 1], [
                                  row + 1, col], [row + 1, col + 1]:
            if 1 <= row <= 4 and 1 <= col <= 4:
                if [r, c] in min_visit:
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
    global min_visit
    global opponent_visit
    open_two_in_row_position = []
    for [row, col] in opponent_visit:
        for [r, c] in [row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1,
                                                                                                               col - 1], [
                                  row + 1, col], [row + 1, col + 1]:
            if 1 <= row <= 4 and 1 <= col <= 4:
                if [r, c] in opponent_visit:
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
    global min_visit
    global opponent_visit

    for [row, col] in opponent_visit:
        for [r, c] in [row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1, col - 1], [row + 1, col], [row + 1, col + 1]:
            if 1 <= row <= 4 and 1 <= col <= 4:
                if [r, c] in opponent_visit:
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
    for [row, col] in min_visit:
        for [r, c] in [row - 1, col - 1], [row - 1, col], [row - 1, col + 1], [row, col - 1], [row, col + 1], [row + 1, col - 1], [row + 1, col], [row + 1, col + 1]:
            if 1 <= row <= 4 and 1 <= col <= 4:
                if [r, c] in min_visit:
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

def getMin(dlist):
    for d in dlist:
        min_cost 
def advanced(grid):
    i = 0
    min_cost = -100;
    max_cost = [];
    
    #Lookahead  #1
    for row in range(1, 5):
        for col in range(1, 5):
            #if cell is empty mark
            if grid[(row, col)] == 0:
                grid[(row, col)] = -1
                max_visit.append([row, col])
                
                #Lookahead #2 (terminal)
                for r in range(1, 5):
                    for c in range(1, 5):
                        if grid[(r, c)] == 0:
                            grid[(r, c)] = 1
                            min_visit.append([r, c])
                            #Check if min
                            h = (len(count_two_in_rows_opponent(grid)) - len(count_two_in_rows_player(grid)))
                            
                            #remove garbage
                            grid[(r, c)] = 0
                            min_visit.pop()
                            
                            if(h < min_cost):
                                min_cost = h
                            
                max_visit.pop()                        
                max_cost.append([min_cost,row,column])
                
                grid[(row, col)] = 0
    return max(max_cost, key = lambda x: x[0])
                    