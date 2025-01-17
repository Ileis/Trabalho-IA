from Graph import Graph
from depth_first_search import depth_first_search
from breadth_first_search import breadth_first_search
from utils.algorithm import cost_1, cost_2, cost_3, cost_4, euc
from dijkstra import dijkstra
from a_star import a_star

SIZE: int = 30

def main() -> None:
    graph = Graph(SIZE)

    inicio: tuple[int, int] = (5, 12)
    fim: tuple[int, int] = (12, 12)

    print("dijkstra:", dijkstra(graph, inicio, fim, cost_1), end="\n\n")
    print("dijkstra:", dijkstra(graph, inicio, fim, cost_2), end="\n\n")
    print("dijkstra:", dijkstra(graph, inicio, fim, cost_3), end="\n\n")
    print("dijkstra:", dijkstra(graph, inicio, fim, cost_4), end="\n\n")
    print("A*:", a_star(graph, inicio, fim, cost_4, euc), end="\n\n")

if __name__ == '__main__':
    main()