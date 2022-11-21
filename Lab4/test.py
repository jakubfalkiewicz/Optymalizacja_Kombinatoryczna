# Prim's Algorithm in Python
import math


# number of vertices in graph

#creating graph by adjacency matrix method
# G = [[0, 19, 5, 0, 0],
#      [19, 0, 5, 9, 2],
#      [5, 5, 0, 1, 6],
#      [0, 9, 1, 0, 1],
#      [0, 2, 6, 1, 0]]
G = [[0,1,0,0,0,3],
     [1,0,9,7,0,5],
     [0,9,0,8,0,0],
     [0,7,8,0,5,2],
     [0,0,0,5,0,4],
     [3,5,0,2,4,0]]



# # printing for edge and weight
# print("Edge : Weight\n")
# for i in range(N-1):
#     minimum = INF
#     a = 0
#     b = 0
#     for m in range(N):
#         if selected_node[m]:
#             for n in range(N):
#                 if ((not selected_node[n]) and G[m][n]):  
#                     # not in selected and there is an edge
#                     if minimum > G[m][n]:
#                         minimum = G[m][n]
#                         a = m
#                         b = n
#     print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
#     selected_node[b] = True

def getMST(matrix):
    nodes = len(matrix[0])
    selected_node = [0] * nodes
    selected_node[0] = True
    INF = math.inf
    no_edge = 0

    while (no_edge < nodes - 1):
        minimum = INF
        a = 0
        b = 0
        for m in range(nodes):
            if selected_node[m]:
                for n in range(nodes):
                    if ((not selected_node[n]) and matrix[m][n]):  
                        # not in selected and there is an edge
                        if minimum > matrix[m][n]:
                            minimum = matrix[m][n]
                            a = m
                            b = n
        print(str(a) + "-" + str(b) + ":" + str(matrix[a][b]))
        selected_node[b] = True
        no_edge+=1

getMST(G)