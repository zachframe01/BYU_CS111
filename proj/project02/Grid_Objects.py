#15 passed.
from Grid import Grid
from Particle import Particle

class Rock(Particle):
    def physics(self):
        '''defines the physics of a rock. Rocks stay still.'''
        return None
class Sand(Particle):
    def physics(self):
        '''
        physics of sand will fall to a lower point in an array unless blocked.
        order is down, down/left, down/right, blocked, corner rule
        '''
        if self.is_move_ok(self.x, self.y):
            if self.grid.get(self.x, self.y+1) == None:
                return self.x,self.y+1
            elif (self.grid.get(self.x-1, self.y+1) == None and
                self.grid.get(self.x-1, self.y) == None):
                return (self.x-1,self.y+1)
            elif (self.grid.get(self.x+1, self.y+1) == None and
                self.grid.get(self.x+1, self.y) == None):
                return self.x+1,self.y+1
        return None
    def is_move_ok(self,x,y):
        '''
        checks if the move is okay. if the move is filled with rock or other particles, it will
        return a false. If move is okay, it will return true. 
        '''
        if (self.grid.in_bounds(x, y+1) and 
            self.grid.get(x, y+1) == None):
            return True
        elif (self.grid.in_bounds(self.x-1, self.y) and
            self.grid.in_bounds(self.x-1, self.y + 1) and 
            self.grid.get(self.x-1, self.y) == None and
            self.grid.get(self.x-1, self.y+1) == None):
            return True
        elif (self.grid.in_bounds(self.x+1, self.y) and
            self.grid.in_bounds(self.x+1, self.y + 1) and 
            self.grid.get(self.x+1, self.y) == None and
            self.grid.get(self.x+1, self.y+1) == None):
            return True
        else: 
            return False
class Bubble(Particle):
    def physics(self):
        '''
        physics of bubble will rise to a higher point in an array unless blocked.
        order of movement is up, up/left, up/right, blocked, corner rule       
        '''

        if self.is_move_ok(self.x, self.y - 1):
            return self.x,self.y-1
        elif (self.is_move_ok(self.x+1, self.y - 1) and 
              self.grid.get(self.x+1, self.y) == None):
            return self.x+1, self.y - 1
        elif (self.is_move_ok(self.x-1, self.y - 1) and 
              self.grid.get(self.x-1, self.y) == None):
            return self.x-1, self.y - 1
        return None
    def is_move_ok(self,x,y):
        if (self.grid.in_bounds(x, y) and 
            self.grid.get(x, y) == None):
            return True
        else:
            return False