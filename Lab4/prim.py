import math

f = open("Lab4\input.txt","r")
lines = f.readlines()
# print(lines)
with open("Lab4\input.txt") as f:
    mylist = f.read().splitlines() 
mylist.pop(0)

def parseInt(integer):
    return int(integer)

def reformatWeights(string):
    return list(string.replace("{","").replace("}",",").split(","))

def reformat1st(string):
    return list(string.replace("n=","").replace("m=","").split(","))

# print(list(map(parseInt, reformat1st('n=6,m=9 '))))

def matrix(n):
    baseMatrix = []
    for i in range(n):
        baseMatrix.append([0]*n)
    return baseMatrix

def createMatrix(nodes,edges, weights):
    baseMatrix = matrix(nodes)
    for i in range(edges):
        baseMatrix[weights[i][0]][weights[i][1]] = weights[i][2]
        baseMatrix[weights[i][1]][weights[i][0]] = weights[i][2]
    return baseMatrix

def getMST(matrix):
    nodes = len(matrix[0])
    selected_node = [0] * nodes
    selected_node[0] = True
    INF = math.inf
    no_edge = 0
    minSum = 0
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
        minSum += matrix[a][b]
        print(str(a) + "-" + str(b) + ":" + str(matrix[a][b]))
        selected_node[b] = True
        no_edge+=1
    print(minSum)
    # print(selected_node)


for i in range(len(mylist)):
    if i%2 == 1:
        nodes = mylist[i].split()
        newnodes = []
        for j in range(len(nodes)):
            newnodes.append(list(map(parseInt, reformatWeights(nodes[j]))))
        firstLine = list(map(parseInt, reformat1st(mylist[i-1])))
        if firstLine[0] - 1 > firstLine[1]:
            print("graf niespójny - brak drzewa spinającego")
        else:
            newMatrix = createMatrix(firstLine[0],firstLine[1],newnodes)
            # print(newMatrix)
            getMST(newMatrix)
