from Graph import Graph
from depth_first_search import depth_first_search
from breadth_first_search import breadth_first_search

SIZE: int = 30

def main() -> None:
    graph = Graph(SIZE)

    inicio: tuple[int, int] = (5, 12)
    fim: tuple[int, int] = (12, 12)

    print(breadth_first_search(graph, inicio, fim))
    print(depth_first_search(graph, inicio, fim))
    
if __name__ == '__main__':
    main()