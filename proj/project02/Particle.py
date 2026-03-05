from Grid import Grid

class Particle:

    def __init__(self, grid, x=0 ,y=0):
        self.x = x
        self.y = y
        self.grid = grid
    def __str__(self):
        return f"{type(self).__name__}(({self.x}), ({self.y}))"
    def move(self):
        self.physics = physics(self)
        pass
    def physics(self):
        pass
    
class Rock(Particle):
    pass

class Sand(Particle):
    pass

class Bubble(Particle):
    pass