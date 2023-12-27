import networkx as nx
import matplotlib.pyplot as plt
from atv import atv2 as second_graph
from atv import atv1 as first_graph
from busca import dijkstra,prim,kruskal
import time
class Search():
    def __init__(self, G=None):
        self.G = G

    def see(self):
        pos = nx.get_node_attributes(self.G, 'pos')
        edge_labels = {(u, v): self.G[u][v]['weight'] for u, v in self.G.edges}
        nx.draw(self.G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)
        plt.show()

    def create(self, info=2):
        self.G = second_graph() if info == 2 else first_graph()

    def main(self):
        while True:
            x = None
            self.G = None
            try:
                print("Grafo 1 ou 2 (r: 1 || 2): ", end='')
                x = int(input())
                self.create(x)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")

            self.see()

            if x >= 1 and x <= 2:
                aux = 0
                try:
                    print("1 - Dijkstra\n2 - Prim\n3 - Kruskal\nDigite modelo (r: 1 || 2 || 3): ", end='')
                    aux = int(input())
                    if aux == 1:
                        i = int(input("caminho inicial"))
                        f = int(input("onde termina"))
                        dijkstra(self.G,i,f)
                    elif aux == 2:
                        prim(self.G)
                    elif aux == 3:
                        kruskal(self.G)

                except ValueError:
                    print("Entrada inválida. Por favor, insira um número inteiro.")

            plt.show() 

    def dijkstra(self,source_node,target_node):
        start_time = time.time()
        shortest_path_nodes = nx.shortest_path(self.G, source=source_node, target=target_node, weight='weight', method='dijkstra')
        print(f"Caminho mais curto de {source_node} para {target_node}: {shortest_path_nodes}")
        pos = nx.get_node_attributes(self.G, 'pos')
        edge_labels = {(u, v): self.G[u][v]['weight'] for u, v in self.G.edges}
        node_colors = ['red' if node in shortest_path_nodes else 'skyblue' for node in self.G.nodes()]

        nx.draw(self.G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_color="black", font_weight="bold", arrowsize=20)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)
        end_time = time.time()
        print(f"Tempo de execução do Dijkstra: {end_time - start_time} segundos")
        plt.show()

    def prim(self):
        start_time = time.time()
        inf = nx.minimum_spanning_tree(self.G, algorithm='prim')
        pos = nx.get_node_attributes(self.G, 'pos')
        nx.draw(self.G, pos, with_labels=True, font_weight='bold')
        nx.draw(inf, pos, edge_color='r', width=2, alpha=0.5)
        end_time = time.time()
        print(f"Tempo de execução do Prim: {end_time - start_time} segundos")
    
    def kruskal(self):
        start_time = time.time()
        inf = nx.minimum_spanning_tree(self.G, algorithm='kruskal')
        pos = nx.get_node_attributes(self.G, 'pos')
        nx.draw(self.G, pos, with_labels=True, font_weight='bold')
        nx.draw(inf, pos, edge_color='r', width=2, alpha=0.5)
        end_time = time.time()
        print(f"Tempo de execução do Kruskal: {end_time - start_time} segundos")

        
if __name__ == "__main__":
    algorithms = Search()
    algorithms.main()
