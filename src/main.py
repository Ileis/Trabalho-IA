from Graph import Graph
from depth_first_search import depth_first_search
from breadth_first_search import breadth_first_search
from utils.algorithm import Moves, cost_1, cost_2, cost_3, cost_4
from dijkstra import dijkstra

SIZE: int = 30

def main() -> None:
    graph = Graph(SIZE)
    print(type(Moves.UP))

    inicio: tuple[int, int] = (5, 12)
    fim: tuple[int, int] = (12, 12)

    # print(breadth_first_search(graph, inicio, fim, cost_1))
    # print(depth_first_search(graph, inicio, fim))
    print(dijkstra(graph, inicio, fim, cost_3))
    
if __name__ == '__main__':
    main()