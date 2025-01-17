import random
from Graph import Graph
from depth_first_search import depth_first_search
from breadth_first_search import breadth_first_search
from utils.algorithm import cost_1, cost_2, cost_3, cost_4, euc, man
from dijkstra import dijkstra
from a_star import a_star
from greedy_search import greedy_search

SIZE: int = 30

def random_pos() -> tuple[int, int]:
    return (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))

def main() -> None:
    graph = Graph(SIZE)

    inicio = random_pos()
    fim = random_pos()

    print("start:", inicio)
    print("end:", fim, end="\n\n")

    # print("dijkstra:", dijkstra(graph, inicio, fim, cost_1), end="\n\n")
    # print("dijkstra:", dijkstra(graph, inicio, fim, cost_2), end="\n\n")
    # print("dijkstra:", dijkstra(graph, inicio, fim, cost_3), end="\n\n")
    # print("dijkstra:", dijkstra(graph, inicio, fim, cost_4), end="\n\n")
    print("A*:", a_star(graph, inicio, fim, cost_4, euc, call=True, parent_node=True, neighbors=True, structure_neighbors=True), end="\n\n")
    # print("greedy1:", greedy_search(graph, inicio, fim, cost_1, euc, call=True, parent_node=True, neighbors=True), end="\n\n")
    # print("greedy2:", greedy_search(graph, inicio, fim, cost_1, man, call=True, parent_node=True, neighbors=True), end="\n\n")

if __name__ == '__main__':
    main()
