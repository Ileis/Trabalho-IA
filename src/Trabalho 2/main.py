from functions import *

def main():
    #Aqui nós chamamos a função principal com os parâmetros definidos.
    #Se você quiser testar com diferentes parâmetros, basta mudar os valores aqui
    #Mutações: swap_mutation, scramble_mutation, reverse_mutation
    #Crossovers: order_crossover, pmx_crossover
    #Seleções: random_selection, elitism_selection, tournament_selection
    GENOME_LENGTH = 10
    POPULATION_SIZE = 5000
    flow_matrix = random_flow_matrix(10)
    distance_matrix = random_distance_matrix(10)
    genetic_algorithm(POPULATION_SIZE, GENOME_LENGTH, distance_matrix, flow_matrix, tournament_selection, swap_mutation,pmx_crossover)



if __name__ == '__main__':
    main()