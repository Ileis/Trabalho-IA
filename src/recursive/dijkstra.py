from typing import Callable
from Graph import Graph
from Node import Node
from Heap import Heap
from utils.algorithm import Position, Path, init_table, sum_position, is_true, set_true, get_path, SearchResult

def dijkstra(g: Graph, start: Position, end: Position, fun_cost: Callable[[Node, Position], int], **kwargs) -> SearchResult:
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
    visited: list[list[bool]] = init_table(g.size)
    generated: list[list[bool]] = init_table(g.size)
    heap: Heap[Node] = Heap(lambda x, y: x.g <= y.g)
    call: int = 1
    count_visited: int = 0
    count_generated: int = 1

    def _dijkstra(r: Node | None) -> Node | None:
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

        set_true(visited, r.position)
        count_visited += 1

        if r.position == end:
            return r

        call += 1

        # set neighbors
        for move in r.moves:
            neighbor_position: Position = sum_position(r.position, move)
            g_cost: int = fun_cost(r, neighbor_position) + r.g
            
            if not(is_true(visited, neighbor_position) or is_true(generated, neighbor_position)):
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), r, g_cost)
                heap.insert(neighbor_node)
                set_true(generated, neighbor_position)
                count_generated += 1

                # debug: generated neighbors
                if kwargs.get("neighbors"):
                    print(neighbor_node)

        # debug: structure neighbors
        if kwargs.get("structure_neighbors"):
            print("(" + ", ".join(f"{x:values}" for x in heap) + ")")

        return _dijkstra(heap.extract_head())

    last_node: Node | None = _dijkstra(root)
    path: Path = get_path(last_node)
    path_cost = last_node.g if last_node is not None else 0

    return (start, end, path, path_cost, count_generated, count_visited)
