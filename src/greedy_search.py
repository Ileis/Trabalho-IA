from typing import Callable
from Graph import Graph
from Node import Node
from utils.algorithm import Position, Path, init_visited, sum_position, is_visited, set_visited, get_path

def greedy_search(g: Graph, start: Position, end: Position, fun_g: Callable[[Node, Position], int], fun_h: Callable[[Position, Position], int]) -> Path:
    root: Node = Node(start, g.get_moves(start))
    visited: list[list[bool]] = init_visited(g.size)

    def _greedy_search(r: Node | None) -> Node | None:
        nonlocal visited
        nonlocal end

        if r is None or r.position == end:
            return r

        # set neighbors
        next_node: Node | None = None
        for move in r.moves:
            neighbor_position: Position = sum_position(r.position, move)
            g_cost: int = fun_g(r, neighbor_position)
            h_cost: int = fun_h(r.position, neighbor_position)
            
            if not is_visited(visited, neighbor_position):
                set_visited(visited, neighbor_position)
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), r, g_cost, h_cost)

                if next_node is None:
                    next_node = neighbor_node
                elif neighbor_node.h < next_node.h:
                    next_node = neighbor_node

        return _greedy_search(next_node)

    return get_path(_greedy_search(root))
