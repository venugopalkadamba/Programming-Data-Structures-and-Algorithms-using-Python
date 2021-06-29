''' 
A graph is bipartite if the graph nodes can be colored woth two colors such that no two nodes have same color.
A graph with odd cycle length can't be bipartite.
'''

# Assuming the nodes are from 0 to n-1


def bfsCheck(adjacencyList, node, colors):
    queue = []
    queue.append(node)
    colors[node] = 1
    while queue:
        currentNode = queue.pop(0)

        for adjNode in adjacencyList[currentNode]:
            if colors[adjNode] == -1:
                colors[adjNode] = 1 - colors[currentNode]
                queue.append(adjNode)
            elif colors[adjNode] == colors[currentNode]:
                return False

    return True


def dfsCheck(adjacencyList, node, colors):
    if colors[node]==-1:
        colors[node] = 1
    for adjNode in adjacencyList[node]:
        if colors[adjNode] == -1:
            colors[adjNode] = 1 - colors[node]
            if(dfsCheck(adjacencyList, adjNode, colors) == False):
                return False
        elif colors[node] == colors[adjNode]:
            return False
    return True


def checkBipartite(adjacencyList, n):
    # taking colors as 0 ans 1
    colors = [-1]*(n)

    for index in range(n):
        if colors[index] == -1:
            if bfsCheck(adjacencyList, index, colors) == False:
                return False
    return True
