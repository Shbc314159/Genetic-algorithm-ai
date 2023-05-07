from OpenGL.GL import *
from OpenGL.GLU import *

class Barrier():
    def __init__(self, xmin, xmax, ymin, ymax, zmin, zmax):
        self.vertices = (
            (xmin, ymin, zmin),
            (xmax, ymin, zmin),
            (xmax, ymax, zmin),
            (xmin, ymax, zmin),
            (xmin, ymin, zmax),
            (xmax, ymin, zmax),
            (xmax, ymax, zmax),
            (xmin, ymax, zmax),
        )
        
        self.surfaces = (
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (0, 1, 4, 5),
            (2, 3, 6, 7),
            (1, 2, 5, 6),
            (0, 3, 4, 7),
        )
    
    def draw(self):
        glBegin(GL_QUADS)
        
        for surface in self.surfaces:
            for vertex in surface:
                glColor3fv((1, 1, 1))
                glVertex3fv(self.vertices[vertex])
                
        glEnd()
