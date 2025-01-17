from typing import Callable
from Graph import Graph
from Node import Node
from Heap import Heap
from utils.algorithm import Position, Path, init_visited, sum_position, is_visited, set_visited, get_path

def a_star(g: Graph, start: Position, end: Position, fun_g: Callable[[Node, Position], int], fun_h: Callable[[Position, Position], int]) -> Path:
    root: Node = Node(start, g.get_moves(start))
    visited: list[list[bool]] = init_visited(g.size)
    heap: Heap[Node] = Heap(lambda x, y: (x.h + x.g) <= (y.h + y.g))

    def _a_star(r: Node | None) -> Node | None:
        nonlocal visited
        nonlocal heap
        nonlocal end

        if r is None or r.position == end:
            return r

        # set neighbors
        for move in r.moves:
            neighbor_position: Position = sum_position(r.position, move)
            g_cost: int = fun_g(r, neighbor_position) + r.g
            h_cost: int = fun_h(r.position, neighbor_position)
            
            if not is_visited(visited, neighbor_position):
                set_visited(visited, neighbor_position)
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), r, g_cost, h_cost)
                heap.insert(neighbor_node)

        return _a_star(heap.extract_head())

    return get_path(_a_star(root))

