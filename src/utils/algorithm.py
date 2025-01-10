import math
from enum import Enum
from collections import deque
from Node import Node
from Graph import Graph

Position = tuple[int, int]
Path = list[Position]

class Moves(Enum):
    UP = (1, 0)
    RIGHT = (0, 1)
    DOWN = (-1, 0)
    LEFT = (0, -1)

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

def euc(t1: Position, t2: Position) -> float:
    return math.sqrt(abs(fst(t1) - fst(t2))**2 + abs(scd(t1) - scd(t2))**2)

def man(t1: Position, t2: Position) -> int:
    return (abs(fst(t1) - fst(t2)) + abs(scd(t1) - scd(t2)))

def cost_1(parent: Node, pos: Position) -> int:
    return 10

# def cost_2(parent: Node, pos: Position) -> int:
    # return