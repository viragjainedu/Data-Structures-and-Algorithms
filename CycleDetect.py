
# class Graph:
#     def __init__(self)
#     self.graph = [[0 for x in range(10)] for y in range(10)]

def DFS(graph):
    stack = []
    stack.append(0)
    
    visited = [0 for x in range(len(graph[0]))]
    visited[0] = 1

    while(len(stack) != 0):
        top = stack[-1]

        print(stack[-1])
        stack.pop(-1)

        for i in range(len(graph[top])):
            if(graph[top][i] == 1 and visited[i] == 0):
                stack.append(i)
                visited[i] = 1

def CycleDetection(graph):
    stack = []
    stack.append(0)
    
    visited = [0 for x in range(len(graph[0]))]
    visited[0] = 1
    parent = [-1 for x in range(13)]
    # parent[0] = 

    while(len(stack) != 0):
        top = stack[-1]

        print(stack[-1])

        # if(parent[top] != -1):        
        #     print("Cycle Detected: ",top)
        #     return

        stack.pop(-1)

        for i in range(len(graph[top])):
                
            # if(graph[top][i] == 1 and visited[i] == 1 and parent[i] != -1):
            #     print("Cycle detected")
            #     return
            if(graph[top][i] == 1 and visited[i] == 0):

                if(visited[i] == 0):
                    stack.append(i)
                    visited[i] = 1
                    if(parent[i] == -1): #if parent doest not exist
                        parent[i] = top
                        print("Parent of ", i, "is ",top)
                     


def AddNode(graph,i,j):
    graph[i][j] = 1
    graph[j][i] = 1

if __name__ == '__main__':
    graph = [[0 for x in range(13)] for y in range(13)]
    # print(graph)
    AddNode(graph,0,1)
    AddNode(graph,1,2)
    AddNode(graph,1,3)
    AddNode(graph,1,4)
    AddNode(graph,2,5)
    AddNode(graph,2,6)
    AddNode(graph,5,9)
    AddNode(graph,5,10)
    AddNode(graph,6,10)
    AddNode(graph,1,4)
    AddNode(graph,4,7)
    AddNode(graph,4,8)
    AddNode(graph,7,11)
    AddNode(graph,7,12)

    # AddNode(graph,1,2)
    AddNode(graph,2,3)
    # DFS(graph)
    CycleDetection(graph)
    # print(graph)


    """
4---0-----1
     \     |
       \   |
    3-----2

    such that if v is already visited and u is not parent of v
    """

