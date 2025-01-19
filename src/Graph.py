from utils.algorithm import Moves
import random
class Graph:

    size: int
    rand: bool 
    def __init__(self, size: int) -> None:
        self.rand = False
        self.size = size
    
    def set_random(self, rand: bool) -> None:
        self.rand: bool = rand

    def get_moves(self, pos: tuple[int, int]) -> list[tuple[int, int]]:
        output: list[tuple[int, int]] = list()

        # f1: down
        if pos[0] > 0:
            output.append(Moves.DOWN.value)

        # f2: up
        if pos[0] < (self.size - 1):
            output.append(Moves.UP.value)
        
        # f3: left
        if pos[1] > 0:
            output.append(Moves.LEFT.value)

        # f4: right
        if pos[1] < (self.size - 1):
            output.append(Moves.RIGHT.value)
        
        if self.rand:
            random.shuffle(output)
        
        return output
 