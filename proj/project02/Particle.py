from Grid import Grid

class Particle:
    '''
    3 particles in the class particle: sand, bubble, rock
    rocks stay still, sand falls, bubbles rise. 
    The particle object has a grid (class/object), x and y value (int)
    '''

    def __init__(self, grid, x=0 ,y=0):
        '''
        
        inputs: Particle has a grid, x value (int), and a y value (int)
        outputs: makes an object (particle) which can be changed later. 
        '''
        self.x = x
        self.y = y
        self.grid = grid
    def __str__(self):
        '''
        input the self/object. 
        outputs a human readable string. 
        '''
        return f"{type(self).__name__}({self.x},{self.y})"
    def move(self):
        '''
        input: class/object 
        output: will move the object in a specified way. (rock/bubble/sand)
        this funciton will call on each particle to show how to behave. 
        Rock will stay the same.
        Sand will fall down the array.
        Bubbles will float. 
        '''
        physics_value =self.physics()
        if physics_value != None:
            old_x = self.x
            old_y = self.y
            self.x , self.y = physics_value
            self.grid.set(self.x, self.y, self)
            self.grid.set(old_x, old_y, None)

