from Cube import Cube
import keyboard
import globalvars

class Individual(Cube):
    def __init__(self, genes):
        super().__init__()
        self.current_move = 0
        self.genes = genes
        self.moves_executed = 0
        self.score = 0
        self.fitness = 0
        self.moves_taken = 1
        x_center = sum(vertex[0] for vertex in globalvars.target_vertices) / len(globalvars.target_vertices)
        y_center = sum(vertex[1] for vertex in globalvars.target_vertices) / len(globalvars.target_vertices)
        z_center = sum(vertex[2] for vertex in globalvars.target_vertices) / len(globalvars.target_vertices)
        self.target_centre = [x_center, y_center, z_center]
    
    def update(self):
        if self.current_move < len(self.genes):
            self.move(self.genes[int(self.current_move)])
            
            if keyboard.is_pressed("w"):
 #               self.move("w")
  #          elif keyboard.is_pressed("a"):
   #             self.move("a")
    #        elif keyboard.is_pressed("d"):
     #           self.move("d")
      #      elif keyboard.is_pressed("u"):
       #         self.move("u")
                pass
            
            self.current_move += 0.2
            self.moves_executed += 1
            
        self.distance_from_target = ((self.target_centre[0] - self.cube_pos[0]) ** 2 + 
                            (self.target_centre[1] - self.cube_pos[1]) ** 2 + 
                            (self.target_centre[2] - self.cube_pos[2]) ** 2) ** 0.5 
        self.score += 1/self.distance_from_target ** 10
        
            
        
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
        
    

        
        
        