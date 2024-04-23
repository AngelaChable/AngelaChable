class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        return True

def kruskal(graph):
    edges = []
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    edges.sort(key=lambda x: x[2])

    disjoint_set = DisjointSet(len(graph))
    minimum_spanning_tree = []
    
    for edge in edges:
        u, v, weight = edge
        if disjoint_set.union(u, v):
            minimum_spanning_tree.append((u, v, weight))
    
    return minimum_spanning_tree


if __name__ == "__main__":
    
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    minimum_spanning_tree = kruskal(graph)
    print("Aristas del árbol de expansión mínima:")
    for edge in minimum_spanning_tree:
        print(edge)
