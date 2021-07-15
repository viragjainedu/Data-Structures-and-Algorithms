
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def createTree(data):
    return Node(data)

def addNode(Head,data):
    Temp = Head
    # print(Temp.data)
    while(Temp != None): 
        if(Temp.left != None and data <= Temp.data):
            Temp = Temp.left
            # print(Temp.data)
            continue

        if(Temp.right != None and data >= Temp.data):
            Temp = Temp.right
            # print(Temp.data)
            continue

        if(data <= Temp.data):
            Temp.left = Node(data)
            # PreOrderTree(Head)
            # print()
            # print(Temp.left.data)
            break
        else:
            Temp.right = Node(data)
            # PreOrderTree(Head)
            # print()
            # print(Temp.right.data)
            break

def PreOrderTree(Temp):
    if(Temp == None):
        return
    print(Temp.data,end=" ")
    PreOrderTree(Temp.left)
    PreOrderTree(Temp.right)

def FlattenLL(Head):
    Temp = Head 
    queue = []
    queue.append(Head)
    queue_backup = []

    while(len(queue) != 0): #while queue is not empty
        if(queue[0].left != None):
            queue.append(queue[0].left)
        if(queue[0].right != None):
            queue.append(queue[0].right)
        # print(queue[0].data)
        queue_backup.append(queue[0])    
        queue.pop(0)
    
    while(len(queue_backup) != 1):
        queue_backup[0].left = None
        queue_backup[0].right = queue_backup[1]
        queue_backup.pop(0)

def PrintLL(Head):
    while(Head != None):
        print(Head.data)
        Head = Head.right

if __name__ == '__main__':
    Head = createTree(10)
    addNode(Head,5)
    addNode(Head,15)
    addNode(Head,2)
    addNode(Head,8)
    addNode(Head,12)
    addNode(Head,18)

    FlattenLL(Head)
    PrintLL(Head)
