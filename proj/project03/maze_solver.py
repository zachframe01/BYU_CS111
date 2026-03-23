import sys
import maze_maker
import validate_argv



#move order 
#East (right)
# West (left)
# South (down)
# North (up)
#E == end

#prints the solution as start(s) to end (e)
# It is important to note that the path it finds may not be \n
# the only valid solution or even the shortest solution.


#Success! The path is as follows:
#######
#S....#
# ###.#
# #  .#
#   #E#
#######

#solving format:  python3 maze_solver.py -s <filename>
#hint (zach - maybe use your sodoku file to display the maze. )


#Check the value at the x and y coordinates.
# E (End): Stop searching! You've found the end, you can break the recursive loop and return a successful value to propagate the result.
# # (Wall) or . (Marked): Path is blocked, return a value that will indicate that your current path cannot be followed any further.
#  (Blank) and not S: mark as visited by using a ..

#Base case of above ^^
# If you get a successful value from a direction, that means you found a solution. \n
# Return a success value to propagate the result upward in your recursive call stack.
#return a "Error! Solver could find no solution to maze!" if nothing is found

def find_s(maze):
    '''
    input: maze 
    output: cordinates of the starting position x, y position
    '''
    pass

def this_is_end(x,y):
    '''
    input: x and y cordinates
    output: true or false. True if the cord is = to E. False if wall or empty space.
    '''
    pass

def nesw_is_full(current_x, current_y):
    '''
    returns true or false if a move is all filled. 
    '''




if __name__ == "__main__":
    commands = sys.argv [1:]
    validate_argv.validate_arg(commands)
    maze_maker.print_board()
