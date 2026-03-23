# Solve a Sudoku board using backtracking.

def solve(board):
    # Solve the sudoku board. Return True if solved.
    cell = find_empty_cell(board)
    if not cell:
        return True
    row, col = cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # change the number then recurse.
            solve(board)
            pass

    return False


def find_empty_cell(board):
    # Find the next empty cell (value 0). Returns (row, col) or None.
    # for cell in board:
    #     for index in cell:
            
        


    pass

def is_valid(board, row, col, num):
    for cell in board:
        for cell in row:
            for cell in col:
                if num == cell:
                    return False
    return True

def print_board(board):
    # Print the board in a readable format.
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        line = ""
        for col in range(len(board[row])):
            if col % 3 == 0 and col != 0:
                line += "| "
            val = board[row][col]
            line += (str(val) if val != 0 else ".") + " "
        print(line)


if __name__ == "__main__":
    # Example puzzle (0 = empty)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("Puzzle:")
    print_board(board)
    print()

    if solve(board):
        print("Solution:")
        print_board(board)
    else:
        print("No solution exists.")
