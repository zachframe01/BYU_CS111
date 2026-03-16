# def merge(el1,el2):
#     """
#     merge takes 2 arguments (2 lists of integers)
#     merge combine 2 lists and them in order 
#     >>> merge([2],[1])
#     [1,2]
#     >>> merge([4,2],[1])
#     [1,2,4]
#     """
#     index2 = 0
#     new_list = []
#     for element in el1:
#         if index2 >= len(el2):
#             new_list.append(element)
#         elif int(element) <= int(el2[index2]):
#             new_list.append(element)
#         else:
#             new_list.append(el2[index2])
#             index2 += 1
#     return new_list

def merge(el1,el2):
    """
    merge takes 2 arguments (2 lists of integers)
    merge combine 2 lists and them in order 
    >>> merge([2],[1])
    [1,2]
    >>> merge([4,2],[1])
    [1, 2, 4]
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

        

print(merge([2,4],[1,4,5,6]))
print(merge([2,4],[1,4,5,6]))
print(merge([4,2],[1]))
print(type((merge([4,2],[1]))[0]))
print((merge([4,2],[1]))[0])