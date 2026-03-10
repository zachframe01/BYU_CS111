from Link import Link

def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    new_list = []
    x = str(link)
    x = x.strip('<')
    x = x.strip('>')
    x = x.split(' ')
    for x in x:
        new_list.append(int(x))
    return new_list

def convert_link_2(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    new_list = []
    while link is not Link.empty:
        new_list.append(link.first)
        link = link.rest
    return new_list

def convert_link_3(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """

    if link is Link.empty:
        return []
    return [link.first] + convert_link_3(link.rest)


link = Link(1, Link(2, Link(3, Link(4))))
print(convert_link(link))
print(convert_link_2(link))
print(convert_link_3(link))



def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    if link is Link.empty:
        return 
    return link.first + store_digits(link.rest)
store_digits(link)


def every_other(link):
    """Mutates a linked list so that all the odd-indexed elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    if link is Link.empty:
        return []
    return [link.first] + convert_link_3(link.rest)


def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> link1
    Link(9, Link(Link(16), Link(25, Link(36))))
    """
    if link is Link.empty:
        return
    if not isinstance(link.first, int):
        deep_map_mut(fn, link.first)
    else:
        link.first = fn(link.first)
    deep_map_mut(fn,link.rest)

link1 = Link(3, Link(Link(4), Link(5, Link(6))))
deep_map_mut(lambda x: x * x, link1)
print(link1)
