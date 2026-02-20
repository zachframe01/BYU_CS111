from Grid import Grid

grid1 = Grid.build([[1, 1, 1], [2, 3, 5]])
grid2 = Grid.build([[1, 1, 1], [2, 3, 5]])
grid_lst = [[1, 1, 1], [2, 3, 5]]

grid1 == grid2
grid1 == grid_lst
# Expecting:
#     True
grid1 == grid_lst