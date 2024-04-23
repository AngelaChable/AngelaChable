INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
   
    distance = [[graph[i][j] if graph[i][j] != 0 else INF for j in range(n)] for i in range(n)]
    
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance

if __name__ == "__main__":
    
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]
    
    shortest_distances = floyd_warshall(graph)
    
    print("Distancias más cortas entre todos los pares de nodos:")
    for row in shortest_distances:
        print(row)
