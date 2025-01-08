from Graph import Graph
from Node import Node
import algorithm as algo

SIZE: int = 30

def main() -> None:
    graph = Graph(SIZE)
    # print(graph.get_moves((0, 0)))
    # print(graph.get_moves((SIZE - 1, 0)))
    # print(graph.get_moves((0, SIZE - 1)))
    # print(graph.get_moves((SIZE - 1, SIZE - 1)))
          
    inicio: tuple[int, int] = (5, 12)
    fim: tuple[int, int] = (12, 12)

    print(algo.BFS(graph, inicio, fim))
    print(algo.DFS(graph, inicio, fim))
    
if __name__ == '__main__':
    main()