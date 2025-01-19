import random
from Graph import Graph
from utils.algorithm import cost_1, cost_2, cost_3, cost_4, euc, man
from search.a_star import a_star
from search.dijkstra import dijkstra
from search.breadth_first_search import breadth_first_search as bfs
from search.depth_first_search import depth_first_search as dfs

SIZE: int = 31

def random_pos() -> tuple[int, int]:
    return (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))

def main() -> None:
    graph = Graph(SIZE)

    # start = (3, 12)
    # end = (2, 24)

    for i in range(1):
        start = random_pos()
        end = random_pos()
        print("start:" if i == 0 else "\nstart:", start)
        print("end:", end, end="\n\n")
        print("s_star:")
        print(a_star(graph, start, end, cost_1, euc))
        print("dijkstra:")
        print(dijkstra(graph, start, end, cost_1))
        print("bfs:")
        print(bfs(graph, start, end, cost_1))

if __name__ == '__main__':
    main()
