def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
                
            board[row][col] = 0 
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_valid(board, num, row, col):

    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False
    

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True


sudoku_board = [
    [2, 0, 9, 0, 8, 0, 4, 5, 0],
    [4, 0, 7, 0, 0, 0, 0, 0, 8],
    [0, 0, 5, 4, 0, 0, 0, 2, 3],
    [0, 8, 2, 5, 0, 4, 1, 0, 7],
    [0, 0, 3, 6, 7, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 2, 6, 9],
    [0, 4, 8, 0, 2, 0, 0, 0, 1],
    [0, 7, 0, 0, 0, 0, 3, 4, 2],
    [9, 0, 0, 0, 0, 3, 0, 0, 9]
]

if solve_sudoku(sudoku_board):
    for row in sudoku_board:
        print(row)
else:
    print("This sudoku is unsolvable.")
