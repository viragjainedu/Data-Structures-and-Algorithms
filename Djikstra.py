def printMST(dist):
        # print ("Edge \tWeight")
        # for i in range(6):
        #     print (parent[i], "-", i, "\t", graph[i][ parent[i] ])
        for i in range(9):
            print(i,dist[i])
  
def MinDistance(dist,mstSet):
    min = 100
    for i in range(len(dist)):
        if(dist[i] < min and mstSet[i] == False):
            min = dist[i]
            min_index = i
    return min_index

def PrimsMST(graph,src):
    dist = [100]*9
    parent = [-1]*9
    mstSet = [False]*9
    dist[0] = 0
    parent[0] = -1

    for i in range(len(graph[src])):
        u = MinDistance(dist,mstSet)
        mstSet[u] = True

        for v in range(9):
            if(graph[u][v] > 0 and mstSet[v] == False and dist[u] + graph[u][v] < dist[v]):
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u 
    
    printMST(dist)

if __name__ == '__main__':
    graph = [
                [0, 4, 0, 0, 0, 0, 0, 8, 0],
                [4, 0, 8, 0, 0, 0, 0, 11, 0],
                [0, 8, 0, 7, 0, 4, 0, 0, 2],
                [0, 0, 7, 0, 9, 14, 0, 0, 0],
                [0, 0, 0, 9, 0, 10, 0, 0, 0],
                [0, 0, 4, 14, 10, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 1, 6],
                [8, 11, 0, 0, 0, 0, 1, 0, 7],
                [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]
    PrimsMST(graph,0)   
