from OpenGL.GL import *
from OpenGL.GLU import *

class Walls: 
    def __init__(self):
        self.back_wall_vertices = (
            (25, -10, -60),
            (-25, -10, -60),
            (-25, 20, -60),
            (25, 20, -60),
        )


        self.back_wall_surface = (
            (0, 1, 2, 3)
        )
        
        self.floor_vertices = (
            (25, -10, -10),
            (-25, -10, -10),
            (-25, -10, -60),
            (25, -10, -60),   
        )

        self.floor_surface = (
            (0, 1, 2, 3)
        )
        
        self.target_vertices = (
            (-20, -9.5, -55),
            (-25, -9.5, -55),
            (-25, -9.5, -60),
            (-20, -9.5, -60),
        )
        
        self.target_surface = (
            (0, 1, 2, 3)
        )
        
        self.barrier_vertices = (
            (-25, -10, -35),
            (25, -10, -35),
            (25, -5, -35),
            (-25, -5, -35),
            (-25, -10, -30),
            (25, -10, -30),
            (25, -5, -30),
            (-25, -5, -30),
        )
        
        self.barrier_surfaces = (
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (0, 1, 4, 5),
            (2, 3, 6, 7),
            (1, 2, 5, 6),
            (0, 3, 4, 7),
        )
        

    def Draw_Back_Wall(self):
        
        glBegin(GL_QUADS)
        
        for back_wall_vertex in self.back_wall_surface:
            glColor3fv((0, 0, 1))
            glVertex3fv(self.back_wall_vertices[back_wall_vertex])
        
        glEnd()
        
    def Draw_Target(self):
        
        glBegin(GL_QUADS) 
        
        for target_vertex in self.target_surface:
            glColor3fv((0, 1, 1))
            glVertex3fv(self.target_vertices[target_vertex])
        
        glEnd()
    
    def Draw_Barrier(self):
        
        glBegin(GL_QUADS)
        
        for surface in self.barrier_surfaces:
            for vertex in surface:
                glColor3fv((1, 1, 1))
                glVertex3fv(self.barrier_vertices[vertex])
                
        glEnd()
    
    def Draw_Floor(self):
    
        glBegin(GL_QUADS)

        for floor_vertex in self.floor_surface:
            glColor3fv((1, 0, 0))
            glVertex3fv(self.floor_vertices[floor_vertex])

        glEnd()