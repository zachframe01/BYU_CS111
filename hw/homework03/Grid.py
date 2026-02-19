from copy import deepcopy

class Grid: 

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = []
        for y in range(height):
            row = [None] * self.width
            self.array.append(row)

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
        if y >= len(self.array) or (y < 0):
            return False
        elif (x >= len(self.array[0])) or (x < 0):
            return False
        else:
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
        if self.in_bounds(x,y):
            return self.array[y][x]
        else:
            raise IndexError

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
        if self.in_bounds(x,y):
            self.array[y][x] = val
        else:
            raise IndexError
    
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
        #failed Grid.check_list_malformed([[1, 2], 3])
        #ValueError: Input must be a list of lists.
        #2/4 correct

        #  The object passed in should be a list object
        # The top-level list should not be empty
        # Each element of the list object should also be a list object
        #  (GOOD) Each element of the top-level list should have the same length

        expected_length = len(lst[0]) 

        for i in range(len(lst)):
            if len(lst[i]) != expected_length:
                raise ValueError("All items in list must be lists of the same length.")
            # if i != list:
            #     raise ValueError("it needs to be a list")
            

    
    # @staticmethod
    # def build(lst):
    #     """
    #     Given a list that represents a 2D nested Grid construct a Grid object.
    #     Grid.build([[1, 2, 3], [4, 5 6]])
    #     >>> Grid.build([[1, 2, 3], [4, 5, 6]]).array
    #     [[1, 2, 3], [4, 5, 6]]
    #     """
    #     self.lst = lst
    #     return True
    
    # def __eq__(self, other):
    #     """
    #     >>> grid1 = Grid.build([[1, 1, 1], [2, 3, 5]])
    #     >>> grid2 = Grid.build([[1, 1, 1], [2, 3, 5]])
    #     >>> grid_lst = [[1, 1, 1], [2, 3, 5]]
    #     >>> grid1 == grid2
    #     True
    #     >>> grid1 == grid_lst
    #     True
    #     """
    #     return True
    
    # def __str__(self):
    #     """
    #     >>> print(Grid(6, 2))
    #     Grid(6, 2, first = None)
    #     """
    #     return True
    
    # def __repr__(self):
    #     """
    #     >>> repr(Grid.build([[5, 5], [3, 2]]))
    #     'Grid.build([[5, 5], [3, 2]])'
    #     """
    #     return f"Grid({self.width}, {self.height}, array={self.array})"
    
