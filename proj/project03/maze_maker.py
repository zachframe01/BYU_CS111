# The program should take in the width and height of the maze as well as the output filename.
#ensure that they are rounded up to an odd value when the input is even. 
#uses the correctly rounded dimensions
# has walls all along the outside border
# places S at the top-left interior cell
# places E at the bottom-right interior cell
# only uses valid maze characters (#, S, E, and spaces)
# contains a path from S to E


# Command
# One possible example1.txt
# python3 maze_solver.py -g 5 4 example1.txt

# #####
# #S# #
# # # #
# #  E#
# #####

#-s will start solving a maze
# maze_file is the only other argument taken in this mode and should be a .txt file containing the maze to solve

#-g will start generating a maze

# width width of the maze to generate
# height height of the maze to generate
# maze_file the output .txt file to save the generated maze to

# When maze_solver.py is passed invalid input arguments, or encounters an exception while performing \n
# any operations, it should print a user-friendly message indicating an error has occurred and why.

#Error Examples
# No Solution to Maze
# If there is no solution to an input maze file, your program should report that condition to the user. For grading purposes, your program should print a message starting with Error and then containing the words no solution somewhere in the full message

# python3 maze_solver.py -s bad_maze.txt
# Error! Solver could find no solution to maze!
# Invalid or Missing Arguments
# python3 maze_solver.py -s
# Usage: python3 maze_solver.py [-s maze_file] [-g width height maze_file]
# Your implementation can change the names representing the inputs, but your help message should contain Usage: and then each of the operation flags with their corresponding inputs.

# Invalid Maze Size for Generation
# python3 maze_solver.py -g 3 3 maze.txt
# Error! Minimum maze size is 3x5!
# Your implementation should contain E

# Hint

# You should use the string representation of any exceptions that you catch as the description of the issue when possible.
#pytest test_maze_solver.py

#minimu 3x5

#python3 maze_solver.py -g 5 4 example1.txt
#####
#S# #
# # #
#  E#
#####

import sys

def print_board(x,y,file):
    # Print the board in a readable format.
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
    '''
    empty_list = []
    if is_even(x):
        x = x+1
    if is_even(y):
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
            else:
                empty_list[x_count].append(0)
    empty_list[1][1] = 'S'
    empty_list[-2][-2] = 'E'
            

    return empty_list

def look_at_maze(list):
    for row in list:
        print(row)

    # for row in range(len(x)):
    #     if row % 3 == 0 and row != 0:
    #         print("-" * 21)
    #     line = ""
    #     for col in range(len(board[row])):
    #         if col % 3 == 0 and col != 0:
    #             line += "| "
    #         val = board[row][col]
    #         line += (str(val) if val != 0 else ".") + " "
    #     print(line)

def is_even(number):
    '''
    input: integer
    output: true or false based on weather int is even or odd.
    '''
    return (number % 2 == 0)



if __name__ == "__main__":
    print_board(9,8,"example1.txt")