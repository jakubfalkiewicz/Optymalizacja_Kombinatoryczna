import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Create an empty directed graph
G = nx.DiGraph()

# Nodes from A to J
nodes =['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'U']

# The list of edges
edges = [['Z', 'A', 3], ['Z', 'B', 2], ['Z', 'C', 8], ['A', 'C', 4], ['A', 'D', 2],
         ['B', 'C', 6], ['B', 'E', 9], ['C', 'F', 1], ['C', 'G', 2], ['D', 'F', 2], 
         ['E', 'G', 1], ['E', 'H', 2], ['F', 'I', 6], ['G', 'I', 5], ['G', 'J', 6],
         ['G', 'U', 9], ['H', 'J', 2], ['I', 'U', 5],  ['J', 'U', 3]]
# edges = [['Z', 'A', 3], ['Z', 'B', 2], ['Z', 'C', 8], ['B', 'C', 6], ['B', 'E', 9],
#          ['A', 'C', 4], ['A', 'D', 2], ['D', 'F', 2], ['C', 'F', 1], ['C', 'G', 2], 
#          ['F', 'I', 6], ['E', 'G', 1], ['E', 'H', 2], ['G', 'I', 5], ['G', 'J', 6],
#          ['G', 'U', 9], ['H', 'J', 2], ['I', 'U', 5], ['J', 'U', 3]]
         

#NIE MA INNEJ ŚCIEŻKI PROWADZĄCEJ DO WIERZCHOŁKA
#POZOSTAŁE ŚCIEŻKI PROWADZĄCE DO WIERZCHOŁKA ZOSTAŁY ODKRYTE (w visitedNodes)
def pathWeight(path,graph):
    weightSum = 0
    for k in range(len(path) - 1):
        # sumuje wagi krawędzi oryginalnego grafu
        weightSum += graph[path[k]][path[k+1]]["weight"]
    return weightSum

def greatest_weight(u, v, data):
        return -data['weight']

def najwczesniejsze(edges):
    maksSciezka = []
    # print(nx.bellman_ford_path(G, 'Z', 'U', weight=greatest_weight))
    for edge in edges:
        # Find the path with the greatest weight
        path = [edge[0],edge[1]]
        pathToNode = nx.bellman_ford_path(G, 'Z', edge[0], weight=greatest_weight)
        #WARUNKI
        if (edge[0] == 'Z'):
            path.append([0, pathWeight(path,G)])
        else:
            path.append([pathWeight(pathToNode,G), pathWeight(pathToNode,G) + pathWeight(path,G)])
        maksSciezka.append(path)
    return maksSciezka

def najpozniejsze(edges):
    maksSciezka = najwczesniejsze(edges)
    maksSciezka.reverse()
    minSciezka = []
    reversedG = G.copy().reverse()
    maxPathWeight = pathWeight(nx.bellman_ford_path(G, 'Z', 'U' , weight=greatest_weight),G)
    for edge in maksSciezka:
    #     # Find the path with the greatest weight
        path = [edge[1],edge[0]]
        pathToNode = nx.bellman_ford_path(reversedG, 'U', edge[1] , weight=greatest_weight)
        #WARUNKI
        if (edge[1] == 'U'):
            path.append([maxPathWeight - pathWeight(path,reversedG), maxPathWeight])
        else:
            path.append([maxPathWeight - pathWeight(pathToNode,reversedG) - pathWeight(path,reversedG), maxPathWeight - pathWeight(pathToNode,reversedG)])
        minSciezka.append(path)
        # print(path)
    return minSciezka


def computeCMP(nodes,edges):
    G.add_nodes_from(nodes)
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])
    #WARUNEK NA ACYKLICZNOŚĆ DIGRAFU
    if not nx.is_directed_acyclic_graph(G):
        print("Graf nieacykliczny")
        return

    #najwcześniejszy i najpóźniejszy moment rozpoczęcia zadania
    tab1 = najwczesniejsze(edges)
    tab2 = najpozniejsze(edges)
    tab2.reverse()

    # 'rys': {4*('⬜') + ''}
    gantt = []
    #SCIEŻKA KRYTYCZNA
    for i in range(len(tab1)):
        gantt.append({'z': f'z{i+1}: {tab1[i][0]}-{tab1[i][1]}','rys': {tab1[i][2][0]*('⬜') + (tab1[i][2][1] - tab1[i][2][0])*('⬛') + (tab2[i][2][1] - tab1[i][2][1])*('🟥')} ,'ES': tab1[i][2][0],'EF': tab1[i][2][1],'LS': tab2[i][2][0],'LF': tab2[i][2][1]})
        if tab1[i][2] == tab2[i][2]:
            print(tab1[i][0],tab1[i][1],tab1[i][2])
    # print(gantt)
    for i in gantt:
        print(i)

    # print(G.path_weight())
    # Define a custom weight function that returns the negative value of the weight
    

    
    graphData = G.edges.data("weight", default=1)

computeCMP(nodes,edges)


############## DRAW DIGRAPH ####################
# Set the positions of the nodes using the spring layout
pos = nx.spring_layout(G, iterations=100, seed=2)
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
# edges
nx.draw_networkx_edges(G, pos, width=1.5, arrowstyle="->", arrowsize=30)
# node labels
nx.draw_networkx_labels(G, pos, font_size=14, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

# Show the plot
ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()