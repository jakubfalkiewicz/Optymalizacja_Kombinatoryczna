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
    

    def dfsTree(self, edge):
      edgesList = []
      def hasCon(edg,prev):
        for i in range(len(self.adjMatrix)):
          if self.adjMatrix[edg][i] == 1 and i != prev:
            pair = [edg,i]
            if pair not in edgesList:
              edgesList.append(pair)
            hasCon(i,edg)
      for i in range(len(self.adjMatrix)):
          if self.adjMatrix[edge][i] == 1:
            pair = [edge,i]
            if pair not in edgesList:
              edgesList.append(pair)
            hasCon(i, edge)
      print("Otrzymane drzewo spinające T = (V,E'):")
      print(f"V= {list(set(sum(edgesList,[])))} oraz E'= {edgesList}")

    # def spanningTree(self, graphMatrix):
    #     graph = nx.Graph()

    def getOddEdges(self, matrix):
        nodes = []
        if matrix.any():
            for j in range(len(matrix)):
                counter = 0
                for i in range(len(matrix)):
                    if matrix[j][i] != 0:
                        counter += 1
                if counter % 2 == 1:
                    nodes.append(j)
            return nodes
        else:
            for j in range(len(self.adjMatrix)):
                counter = 0
                for i in range(len(self.adjMatrix)):
                    if self.adjMatrix[j][i] != 0:
                        counter += 1
                if counter % 2 == 1:
                    nodes.append(j)
            return nodes

    def christofides(self):
        T = nx.minimum_spanning_tree(self.graph)
        oddNodes = self.getOddEdges(nx.to_numpy_array(T))
        for i in range(len(self.adjMatrix)):
            if i not in oddNodes:
                self.graph.remove_node(i)
        minWeightMatch = list(nx.min_weight_matching(self.graph))
        print(T.edges.data("weight"))
        H = nx.MultiGraph()
        for i in self.graph.nodes:
            H.add_node(i)
        # for i in self.graph.edges:
        # self.graph = nx.to_numpy_array(T)
        # print(O)
        # print(G_copy)
        # graphCopy = T
        # print(T.nodes)
        # O = self.getOddEdges()
        # print(O)
        # minWeightMatch2 = list(nx.min_weight_matching(G_copy))
        # print(nx.algorithms.approximation.traveling_salesman_problem(self.graph))
        # print(nx_app.christofides(self.graph, weight="weight"))
      
    # Print the matrix
    def print_matrix(self):

        start = -1
        index = " "
        for i in range(len(self.adjMatrix)):
            index = index + f"  {i}"

        print(index)

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
    gr.christofides()

    gr.print_matrix()


if __name__ == '__main__':
    main()
