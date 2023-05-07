import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from Walls import Walls
from Genetic_Algorithm import GeneticAlgorithm
from graph import Graph
    
def main(): 
    pygame.init()
    display = (1600,1000)
    pygame.display.gl_set_attribute(GL_MULTISAMPLESAMPLES, 10)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)

    gluPerspective(45, (display[0]/display[1]), 0.1, 110.0)
    
    glTranslatef(0, -5, -20)
    glRotatef(25, 2, 0, 0)
    
    glEnable(GL_DEPTH_TEST)
    
    walls = Walls()
    genetic_algorithm = GeneticAlgorithm()   
    graph = Graph()
    
    while genetic_algorithm.current_generation < 100000:
        print("Generation:", genetic_algorithm.current_generation)
        
        if genetic_algorithm.current_generation == 1:
            genetic_algorithm.create_population()
        else:
            genetic_algorithm.create_next_generation()  
        
        for i in range(genetic_algorithm.gene_length*5):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
            
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
            walls.Draw_Back_Wall()
            walls.Draw_Floor()
            walls.Draw_Target()
            walls.Draw_Barrier()
            
            for individual in genetic_algorithm.population:
                individual.update()
                individual.draw()
            
            pygame.display.flip()
        
        update_graph(genetic_algorithm, graph)
        genetic_algorithm.current_generation += 1

def update_graph(genetic_algorithm, graph):
    x = genetic_algorithm.current_generation
    y = genetic_algorithm.current_best_score
    graph.update(x, y)
    
    
main()      
        