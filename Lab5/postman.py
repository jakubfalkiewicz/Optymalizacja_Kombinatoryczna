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


    def getOddEdges(self):
        nodes = []
        for j in range(len(self.adjMatrix)):
            counter = 0
            for i in range(len(self.adjMatrix)):
                if self.adjMatrix[j][i] != 0:
                    counter += 1
            if counter % 2 == 1:
                nodes.append(j)
        return nodes
      
    # Print the matrix
    def print_matrix(self):
        
        #GRAF EULEROWSKI:
        # Spójny multigraf G jest eulerowski wtedy i tylko wtedy, gdy stopień każdego z wierzchołków jest liczbą parzystą.
        if nx.is_eulerian(self.graph):
            eulerPath = list(nx.eulerian_circuit(self.graph, source=None, keys=False))
            first = True
            for i in eulerPath:
                if first == True:
                    first = False
                    print(f"NAJKRÓTSZA DROGA LISTONOSZA: {i[0]} -> {i[1]}", end=" ")
                else: 
                    print(f"-> {i[1]}", end=" ")
            print("\n")
        # NAJKRÓTSZA DROGA LISTONOSZA: 0 -> 5 -> 4 -> 2 -> 5 -> 1 -> 4 -> 3 -> 2 -> 1 -> 0 

        #GRAF PÓŁEULEROWSKI:
        # Spójny multigraf G jest półeulerowski wtedy i tylko wtedy, gdy posiada co najwyżej dwa wierzchołki nieparzystego stopnia,
        # z czego jeden z nich jest początkiem łańcucha Eulera, a drugi jego końcem.
        elif nx.is_semieulerian(self.graph):
            # DROGA EULERA:
            eulerPath = list(nx.eulerian_path(self.graph))
            # NAJKRÓTSZA DROGA MIĘDZY NIEPARZYSTYMI WIERZCHOŁKAMI
            shortestOdd = nx.bellman_ford_path(self.graph, eulerPath[-1][-1], eulerPath[0][0])
            first = True
            for i in eulerPath:
                if first == True:
                    first = False
                    print(f"NAJKRÓTSZA DROGA LISTONOSZA: {i[0]} -> {i[1]}", end=" ")
                else: 
                    print(f"-> {i[1]}", end=" ")
            first2 = True
            for i in shortestOdd:
                if first2 == True:
                    first2 = False
                else: 
                    print(f" -> {i}", end=" ")
            
            print("\n")

        elif len(self.getOddEdges()) > 2:
            #OBCIĄŻONY GRAF G'
            H = nx.Graph()
            oddEdges = self.getOddEdges()

            for i in oddEdges:
                H.add_node(i)

            for i in range(len(oddEdges)):
                for j in range(len(oddEdges)):
                    if i != j:
                        shortestOdd = nx.bellman_ford_path(self.graph, oddEdges[i], oddEdges[j])
                        weightSum = 0
                        for k in range(len(shortestOdd) - 1):
                            weightSum += self.graph[shortestOdd[k]][shortestOdd[k+1]]["weight"]
                        H.add_edge(oddEdges[i],oddEdges[j],weight=weightSum)
            
            # self.graph = H

            minWeightMatch = list(nx.min_weight_matching(H))
            for i in minWeightMatch:
                shortestOdd = nx.bellman_ford_path(self.graph, i[0], i[1])
                print(shortestOdd)

            print(list(nx.min_weight_matching(H)))

        
        else:
            print("Podany graf nie jest spójny")
            

        

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


#PRZYPADEK 3
def main():
    gr = Graph(10)
    gr.add_edge(0, 1, 2)
    gr.add_edge(1, 2, 2)
    gr.add_edge(1, 8, 2)
    gr.add_edge(2, 3, 3)
    gr.add_edge(3, 4, 4)
    gr.add_edge(3, 8, 3)
    gr.add_edge(3, 9, 1)
    gr.add_edge(4, 5, 3)
    gr.add_edge(4, 9, 2)
    gr.add_edge(5, 6, 5)
    gr.add_edge(5, 9, 2)
    gr.add_edge(6, 7, 1)
    gr.add_edge(6, 8, 2)
    gr.add_edge(6, 9, 4)
    gr.add_edge(7, 0, 1)
    gr.add_edge(7, 8, 4)
    print(gr.getOddEdges())

    gr.print_matrix()


# #PRZYPADEK 2
# def main():
#     gr = Graph(6)
#     gr.add_edge(0, 1, 3)
#     gr.add_edge(1, 2, 5)
#     gr.add_edge(1, 5, 8)
    
#     #PRZYPADEK 1
#     # gr.add_edge(1, 4, 9)
    
#     gr.add_edge(2, 3, 5)
#     gr.add_edge(2, 4, 10)
#     gr.add_edge(2, 5, 14)
#     gr.add_edge(3, 4, 9)
#     gr.add_edge(4, 5, 6)
#     gr.add_edge(5, 0, 4)
#     print(gr.getOddEdges())

#     gr.print_matrix()


if __name__ == '__main__':
    main()
