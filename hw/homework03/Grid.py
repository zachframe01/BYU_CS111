from copy import deepcopy

class Grid: 

    def __init__(self, width, height):
        self.width = width
        self.height = height



    def in_bounds(self, x, y):
        """
        Returns True if (x, y) is in bounds
        >>> grid = Grid(3, 4)
        >>> grid.in_bounds(0, 0)
        True
        >>> grid.in_bounds(2, 3)
        True
        >>> grid.in_bounds(-1, -1)
        False
        >>> grid.in_bounds(3, 4)
        False
        """
        return True

    def get(self, x, y):
        """
        Gets the value stored value at (x, y).
        (x, y) should be in bounds.
        >>> grid = Grid(2, 2)
        >>> grid.array = [[1, 2], [4, 5]]
        >>> grid.get(0, 1)
        4
        >>> grid.get(1, 0)
        2
        """
        return True

    def set(self, x, y, val):
        """
        Sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        >>> grid = Grid(2, 2)
        >>> grid.set(1, 1, "Milk")
        >>> grid.set(1, 0, "Dud")
        >>> grid.array
        [[None, 'Dud'], [None, 'Milk']]
        """
        return True
    
    @staticmethod
    def check_list_malformed(lst):
        """
        Given a list that represents a 2D nested Grid, check that it has the
        right shape. Raise a ValueError if it is malformed.
        >>> Grid.check_list_malformed([[1, 2], [4, 5]])
        >>> Grid.check_list_malformed(1)
        Traceback (most recent call last):
        ...
        ValueError: Input must be a non-empty list of lists.
        >>> Grid.check_list_malformed([[1, 2], [4, 5, 6]])
        Traceback (most recent call last):
        ...
        ValueError: All items in list must be lists of the same length.
        >>> Grid.check_list_malformed([[1, 2], 3])
        Traceback (most recent call last):
        ...
        ValueError: Input must be a list of lists.
        """
        return True
    
    @staticmethod
    def build(lst):
        """
        Given a list that represents a 2D nested Grid construct a Grid object.
        Grid.build([[1, 2, 3], [4, 5 6]])
        >>> Grid.build([[1, 2, 3], [4, 5, 6]]).array
        [[1, 2, 3], [4, 5, 6]]
        """
        return True
    
    def __eq__(self, other):
        """
        >>> grid1 = Grid.build([[1, 1, 1], [2, 3, 5]])
        >>> grid2 = Grid.build([[1, 1, 1], [2, 3, 5]])
        >>> grid_lst = [[1, 1, 1], [2, 3, 5]]
        >>> grid1 == grid2
        True
        >>> grid1 == grid_lst
        True
        """
        return True
    
    def __str__(self):
        """
        >>> print(Grid(6, 2))
        Grid(6, 2, first = None)
        """
        return True
    
    def __repr__(self):
        """
        >>> repr(Grid.build([[5, 5], [3, 2]]))
        'Grid.build([[5, 5], [3, 2]])'
        """
        return True
    
