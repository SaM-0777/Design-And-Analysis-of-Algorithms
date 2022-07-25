# Bellman Ford in Python

MAX = 9999

class Edge():
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


if __name__ == "__main__":
    Graph = (
        (0, -1, 4, MAX, MAX),
        (MAX, 0, 3, 2, 2),
        (MAX, MAX, 0, MAX, MAX),
        (MAX, 1, 5, 0, MAX),
        (MAX, MAX, MAX, -3, 0)
    )
    
    edge_list = []
    
    for i in Graph:
        for j in i:
            edge_list.append(Edge(i, j, Graph[i][j]))




