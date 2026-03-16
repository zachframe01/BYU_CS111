# tree abstraction
def tree(label, branches=[]):
	return [label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_leaf(tree):
	return len(branches(tree)) == 0

# create a simple tree
t = tree(3, [
          tree(1),
          tree(2, [
            tree(1),
            tree(1)
        ])])
# same as: 
# t = [3,[1],[2,[1],[1]]]
# or:
# t = [3,
#        [1],
#        [2,
#          [1],
#          [1]
#        ]
#     ]

print(label(t))
print(is_leaf(branches(t)[0]))

# count the leaves in a tree
def count_leaves(t):
    """Returns the number of leaf nodes in t."""
    if is_leaf(t):
        return 1
    leaves_under = 0
    for b in branches(t):
        leaves_under += count_leaves(b)
    return leaves_under

print(count_leaves(t)) 

# print current tree
print(t) 

# create a tree from another tree, but doubling the value of the labels
def double(t):
    """Returns a tree identical to t, but with all labels doubled."""
    if is_leaf(t):                  # do we really need this base case?
        return tree(label(t) * 2)
    doubled_branches = []
    for b in branches(t):
        doubled_branches.append(double(b))
    return tree(label(t) * 2, doubled_branches)

# print tree with doubled labels    
print(double(t))

# same as above, but using a list comprehension to double the branches below each node
def double(t):
    """Returns a tree identical to t, but with all labels doubled."""
    if is_leaf(t):                  # do we really need this base case?
        return tree(label(t) * 2)
    else:
        return tree(label(t) * 2,[double(b) for b in branches(t)])

# print tree with doubled labels    
print(double(t))
