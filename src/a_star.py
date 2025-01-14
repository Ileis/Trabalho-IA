from typing import Callable
from Graph import Graph
from Node import Node
from Heap import Heap
from utils.algorithm import Position, Path, init_visited, sum_position, is_visited, set_visited, get_path

def a_star(g: Graph, start: Position, end: Position, heuristic: Callable[[Node, Position], int]) -> Path:
    root: Node = Node(start, g.get_moves(start))
    heap: Heap[Node] = Heap(lambda x, y: x.h <= y.h)
    visited  = init_visited(g.size)
    heap.insert(root)
    set_visited(visited, start)
    
    while heap.empty() is False:
        current: Node | None = heap.extract_head()
        if current is None or current.position == end:
            return get_path(current)
        for move in current.moves:
            neighbor_position: Position = sum_position(current.position, move)
            h_cost: int = heuristic(current, neighbor_position) + current.h
            if not is_visited(vis   ited, neighbor_position):
                set_visited(visited, neighbor_position)
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), current, h_cost)
                heap.insert(neighbor_node)
    return []