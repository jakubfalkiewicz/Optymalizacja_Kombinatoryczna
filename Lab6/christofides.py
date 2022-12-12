#Zaimplementuj algorytm Christofidesa - uwaga na warunek trójkąta!
from hashlib import new
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import networkx.algorithms.approximation as nx_app
import itertools
import scipy as sp


class Graph:

    # Initialize the matrix
    def __init__(self, size):
        if type(size) != int:
            print("Size of graph has to be an int value")
            return
        self.adjMatrix = []
        self.graph = nx.Graph()
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
            self.graph.add_node(i)
        self.size = size

    # Add edges
    def add_edge(self, v1, v2, weightt):
        if (type(v1) or type(v2)) != int:
            return
        if (v1 or v2) >= self.size:
            return
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = weightt
        self.adjMatrix[v2][v1] = weightt
        self.graph.add_edge(v1, v2, weight=weightt)
    

    def graphIsComplete(self):
    # Iteruj po wierszach macierzy sąsiedztwa
        for i in range(len(self.adjMatrix)):
            # Iteruj po kolumnach macierzy sąsiedztwa
            for j in range(len(self.adjMatrix[i])):
                # Pomiń bieżące położenie, jeśli reprezentuje samoloop (czyli to samo węzło)
                if i == j:
                    continue
                # Jeśli macierz zawiera wartość 0 w bieżącym położeniu, graf nie jest pełny
                if self.adjMatrix[i][j] == 0:
                    return False
        # Jeśli kod dotrze do tego punktu, graf jest pełny
        return True


    def cyclesSatisfyTriangleCondition(self):
        cycles = []
        n = len(self.adjMatrix)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.adjMatrix[i][j] and self.adjMatrix[j][k] and self.adjMatrix[i][k]:
                        cycles.append((self.adjMatrix[i][j], self.adjMatrix[j][k], self.adjMatrix[i][k]))

        for cycle in cycles:
            if cycle[0] + cycle[1] <= cycle[2] or cycle[1] + cycle[2] <= cycle[0] or cycle[0] + cycle[2] <= cycle[1]:
                print(cycle)
                return False

        return True


    def christofides(self):

        if not self.graphIsComplete():
                print("Graf nie jest pełny")
                return None

        if not self.cyclesSatisfyTriangleCondition():
            print("Graf nie spełnia warunku nierówności trójkąta")
            return None


        # 1. minimalne drzewo rozpinające
        T_MST = nx.minimum_spanning_tree(self.graph)
        # print(T_MST.degree())

        # 2. nieparzyste wierzchołki
        Odd_nodes = [node for node in T_MST.nodes() if T_MST.degree(node) % 2 == 1]
        # print(odd_nodes)

        # graf stworzony z nieparzystych wierzchołków
        odd_subgraph = self.graph.subgraph(Odd_nodes)
        # print(odd_subgraph.edges.data("weight"))

        #  minimalne skojarzenienie doskonałe
        perfect_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, weight="weight")
        # print(list(perfect_matching))

        # 3. graf stworzony z MST i skojarzenia doskonałego
        eulerian = nx.MultiGraph(T_MST)
        eulerian.add_edges_from(perfect_matching)
        
        # 4. ścieżka Eulera
        eulerian_path = nx.eulerian_circuit(eulerian)
        nodes_in_circuit = [node for node, _ in list(eulerian_path)]
        # print(nodes_in_circuit)

        # 5. cykl Hamiltona
        hamilton_cycle = []
        for i in range(len(nodes_in_circuit)):
            if nodes_in_circuit[i] not in hamilton_cycle:
                hamilton_cycle.append(nodes_in_circuit[i])

        hamilton_cycle.append(nodes_in_circuit[0])

        return hamilton_cycle

      
    # Print the matrix
    def print_matrix(self):

        start = -1
        index = " "
        for i in range(len(self.adjMatrix)):
            index = index + f"  {i}"

        # print(index)

        for row in self.adjMatrix:
            start = start + 1
            print(f"{start} {row}")

        elarge = [(u, v) for (u, v, d) in self.graph.edges(data=True) if d["weight"] > 0.5]
        esmall = [(u, v) for (u, v, d) in self.graph.edges(data=True) if d["weight"] <= 0.5]

        pos = nx.spring_layout(self.graph, seed=7)  # positions for all nodes - seed for reproducibility

        # nodes
        nx.draw_networkx_nodes(self.graph, pos, node_size=700)

        # edges
        nx.draw_networkx_edges(self.graph, pos, edgelist=elarge, width=3)
        nx.draw_networkx_edges(
            self.graph, pos, edgelist=esmall, width=3, alpha=0.5, edge_color="b", style="dashed"
        )

        # node labels
        nx.draw_networkx_labels(self.graph, pos, font_size=20, font_family="sans-serif")
        # edge weight labels
        edge_labels = nx.get_edge_attributes(self.graph, "weight")
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()




#PRZYPADEK 2
def main():
    gr = Graph(5)
    gr.add_edge(0, 1, 2)
    gr.add_edge(0, 2, 6)
    gr.add_edge(0, 3, 3)
    gr.add_edge(1, 2, 6)
    gr.add_edge(1, 3, 4)
    gr.add_edge(1, 4, 8)
    gr.add_edge(2, 3, 5)
    gr.add_edge(2, 4, 8)
    gr.add_edge(3, 4, 9)
    gr.add_edge(4, 0, 7)
    print(gr.christofides())

    # gr.print_matrix()


if __name__ == '__main__':
    main()
