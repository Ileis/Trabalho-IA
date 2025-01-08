class Node:
    parent: 'Node | None'
    moves: list[tuple[int, int]]
    position: tuple[int, int]

    def __init__(self, position: tuple[int, int], moves: list[tuple[int, int]], parent:'Node | None' = None) -> None:
        self.parent = parent
        self.position = position
        self.moves = moves

    def __str__(self) -> str:
        return f"pos: {str(self.position)}, parent: {str(self.parent.position if self.parent is not None else None)}"