from typing import Callable
from Graph import Graph
from Node import Node
from Heap import Heap
from utils.algorithm import Position, Path, init_table, sum_position, is_true, set_true, get_path, SearchResult

def dijkstra(g: Graph, start: Position, end: Position, fun_g: Callable[[Node, Position], int], **kwargs) -> SearchResult:
    """
    ## arguments
    `g`: grafo do tipo Graph
    `start`: posicao inicial
    `end`: posicao final
    `fun_cost`: funcao de custo
    ## **kwargs
    `it`: printa o numero da iteracao
    `parent_node`: printa o no pai da chamada recursiva
    `neighbors`: printa os vizinhos descubertos na busca
    `structure_neighbors`: printa a estrutura em que os nós descubertos estão guardados
    """

    root: Node = Node(start, g.get_moves(start))
    visited: list[list[bool]] = init_table(g.size)
    generated: list[list[bool]] = init_table(g.size)
    heap: Heap[Node] = Heap(lambda x, y: (x.g) <= (y.g))
    it: int = 1
    count_visited: int = 0
    count_generated: int = 1

    heap.insert(root)
    current_node = None

    while not heap.is_empty():

        current_node = heap.extract_head()

        # debug: recursive call layer
        if kwargs.get("it"):
            print(f"it {it}" if it <= 1 else f"\nit {it}")

        # debug: parent node
        if kwargs.get("parent_node"):
            print(f"parent_node: {current_node}")

        # inicio do algoritmo
        if current_node is None:
            break

        set_true(visited, current_node.position)
        count_visited += 1

        if current_node.position == end:
            break

        it += 1

        # set neighbors
        for move in current_node.moves:
            neighbor_position: Position = sum_position(current_node.position, move)
            g_cost: int = fun_g(current_node, neighbor_position) + current_node.g
            
            if not (is_true(visited, neighbor_position) or is_true(generated, neighbor_position)):
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), current_node, g_cost)
                heap.insert(neighbor_node)
                set_true(generated, neighbor_position)
                count_generated += 1

                # debug: generated neighbors
                if kwargs.get("neighbors"):
                    print(neighbor_node)

        # debug: structure neighbors
        if kwargs.get("structure_neighbors"):
            print("(" + ", ".join(f"{x:values}" for x in heap) + ")")

    last_node: Node | None = current_node
    path: Path = get_path(last_node)
    path_cost = last_node.g if last_node is not None else 0

    return (start, end, path, path_cost, count_generated, count_visited)
