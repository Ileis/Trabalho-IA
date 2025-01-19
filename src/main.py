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
    for i in range(20):
        start_positions.append(random_pos())
        end_positions.append(random_pos())
    # start = (3, 12)
    # end = (2, 24)
    graph.set_random(True)
    for i in range(50):
        start: tuple[int, int] = start_positions[i]
        end: tuple[int, int] = end_positions[i]
        output: tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]], int, int, int]
        for j in range(4):
            output = greedy_search(graph, start, end, costs(j+1), euc)


            
        
if __name__ == '__main__':
    main()
