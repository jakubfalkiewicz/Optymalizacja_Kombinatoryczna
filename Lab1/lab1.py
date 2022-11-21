import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,1)
G.add_edge(4,2)
G.add_edge(5,1)

nx.draw(G, with_labels=True)
plt.show() 