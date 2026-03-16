from sys import argv


def merge(el1,el2):
    """
    merge takes 2 arguments (2 lists of integers)
    merge combine 2 lists and them in order 
    """
    new_list = []
    while len(el1) != 0 and len(el2) != 0:
        if el1[0] >= el2[0]:
            new_list.append(el2[0])
            el2.pop(0)
        else:
            new_list.append(el1[0])
            el1.pop(0)
    if len(el1) != 0 and len(el2) == 0:
        new_list.extend(el1)
    elif len(el2) != 0 and len(el1) == 0:
        new_list.extend(el2)
    return new_list


def sorting(l):
    """
    takes a list as an argument
    sorting will split a list into 2 lists recursivly till lenth is 1. 
    after length is 1 it will start to merge at the bottom. 
    this will return a sorted list. 
    """
    if len(l) == 1:
        return l 
    else:
        if is_even(l):  
            return merge(sorting(l[:(len(l))//2]), sorting(l[(len(l))//2:]))
        else:
            return merge(sorting(l[:(len(l))//2]), sorting(l[((len(l))//2):]))

def is_even(l):
    """
    takes in a list as an argument. 
    returns a boolean for if the len(list) is even or odd. 
    """
    return len(l) % 2 == 0


def add_to_list(file):
    """
    takes a file as input. Takes each line in the file and commits those lines as elements in a list.
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