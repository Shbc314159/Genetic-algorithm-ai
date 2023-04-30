from Individual_AI import Individual
import random

class GeneticAlgorithm:
    def __init__(self):
        self.population = []
        self.current_generation = 1
        self.gene_length = 500 + self.current_generation
        self.pop_size = 10
        self.mutation_rate = 0.2
    
    def create_population(self):
        for i in range(self.pop_size):
            self.genome = [random.choice(["w", "a", "d"]) for j in range(self.gene_length)]    
            ai = Individual(self.genome)
            self.population.append(ai)
    
    def calculate_fitness(self, individual):
        fitness = individual.score / individual.moves_taken
        return fitness
            
    def selection(self):
        selected_individuals = []
        sorted_population = sorted(self.population, key=self.calculate_fitness, reverse=True)
        selected_individuals = sorted_population[-4:]
        for i in range(selected_individuals):
            print(self.calculate_fitness(i))
            
        return selected_individuals
        
    def crossover(self, parent1, parent2):
        crossover_point = random.randint(0, self.gene_length - 1)
        child1_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
        child2_genes = parent2.genes[:crossover_point] + parent1.genes[crossover_point:]
        child1 = Individual(child1_genes)
        child2 = Individual(child2_genes)
        return child1, child2 
    
    def mutation(self, individual):
        for i in range(self.gene_length):
            if random.random() < self.mutation_rate:
                individual.genes[i] = random.choice(["w", "a", "d"])
                
    def create_next_generation(self):
        selected_individuals = self.selection() 
        self.population = []

        for i in range(self.pop_size // 2):
            parent1, parent2 = random.sample(selected_individuals, 2)
            child1, child2 = self.crossover(parent1, parent2)
            self.mutation(child1)
            self.mutation(child2)
            self.population.append(child1)
            self.population.append(child2)
    
        