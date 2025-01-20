import random
from Graph import Graph
from utils.algorithm import cost_1, cost_2, cost_3, cost_4, euc, man,costs,interest_cost
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
    interest_positions:list[list[tuple[int, int]]] = list()
    for i in range(25):
        start_positions.append(random_pos())
        end_positions.append(random_pos())
        interest_positions.append(list())
        for j in range (4):
            interest_positions[i].append(random_pos())

    # start = (3, 12)
    # end = (2, 24)
    
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
            output_1 = a_star(graph, start, interest_point, costs(j), euc)
            output_2 = a_star(graph, interest_point, end, costs(j), euc)
            output_2[2].pop(0)
            print("Inicio:", output_1[0],"\nChegada:", output_2[1],"\nPontos de Interesse:",interest_positions[i], "\nCaminho:", output_1[2] + output_2[2],"\nCusto:", output_1[3] + output_2[3],"\nNos Expandidos:", output_1[4] + output_2[4],"\nNos Visitados:", output_1[5] + output_2[5],"\nFuncao de Custo:",j+1,"\n")
            
        
            
        
if __name__ == '__main__':
    main()
