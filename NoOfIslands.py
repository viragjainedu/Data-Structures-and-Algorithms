def CheckIsland(graph,i,j):
    if(i>=5 or j>=5 or i<0 or j<0):
        return False

    if(graph[i][j] == 0 ):
        return False
    elif(graph[i][j] == 2):
        return False
    else:
        graph[i][j] = 2

    CheckIsland(graph,i+1,j)
    CheckIsland(graph,i,j+1) 
    CheckIsland(graph,i-1,j) 
    CheckIsland(graph,i,j-1) 
    
    return True

def NoOfIslands(graph):
    count = 0
    for i in range(5):
        for j in range(5):
            if(CheckIsland(graph,i,j) == True):
                count += 1
    print(count)
if __name__ == '__main__':
    graph = [
                [1, 1, 0, 0, 0],
                [1, 0, 1, 0, 1],
                [0, 0, 1, 0, 1],
                [1, 1, 1, 1, 0],
                [1, 1, 0, 1, 0],
            ]
    NoOfIslands(graph)   
