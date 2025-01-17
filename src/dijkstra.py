from typing import Callable
from Graph import Graph
from Node import Node
from Heap import Heap
from utils.algorithm import Position, Path, init_visited, sum_position, is_visited, set_visited, get_path

def dijkstra(g: Graph, start: Position, end: Position, fun_cost: Callable[[Node, Position], int], **kwargs) -> Path:
    """
    ## arguments
    `g`: grafo do tipo Graph
    `start`: posicao inicial
    `end`: posicao final
    `fun_cost`: funcao de custo
    ## **kwargs
    `call`: printa a camada da chamada recursiva
    `parent_node`: printa o no pai da chamada recursiva
    `neighbors`: printa os vizinhos descubertos na busca
    `structure_neighbors`: printa a estrutura em que os nós descubertos estão guardados
    """

    root: Node = Node(start, g.get_moves(start))
    visited: list[list[bool]] = init_visited(g.size)
    heap: Heap[Node] = Heap(lambda x, y: x.h <= y.h)
    call: int = 1

    def _dijkstra(r: Node | None) -> Node | None:
        nonlocal visited
        nonlocal heap
        nonlocal end
        nonlocal call

        if kwargs.get("call"):
            print(f"call {call}" if call <= 1 else f"\ncall {call}")
        
        call += 1

        if kwargs.get("parent_node"):
            print(f"parent_node: {r}")

        if r is None or r.position == end:
            return r

        # set neighbors
        for move in r.moves:
            neighbor_position: Position = sum_position(r.position, move)
            g_cost: int = fun_cost(r, neighbor_position) + r.g
            
            if not is_visited(visited, neighbor_position):
                set_visited(visited, neighbor_position)
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), r, g_cost)
                heap.insert(neighbor_node)

                if kwargs.get("neighbors"):
                    print(neighbor_node)

        if kwargs.get("structure_neighbors"):
            print("(" + ", ".join(f"{x:values}" for x in heap) + ")")

        return _dijkstra(heap.extract_head())

    return get_path(_dijkstra(root))
