import sys
import random
from Graph import Graph
from utils.algorithm import cost_1, cost_2, cost_3, cost_4, euc, man
from iterative.g_a_star import a_star as g_a_star
from iterative.a_star import a_star as a_star
from iterative.dijkstra import dijkstra


SIZE: int = 300
sys.setrecursionlimit(5000)

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

        print("g_a_star:")
        print(g_a_star(graph, start, end, cost_1, euc))
        print("a_star:")
        print(a_star(graph, start, end, cost_1, euc))
        print("dijkstra:")
        print(dijkstra(graph, start, end, cost_1))


if __name__ == '__main__':
    main()
