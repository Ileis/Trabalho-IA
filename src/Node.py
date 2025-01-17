class Node:
    parent: 'Node | None'
    moves: list[tuple[int, int]]
    position: tuple[int, int]
    height: int
    g: int
    h: int
    
    def __init__(self, position: tuple[int, int], moves: list[tuple[int, int]], parent:'Node | None' = None, g: int = 10, h: int = 0) -> None:
        self.parent = parent
        self.position = position
        self.moves = moves
        self.g = g
        self.h = h

        if self.parent is None:
            self.height = 0
        else:
            self.height = self.parent.height + 1

    def __str__(self) -> str:
        return f"pos: {str(self.position)}, parent: {str(self.parent.position if self.parent is not None else None)}, h: {self.h}, g: {self.g}"