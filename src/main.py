from Graph import Graph
from DFS import DFS
from BFS import breadth_first_search

SIZE: int = 30

def main() -> None:
    graph = Graph(SIZE)
    # print(graph.get_moves((0, 0)))
    # print(graph.get_moves((SIZE - 1, 0)))
    # print(graph.get_moves((0, SIZE - 1)))
    # print(graph.get_moves((SIZE - 1, SIZE - 1)))
          
    inicio: tuple[int, int] = (5, 12)
    fim: tuple[int, int] = (12, 12)

    print(breadth_first_search(graph, inicio, fim))
    print(DFS(graph, inicio, fim))
    
if __name__ == '__main__':
    main()