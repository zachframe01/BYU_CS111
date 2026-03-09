class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
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


# Similar to [x for x in range(3, 6)]
def range_link(start, end):
    """Return a Link containing consecutive integers
    from start to end, not including end.
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    return Link(start, range_link(start + 1, end))

print(range_link(3,6))
print(repr(range_link(3,6)))


def copy_link(ll):
    """Return a list that is a copy of LL
    """
    if ll is Link.empty:
        return Link.empty
    return Link(ll.first,copy_link(ll.rest))

ll = Link(3, Link(4, Link(5)))
print(copy_link(ll))
print(repr(copy_link(ll)))


# For you to try
def map_link(f, ll):
    """Return a Link that contains f(x) for each x 
       in Link LL.
    >>> square = lambda x: x * x
    >>> LL = Link(3, Link(4, Link(5)))
    >>> map_link(square,LL)
    Link(9, Link(16, Link(25)))
    """
    if ll is Link.empty:
        return Link.empty
    return Link(f(ll.first), map_link(f,ll.rest))

LL = Link(3, Link(4, Link(5)))
square = lambda x: x * x
print(map_link(square,LL))
print(repr(map_link(square,LL)))


# For you to try
def filter_link(f, ll):
    """Return a Link that contains only the elements
       x of Link LL for which f(x) is a true value.
    >>> is_odd = lambda x: x % 2 == 1
    >>> LL = Link(3, Link(4, Link(5)))
    >>> filter_link(is_odd, LL)
    Link(3, Link(5))
    """
    if ll is Link.empty:
        return Link.empty
    return Link(f(ll.first), filter_link(f,ll.rest))

LL = Link(3, Link(4, Link(5)))
is_odd = lambda x: x % 2 == 1
print(filter_link(is_odd,LL))
print(repr(filter_link(is_odd,LL)))

# Linked lists are mutable!
s = Link("A", Link("B", Link("C")))
print(s)
s.first = "Hi"
s.rest.first = "Hola"
s.rest.rest.first = "Oi"
print(s)
print(repr(s))

# Beware infinite lists!
s = Link("A", Link("B", Link("C")))
t = s.rest
t.rest = s

print(s.first)
print(s.rest.rest.rest.rest.rest.first)

# For you to try - adding to front of linked list
def insert_front(linked_list, new_val):
    """Inserts new_val in front of linked_list,
    returning new linked list.

    >>> ll = Link(1, Link(3, Link(5)))
    >>> insert_front(ll, 0)
    Link(0, Link(1, Link(3, Link(5))))
    """
    pass

ll = Link(1, Link(3, Link(5)))
print(insert_front(ll,0))
print(repr(insert_front(ll,0)))


# For you to try - adding to an ordered list
def add(ordered_list, new_val):
    """Add new_val to ordered_list, returning modified ordered_list.
    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    """
    if new_val < ordered_list.first:  # insert new Link before the current Link - ho can you do that?
        pass
    elif new_val > ordered_list.first and ordered_list.rest is Link.empty:  # insert new Link at end of list
        pass
    elif new_val > ordered_list.first: # recursively move on to the next Link
        pass
    return ordered_list  # new_val is equal to the value of the current Link (ordered_list.first), 
                         # so don't insert a new Link and just return the rest of the list instead

s = Link(1, Link(3, Link(5)))
print(add(s, 0))
print(add(s, 3))
print(add(s, 4))
print(add(s, 6))
print(repr(s))