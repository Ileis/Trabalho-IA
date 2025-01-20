import random
from Graph import Graph
from utils.algorithm import cost_1, cost_2, cost_3, cost_4, euc, man,costs
from search.a_star import a_star
from search.dijkstra import dijkstra
from search.breadth_first_search import breadth_first_search as bfs
from search.depth_first_search import depth_first_search as dfs
from search.greedy_search import greedy_search

SIZE: int = 31

def random_pos() -> tuple[int, int]:
    return (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))

def main() -> None:
    graph = Graph(SIZE)
    start_positions:list[tuple[int, int]] = list()
    end_positions:list[tuple[int, int]] = list()
    for i in range(50):
        start_positions.append(random_pos())
        end_positions.append(random_pos())
    # start = (3, 12)
    # end = (2, 24)
    
    #Gerador pra parte 1
    '''
    for i in range(50):
        start: tuple[int, int] = start_positions[i]
        end: tuple[int, int] = end_positions[i]
        output: tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        for j in range(4):
            output = bfs(graph, start, end, costs(j+1))
            print("BFS:\nInicio:",output[0],"\nChegada:",output[1], "\nCaminho:" ,output[2], "\nCusto:" , output[3], "\nNos Gerados:", output[4],"\nNos Visitados:", output[5],"\nFuncao de Custo:", j+1,"\n")
    for i in range(50):
        start: tuple[int, int] = start_positions[i]
        end: tuple[int, int] = end_positions[i]
        output: tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        for j in range(4):
            output = dfs(graph, start, end, costs(j+1))
            print("DFS:\nInicio:",output[0],"\nChegada:",output[1], "\nCaminho:" ,output[2], "\nCusto:" , output[3], "\nNos Gerados:", output[4],"\nNos Visitados:", output[5],"\nFuncao de Custo:", j+1,"\n")
    for i in range(50):
    '''





#Gerador pra parte 2
'''
    for i in range(50):
        start: tuple[int, int] = start_positions[i]
        end: tuple[int, int] = end_positions[i]
        output: tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        for j in range(4):
            output = dijkstra(graph, start, end, costs(j+1))
            print("Dijkstra:\nInicio:",output[0],"\nChegada:",output[1], "\nCaminho:" ,output[2], "\nCusto:" , output[3], "\nNos Gerados:", output[4],"\nNos Visitados:", output[5],"\nFuncao de Custo:", j+1,"\n")
    for i in range(50):
        start: tuple[int, int] = start_positions[i]
        end: tuple[int, int] = end_positions[i]
        output: tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        for j in range(4):
            output = a_star(graph, start, end, costs(j+1), euc)
            print("A*:\nInicio:",output[0],"\nChegada:",output[1], "\nCaminho:" ,output[2], "\nCusto:" , output[3], "\nNos Gerados:", output[4],"\nNos Visitados:", output[5],"\nFuncao de Custo:", j+1,"\n", "Heuristica: Euclidiana\n")
    for i in range(50):
        start: tuple[int, int] = start_positions[i]
        end: tuple[int, int] = end_positions[i]
        output: tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        for j in range(4):
            output = a_star(graph, start, end, costs(j+1),man)
            print("A*:\nInicio:",output[0],"\nChegada:",output[1], "\nCaminho:" ,output[2], "\nCusto:" , output[3], "\nNos Gerados:", output[4],"\nNos Visitados:", output[5],"\nFuncao de Custo:", j+1,"\n", "Heuristica: Manhattan\n")
            '''






#gerador pra parte 3
'''
    for i in range(50):
        start: tuple[int, int] = start_positions[i]
        end: tuple[int, int] = end_positions[i]
        output: tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        output = greedy_search(graph, start, end, cost_1, euc)
        print("Greedy Search:", "\nStart:", start, "\nEnd:", end, "\nPath:", output[2], "\nCusto F 1:", output[3],)
        for j in range(3):
            output = greedy_search(graph, start, end,costs(j+2), euc)
            print("Custo F",j+2,":",output[3])
        print("Nos Gerados: ",output[4])
        print("Nos Visitados: ", output[5])
    for i in range (50):
        start: tuple[int, int] = start_positions[i]
        end: tuple[int, int] = end_positions[i]
        output: tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        for j in range(4):
            output = a_star(graph, start, end, costs(j+1), euc)
            print("A*:\nInicio:",output[0],"\nChegada:",output[1], "\nCaminho:" ,output[2], "\nCusto:" , output[3], "\nNos Gerados:", output[4],"\nNos Visitados:", output[5],"\nFuncao de Custo:", j+1,"\n", "Heuristica: Euclidiana\n")
    for i in range(50):
        start: tuple[int, int] = start_positions[i]
        end: tuple[int, int] = end_positions[i]
        output: tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        for j in range(4):
            output = a_star(graph, start, end, costs(j+1),man)
            print("A*:\nInicio:",output[0],"\nChegada:",output[1], "\nCaminho:" ,output[2], "\nCusto:" , output[3], "\nNos Gerados:", output[4],"\nNos Visitados:", output[5],"\nFuncao de Custo:", j+1,"\n", "Heuristica: Manhattan\n")
'''


#Gerador pra Parte 4
'''
    graph.set_random(True)
    for i in range (20):
        start = start_positions[i]
        end = end_positions[i]
        output : tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        for j in range (10):
            output = bfs(graph, start, end, costs(0))
            print("BFS:\nInicio:",output[0],"\nChegada:",output[1], "\nCaminho:" ,output[2])
            for k in range (4):
                output = bfs(graph, start, end, costs(k+1))
                print ("Funcao de Custo:",k+1,":",output[3])
            print("Nos gerados:",output[4],"\nNos visitados:", output[5], "\n")
    for i in range (20):
        start = start_positions[i]
        end = end_positions[i]
        output : tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        for j in range (10):
            output = dfs(graph, start, end, costs(0))
            print("DFS:\nInicio:",output[0],"\nChegada:",output[1], "\nCaminho:" ,output[2])
            for k in range (4):
                output = dfs(graph, start, end, costs(k+1))
                print ("Funcao de Custo:",k+1,":",output[3])
            print("Nos gerados:",output[4],"\nNos visitados:", output[5], "\n")
'''    

# Gerador pra Parte 5
'''
    for i in range(25):
        start: tuple[int, int] = start_positions[i]
        end: tuple[int, int] = end_positions[i]
        output_2: tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        output_1: tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        interest_point: tuple[int, int] = interest_positions[i][0]
        for j in range(4):
            if (interest_cost(interest_positions[i][j], start, end, euc) < interest_cost(interest_point, start, end, euc)):
                interest_point = interest_positions[i][j]
        for j in range (4):
            output_1 = a_star(graph, start, interest_point, costs(j), man)
            output_2 = a_star(graph, interest_point, end, costs(j), man)
            output_2[2].pop(0)
            print("Inicio:", output_1[0],"\nChegada:", output_2[1],"\nPontos de Interesse:",interest_positions[i], "\nCaminho:", output_1[2] + output_2[2],"\nCusto:", output_1[3] + output_2[3],"\nNos Expandidos:", output_1[4] + output_2[4],"\nNos Visitados:", output_1[5] + output_2[5],"\nFuncao de Custo:",j+1,"\n")
    '''







if __name__ == '__main__':
    main()
