CLASS_CODE = "CS111_W26_LINKED_AROUND_TARGET"


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

def count_targets_iterative(link, targets):
    """WILL COUNT THE TARGETS ITERATIVELY. """
    empty_dict = dict()
    string_link = str(link)
    string_link = string_link.split('>')
    string_link = string_link[0]
    string_link = string_link.split('<')
    string_link = string_link[1]
    string_link = string_link.split(' ')
    for el1 in string_link:
        for el2 in targets:
            if el1 == el2:
                empty_dict()
                


def count_targets_recursive(link, targets):
    """WILL COUNT THE TARGETS RECRUSIVELY"""
    if link.rest == ():
        for element in targets:
            if element == link.first:
                my_list.append(element)
                my_dict.update(element=0)
        return
    else:
        for element in targets:
            if element == link.first:
                my_list.append(element)
        count_targets_recursive(link.rest, targets)
    return

def remove_targets(link, targets):
    if link.rest != ():
        for element in targets:
            if element == link.first:
                Link.self.first = Link.self.rest
                remove_targets(link.rest, targets)
    elif link.rest == ():
        return
    else:
        return 


link = Link('c', Link(2, Link(2, Link('a', Link('b', Link(4, Link('t', Link(2, Link('s', Link(4))))))))))
# count_targets_iterative(link, 2)
my_list = []
my_dict = {}
print(count_targets_recursive(link, [2,4]))
print(my_list)
print(my_dict)
my_dict.fromkeys(my_list)
print(my_dict)
mi = [1,2,3]
md = {}
print(md)
# >>> targets = [2, 4, 'b']
# >>> count_targets(link, targets)
# {2: 3, 'b': 1, 4: 2}
# >>> link = remove_targets(link, targets)
# >>> print(link)
# <c a t s>
# >>> count_targets(link, targets)
# {}


#