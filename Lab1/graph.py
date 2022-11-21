import networkx as nx
import matplotlib.pyplot as plt
import numpy as np



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
        self.graph.add_edge(v1,v2)

    # Remove edges
    def remove_edge(self, v1, v2):
        if (type(v1) or type(v2)) != int:
            return
        if (v1 or v2) >= self.size:
            return 
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        self.graph.remove_edge(v1,v2)

    # Edge degree
    def edge_degree(self,v1):
        if type(v1) != int:
            return
        if v1 >= self.size:
            return 
        sum = 0
        for i in self.adjMatrix[v1]:
            sum += i
        print(sum)

    # Max edge degree
    def max_edge_degree(self):
        sum = 0
        maxSum = 0
        for row in self.adjMatrix:
            for i in row:
                sum += i
            if sum > maxSum:
                maxSum = sum
            sum = 0
        print(maxSum)

    # Min edge degree
    def min_edge_degree(self):
        sum = 0
        minSum = len(self.adjMatrix)
        for row in self.adjMatrix:
            for i in row:
                sum += i
            if sum < minSum:
                minSum = sum
            sum = 0
        print(minSum)
    
    # Even/Odd edges degree
    def even_odd_edges(self):
        even = 0
        odd = 0
        sum=0
        for row in self.adjMatrix:
            for i in row:
                sum += i
            if (sum % 2) == 0 :
                even += 1
            else: odd += 1
            sum = 0
        print(f"Even edges: {even}, odd edges: {odd}")

    # Edges descending degree order
    def desc_edge_degree(self):
        sum = 0
        resTab = []
        for row in self.adjMatrix:
            for i in row:
                sum += i
            resTab.append(sum)
            sum = 0
        resTab.sort(reverse=True)
        print(f"Posortowany nierosnaco ciag stopni wierzcholkow: {resTab}")

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        start = -1
        index = " "
        for i in range(len(self.adjMatrix)):
            index = index + f"  {i}"

        print(index)
            
        for row in self.adjMatrix:
                start = start+1
                print(f"{start} {row}")

        nx.draw(self.graph,with_labels=1)
        plt.show()


def main():
    gr = Graph(5)
    gr.add_edge(0, 1)
    gr.add_edge(0, 3)
    gr.add_edge("dwa", 2)
    gr.add_edge(1, 4)
    gr.add_edge(3, 2)
    gr.add_edge(3, 4)
    gr.add_edge(2, 2)
    gr.add_edge(5,5)
    gr.remove_edge(2, 2)
    # gr.edge_degree(0)
    # gr.edge_degree(3)
    # gr.max_edge_degree()
    # gr.min_edge_degree()
    # gr.even_odd_edges()
    gr.desc_edge_degree()

    gr.print_matrix()


if __name__ == '__main__':
    main()