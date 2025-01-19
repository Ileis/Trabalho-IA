from typing import Callable
from Graph import Graph
from Node import Node
from utils.algorithm import Position, Path, init_visited, sum_position, is_visited, set_visited, get_path

def depth_first_search(g: Graph, start: Position, end: Position, func_cost: Callable[[Node, Position], bool], **kwargs) -> Path:
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
    stack: list[Node] = list()
    call: int = 1

    def _depth_first_search(r: Node) -> Node | None:
        # variaveis usadas da funcao exterior
        nonlocal visited
        nonlocal stack
        nonlocal end
        nonlocal call

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

        if r.position == end:
            return r

        call += 1

        # set neighbors
        for move in r.moves:
            neighbor_position: Position = sum_position(r.position, move)
            h_cost: int = func_cost(r, neighbor_position) + r.h

            if not is_visited(visited, neighbor_position):
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), r, h_cost)
                stack.append(neighbor_node)

                # debug: generated neighbors
                if kwargs.get("neighbors"):
                    print(neighbor_node)

        # debug: structure neighbors
        if kwargs.get("structure_neighbors"):
            print("(" + ", ".join(f"{x:values}" for x in stack) + ")")
           
        return _depth_first_search(stack.pop())

    return get_path(_depth_first_search(root))
