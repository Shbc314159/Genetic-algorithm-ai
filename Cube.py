from OpenGL.GL import *
from OpenGL.GLU import *

import math
import globalvars

class Cube():
    def __init__(self):
        self.cube_pos = [15, -9, -15]
        self.velocity = [0, 0]  
        self.acceleration = [0, 0] 
        self.friction_coefficient = 0.9
        self.gravity = -0.2
        self.force_up = 2
        self.force_horizontal = 1
        self.mass = 100
        self.direction = 45
        self.touching_ground = False
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
        
        self.current_vertices = ()
    
    def move(self, movement):
        self.horizontal_movement(movement)
        self.vertical_movement(movement)
        self.set_direction(movement)
        self.velocity_acceleration(movement)
        self.collision_detections()
            
    
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
    
    def horizontal_movement(self, movement):
        if movement == "w":
            self.acceleration[0] += self.force_horizontal/self.mass
        else:
            if self.velocity[0] > 0:
                self.acceleration[0] -= self.friction_coefficient
            else:
                self.acceleration[0] = 0
                self.velocity[0] = 0   
                
            if movement == "d":
                self.direction -= 5
            elif movement == "a":
                self.direction += 5
            elif movement == " ":
                self.direction += 360
    
    def vertical_movement(self, movement):
        #up/down movement calculations
        if self.over_floor() and (self.cube_pos[1] <= -9 or self.touching_ground == True):
            if movement == "u":
                self.velocity[1] = 0
                self.acceleration[1] = self.force_up
            else:
                self.acceleration[1] = 0
                
        if not self.over_floor():
            self.acceleration[1] = self.gravity
            
        if self.cube_pos[1] > -9 and self.touching_ground != True:
            self.acceleration[1] = self.gravity
    
    def set_direction(self, movement):
        #set direction and calculate angular velocity   
        if self.direction >= 360:
            self.direction -= 360
        elif self.direction <= 0:
            self.direction += 360
        
        self.direction_x = math.sin(math.radians(self.direction))
        self.direction_z = math.cos(math.radians(self.direction))
        
       
    def velocity_acceleration(self, movement): 
        #set velocities and accelerations
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        
        self.cube_pos[0] += max(self.velocity[0], 0) * self.direction_x
        self.cube_pos[1] += self.velocity[1]
        self.cube_pos[2] += max(self.velocity[0], 0) * self.direction_z
        
        self.touching_ground = False
        
    def collision_detections(self):
        if self.cube_pos[2] - 1 < -60:
            self.cube_pos[2] = -59
                
        if self.over_floor() and self.cube_pos[1] < -9:
            self.cube_pos[1] = -9
            
        for barrier in globalvars.barriers:
            collisionpoints = self.collides_with(self.current_vertices, barrier.vertices)
            self.adjust_pos_collision(collisionpoints, barrier.vertices)
            
        self.current_vertices = self.get_current_vertices()  
        
    def over_floor(self):
        if 25 >= self.cube_pos[0] >= -25:
            if -10 >= self.cube_pos[2] >= -60:
                return True
        
        
    def point_within(self, point, xmin, xmax, ymin, ymax, zmin, zmax):
        if xmin <= point[0] <= xmax:
            if ymin <= point[1] <= ymax:
                if zmin <= point[2] <= zmax:
                    return True
            
    def collides_with(self, obj1_vertices, obj2_vertices):
        target_xpoints = [element[0] for element in obj2_vertices]
        target_ypoints = [element[1] for element in obj2_vertices]
        target_zpoints = [element[2] for element in obj2_vertices]
        
        xmax, xmin = max(target_xpoints), min(target_xpoints)
        ymax, ymin = max(target_ypoints), min(target_ypoints)
        zmax, zmin = max(target_zpoints), min(target_zpoints)
        
        pointcollided = None
        pointscollided = []
        
        for vertice in obj1_vertices:
            if self.point_within(vertice, xmin, xmax, ymin, ymax, zmin, zmax):
                pointcollided = obj1_vertices.index(vertice)
                pointscollided.append(pointcollided)
                
        return pointscollided
        
    
    def adjust_pos_collision(self, collisionpoints, vertices):
        xmin, xmax, ymin, ymax, zmin, zmax = self.vertices_minmax(vertices)
        
        if collisionpoints == [0, 1, 2, 3]:
            self.cube_pos[2] = zmax + 1
            self.acceleration[0] = 0
        elif collisionpoints == [4, 5, 6, 7]:
            self.cube_pos[2] = zmin - 1
            self.acceleration[0] = 0
        elif collisionpoints == [2, 3, 6, 7]:
            self.cube_pos[0] = xmax + 1
            self.acceleration[0] = 0
        elif collisionpoints == [0, 1, 4, 5]:
            self.cube_pos[0] = xmin - 1
            self.acceleration[0] = 0
        elif collisionpoints == [0, 3, 4, 6]:
            self.touching_ground = True
            if self.cube_pos[1] < ymax + 1: 
                self.cube_pos[1] = ymax + 1
                self.velocity[1] = 0
        elif collisionpoints == [0, 3] or \
            collisionpoints == [0, 4] or \
            collisionpoints == [3, 6] or \
            collisionpoints == [4, 6]:
            self.touching_ground = True
            if self.cube_pos[1] < ymax + 1:
                self.cube_pos[1] = ymax + 1
                
    def vertices_minmax(self, vertices):
        results = []
        for i in range(0, 3):
            column_values = [row[i] for row in vertices]
            smallest_value = min(column_values)
            largest_value = max(column_values)
            results.append(smallest_value)
            results.append(largest_value)

        return results
    
    def get_current_vertices(self):
        return (
            (self.cube_pos[0]+1, self.cube_pos[1]-1, self.cube_pos[2]-1),
            (self.cube_pos[0]+1, self.cube_pos[1]+1, self.cube_pos[2]-1),
            (self.cube_pos[0]-1, self.cube_pos[1]+1, self.cube_pos[2]-1),
            (self.cube_pos[0]-1, self.cube_pos[1]-1, self.cube_pos[2]-1),
            (self.cube_pos[0]+1, self.cube_pos[1]-1, self.cube_pos[2]+1),
            (self.cube_pos[0]+1, self.cube_pos[1]+1, self.cube_pos[2]+1),
            (self.cube_pos[0]-1, self.cube_pos[1]-1, self.cube_pos[2]+1),
            (self.cube_pos[0]-1, self.cube_pos[1]+1, self.cube_pos[2]+1)
        )
        
            
            