import sys
import maze_maker
import maze_solver

def validate_arg(command):
    '''
    input: the argv artguments
    output: true or false depending on if the arguments meet specified criteria. 
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
    '''
    if len(command) != 4:
        print(f'Usage: python3 maze_solver.py [-s maze_file] [-g width height maze_file]')
        return False
    elif int(command[1]) <= 2 or int(command[2]) <= 4:
        print(f'Error! The minimum maze size is 3x5!')
        return False
    maze_maker.print_board(command[1],command[2],command[3])
    return True

def validate_solve(command):
    '''
    input: the argv artguments
    output: true or false depending on if the arguments meet specified criteria. 
    '''
    if len(command) != 2:
        print(f'Usage: python3 maze_solver.py [-s maze_file] [-g width height maze_file]')
        return False
    maze_solver.construct(command[1])
    return True