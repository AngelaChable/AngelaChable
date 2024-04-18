import networkx as nx
import matplotlib.pyplot as plt


estados = {
    'Baja California': {'Baja California Sur': 100, 'Sonora': 200},
    'Baja California Sur': {'Baja California': 100, 'Sinaloa': 150},
    'Sonora': {'Baja California': 200, 'Chihuahua': 250},
    'Sinaloa': {'Baja California Sur': 150, 'Durango': 180},
    'Chihuahua': {'Sonora': 250, 'Coahuila': 300},
    'Durango': {'Sinaloa': 180, 'Zacatecas': 120},
    'Zacatecas': {'Durango': 120, 'Coahuila': 200},
    'Coahuila': {'Chihuahua': 300, 'Zacatecas': 200}
}

def recorrer_estados_sin_repetir(grafo, inicio):
    visitados = set()
    camino = []

    def dfs(estado):
        visitados.add(estado)
        camino.append(estado)

        for vecino, _ in grafo[estado].items():
            if vecino not in visitados:
                dfs(vecino)

    dfs(inicio)
    return camino

def recorrer_estados_con_repeticion(grafo, inicio):
    visitados = set()
    camino = []

    def dfs(estado):
        visitados.add(estado)
        camino.append(estado)

        for vecino, _ in grafo[estado].items():
            if vecino not in visitados or len(camino) == 7:
                dfs(vecino)

    dfs(inicio)
    return camino


def calcular_costo_total(camino, grafo):
    costo_total = 0
    for i in range(len(camino) - 1):
        costo_total += grafo[camino[i]][camino[i+1]]
    return costo_total


G = nx.Graph()

for estado, vecinos in estados.items():
    for vecino, peso in vecinos.items():
        G.add_edge(estado, vecino, weight=peso)


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Grafo de Estados de la República Mexicana')
plt.show()


print("Estados y sus relaciones:")
for estado, vecinos in estados.items():
    print(estado, "->", vecinos)


camino_sin_repetir = recorrer_estados_sin_repetir(estados, 'Durango')
print("\nRecorrido sin repetir ningún estado:", camino_sin_repetir)
costo_sin_repetir = calcular_costo_total(camino_sin_repetir, estados)
print("Costo total del recorrido sin repetir ningún estado:", costo_sin_repetir)


camino_con_repeticion = recorrer_estados_con_repeticion(estados, 'Baja California')
print("\nRecorrido repitiendo al menos un estado:", camino_con_repeticion)
costo_con_repeticion = calcular_costo_total(camino_con_repeticion, estados)
print("Costo total del recorrido repitiendo al menos un estado:", costo_con_repeticion)
