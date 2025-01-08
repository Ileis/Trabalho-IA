import Node as n
import Graph as g
from collections import deque

def sum_t(t1, t2) -> tuple[int, int]:
    return (t1[0] + t2[0], t1[1] + t2[1])

def is_visited(table_visited: list[list[bool]], t: tuple[int, int]) -> bool:
    return table_visited[t[0]][t[1]]

def set_visited(visited: list[list[bool]], pos: tuple[int, int]) -> None:
    visited[pos[0]][pos[1]] = True

def get_path(node: n.Node | None) -> list[tuple[int, int]]:
    output: list[tuple[int, int]] = list()

    def _get_path(p: n.Node | None):
        nonlocal output

        if p is None:
            return

        output.append(p.position)
        _get_path(p.parent)

    _get_path(node)
    output.reverse()

    return output

def BFS (graph: g.Graph, start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    root: n.Node = n.Node(start, graph.get_moves(start))
    visited: list[list[bool]] = [[False for _ in range(60)] for _ in range(60)]
    queue: deque[n.Node] = deque()

    def _BFS(r: n.Node) -> n.Node | None:
        nonlocal visited
        nonlocal queue
        nonlocal end

        if r is None or r.position == end:
            return r

        # set neighbors
        for move in r.moves:
            neighbor_position: tuple[int, int] = sum_t(r.position, move)

            if not is_visited(visited, neighbor_position):
                set_visited(visited, neighbor_position)
                neighbor_node: n.Node = n.Node(neighbor_position, graph.get_moves(neighbor_position), r)
                queue.append(neighbor_node)

        # recursive call
        return _BFS(queue.popleft())

    last_node = _BFS(root)

    return get_path(last_node)