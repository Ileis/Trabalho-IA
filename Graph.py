class Graph:
    size: int

    def __init__(self, size: int) -> None:
        self.size = size
    
    def get_node_moves(self,position:tuple[int,int]) -> list[tuple[int, int]]:
        output:list[tuple[int,int]] = list()

        if position[0] < self.size:
            output.append((1,0))
        if position[1] < self.size:
            output.append((0,1))
        if position[0] > 0:
            output.append((-1,0))
        if position[1] > 0:
            output.append((0,-1))
        
        return output