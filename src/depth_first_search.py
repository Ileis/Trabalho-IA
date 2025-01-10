from typing import Callable
from Graph import Graph
from Node import Node
from utils.algorithm import Position, Path, init_visited, sum_position, is_visited, set_visited, get_path

def depth_first_search(g: Graph, start: Position, end: Position, func_cost: Callable[[Node, Position], bool]) -> Path:
    root: Node = Node(start, g.get_moves(start))
    visited: list[list[bool]] = init_visited(g.size)
    stack: list[Node] = list()

    def _depth_first_search(r: Node) -> Node | None:
        nonlocal visited
        nonlocal stack
        nonlocal end

        if r is None or r.position == end:
            return r

        # set neighbors
        for move in r.moves:
            neighbor_position: Position = sum_position(r.position, move)
            h_cost: int = func_cost(r, neighbor_position)

            if not is_visited(visited, neighbor_position):
                set_visited(visited, neighbor_position)
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), r, h_cost)
                stack.append(neighbor_node)

        # recursive call
        return _depth_first_search(stack.pop())

    return get_path(_depth_first_search(root))