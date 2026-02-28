from Grid import Grid

class Particle:

    def __init__(self, grid, x=0 ,y=0):
        self.x = x
        self.y = y
        self.grid = grid
        
        pass
    def __str__(self):
        return f"{type(self).__name__}(({self.x}), ({self.y}))"
