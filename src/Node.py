class Node:
    parent: 'Node | None'
    moves: list[tuple[int, int]]
    position: tuple[int, int]
    height: int
    g: int
    h: int
    tag: str
    
    def __init__(self, position: tuple[int, int], moves: list[tuple[int, int]], parent:'Node | None' = None, g: int = 10, h: int = 0, **kwargs) -> None:
        self.parent = parent
        self.position = position
        self.moves = moves
        self.g = g
        self.h = h
        self.tag = kwargs.get("tag", "")

        if self.parent is None:
            self.height = 0
        else:
            self.height = self.parent.height + 1

    def __str__(self) -> str:
        pos = "(" + ", ".join(f"{x:02}" for x in self.position) + ")"
        par = "(" + ", ".join(f"{x:02}" for x in self.parent.position) + ")" if self.parent is not None else "(nl, nl)"
        return f"<pos: {pos}, parent: {par}, h: {self.h:02d}, g: {self.g:02d}, height: {self.height:02d}>"

    def __format__(self, format_spec: str) -> str:
        if format_spec == "values":
            return f"<g: {self.g:02d}, h: {self.h:02d}, t: {(self.g + self.h):02d}>"
        return str(self)
    