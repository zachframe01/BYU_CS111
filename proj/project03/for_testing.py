from sys import argv




def solve(maze, current_x, current_y, target_x, target_y):
    '''
    inputs: a maze(list), x location, y location, target x location, target y location
    output: maps out the maze.
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
    '''
    if maze[destination_y][destination_x] == " " or maze[destination_y][destination_x] == "E":
        return True
    return False

if __name__ == "__main__":
    maze = [['#','#'],[' ','#']]
    print(is_move_ok(maze,0,1))

    pass
#####
#S# #
# # #
#  E#
#####

    