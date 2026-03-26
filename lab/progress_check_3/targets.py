CLASS_CODE = "PLEASE_UPDATE_CLASS_CODE"


class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(
            rest, Link), "Link does not follow proper structure"
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
def count_targets(link, targets):
    return count_targets_iterative(link, targets)
    # return count_targets_recursive(link, targets)
    ...

def count_targets_iterative(link, targets):
    """YOUR CODE HERE"""
    my_dict = {x:0 for x in targets}
    while link.rest != None:
        for key in list(my_dict):
            if key == link.first:
                my_dict[key] +=1
        link.first = link.rest
    return my_dict



def count_targets_recursive(link, targets):
    my_dict = {}
    for target in targets:
        my_dict[target] = 0
    new_list = get_list(link)
    for element in new_list:
        for key in my_dict:
            if key == element:
                my_dict[key] += 1
    for key in list(my_dict):
        if my_dict[key] == 0:
            del my_dict[key]
    return my_dict


def get_list(link):
    new_list = []
    if link.rest == ():
        return [link.first]
    new_list.append(link.first)
    return new_list + get_list(link.rest)

def make_link(list):
    pass

def remove_targets(link, targets):
    my_dict = count_targets_recursive(link,targets)
    for key in my_dict:
        if link.first == key: 
            remove_targets(link.rest,targets)

    return Link(link.first, remove_targets(link.rest,targets))


if __name__ == "__main__":
    link = Link('c', Link(2, Link(2, Link('a', Link('b', Link(4, Link('t', Link(2, Link('s', Link(4))))))))))
    targets = [2, 4, 'b']
    print(count_targets(link,targets))