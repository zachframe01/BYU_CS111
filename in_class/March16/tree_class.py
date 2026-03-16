# now working with a Tree class instead of a tree data abstraction
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

# double the value of every label, mutating the tree (not creating a new tree!)
def double(t):
    """Doubles every label in t, mutating t.
    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> double(t)
    >>> t
    Tree(2, [Tree(6, [Tree(10)]), Tree(14)])
    """
    t.label *= 2
    for b in t.branches:
        double(b)
    return

t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
print(t)
double(t)
print(t)
print(repr(t))

# For you to do: create a *NEW* tree, doubling the value of every label in the original
def double(t):
    """Return a new tree with every label in t doubled
    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> t2 = double(t)
    >>> t2
    Tree(2, [Tree(6, [Tree(10)]), Tree(14)])
    """
    return  Tree(t.label *2 , [double(branch) for branch in t.branches])

t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
print(t)
t2 = double(t)
print(t2) 
print(repr(t2))
print(t is t2)

# For you to do: delete all sub-trees with label n
def prune(t, n):
    """Prune all sub-trees whose label is n.
    >>> t = Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, 
            [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
    >>> prune(t, 1)
    >>> t
    Tree(3, [Tree(2)])
    """
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
       prune('put an expression here','put an expression here')

t = Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, 
            [Tree(1), Tree(1, [Tree(0), Tree(1)])])])
print(t)
prune(t,1)
print(t)
print(repr(t))
