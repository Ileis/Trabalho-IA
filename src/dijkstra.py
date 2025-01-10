from Graph import Graph
from Node import Node
from utils.algorithm import Position, Path, init_visited, sum_position, is_visited, set_visited, get_path
from Heap import Heap
def dijiskstra(g:Graph,start:Position,end:Position)->Path:
    root: Node = Node(start, g.get_moves(start))
    visited: list[list[bool]] = init_visited(g.size)
    heap: Heap = Heap(lambda a, b: 1 *a < b)
    return Path()
