import random
import time

#Create grid and init each cell to 0
grid = {}
for row in range(1,5):
    for column in range(1,5):
        grid[(row, column)] = 0


#Global lists for tracking cells visited
beginner_visit = []
advanced_visit = []

#Code which defines the behavour of  beginner player
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

#Calcs the # of 2-in-a-row that max has
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

#Calcs the # of 2-in-a-row that min has
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

#Takes in grid (dictionary -> key=(row,col), value= 1|0|-1)
#returns:
#       0 - no winner
#       1 - min wins
#      -1 - max wins
# wins = 3 in a row 
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



#Function that returns min value from list
def minimum_value(list):
    for i in range(len(list) - 1):
        if list[i] <= list[i + 1]:
            min = list[i]
            return min
        
#Function that returns max value from list
def maximum_value(list):
    for i in range(len(list) - 1):
        if list[i][2] > list[i + 1][2]:
            max = list[i]
            return max

max_node1 = []
count = 0


#function which defines advance behavour
def advanced(grid):
    #var(s) she blows!
    global advanced_visit
    global beginner_visit
    global max_node1
    global count
    max_value = -10000
    
    #Look ahead to 
    for row in range(1, 5):
        for col in range(1, 5):
            #Check if cell is empty mark
            if grid[(row, col)] == 0:
                grid[(row, col)] = -1
                advanced_visit.append([row, col]) #add newly marked cell to list of visited
                count += 1
                #Check if next node is a terminal (winning) node
                if check_win(grid) != 1:
                #It is not a winning node
                    min_value = 10000
                    #Look ahead to min's turn
                    for r in range(1, 5):
                        for c in range(1, 5):
                            #Check if cell is empty 
                            if grid[(r, c)] == 0:
                                grid[(r, c)] = -1 #mark it
                                beginner_visit.append([r, c])
                                count += 1
                                #Check if next node is a terminal (winning) node
                                if check_win(grid) != 1:
                                    #Calculate heuristic
                                    h = (len(count_two_in_rows_opponent(grid)) - len(count_two_in_rows_player(grid)))
                                    #Check if new h value is less than former min
                                    min_value = min(h, min_value)
                                else:
                                    min_value = -10000

                                grid[(r, c)] = 0
                                beginner_visit.pop()
                    #Check if max value needs updating
                    if min_value >= max_value:
                        max_value = min_value
                        max_node1 = [row, col]
                    
                else:
                #it is a winning node
                    max_value = 10000
                    max_node1 = [row, col]
                grid[(row, col)] = 0
                advanced_visit.pop()

    return max_value

#Running beginner vs advanced
def beginner_vs_advanced(grid):
    global advanced_visit
    global beginner_visit
    global count
    
    while check_win(grid) == 0:
        #Beginner should take a turn
        [row, col] = beginner(grid) #get turn played by beginner
        
        print "beginner:", (row, col)
        
        grid[(row, col)] = 1 #play beginner's turn
        beginner_visit.append([row, col])
        
        #Check if beginner has won
        if check_win(grid) == 1:
            print "beginner wins"
            return
        else: #Beginner hasn't won
            #Advanced should take a turn
            start_time = time.time()
            advanced(grid)
            stop_time = time.time()
            

            print "advanced:", (max_node1[0], max_node1[1])
            print "\texecution time: %f ms"%((stop_time-start_time)*1000)
            print "\t#of nodes expanded:%d"%count
            count = 0
            
            advanced_visit.append([max_node1[0], max_node1[1]])
            grid[(max_node1[0], max_node1[1])] = -1
            
            #Check if advanced has won
            if check_win(grid) == -1:
                print "advanced wins"
                return


#Start the storm
beginner_vs_advanced(grid)





