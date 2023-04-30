import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from Walls import Walls
from Genetic_Algorithm import GeneticAlgorithm
    
def main(): 
    pygame.init()
    display = (800,500)
    pygame.display.gl_set_attribute(GL_MULTISAMPLESAMPLES, 10)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 110.0)
    
    glTranslatef(0, -5, -20)
    glRotatef(25, 2, 0, 0)
    
    glEnable(GL_DEPTH_TEST)
    
    walls = Walls()
    genetic_algorithm = GeneticAlgorithm()   
    
    while genetic_algorithm.current_generation < 10:
        print("Generation: ", genetic_algorithm.current_generation)
        
        if genetic_algorithm.current_generation == 1:
            genetic_algorithm.create_population()
        else:
            genetic_algorithm.create_next_generation()  
        
        #game loop
        for i in range(genetic_algorithm.gene_length*5):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
            
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
            walls.Draw_Back_Wall()
            walls.Draw_Floor()
            walls.Draw_Target()
            
            for individual in genetic_algorithm.population:
                individual.update()
                individual.draw()
            
            pygame.display.flip()
        
        genetic_algorithm.current_generation += 1
    
main()      
        