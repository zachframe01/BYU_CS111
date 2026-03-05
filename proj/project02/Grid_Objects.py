#15 passed.
from Particle import Particle

class Rock(Particle):
    def physics(self):
        '''defines the physics of a rock. Rocks stay still.'''
        return None
class Sand(Particle):
    def physics(self):
        '''physics of sand will fall to a lower point in an array unless blocked.'''
        #order is down, down/left, down/right, blocked, corner rule
        # get location of sand
        # check below sand (make sure in bounds) no rock 
        #check to left and right (make sure in bounds) no rock
        # check diagonally left and right (no rocks) and in bounds
        if self.is_move_ok(self.x, self.y + 1):
            self.y = self.y + 1
        elif self.is_move_ok(self.x-1, self.y + 1) & (self.grid.in_bounds(self.x-1, self.y + 1) & self.grid.get(self.x-1, self.y + 1) == None): 
            self.x = self.x-1
            self.y = self.y + 1
        elif self.is_move_ok(self.x+1, self.y + 1) & (self.grid.in_bounds(self.x+1, self.y + 1) & self.grid.get(self.x+1, self.y + 1) == None): 
            self.x = self.x+1
            self.y = self.y + 1
        
    def is_move_ok(self,x,y):
        if self.grid.get(x, y) == None & self.grid.in_bounds(x, y):
            return True
        else: 
            return False
class Bubble(Particle):
    def physics(self):
        '''physics of bubble will rise to a higher point in an array unless blocked.'''
        pass
