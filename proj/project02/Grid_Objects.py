#15 passed.
from Grid import Grid
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
        '''physics of bubble will rise to a higher point in an array unless blocked.'''
        #order is down, down/left, down/right, blocked, corner rule
        # get location of sand
        # check below sand (make sure in bounds) no rock 
        #check to left and right (make sure in bounds) no rock
        # check diagonally left and right (no rocks) and in bounds
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
            

# if __name__ == '__main__':
#     grid = Grid.build([[None, None, None],[None, None, None]])
#     sand = Sand(grid, 1, 0)
#     grid.set(1,0,sand)
#     sand.move()
#     grid.get(0,1)
#     grid.get(1,1)
#     print(grid)
