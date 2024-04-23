import heapq
    
def dijkstra(graph, start):
   
    distances = {node: float('inf') for node in graph}

    distances[start] = 0
   
    priority_queue = [(0, start)]

    while priority_queue:
        
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
   
    graph = {
        'A': {'B': 2, 'C': 1},
        'B': {'A': 2, 'C': 3},
        'C': {'A': 1, 'B': 3, 'D': 1},
        'D': {'C': 1, 'E': 3},
        'E': {'D': 3}
    }
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    print("Distancias más cortas desde el nodo", start_node)
    for node, distance in distances.items():
        print("Nodo:", node, "Distancia:", distance)
