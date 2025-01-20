import math
from enum import Enum
from Node import Node
from typing import Callable
Position = tuple[int, int]
"""
Position[0]: int = coordenada x da posicao
Position[1]: int = coordenada y da posicao
"""

Path = list[Position]
"""
Path = lista de posicoes p_0, p_1, ..., p_n onde p_0 eh o estado inicial
    e p_n eh o objetivo da busca
"""

SearchResult = tuple[Position, Position, Path, int, int, int]
"""
- `SearchResult[0]: Position` = Estado Inicial.
- `SearchResult[1]: Position` = Objetivo de Busca.
- `SearchResult[2]: Path`     = Caminho encontrado.
- `SearchResult[3]: int`      = Custo do caminho encontrado.
- `SearchResult[4]: int`      = Quantidade de nos que foram gerados na busca.
- `SearchResult[5]: int`      = Quantidade de nos que foram visitados na busca.
"""

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

def diff_position(t1: Position, t2:Position) -> Position:
    return (fst(t1) - fst(t2), scd(t1) - scd(t2))

def is_true(table_visited: list[list[bool]], t: Position) -> bool:
    return table_visited[fst(t)][scd(t)]

def set_true(visited: list[list[bool]], pos: Position) -> None:
    visited[fst(pos)][scd(pos)] = True

def init_table(size: int) -> list[list[bool]]:
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

def euc(t1: Position, t2: Position) -> int:
    return math.floor(math.sqrt(abs(fst(t1) - fst(t2))**2 + abs(scd(t1) - scd(t2))**2)) * 10

def man(t1: Position, t2: Position) -> int:
    return (abs(fst(t1) - fst(t2)) + abs(scd(t1) - scd(t2))) * 10

def cost_1(parent: Node, pos: Position) -> int:
    return 10

def cost_2(parent: Node, pos: Position) -> int:
    mov_diff: Position = diff_position(parent.position, pos)

    if mov_diff == Moves.UP.value or mov_diff == Moves.DOWN.value: return 10
    if mov_diff == Moves.LEFT.value or mov_diff == Moves.RIGHT.value: return 15

    return 0

def cost_3(parent: Node, pos: Position) -> int:
    mov_diff: Position = diff_position(parent.position, pos)

    if mov_diff == Moves.UP.value or mov_diff == Moves.DOWN.value: return 10
    if mov_diff == Moves.LEFT.value or mov_diff == Moves.RIGHT.value:
        return 10 + (abs(5 - parent.height + 1) % 6)

    return 0

def cost_4(parent: Node, pos: Position) -> int:
    mov_diff: Position = diff_position(parent.position, pos)

    if mov_diff == Moves.UP.value or mov_diff == Moves.DOWN.value: return 10
    if mov_diff == Moves.LEFT.value or mov_diff == Moves.RIGHT.value:
        return 5 + (abs(10 - parent.height + 1) % 11)

    return 0

def costs(i:int) -> Callable[[Node, Position], int]:
    if i == 1:
        return cost_1
    if i == 2:
        return cost_2
    if i == 3:
        return cost_3
    else:
        return cost_4
    
def interest_cost(position: Position, start: Position, end: Position,h: Callable[[Position,Position], int]) -> int:
    return h(position, start) + h(position, end)
