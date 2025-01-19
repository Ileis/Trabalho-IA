from typing import Callable
from Graph import Graph
from Node import Node
from utils.algorithm import Position, Path, init_visited, sum_position, is_visited, set_visited, get_path

def greedy_search(g: Graph, start: Position, end: Position, fun_g: Callable[[Node, Position], int], fun_h: Callable[[Position, Position], int], **kwarg) -> Path:
    """
    ## arguments
    `g`: grafo do tipo Graph
    `start`: posicao inicial
    `end`: posicao final
    `fun_g`: funcao de custo
    `fun_h`: funcao heuristica
    ## kwargs
    `call`: printa a camada da chamada recursiva
    `parent_node`: printa o no pai da chamada recursiva
    `neighbors`: printa os vizinhos descubertos na busca
    """
    root: Node = Node(start, g.get_moves(start))
    visited: list[list[bool]] = init_visited(g.size)
    call: int = 1

    def _greedy_search(r: Node | None) -> Node | None:
        # variaveis usadas da funcao exterior 
        nonlocal visited
        nonlocal end
        nonlocal call

        # debug: recursive call layer 
        if kwarg.get("call"):
            print(f"call {call}" if call <= 1 else f"\ncall {call}")

        call += 1

        # debug: parent node
        if kwarg.get("parent_node"):
            print(f"parent_node: {r}")

        # inicio do algoritmo
        if r is None:
            return r

        set_visited(visited, r.position)
            
        if r.position == end:
            return r

        # set neighbors
        next_node: Node | None = None
        for move in r.moves:
            neighbor_position: Position = sum_position(r.position, move)
            g_cost: int = fun_g(r, neighbor_position) + r.g
            h_cost: int = fun_h(neighbor_position, end)
            
            if not is_visited(visited, neighbor_position):
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), r, g_cost, h_cost)

                # debug: generated neighbors
                if kwarg.get("neighbors"):
                    print(neighbor_node)

                if next_node is None:
                    next_node = neighbor_node

                elif neighbor_node.h < next_node.h:
                    next_node = neighbor_node
                    
        return _greedy_search(next_node)

    return get_path(_greedy_search(root))
