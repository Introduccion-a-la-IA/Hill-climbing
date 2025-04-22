import networkx as nx
import matplotlib.pyplot as plt

# Crear grafo
G = nx.Graph()

# Añadir nodos con posiciones (para visualización como un mapa)
pos = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (2, 0),
    'D': (2, 4),
    'E': (3, 2),
    'F': (4, 0)
}

# Añadir nodos al grafo
G.add_nodes_from(pos.keys())

# Añadir aristas con pesos
edges = [
    ('A', 'B', 2), ('A', 'C', 5),
    ('B', 'D', 4), ('B', 'E', 6),
    ('C', 'F', 3), ('E', 'F', 1)
]
G.add_weighted_edges_from(edges)

def costo(camino):
    return sum(G[camino[i]][camino[i+1]]['weight'] for i in range(len(camino)-1))

def vecinos(camino):
    ult = camino[-1]
    return [camino + [nodo] for nodo in G.neighbors(ult) if nodo not in camino]

def hill_climbing(inicio, objetivo):
    actual = [inicio]
    mejor_costo = float('inf')

    while True:
        candidatos = vecinos(actual)
        if not candidatos:
            break
        candidato = min(candidatos, key=costo)
        if costo(candidato) < costo(actual):
            actual = candidato
            mejor_costo = costo(actual)
        else:
            break
        if actual[-1] == objetivo:
            break

    return actual, mejor_costo

# Ejecutar algoritmo
inicio = 'A'
objetivo = 'F'
camino, total = hill_climbing(inicio, objetivo)

# Visualización
plt.figure(figsize=(8,6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Dibujar la ruta encontrada
path_edges = list(zip(camino, camino[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

plt.title(f"Ruta encontrada: {' → '.join(camino)} (Costo total: {total})")
plt.show()