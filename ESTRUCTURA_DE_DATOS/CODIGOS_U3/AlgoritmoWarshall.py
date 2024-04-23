def warshall(graph):
    n = len(graph)
    closure = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure


if __name__ == "__main__":
    graph = [
        [1, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1]
    ]
    transitive_closure = warshall(graph)
  
    print("Cierre transitivo del grafo:")
    for row in transitive_closure:
        print(row)
