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
            (0, 3, 2, 1),
            (4, 5, 6, 7),
            (0, 4, 5, 1),
            (1, 5, 6, 2),
            (2, 6, 7, 3),
            (3, 7, 4, 0),
        )
    
    def draw(self):
        glBegin(GL_QUADS)
        
        for surface in self.surfaces:
            for vertex in surface:
                glColor3fv((1, 1, 1))
                glVertex3fv(self.vertices[vertex])
                
        glEnd()
