import sys
import validate_argv
import maze_maker

def construct(filename):
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
    for i in range(len(nested_lst)):
        for j in range(len(nested_lst[i])):
            if nested_lst[i][j] == target:
                return j, i

def solve(maze, current_x, current_y, target_x, target_y):
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
    if maze[destination_y][destination_x] == " " or maze[destination_y][destination_x] == "E":
        return True
    return False

if __name__ == "__main__":
    args = sys.argv[1:]
    validate_argv.validate_arg(args)
    # commands = ['-g', '11', '12', 'example1.txt']
    # validate_argv.validate_arg(commands)
    # if args[0] == "-s":
    #     construct(args[1])
    # commands =['-s', 'proj/project03/test_files/maze1.txt']
    # commands =['-s', 'test_files/maze1.txt']
    # validate_argv.validate_arg(commands)
    pass
