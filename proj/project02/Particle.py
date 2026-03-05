from Grid import Grid

class Particle:

    def __init__(self, grid, x=0 ,y=0):
        self.x = x
        self.y = y
        self.grid = grid
    def __str__(self):
        return f"{type(self).__name__}({self.x},{self.y})"
    def move(self):
        '''
        this funciton will call on each particle to show how to behave. 
        Rock will stay the same.
        Sand will fall down the array.
        Bubbles will float. 
        '''
        self.physics
        pass

