from OpenGL.GL import *
from OpenGL.GLU import *

import math
import random

class Cube():
    def __init__(self):
        self.cube_pos = [-15, -9, -50]
        self.velocity = [0, 0, 0]  
        self.acceleration = [0, 0, 0]  
        self.friction_coefficient = 0.9
        self.force_applied = 0.01
        self.mass = 100
        self.direction = random.randint(0, 360)
        self.vertices = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
            )

        self.surfaces = (
            (0,1,2,3),
            (3,2,7,6),
            (6,7,5,4),
            (4,5,1,0),
            (1,5,7,2),
            (4,0,3,6)
        )
    
    def move(self, movement):
        if movement == "w":
            self.acceleration[0] += self.force_applied/self.mass
        else:
            if self.velocity[0] > 0:
                self.acceleration[0] -= self.friction_coefficient
            else:
                self.acceleration[0] = 0
                self.velocity[0] = 0   
                
            if movement == "d":
                self.direction -= 1
            elif movement == "a":
                self.direction += 1
        
        if self.direction >= 360:
            self.direction -= 360
        elif self.direction <= 0:
            self.direction += 360
        
        direction_x = math.sin(math.radians(self.direction))
        direction_z = math.cos(math.radians(self.direction))
        
        self.velocity[0] += self.acceleration[0]
        
        self.cube_pos[0] += max(self.velocity[0], 0) * direction_x
        self.cube_pos[2] += max(self.velocity[0], 0) * direction_z
        
        if self.cube_pos[2] - 1 < -60:
            self.cube_pos[2] = -59

    
    def draw(self):
        glPushMatrix()
        glTranslatef(*self.cube_pos)
        glRotatef(self.direction, 0, 1, 0)
        
        glBegin(GL_QUADS)
        
        for surface in self.surfaces:
            for vertex in surface:
                if surface == (6,7,5,4):
                    glColor3fv((0, 0, 1))
                    glVertex3fv(self.vertices[vertex])
                else:
                    glColor3fv((0, 1, 0))
                    glVertex3fv(self.vertices[vertex])
                
        glEnd()
        
        glPopMatrix()
        