
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def Add(Head,data):
    Temp = Head
    while(Temp.next != None):
        Temp = Temp.next
    Temp.next = Node(data)
    # print(Temp.data)

def create(data):
    Head = Node(data)
    return Head

def printLL(Head):
    Temp = Head
    while(Temp != None):
        # input()
        print(Temp.data,end=" ")
        Temp = Temp.next
    print()

def Reverse(Head):  
    Temp = Head
    TempNext = Head.next
    # curr = TempNext
    while(TempNext != None):
        NextSaved = TempNext.next
        TempNext.next = Temp
        
        Temp = TempNext
        TempNext = NextSaved
    
    Head.next = None
    Head = Temp
    return Head

if __name__ == '__main__':
    Head = create(5)
    Add(Head,6)
    Add(Head,7)
    Add(Head,8)
    Add(Head,9)
    Add(Head,10)
    printLL(Head)
    NewHead = Reverse(Head)
    printLL(NewHead)

