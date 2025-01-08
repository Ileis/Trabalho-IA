from collections import deque
from Node import Node
from Graph import Graph

Position = tuple[int, int]
Path = list[Position]

def fst(t: Position) -> int:
    return t[0]

def scd(t: Position) -> int:
    return t[1]

def sum_position(t1: Position, t2: Position) -> Position:
    return (fst(t1) + fst(t2), scd(t1) + scd(t2))

def is_visited(table_visited: list[list[bool]], t: Position) -> bool:
    return table_visited[fst(t)][scd(t)]

def set_visited(visited: list[list[bool]], pos: Position) -> None:
    visited[fst(pos)][scd(pos)] = True

def init_visited(size: int) -> list[list[bool]]:
    return [[False for _ in range(size)] for _ in range(size)]

def get_path(n: Node | None) -> Path:
    output: Path = list()

    def _get_path(m: Node | None):
        nonlocal output

        if m is None:
            return

        output.append(m.position)
        _get_path(m.parent)

    _get_path(n)
    output.reverse()

    return output

def BFS(g: Graph, start: Position, end: Position) -> Path:
    root: Node = Node(start, g.get_moves(start))
    visited: list[list[bool]] = init_visited(g.size)
    queue: deque[Node] = deque()

    def _BFS(r: Node) -> Node | None:
        nonlocal visited
        nonlocal queue
        nonlocal end

        if r is None or r.position == end:
            return r

        # set neighbors
        for move in r.moves:
            neighbor_position: Position = sum_position(r.position, move)

            if not is_visited(visited, neighbor_position):
                set_visited(visited, neighbor_position)
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), r)
                queue.append(neighbor_node)

        # recursive call
        return _BFS(queue.popleft())

    return get_path(_BFS(root))

def DFS(g: Graph, start: Position, end: Position) -> Path:
    root: Node = Node(start, g.get_moves(start))
    visited: list[list[bool]] = init_visited(g.size)
    stack: list[Node] = list()

    def _DFS(r: Node) -> Node | None:
        nonlocal visited
        nonlocal stack
        nonlocal end

        if r is None or r.position == end:
            return r

        # set neighbors
        for move in r.moves:
            neighbor_position: Position = sum_position(r.position, move)

            if not is_visited(visited, neighbor_position):
                set_visited(visited, neighbor_position)
                neighbor_node: Node = Node(neighbor_position, g.get_moves(neighbor_position), r)
                stack.append(neighbor_node)

        # recursive call
        return _DFS(stack.pop())

    return get_path(_DFS(root))

