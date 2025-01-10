from typing import Callable
from Graph import Graph
from Node import Node
from utils.algorithm import Position, Path, init_visited, sum_position, is_visited, set_visited, get_path
from Heap import Heap

def dijkstra(g: Graph, start: Position, end: Position, fun_cost: Callable[[Node, Position], int]) -> Path:
    root: Node = Node(start, g.get_moves(start))
    visited: list[list[bool]] = init_visited(g.size)
    heap: Heap[Node] = Heap(lambda x, y: x.h <= y.h)

    def _dijkstra(r: Node | None) -> Node | None:
        nonlocal visited
        nonlocal heap
        nonlocal end

        if r is None or r.position == end:
            return r

        # set neighbors
        for move in r.moves:
            neighbor_position: Position = sum_position(r.position, move)
            h_cost: int = fun_cost(r, neighbor_position)
            
            if not is_visited(visited, neighbor_position):
                set_visited(visited, neighbor_position)
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), r, h_cost)
                heap.insert(neighbor_node)

        return _dijkstra(heap.extract_head())

    return get_path(_dijkstra(root))
