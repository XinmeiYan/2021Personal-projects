# create empty board of the sudoku puzzle
board = []

# allow user to input a new sudoku
while True:

    # input a new list row by row
    row = list(input('Please input numbers for one row: '))
    puzzle = []

    # for each value in a row
    for i in row:

        # convert inputs to integer and put it in puzzle
        puzzle.append(int(i))
    
    # put the integers in board
    board.append(puzzle)

    # loop breaks when nine rows are recorded, let user knows when one row is completed
    if len(board) == 9:
        break
    print('Row ' + str(len(board)) + ' is completed')



# solve sudoku using backtracking
def solve(bo):
    
    # step 1: find empty space (zero) on the board
    find = find_empty(bo)

    # when the board is all filled, return true
    if not find:
        return True
    # when there is still empty space, given the indice: row, col
    else:
        row, col = find

    # step 2: check if the value is valid at position (row, col)
    for i in range(1,10):

        # if it is valid, assign that value to this position
        if valid(bo, i, (row, col)): 
            bo[row][col] = i 

            # if values at all positions are valid, sudoku solved and return true
            if solve(bo):
                return True 
                
        # if it is not valid, reset the value to zero (backtracking)
        bo[row][col] = 0 
    return False 


def find_empty(bo):

    # find zero in each row-column
    for i in range(len(bo)): 
        for j in range(len(bo[0])):

             # when it is not filled yet, return the indice (i , j)
            if bo[i][j] == 0:
                return (i, j) #row, column

    # when there is no empty space left on the board, return None
    return None


# check if the added value is valid
def valid(bo, num, pos): 

    # check row
    for i in range(len(bo[0])):

        # go through each value in a row, if any number in this row equals to the added value, not valid---return false
        if bo[pos[0]][i] == num:
            return False

    # check column
    for i in range(len(bo)):

        # go through each value in a column, if any number in this column equals to the added value, not valid---return false
        if bo[i][pos[1]] == num:
            return False

    # check box (3x3 section, 9 sections in total)
    # determine which box it is in (integer division)
    # row
    box_x= pos[0] // 3

    # column
    box_y= pos[1] // 3

    # convert back to rol, col
    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):

            # if any number in this box equals to the added value, not valid---return false
            if bo[i][j] == num:
                return False
    return True


# print the board in clear 3x3 sections
def print_board(bo):

    # separation between every 3 lines (len(bo) is the number of rows)
    for i in range(len(bo)): 
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -") 

        # separation between every 3 numbers (len(bo[0]) is the number of columns)
        # keep 9 numbers in the same row with space separated
        for j in range(len(bo[0])): 
            if j % 3 == 0 and j != 0:
                print("|", end = " ") 

            if j == 8:
                print (bo[i][j])
            else:
                print(str(bo[i][j]) + "", end = " ")


print_board(board)
solve(board)
print("_____________________________")
print("                             ")
print_board(board)