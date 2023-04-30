from Cube import Cube

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
        
        if self.collide_with_target() == True and self.score == 0:
            self.score += 100
            self.moves_taken = self.moves_executed
            print("collision")
            
        
    def collide_with_target(self):
        self.x_limits = (self.cube_pos[0] + 1, self.cube_pos[0] - 1)
        self.z_limits = (self.cube_pos[2] + 1, self.cube_pos[2] - 1)
        self.target_x_limits = (-25, -20)
        self.target_z_limits = (-60, -55)

        if self.x_limits[1] >= self.target_x_limits[1] or  \
            self.x_limits[0] <= self.target_x_limits[1] or \
            self.z_limits[1] >= self.target_z_limits[1] or \
            self.z_limits[0] <= self.target_z_limits[0]:
                return False
        else:     
            return True
        
    

        
        
        