import sys
import random
from Graph import Graph
from iterative.depth_first_search import depth_first_search
from iterative.breadth_first_search import breadth_first_search
from utils.algorithm import cost_1, cost_2, cost_3, cost_4, euc, man
from iterative.dijkstra import dijkstra
from recursive.a_star import a_star as r_a_star
from iterative.a_star import a_star as it_a_star
from recursive.greedy_search import greedy_search

SIZE: int = 30
sys.setrecursionlimit(5000)

def random_pos() -> tuple[int, int]:
    return (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))

def main() -> None:
    graph = Graph(SIZE)

    # start = (3, 12)
    # end = (2, 24)

    for i in range(1):
        start = random_pos()
        end = random_pos()
        print("start:" if i == 0 else "\nstart:", start)
        print("end:", end, end="\n\n")
        # print(breadth_first_search(graph, start, end, cost_1))
        # print(depth_first_search(graph, start, end, cost_1))
        # print(greedy_search(graph, start, end, cost_1, man))
        # print("dijkstra:")
        print(dijkstra(graph, start, end, cost_1, it=True, parent_node=True, neighbors=True, structure_neighbors=True))
        # print("iterative A*:")
        # print(it_a_star(graph, start, end, cost_1, euc))
        
    # print(breadth_first_search(graph, start, end, cost_1))

if __name__ == '__main__':
    main()
