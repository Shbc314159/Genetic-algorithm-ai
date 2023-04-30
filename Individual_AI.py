from Cube import Cube
import keyboard

class Individual(Cube):
    def __init__(self, genes):
        super().__init__()
        self.current_move = 0
        self.genes = genes
        self.moves_executed = 0
        self.score = 0
        self.fitness = 0
        self.moves_taken = 1
    
    def update(self):
        if self.current_move < len(self.genes):
            self.move(self.genes[int(self.current_move)])
            self.current_move += 0.05
            self.moves_executed += 1
        
        if self.collide_with_target() == True:
            if self.score == 0:
                self.score += 100
                self.moves_taken = self.moves_executed
            else:
                self.score += 20
                
            print("collision")
            
        
    def collide_with_target(self):
        corner1 = (self.cube_pos[0] + 1, self.cube_pos[2] - 1)
        corner2 = (self.cube_pos[0] + 1, self.cube_pos[2] + 1)
        corner3 = (self.cube_pos[0] - 1, self.cube_pos[2] + 1)
        corner4 = (self.cube_pos[0] - 1, self.cube_pos[2] - 1)
        
        targetxrange = (-20, -25)
        targetzrange = (-55, -60)
        
        if (targetxrange[0] > corner1[0] > targetxrange[1]) and (targetzrange[0] > corner1[1] > targetzrange[1]):
            return True
        elif (targetxrange[0] > corner2[0] > targetxrange[1]) and (targetzrange[0] > corner2[1] > targetzrange[1]):
            return True
        elif (targetxrange[0] > corner3[0] > targetxrange[1]) and (targetzrange[0] > corner3[1] > targetzrange[1]):
            return True
        elif (targetxrange[0] > corner4[0] > targetxrange[1]) and (targetzrange[0] > corner4[1] > targetzrange[1]):
            return True
        else:
            return False
        
    

        
        
        