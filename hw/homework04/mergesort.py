from sys import argv


def merge(list_one,list_two):
    """
    merge takes 2 arguments (2 lists of integers)
    merge combine 2 lists and them in order 
    """
    new_list = []
    while len(list_one) != 0 and len(list_two) != 0:
        if list_one[0] >= list_two[0]:
            new_list.append(list_two[0])
            list_two.pop(0)
        else:
            new_list.append(list_one[0])
            list_one.pop(0)
    if len(list_one) != 0 and len(list_two) == 0:
        new_list.extend(list_one)
    elif len(list_two) != 0 and len(list_one) == 0:
        new_list.extend(list_two)
    return new_list


def sorting(list):
    """
    takes a list as an argument
    sorting will split a list into 2 lists recursivly till lenth is 1. 
    after length is 1 it will start to merge at the bottom. 
    this will return a sorted list. 
    """
    if len(list) == 1:
        return list 
    else:
        if is_even(list):  
            return merge(sorting(list[:(len(list))//2]), sorting(list[(len(list))//2:]))
        else:
            return merge(sorting(list[:(len(list))//2]), sorting(list[((len(list))//2):]))

def is_even(list):
    """
    takes in a list as an argument. 
    returns a boolean for if the len(list) is even or odd. 
    """
    return len(list) % 2 == 0


def add_to_list(file):
    """
    takes a file as input. 
    Takes each line in the file and commits those lines as elements in a list.
    """
    for line in file:
        mega_list.append(line)

if __name__ == "__main__":
    user_files = argv[:]
    file1 = open(user_files[1], "r")
    output_file = open(user_files[2], "w")
    mega_list = []
    add_to_list(file1)
    for line in sorting(mega_list):
        output_file.write(f'{str(line)}')
    file1.close()
    output_file.close()