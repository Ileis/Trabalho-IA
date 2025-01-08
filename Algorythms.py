import Node as n
import Graph as g

def BFS (Graph: g.Graph, start: tuple[int, int], end: tuple[int, int]):
    root: n.Node = n.Node(start, Graph.get_node_moves(start))
    visited: list[list[bool]] = [[False for _ in range(60)] for _ in range(60)]

    # def _BFS() -> list[Node]: