from time import time
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(G,source_node,target_node):
    start_time = time()
    shortest_path_nodes = nx.shortest_path(G, source=source_node, target=target_node, weight='weight', method='dijkstra')
    print(f"Caminho mais curto de {source_node} para {target_node}: {shortest_path_nodes}")
    pos = nx.get_node_attributes(G, 'pos')
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges}
    node_colors = ['red' if node in shortest_path_nodes else 'skyblue' for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_color="black", font_weight="bold", arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    end_time = time()
    print(f"Tempo de execução do Dijkstra: {end_time - start_time} segundos")
    plt.show()

def prim(G):
    start_time = time()
    inf = nx.minimum_spanning_tree(G, algorithm='prim')
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    nx.draw(inf, pos, edge_color='r', width=2, alpha=0.5)
    end_time = time()
    print(f"Tempo de execução do Prim: {end_time - start_time} segundos")
    plt.show()

def kruskal(G):
    start_time = time()
    inf = nx.minimum_spanning_tree(G, algorithm='kruskal')
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    nx.draw(inf, pos, edge_color='r', width=2, alpha=0.5)
    end_time = time()
    print(f"Tempo de execução do Kruskal: {end_time - start_time} segundos")
    plt.show()