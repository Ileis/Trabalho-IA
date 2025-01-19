from typing import Callable
from Graph import Graph
from Node import Node
from Heap import Heap
from utils.algorithm import Position, Path, init_visited, sum_position, is_visited, set_visited, get_path, reduce, SearchResult

def a_star(g: Graph, start: Position, end: Position, fun_g: Callable[[Node, Position], int], fun_h: Callable[[Position, Position], int], **kwargs) -> SearchResult:
    """
    ## arguments
    `g`: grafo do tipo Graph
    `start`: posicao inicial
    `end`: posicao final
    `fun_g`: funcao de custo
    `fun_h`: funcao heuristica
    ## **kwargs
    `call`: printa a camada da chamada recursiva
    `parent_node`: printa o no pai da chamada recursiva
    `neighbors`: printa os vizinhos descubertos na busca
    `structure_neighbors`: printa a estrutura em que os nós descubertos estão guardados
    """

    root: Node = Node(start, g.get_moves(start))
    visited: list[list[bool]] = init_visited(g.size)
    heap: Heap[Node] = Heap(lambda x, y: (x.h + x.g) <= (y.h + y.g))
    call: int = 1
    count_visited: int = 0
    count_generated: int = 0

    def _a_star(r: Node | None) -> Node | None:
        # variaveis usadas da funcao exterior
        nonlocal visited
        nonlocal heap
        nonlocal end
        nonlocal call
        nonlocal count_visited
        nonlocal count_generated

        # debug: recursive call layer 
        if kwargs.get("call"):
            print(f"call {call}" if call <= 1 else f"\ncall {call}")
        
        # debug: parent node
        if kwargs.get("parent_node"):
            print(f"parent_node: {r}")

        # inicio do algoritmo
        if r is None:
            return r

        set_visited(visited, r.position)
        count_visited += 1

        if r.position == end:
            return r

        call += 1

        # set neighbors
        for move in r.moves:
            neighbor_position: Position = sum_position(r.position, move)
            g_cost: int = fun_g(r, neighbor_position) + r.g
            h_cost: int = fun_h(neighbor_position, end)
            
            if not is_visited(visited, neighbor_position):
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), r, g_cost, h_cost)
                heap.insert(neighbor_node)
                count_generated += 1

                # debug: generated neighbors
                if kwargs.get("neighbors"):
                    print(neighbor_node)

        # debug: structure neighbors
        if kwargs.get("structure_neighbors"):
            print("(" + ", ".join(f"{x:values}" for x in heap) + ")")

        return _a_star(heap.extract_head())

    last_node: Node | None = _a_star(root)
    path: Path = get_path(last_node)
    path_cost = last_node.g if last_node is not None else 0

    return (start, end, path, path_cost, count_generated, count_visited)
