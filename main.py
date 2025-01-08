import Node as n
import Graph as g
import algorithm as algo

SIZE: int = 30

def main() -> None:
    graph = g.Graph(SIZE)

    inicio: tuple[int, int] = (5, 12)
    fim: tuple[int, int] = (12, 12)

    print(algo.BFS(graph, inicio, fim))
    
    
if __name__ == '__main__':
    main()