from hashlib import new
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

    def checkC3Cycle(self):
        l = self.adjMatrix
        solTab = []
        for i in range(self.size):
            memo = []
            for j in range(self.size):
                if l[i][j] == 1:
                    memo.append(j)
            for h in range(len(memo)):
                for k in range(len(memo)):
                    if self.adjMatrix[memo[h]][memo[k]] == 1:
                        tablica = [i,memo[h],memo[k]]
                        tablica.sort()
                        if tablica not in solTab:
                            solTab.append(tablica)
        print(f"Found {len(solTab)} cycles: {solTab}")

    def not_naive_get_cycles2(self):
        graph1 = np.array(self.adjMatrix)
        graph2 = np.dot(self.adjMatrix, self.adjMatrix)
        print(graph1)
        print(graph2)

        for i in range(len(graph2)):
            for j in range(i):
                if graph2[i][j] == 1:
                    if self.adjMatrix[i][j] == 1:
                        return True

        return False

    def numpy_power(self):
        m1 = np.array(self.adjMatrix)
        m2 = np.dot(m1,m1)
        m3 = np.dot(m1,m2)
        trace = 0
        for i in range(len(self.adjMatrix)):
            trace += m3[i][i]
        print(f"Znalzłem {trace/6} cykli C3 metodą mnożenia")

        # print(m3)

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
    gr = Graph(7)
    gr.add_edge(0, 1)
    gr.add_edge(0, 3)
    gr.add_edge(1, 2)
    # gr.add_edge(1, 3)
    gr.add_edge(1, 4)
    gr.add_edge(4, 3)
    # gr.add_edge(6, 5)
    # gr.add_edge(5, 4)
    # gr.add_edge(4, 6)
    gr.checkC3Cycle()
    # gr.matrix_power3()
    gr.numpy_power()
    print(gr.not_naive_get_cycles2())

    gr.print_matrix()


if __name__ == '__main__':
    main()