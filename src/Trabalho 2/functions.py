import random
import math

MUTATION_RATE = 0.05 # Taxa de mutação
CROSSOVER_RATE = 0.75 # Taxa de crossover
GENERATIONS = 300 #Total de gerações


def random_distance_matrix(lenght):
    #Nós iremos gerar N pontos com posições aleatórias x e y entre 0 e 30 e depois calcular a matriz de distâncias euclidianas e usar como nossa matriz de distâncias
    interest_points = list()
    for _ in range(lenght):
        interest_points.append((random.randint(0, 30), random.randint(0, 30)))
    distance_matrix = [[0 for _ in range(lenght)] for _ in range(lenght)]
    for i in range(lenght):
        for j in range(lenght):
            distance_matrix[i][j] = euclidian_distance(interest_points[i], interest_points[j])

    #debug matrix para testar consistência
    #return [[0, 29, 21, 20, 18, 14, 20, 16, 10, 8, 15, 22, 7, 23, 22, 17, 22, 22, 13, 25, 20, 7, 1, 27, 3, 21, 21, 26, 7, 11], [29, 0, 11, 22, 25, 21, 20, 12, 18, 25, 27, 18, 33, 7, 8, 12, 22, 14, 16, 4, 16, 28, 29, 4, 31, 15, 24, 10, 31, 19], [21, 11, 0, 23, 25, 10, 9, 7, 12, 21, 16, 7, 24, 4, 11, 6, 11, 3, 8, 8, 18, 24, 22, 13, 22, 17, 13, 17, 22, 15], [20, 22, 23, 0, 3, 25, 29, 16, 15, 12, 30, 29, 27, 21, 14, 17, 32, 26, 18, 19, 6, 13, 19, 18, 23, 7, 32, 13, 27, 10], [18, 25, 25, 3, 0, 25, 29, 17, 15, 10, 29, 29, 25, 23, 17, 18, 32, 27, 19, 22, 9, 11, 17, 21, 21, 10, 32, 16, 25, 10], [14, 21, 10, 25, 25, 0, 6, 11, 9, 17, 6, 8, 14, 13, 18, 11, 8, 9, 7, 17, 21, 19, 15, 21, 14, 21, 7, 24, 12, 14], [20, 20, 9, 29, 29, 6, 0, 13, 14, 22, 8, 2, 20, 13, 19, 13, 2, 6, 10, 17, 25, 25, 21, 22, 20, 24, 4, 25, 17, 19], [16, 12, 7, 16, 17, 11, 13, 0, 5, 14, 17, 12, 21, 7, 7, 1, 16, 10, 4, 8, 11, 17, 17, 11, 18, 11, 17, 13, 19, 8], [10, 18, 12, 15, 15, 9, 14, 5, 0, 9, 14, 14, 15, 12, 12, 6, 17, 13, 4, 14, 13, 12, 11, 17, 12, 13, 17, 17, 14, 5], [8, 25, 21, 12, 10, 17, 22, 14, 9, 0, 20, 23, 15, 21, 17, 15, 25, 22, 13, 21, 13, 3, 7, 22, 11, 14, 25, 20, 15, 6], [15, 27, 16, 30, 29, 6, 8, 17, 14, 20, 0, 11, 13, 19, 24, 17, 9, 14, 13, 23, 27, 21, 16, 27, 13, 27, 7, 30, 10, 19], [22, 18, 7, 29, 29, 8, 2, 12, 14, 23, 11, 0, 22, 11, 18, 12, 4, 4, 10, 15, 24, 26, 23, 20, 22, 23, 6, 24, 19, 19], [7, 33, 24, 27, 25, 14, 20, 21, 15, 15, 13, 22, 0, 27, 28, 21, 22, 24, 17, 29, 27, 14, 8, 32, 4, 27, 20, 32, 3, 18], [23, 7, 4, 21, 23, 13, 13, 7, 12, 21, 19, 11, 27, 0, 7, 6, 15, 7, 9, 4, 15, 24, 23, 9, 24, 15, 17, 13, 24, 15], [22, 8, 11, 14, 17, 18, 19, 7, 12, 17, 24, 18, 28, 7, 0, 7, 21, 14, 11, 5, 8, 21, 22, 5, 24, 7, 23, 6, 26, 11], [17, 12, 6, 17, 18, 11, 13, 1, 6, 15, 17, 12, 21, 6, 7, 0, 15, 9, 4, 7, 12, 18, 17, 11, 19, 11, 16, 13, 20, 9], [22, 22, 11, 32, 32, 8, 2, 16, 17, 25, 9, 4, 22, 15, 21, 15, 0, 8, 13, 19, 27, 27, 23, 24, 22, 27, 2, 27, 19, 21], [22, 14, 3, 26, 27, 9, 6, 10, 13, 22, 14, 4, 24, 7, 14, 9, 8, 0, 9, 11, 21, 25, 23, 16, 22, 20, 10, 20, 21, 17], [13, 16, 8, 18, 19, 7, 10, 4, 4, 13, 13, 10, 17, 9, 11, 4, 13, 9, 0, 12, 14, 16, 14, 15, 15, 14, 13, 17, 15, 8], [25, 4, 8, 19, 22, 17, 17, 8, 14, 21, 23, 15, 29, 4, 5, 7, 19, 11, 12, 0, 13, 25, 25, 5, 27, 13, 21, 10, 27, 15], [20, 16, 18, 6, 9, 21, 25, 11, 13, 13, 27, 24, 27, 15, 8, 12, 27, 21, 14, 13, 0, 16, 20, 12, 23, 1, 28, 7, 26, 9], [7, 28, 24, 13, 11, 19, 25, 17, 12, 3, 21, 26, 14, 24, 21, 18, 27, 25, 16, 25, 16, 0, 6, 25, 10, 16, 26, 23, 15, 9], [1, 29, 22, 19, 17, 15, 21, 17, 11, 7, 16, 23, 8, 23, 22, 17, 23, 23, 14, 25, 20, 6, 0, 27, 4, 20, 22, 26, 8, 11], [27, 4, 13, 18, 21, 21, 22, 11, 17, 22, 27, 20, 32, 9, 5, 11, 24, 16, 15, 5, 12, 25, 27, 0, 29, 11, 26, 5, 31, 16], [3, 31, 22, 23, 21, 14, 20, 18, 12, 11, 13, 22, 4, 24, 24, 19, 22, 22, 15, 27, 23, 10, 4, 29, 0, 23, 20, 29, 5, 14], [21, 15, 17, 7, 10, 21, 24, 11, 13, 14, 27, 23, 27, 15, 7, 11, 27, 20, 14, 13, 1, 16, 20, 11, 23, 0, 28, 6, 26, 9], [21, 24, 13, 32, 32, 7, 4, 17, 17, 25, 7, 6, 20, 17, 23, 16, 2, 10, 13, 21, 28, 26, 22, 26, 20, 28, 0, 29, 17, 22], [26, 10, 17, 13, 16, 24, 25, 13, 17, 20, 30, 24, 32, 13, 6, 13, 27, 20, 17, 10, 7, 23, 26, 5, 29, 6, 29, 0, 31, 15], [7, 31, 22, 27, 25, 12, 17, 19, 14, 15, 10, 19, 3, 24, 26, 20, 19, 21, 15, 27, 26, 15, 8, 31, 5, 26, 17, 31, 0, 17], [11, 19, 15, 10, 10, 14, 19, 8, 5, 6, 19, 19, 18, 15, 11, 9, 21, 17, 8, 15, 9, 9, 11, 16, 14, 9, 22, 15, 17, 0]]
    return distance_matrix

def random_flow_matrix(lenght):
    flow_matrix = [[random.randint(0,2*lenght) for _ in range(lenght)] for _ in range(lenght)]
    return flow_matrix

def euclidian_distance(point1, point2):
    #Calcular distância euclidiana entre dois pontos
    return math.floor(((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5)

def random_genome(lenght):
    #Criar um genoma aleatório
    genome = [_ for _ in range(lenght)]
    random.shuffle(genome)
    return genome

def init_population(population_size, genome_lenght):
    #Criar uma população inicial de N genomas
    return [random_genome(genome_lenght) for _ in range(population_size)]

def fitness(genome: list[int], distance_matrix, flow_matrix):
    # função fitness é o somatório do produto do fluxo entre os genes e a distância entre eles
    total_fitness = 0
    for i in range(len(genome)):
        for j in range(i + 1, len(genome)):
            total_fitness += flow_matrix[i][j] * distance_matrix[genome[i]][genome[j]]
    return total_fitness * 2  # Multiplica por 2 para considerar a simetria

def random_selection(population,fitness_values):
    #Seleção aleatória de um genoma
    return random.choice(population)

def elitism_selection(population, fitness_values):
    #Seleção do melhor genoma
    best_fitness = min(fitness_values)
    best_genome = population[fitness_values.index(best_fitness)]
    return best_genome

def tournament_selection(population, fitness_values, tournament_size=3):
    #Seleção de um genoma por torneio, onde N genomas são escolhidos aleatoriamente e o melhor é selecionado, troque o tournament size na função pra modificar o tamanho do torneio
    tournament = random.sample(list (fitness_values), tournament_size)
    winner = min(tournament)
    return population[fitness_values.index(winner)]


#Crossovers:
#Crossover de ordem, onde um ponto de corte é escolhido e os genes são trocados entre os pais, respeitando a unicidade
def order_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 2)
    child1 = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [gene for gene in parent1 if gene not in parent2[:crossover_point]]
    return child1, child2

    #PMX (Partially Mapped Crossover), Escolhemos dois pontos de corte, e copiamos o segmento entre eles do primeiro pai para o primeiro filho e vice-versa
    #Depois usando a relação de mapeamento do meio nós preenchemos os genes restantes respeitando a ordem.
def pmx_crossover(parent1, parent2):

    size = len(parent1)
    p1, p2 = [-1]*size, [-1]*size

    # Escolha de dois pontos de corte
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))

    # Colocamos o meio nos filhos
    for i in range(cxpoint1, cxpoint2):
        p1[i] = parent1[i]
        p2[i] = parent2[i]
    # Preenchemos o resto dos genes usando a relação de mapeamento
    def fill_remaining(parent, child):
        for i in range(size):
            if child[i] == -1:
                gene = parent[i]
                while gene in child:
                    gene = parent[child.index(gene)]
                child[i] = gene

    fill_remaining(parent2, p1)
    fill_remaining(parent1, p2)

    return p1, p2

#Função genérica de crossover, onde nós aleatóriamente decidimos se vamos fazer o crossover ou não
def crossover(parent1, parent2,crossover_type):
    
    if random.random() < CROSSOVER_RATE:
        return crossover_type(parent1, parent2)
    else:
        return parent1, parent2

#Mutações:
#Swap: Troca a posição de dois genes aleatóriamente
def swap_mutation(genome):
    random_indices = [random.randint(0, len(genome) - 1) for _ in range(2)]
    genome[random_indices[0]], genome[random_indices[1]] = genome[random_indices[1]], genome[random_indices[0]]
    return genome

#Scramble: Embaralha os genes entre dois pontos aleatórios
def scramble_mutation(genome):
    random_indices = [random.randint(0, len(genome) - 1) for _ in range(2)]
    start, end = min(random_indices), max(random_indices)
    genome[start:end] = random.sample(genome[start:end], len(genome[start:end]))
    return genome

#Reverse: Inverte a ordem dos genes entre dois pontos aleatórios
def reverse_mutation(genome):
    random_indices = [random.randint(0, len(genome) - 1) for _ in range(2)]
    start, end = min(random_indices), max(random_indices)
    genome[start:end] = reversed(genome[start:end])
    return genome

#Mutação genérica, onde nós aleatóriamente decidimos se vamos fazer a mutação ou não
def mutate(genome, mutation_type):
    if random.random() < MUTATION_RATE:
        return mutation_type(genome)
    else:
        return genome


#Função principal do algoritmo genético, é aqui que a mágica acontece
def genetic_algorithm(population_size, genome_length, distance_matrix, flow_matrix, selection_type,mutation_type,crossover_type):
    population = init_population(population_size, genome_length) 
    fitness_values = [fitness(genome, distance_matrix, flow_matrix) for genome in population]
    for generation in range(GENERATIONS): #Iterar sobre as gerações
        new_population = []
        for _ in range(population_size // 2): #Aqui populamos a nova geração
            parent1 = selection_type(population, fitness_values)
            parent2 = selection_type(population, fitness_values)
            child1, child2 = crossover(parent1, parent2,crossover_type)
            new_population.append(mutate(child1,mutation_type))
            new_population.append(mutate(child2,mutation_type))
            #Optamos por adicionar os pais na nova geração, para garantir que os melhores genoma não sejam perdidos
            if(child1 != parent1):
                new_population.append(parent1)
            if(child2 != parent2):
                new_population.append(parent2)
        #Ordenamos a nova população por fitness e removemos os genomas excedentes aka os piores
        new_population.sort(key=lambda genome: fitness(genome, distance_matrix, flow_matrix))
        while len(new_population) > population_size:
            new_population.pop()
        #Embaralhamos de novo a fim de garantir diversidade
        random.shuffle(new_population)
        population = new_population
        fitness_values = [fitness(genome, distance_matrix, flow_matrix) for genome in population]
        best_genome = min(fitness_values)
        medium_fitness = sum(fitness_values) / len(fitness_values)

        print(f"Geração {generation+1}")
        best_index = fitness_values.index(best_genome)
        best_solution = population[best_index]
        print(f'Melhor Solução: {best_solution}')
        print(f'Melhor Fitness: {fitness(best_solution, distance_matrix, flow_matrix)}')
        print (f'Média Fitness: {medium_fitness}')
        print('Pior Fitness: ', max(fitness_values))