class Node:
    parent: 'Node | None'
    moves: list[tuple[int, int]]
    position: tuple[int, int]
    h: int
    g: int

    def __init__(self, position: tuple[int, int], moves: list[tuple[int, int]], parent:'Node | None' = None, h: int = 10, g: int = 0) -> None:
        self.parent = parent
        self.position = position
        self.moves = moves
        self.h = h
        self.g = g

    def __str__(self) -> str:
        return f"pos: {str(self.position)}, parent: {str(self.parent.position if self.parent is not None else None)}"