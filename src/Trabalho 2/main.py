import random
import math
GENOME_LENGTH = 10 # Numero de localidades
POPULATION_SIZE = 300 
MUTATION_RATE = 0.1 
CROSSOVER_RATE = 0.8
GENERATIONS = 100


def random_distance_matrix(lenght):
    interest_points = list()
    for _ in range(lenght):
        interest_points.append((random.randint(0, 30), random.randint(0, 30)))
    distance_matrix = [[0 for _ in range(lenght)] for _ in range(lenght)]
    for i in range(lenght):
        for j in range(lenght):
            distance_matrix[i][j] = euclidian_distance(interest_points[i], interest_points[j])

    for i in range(lenght):
        print (distance_matrix[i])
    return distance_matrix


def euclidian_distance(point1, point2):
    return math.floor(((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5)

def random_genome(lenght):
    genome = [_ for _ in range(GENOME_LENGTH)]
    random.shuffle(genome)
    return genome

def init_population(population_size, genome_lenght):
    return [random_genome(genome_lenght) for _ in range(population_size)]

def fitness(genome: list[int],distance_matrix,flow_matrix):
    return sum(flow_matrix[i][j] * distance_matrix[genome[i]][ genome[j]] for i in range(len(genome)) for j in range(len(genome)))

def random_selection(population):
    return random.choice(population)

def elitism_selection(population, fitness_values):
    best_genome = min(fitness_values)
    fitness_values.remove(best_genome)
    population.remove(population[fitness_values.index(best_genome)])
    return fitness_values.index(best_genome)

def tournament_selection(population, fitness_values, tournament_size=3):
    tournament = random.sample(list (fitness_values), tournament_size)
    winner = min(tournament)
    return fitness_values.index(winner)

def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, len(parent1) - 2)
        child1 = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
        child2 = parent2[:crossover_point] + [gene for gene in parent1 if gene not in parent2[:crossover_point]]
        return child1, child2
    else:
        return parent1, parent2

def swap_mutation(genome):
    random_indices = [random.randint(0, len(genome) - 1) for _ in range(2)]
    genome[random_indices[0]], genome[random_indices[1]] = genome[random_indices[1]], genome[random_indices[0]]
    return genome

def scramble_mutation(genome):
    random_indices = [random.randint(0, len(genome) - 1) for _ in range(2)]
    start, end = min(random_indices), max(random_indices)
    genome[start:end] = random.sample(genome[start:end], len(genome[start:end]))
    return genome

def inversion_mutation(genome):
    random_indices = [random.randint(0, len(genome) - 1) for _ in range(2)]
    start, end = min(random_indices), max(random_indices)
    genome[start:end] = reversed(genome[start:end])
    return genome

def mutate(genome, mutation_type):
    if random.random() < MUTATION_RATE:
        return mutation_type(genome)
    else:
        return genome



def genetic_algorithm(population_size, genome_length, distance_matrix, flow_matrix, selection_type,mutation_type):
    return
    population = init_population(population_size, genome_length)
    fitness_values = [fitness(genome, distance_matrix, flow_matrix) for genome in population]
    for generation in range(GENERATIONS):
        new_population = []
        for _ in range(population_size // 2):
            parent1 = population[selection_type(population, fitness_values)]
            parent2 = population[selection_type(population, fitness_values)]
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1,mutation_type))
            new_population.append(mutate(child2,mutation_type))
        population = new_population
        fitness_values = [fitness(genome, distance_matrix, flow_matrix) for genome in population]
        best_genome = min(fitness_values)
        print(f"Generation {generation}: Best Fitness = {best_genome}")
        best_index = fitness_values.index(best_genome)
        best_solution = population[best_index]
        print(f'Best Solution: {best_solution}')
        print(f'Best Fitness: {fitness(best_solution, distance_matrix, flow_matrix)}')


if __name__ == '__main__':
    genetic_algorithm(POPULATION_SIZE, GENOME_LENGTH, random_distance_matrix(GENOME_LENGTH), random_distance_matrix(GENOME_LENGTH), tournament_selection, scramble_mutation)