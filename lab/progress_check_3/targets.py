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
    # return count_targets_iterative(link, targets)
    # return count_targets_recursive(link, targets)
    ...

def count_targets_iterative(link, targets):
    """YOUR CODE HERE"""
    pass

def count_targets_recursive(link, targets):
    """YOUR CODE HERE"""

    pass

def remove_targets(link, targets):
    """YOUR CODE HERE"""


if __name__ == "__main__":
    my_list = [2,4,5]
    second_list = [2,2,2,2,4,3,2]
    my_dict = {}
    for keys in my_list:
        my_dict[keys]=0
    print(my_dict)
    for key in second_list:
        if key in my_dict:
            my_dict[key]+=1
        else:
            pass

    print(my_dict)
            