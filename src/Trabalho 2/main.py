from functions import *
import time
def main():
    #Se você quiser testar com diferentes parâmetros, basta mudar os valores aqui
    #Mutações: swap_mutation, scramble_mutation, reverse_mutation
    #Crossovers: order_crossover, pmx_crossover
    #Seleções: random_selection, elitism_selection, tournament_selection
    #Elitismo: elitism, no_elitism
    GENOME_LENGTH = 10 #tamanho do genoma
    POPULATION_SIZE = 2000 #Tamanho da população
    EXPERIMENT_1_LENGHT = 10


    #Parte 1
    #for _ in range (20):
        #distance_matrix = random_distance_matrix(EXPERIMENT_1_LENGHT) 
        #flow_matrix = random_flow_matrix(EXPERIMENT_1_LENGHT)
        #genetic_algorithm(POPULATION_SIZE, GENOME_LENGTH, distance_matrix, flow_matrix, tournament_selection, swap_mutation,pmx_crossover,elitism)
        #genetic_algorithm(POPULATION_SIZE, GENOME_LENGTH, distance_matrix, flow_matrix, elitism_selection, swap_mutation,pmx_crossover,elitism)
        # Criando novas matrizes para os próximos testes

    #Parte 2
    #for _ in range (20):
        # Criando novas matrizes para os próximos testes
        #distance_matrix = random_distance_matrix(EXPERIMENT_1_LENGHT) 
        #flow_matrix = random_flow_matrix(EXPERIMENT_1_LENGHT)
        #genetic_algorithm(POPULATION_SIZE, GENOME_LENGTH, distance_matrix, flow_matrix, tournament_selection, swap_mutation,pmx_crossover,elitism)
        #genetic_algorithm(POPULATION_SIZE, GENOME_LENGTH, distance_matrix, flow_matrix, tournament_selection, swap_mutation,order_crossover,elitism)


    #Parte 3
    #for _ in range (20):
        # Criando novas matrizes para os próximos testes
        #distance_matrix = random_distance_matrix(EXPERIMENT_1_LENGHT) 
        #flow_matrix = random_flow_matrix(EXPERIMENT_1_LENGHT)
        #genetic_algorithm(POPULATION_SIZE, GENOME_LENGTH, distance_matrix, flow_matrix, tournament_selection, swap_mutation,pmx_crossover,no_elitism)
        #genetic_algorithm(POPULATION_SIZE, GENOME_LENGTH, distance_matrix, flow_matrix, tournament_selection, swap_mutation,order_crossover,elitism)


    #Parte 4
    #for _ in range (20):
        #flow_matrix = random_flow_matrix(EXPERIMENT_1_LENGHT)
        #distance_matrix = random_distance_matrix(EXPERIMENT_1_LENGHT)
        #genetic_algorithm(POPULATION_SIZE, GENOME_LENGTH, distance_matrix, flow_matrix, tournament_selection, reverse_mutation,pmx_crossover,elitism)
        #genetic_algorithm(POPULATION_SIZE, GENOME_LENGTH, distance_matrix, flow_matrix, tournament_selection, swap_mutation,order_crossover,elitism)7

        
    #Parte 5
    for i in range (100):
        start_time = time.time()
        distance_matrix = random_distance_matrix(i+10) 
        flow_matrix = random_flow_matrix(i+10)
        #Escolham os parametros que se sairam melhor nos testes anteriores
        genetic_algorithm(POPULATION_SIZE, i+10, distance_matrix, flow_matrix, tournament_selection, reverse_mutation,pmx_crossover,elitism)
        print("--- %s seconds ---" % (time.time() - start_time))
        # Criando novas matrizes para os próximos testes

    
    
if __name__ == '__main__':
    main()