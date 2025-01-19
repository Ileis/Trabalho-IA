import random
from Graph import Graph
from depth_first_search import depth_first_search
from breadth_first_search import breadth_first_search
from utils.algorithm import cost_1, cost_2, cost_3, cost_4, euc, man
from dijkstra import dijkstra
from a_star import a_star
from greedy_search import greedy_search

SIZE: int = 31

def random_pos() -> tuple[int, int]:
    return (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))

def main() -> None:
    graph = Graph(SIZE)

    start = random_pos()
    end = random_pos()

    print("start:", start)
    print("end:", end, end="\n\n")

    print(a_star(graph, start, end, cost_1, euc, neighbors=True, call=True, parent_node=True, structure_neighbors=True))

    # print("euclides")
    # print(greedy_search(graph, start, end, cost_1, euc))
    # print(greedy_search(graph, start, end, cost_2, euc))
    # print(greedy_search(graph, start, end, cost_3, euc))
    # print(greedy_search(graph, start, end, cost_4, euc))

    # print("manhattan")
    # print(greedy_search(graph, start, end, cost_1, man))
    # print(greedy_search(graph, start, end, cost_2, man))
    # print(greedy_search(graph, start, end, cost_3, man))
    # print(greedy_search(graph, start, end, cost_4, man))


if __name__ == '__main__':
    main()
