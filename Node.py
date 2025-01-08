class Node:
    pai: 'Node | None'
    moves: list[tuple[int, int]]
    position: tuple[int, int]

    def __init__(self, position: tuple[int, int], moves: list[tuple[int, int]], pai:'Node | None' = None) -> None:
        self.pai = pai
        self.position = position
        self.moves = moves
        

    