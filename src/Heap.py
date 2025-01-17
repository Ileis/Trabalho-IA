from typing import Callable, Any, Generic, TypeVar, Iterator
from Node import Node

T = TypeVar("T")

class Heap(Generic[T]):
    harr: list [T]
    capacity: int
    compare: Callable [[T, T], bool]

    def __iter__(self) -> Iterator:
        return iter(self.harr)

    def __str__(self) -> str:
        output: str = "["

        for element in self.harr:
            output += str(element) + ", "

        output = output[:len(output) - 2]
        output += "]"

        return output

    def __init__(self, compare: Callable[[T, T], bool]) -> None:
        self.size = 0
        self.harr = list()
        self.compare = compare
        self.capacity = 1000

    def parent(self, i: int) -> int:
        return (i - 1) // 2
    
    def find(self, k: T) -> int:
        for i in range(self.size):
            if self.harr[i] == k:
                return i
        return -1
    
    def get_head(self) -> Any:
        return self.harr[0]
    
    def extract_head(self) -> T | None:
        if self.size == 0:
            return
        
        if self.size == 1:
            self.size = 0
            return self.harr.pop()
        
        root: T = self.harr[0]
        self.harr[0] = self.harr.pop()
        self.size -= 1
        self.heapify(0)
        return root
    
    def swap(self, i: int, j: int) -> None:
        self.harr[i], self.harr[j] = self.harr[j], self.harr[i]

    def empty(self) -> bool:
        return self.size == 0

    def insert(self, k: Any) -> None:
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
