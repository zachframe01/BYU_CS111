import sys
import random


def validate_arg(command):
    '''
    input: the argv artguments
    output: true or false depending on if the arguments meet specified criteria. 
    >>> validate_arg(['u','file'])
    Error!: the argument was not give right!
    '''
    if command[0] == '-g':
        return validate_gen(command)
    elif command[0] == '-s':
        return validate_solve(command)
    else:
        return (print("Error!: the argument was not give right!"))

def validate_gen(command):
    '''
    input: the argv artguments
    output: true or false depending on if the arguments meet specified criteria. 
    >>> validate_gen(['g',4])
    Usage: python3 maze_solver.py [-s maze_file] [-g width height maze_file]
    False
    '''
    if len(command) != 4:
        print(f'Usage: python3 maze_solver.py [-s maze_file] [-g width height maze_file]')
        return False
    elif int(command[1]) <= 2 or int(command[2]) <= 4:
        print(f'Error! The minimum maze size is 3x5!')
        return False
    print_board(command[1],command[2],command[3])
    return True

def validate_solve(command):
    '''
    input: the argv artguments
    output: true or false depending on if the arguments meet specified criteria. 
    >>> validate_solve(['-s','solve','file'])
    Usage: python3 maze_solver.py [-s maze_file] [-g width height maze_file]
    False
    '''
    if len(command) != 2:
        print(f'Usage: python3 maze_solver.py [-s maze_file] [-g width height maze_file]')
        return False
    construct(command[1])
    return True



def construct(filename):
    '''
    input: file
    output: constructs the maze based on the file given. 
    '''
    with open(filename, "r") as file:
        maze = []
        for line in file.readlines():
            maze.append(list(line.strip("\n")))
        start_x, start_y = find(maze, "S")
        end_x, end_y = find(maze, "E")

        solved_maze = solve(maze, start_x, start_y, end_x, end_y)
        if solved_maze:
            solved_maze[start_y][start_x] = "S"
            print("Success! The path is as follows:")
            for line in solved_maze:
                print("".join(line))
        else:
            print("Error! Solver could find no solution to maze!")

def find(nested_lst, target):
    '''
    input: list of lists. target in the list.
    output: gives the location x/y for the target
    >>> find([[1,2,3],[2,'O',3]],'O')
    (1, 1)
    '''
    for i in range(len(nested_lst)):
        for j in range(len(nested_lst[i])):
            if nested_lst[i][j] == target:
                return j, i

def solve(maze, current_x, current_y, target_x, target_y):
    
    '''
    inputs: a maze(list), x location, y location, target x location, target y location
    output: maps out the maze.
    >>> solve([['#','#','#','#','#'],['#','S','#',' ','#'],['#',' ','#',' ','#'],['#',' ',' ','E','#'],['#','#','#','#','#']], 1,1,-2,-2)
    [['#', '#', '#', '#', '#'], ['#', '.', '#', ' ', '#'], ['#', '.', '#', ' ', '#'], ['#', '.', '.', 'E', '#'], ['#', '#', '#', '#', '#']]
    '''
    if maze[current_y][current_x] == "E":
        return maze
    if is_move_ok(maze, current_x + 1, current_y):
        maze[current_y][current_x] = "."
        if solve(maze, current_x + 1, current_y, target_x, target_y):
            return maze
    if is_move_ok(maze, current_x - 1, current_y):
        maze[current_y][current_x] = "."
        if solve(maze, current_x - 1, current_y, target_x, target_y):
            return maze
    if is_move_ok(maze, current_x, current_y + 1):
        maze[current_y][current_x] = "."
        if solve(maze, current_x, current_y + 1, target_x, target_y):
            return maze
    if is_move_ok(maze, current_x, current_y - 1):
        maze[current_y][current_x] = "."
        if solve(maze, current_x, current_y - 1, target_x, target_y):
            return maze
    maze[current_y][current_x] = " "

def is_move_ok(maze, destination_x, destination_y):
    '''
    checks to see if the move is okay to make. 
    input: maze (list), x location, y location you are trying to move to
    ouput: true or false weather or not the move is okay to make. 
    >>> is_move_ok([['#','#'],[' ','#']],0,1)
    True
    '''
    if maze[destination_y][destination_x] == " " or maze[destination_y][destination_x] == "E":
        return True
    return False

random_bool = random.choice([True, False])

def print_board(y,x,file):
    '''
    prints the board to a file
    input: y and x (how big you want the maze), file name
    output: prints the maze to a file. 
    '''
    x = int(x)
    y = int(y)
    user_input = file
    open_file = open(user_input, 'w')
    if is_even(x):
        x = x+1
    if is_even(y):
        y = y+1
    my_grid = make_board(x,y)
    for row in my_grid:
        cleaned_line = str(row)
        cleaned_line = cleaned_line.strip("[]")
        cleaned_line = cleaned_line.replace(",", "").replace(" ", "")
        cleaned_line = cleaned_line.replace("'", "")
        cleaned_line = cleaned_line.replace("0", " ")
        open_file.write(cleaned_line)
        open_file.write("\n")
    open_file.close()

def make_board(x,y):
    '''
    input: x and y value signifying how big the maze is. (note that even numbers are rounded up to odd)
    output: generates (right now) an empty maze with the borders
    >>> make_board(5,5)
    [['#', '#', '#', '#', '#'], ['#', 'S', 0, 0, '#'], ['#', 0, '#', 0, '#'], ['#', 0, 0, 'E', '#'], ['#', '#', '#', '#', '#']]
    '''
    empty_list = []
    if is_even(int(x)):
        x = x+1
    if is_even(int(y)):
        y = y+1
    for x_count in range(x):
        empty_list.append([])
        for i in range(y):
            if x_count == 0:
                empty_list[x_count].append("#")
            elif i == 0:
                empty_list[x_count].append("#")
            elif i == int(y-1):
                empty_list[x_count].append("#")
            elif x_count == x-1:
                empty_list[x_count].append("#")
            elif is_even(x_count) and is_even(i):
                empty_list[x_count].append("#")
            else:
                empty_list[x_count].append(0)
    empty_list[1][1] = 'S'
    empty_list[-2][-2] = 'E'
    return empty_list

def is_even(number):
    '''
    input: integer
    output: true or false based on weather int is even or odd.
    >>> is_even(7)
    False
    >>> is_even(6)
    True
    '''
    return (number % 2 == 0)


if __name__ == "__main__":
    args = sys.argv[1:]
    try:
        validate_arg(args)
    except RecursionError as e:
        print(f'{e} error maximum recursion depth exceeded ')
