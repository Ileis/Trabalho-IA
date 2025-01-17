from utils.algorithm import Moves

class Graph:

    size: int

    def __init__(self, size: int) -> None:
        self.size = size
    
    def get_moves(self, pos: tuple[int, int]) -> list[tuple[int, int]]:
        output: list[tuple[int, int]] = list()

        # up
        if pos[0] < (self.size - 1):
            output.append(Moves.UP.value)
        
        # right
        if pos[1] < (self.size - 1):
            output.append(Moves.RIGHT.value)

        # down
        if pos[0] > 0:
            output.append(Moves.DOWN.value)

        # left
        if pos[1] > 0:
            output.append(Moves.LEFT.value)

        return output
