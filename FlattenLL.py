
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def createTree(data):
    return Node(5)

def addNode(Head,data):
    Temp = Head
    while(Temp != None): 
        if(Temp.left != None and data <= Temp.left.data):
            Temp = Temp.left
            continue

        if(Temp.right != None and data >= Temp.right.data):
            Temp = Temp.right
            continue

        if(data <= Temp.data):
            Temp.left = Node(data)
            break
        else:
            Temp.right = Node(data)
            break
def PrintTree(Head):
    if(Head == None):
        return
    PrintTree(Head.left)
    print(Head.data)
    PrintTree(Head.right)

if __name__ == '__main__':
    Head = createTree(10)
    addNode(Head,5)
    addNode(Head,15)
    PrintTree(Head)

    FlattenLL(Head)

"""

"""