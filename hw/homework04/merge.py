def merge(el1,el2):
    """
    merge takes 2 arguments (2 lists of integers)
    merge combine 2 lists and them in order 
    >>> merge([2],[1])
    [1, 2]
    >>> merge([4,2],[1])
    [1, 4, 2]
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
