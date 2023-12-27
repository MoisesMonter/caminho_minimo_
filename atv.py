import networkx as nx


def atv1(G = nx.Graph()):
    G.add_node(1, pos=(0, 0))
    G.add_nodes_from([(2, {'pos': (2, 2)}),
                  (3, {'pos': (3.5, 0.5)}),
                  (5, {'pos': (3, -2)}),
                  (4, {'pos': (1, -2)})])

    G.add_edge(1, 2, weight=2)
    G.add_edge(1, 4, weight=3)
    G.add_edge(2, 3, weight=4)
    G.add_edge(2, 4, weight=3)
    G.add_edge(3, 5, weight=3)
    G.add_edge(4, 3, weight=7)
    G.add_edge(4, 5, weight=3)
    G.add_edge(1, 5, weight=6)
    return G

def atv2(G = nx.Graph()):
    G.add_node(1, pos=(-2, 0))
    G.add_nodes_from([(2, {'pos': (-1, 2)}),
                    (3, {'pos': (1.8, 2.4)}),
                    (4, {'pos': (4.7, 2.9)}),
                    (5, {'pos': (8.7, 0.9)}),
                    (6, {'pos': (9, 2.6)}),
                    (7, {'pos': (11, 3.5)}),
                    (8, {'pos': (1, -0.3)}),
                    (9, {'pos': (4, 0.3)}),
                    (10, {'pos': (6.8, -0.2)}),                    
                    
                    (11, {'pos': (10.8, -0.2)}),  
                    (12, {'pos': (-1, -2)}),
                    (13, {'pos': (3, -2)}),    
                    (14, {'pos': (6, -2.1)}), 
                    (15, {'pos': (8.2, -1.3)}),  
                    (16, {'pos': (4, -3)}),        
                    (17, {'pos': (7.7, -2.8)}),
                    (18, {'pos': (10, -2.1)}),])
    G.add_edge(1, 2, weight=20)
    G.add_edge(1, 12, weight=29)
    G.add_edge(1, 13, weight=37)
    G.add_edge(1, 8, weight=29)
    G.add_edge(2, 3, weight=25)
    G.add_edge(2, 8, weight=28)
    G.add_edge(2, 12, weight=39)
    G.add_edge(3, 8, weight=30)
    G.add_edge(3, 4, weight=25)
    G.add_edge(3, 13, weight=54)
    G.add_edge(4, 5, weight=39)
    G.add_edge(4, 6, weight=32)
    G.add_edge(4, 7, weight=42)
    G.add_edge(4, 9, weight=23)
    G.add_edge(4, 10, weight=33)
    G.add_edge(4, 14, weight=56)
    G.add_edge(5, 6, weight=12)
    G.add_edge(5, 7, weight=26)
    G.add_edge(5, 10, weight=19)
    G.add_edge(6, 7, weight=17)
    G.add_edge(6, 10, weight=35)
    G.add_edge(6, 11, weight=30)
    G.add_edge(7, 11, weight=38)
    G.add_edge(8, 12, weight=25)
    G.add_edge(8, 13, weight=22)
    G.add_edge(9, 10, weight=26)
    G.add_edge(9, 13, weight=34)
    G.add_edge(9, 14, weight=34)
    G.add_edge(9, 16, weight=43)
    G.add_edge(10, 11, weight=24)
    G.add_edge(10, 14, weight=30)
    G.add_edge(10, 15, weight=19)
    G.add_edge(11, 15, weight=26)
    G.add_edge(11, 18, weight=36)
    G.add_edge(12, 13, weight=27)
    G.add_edge(12, 16, weight=43)
    G.add_edge(13,14, weight=24)
    G.add_edge(13, 16, weight=19)
    G.add_edge(14, 16, weight=19)
    G.add_edge(14, 17, weight=17)
    G.add_edge(14, 15, weight=20)
    G.add_edge(15, 17, weight=18)
    G.add_edge(15, 18, weight=21)
    G.add_edge(16, 17, weight=26)
    G.add_edge(17, 18, weight=15)

    return G