from hashlib import new
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import itertools


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
    def add_edge(self, v1, v2):
        if (type(v1) or type(v2)) != int:
            return
        if (v1 or v2) >= self.size:
            return
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        self.graph.add_edge(v1, v2)

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

        nx.draw(self.graph, with_labels=1)
        plt.show()


def main():
    gr = Graph(5)
    # gr.add_edge(0, 1)
    gr.add_edge(1, 2)
    gr.add_edge(0, 2)
    gr.add_edge(1, 4)
    gr.add_edge(2, 3)
    gr.dfsTree(2)
   
    gr.print_matrix()


if __name__ == '__main__':
    main()

# gr = Graph(7)
# # gr.add_edge(0, 1)
# gr.add_edge(3, 5)
# gr.add_edge(3, 2)
# gr.add_edge(5, 1)
# gr.add_edge(5, 0)
# gr.add_edge(2, 4)
# gr.add_edge(0, 6)
# gr.add_edge(0, 7)
# gr.dfsTree(3)