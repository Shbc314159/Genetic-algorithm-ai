from Individual_AI import Individual
import random
import globalvars
import barrier

class GeneticAlgorithm:
    def __init__(self):
        self.population = []
        self.current_generation = 1
        self.gene_length = 40
        self.pop_size = 20
        self.mutation_rate = 0.2
        self.current_best_score = 0
        self.maxbarriers = 25
    
    def create_population(self):
        for i in range(self.pop_size):
            self.genome = [random.choice(["w", "a", "d", " ", "u"]) for j in range(self.gene_length)]    
            ai = Individual(self.genome)
            self.population.append(ai)
    
    def calculate_fitness(self, individual):
        fitness = individual.score * 100 / individual.moves_taken ** 2
        print(fitness)
        return fitness
            
    def selection(self):
        sorted_population = sorted(self.population, key=self.calculate_fitness, reverse=True)
        selected_individual = sorted_population[0]
        print("selected fitness:")
        self.current_best_score = self.calculate_fitness(selected_individual)
            
        return selected_individual
    
    def mutation(self, individual):
        for i in range(self.gene_length):
            if random.random() < self.mutation_rate:
                individual.genes[i] = random.choice(["w", "a", "d", " ", "u"])
        
        return individual
                
    def create_next_generation(self):
        best_individual = self.selection() 
        self.population = []

        for i in range(self.pop_size - 1):
            child = Individual(best_individual.genes[:])
            child = self.mutation(child)
            
 #           if self.current_generation % 50 == 0:
 #               child.genes.append(random.choice(["w", "a", "d", " ", "u"]))
            
            self.population.append(child)
                
        child = Individual(best_individual.genes[:])
        child.genes.append(random.choice(["w", "a", "d", " ", "u"]))
        self.population.append(child)
        
        if self.mutation_rate - self.calculate_fitness(best_individual) > 0.1:
            self.mutation_rate -= self.calculate_fitness(best_individual)
        else:
            self.mutation_rate = 0.1
                
 #       if self.current_generation % 0 == 0:
 #           self.gene_length += 1
            
        print(self.mutation_rate)
        
#        self.randomise_target()
        self.randomise_barriers()
    
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(0, self.gene_length - 1)
        child1_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
        child2_genes = parent2.genes[:crossover_point] + parent1.genes[crossover_point:]
        child1 = Individual(child1_genes)
        child2 = Individual(child2_genes)
        return child1, child2 
    
    def randomise_target(self):
        x = random.randint(-25, 20)
        z = random.randint(-60, -15)
        
        globalvars.target_vertices = (
            (x + 5, -9.5, z + 5),
            (x, -9.5, z + 5),
            (x, -9.5, z),
            (x + 5, -9.5, z),
        )
        
    def randomise_barriers(self):
        globalvars.barriers = []
        numbarriers = random.randint(0, self.maxbarriers)
        
        for i in range(numbarriers):
            length = random.randint(1, 15)
            height = random.randint(1, 15)
            width = random.randint(1, 15)
            xmin = random.randint(-25, 10)
            ymin = -10
            zmin = random.randint(-60, -15)
            xmax = xmin + length
            ymax = ymin + height
            zmax = zmin + width
            newbarrier = barrier.Barrier(xmin, xmax, ymin, ymax, zmin, zmax)
            globalvars.barriers.append(newbarrier)