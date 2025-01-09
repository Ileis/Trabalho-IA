from collections.abc import Callable
from utils.algorithm import Position
class Heap:
    harr: list [ Position]
    capacity: int
    compare: Callable [[Position, Position], bool]
    def __init__(self, capacity: int, compare: Callable[[Position, Position], bool]) -> None:
        self.capacity = capacity
        self.size = 0
        self.harr = list()
        self.compare = compare

    def parent(self, i: int) -> int:
        return (i - 1) // 2
    
    def get_head(self) -> Position:
        return self.harr[0]
    
    def extract_head(self) -> Position:
        if self.size == 0:
            return (-1,-1)
        
        if self.size == 1:
            self.size = 0
            return self.harr.pop()
        
        root: tuple [int,int] = self.harr[0]
        self.harr[0] = self.harr.pop()
        self.size -= 1
        self.heapify(0)
        return root
    
    def swap(self, i: int, j: int) -> None:
        self.harr[i], self.harr[j] = self.harr[j], self.harr[i]

    def insert(self, k: Position) -> None:
        if self.size == self.capacity:
            return
        
        self.size += 1
        i: int = self.size - 1
        self.harr.append(k)
        while i != 0 and self.compare(self.harr[i], self.harr[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify(self, i: int) -> None:
        l:int = 2 * i + 1
        r:int = 2 * i + 2
        descend:int = i
        if (l < self.size and self.compare(self.harr[l], self.harr[descend])):
            descend = l
        if (r < self.size and self.compare(self.harr[r], self.harr[descend])):
            descend = r
        if descend != i:
            self.swap(i, descend)
            self.heapify(descend)
        pass