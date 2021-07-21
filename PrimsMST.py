def printMST(graph,parent):
        print ("Edge \tWeight")
        for i in range(6):
            print (parent[i], "-", i, "\t", graph[i][ parent[i] ])
  
def MinDistance(dist,mstSet):
    min = 100
    for i in range(len(dist)):
        if(dist[i] < min and mstSet[i] == False):
            min = dist[i]
            min_index = i
    return min_index

def PrimsMST(graph,src):
    dist = [100]*6
    parent = [-1]*6
    mstSet = [False]*6
    dist[0] = 0
    parent[0] = -1

    for i in range(len(graph[src])):
        u = MinDistance(dist,mstSet)
        mstSet[u] = True

        for v in range(6):
            if(graph[u][v] > 0 and mstSet[v] == False and dist[v] > graph[u][v]):
                dist[v] = graph[u][v]
                parent[v] = u 
    
    printMST(graph,parent)

if __name__ == '__main__':
    graph = [
                [0,4,6,0,0,0],
                [4,0,6,3,4,0],
                [6,6,0,1,0,0],
                [0,3,1,0,2,3],
                [0,4,0,2,0,7],
                [0,0,0,3,7,0]
            ]
    PrimsMST(graph,0)   
