# shifting takes o(1) time 
# searching takes o(1) time 
# used DLL queue and hashmap

class Node: #for doubly Linkedlist Queue
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def InitLL(data):
    Head = Node(data)
    return Head

def AddNode(Head,data):
    while(Head.next != None):
        Head = Head.next
    Head.next = Node(data)
    Head.next.prev = Head
    return Head.next

def RemoveNode(Head,Temp):
    if(Temp == Head):
        return Temp.next
    Temp.prev.next = Temp.next
    return Head

def PopFirst(Head):
    return Head.next

def LenDLL(Head):
    count = 0
    while(Head != None):
        Head = Head.next
        count += 1
    return count

def PrintLL(Head):
    while(Head != None):
        print(Head.data,end=" ")
        Head = Head.next

def LRUCache(page_frames):
    Head = InitLL(page_frames[0]) #initialize DLL
    hashMap = {} #Inititialize HashMap
    hashMap[page_frames[0]] = Head #initialize hashmap

    for i in range(1,len(page_frames)):

        if(page_frames[i] in hashMap): #if pageframe is found in hashmap
            # print(f"Head Data is {Head.data}---",end=" ")
            address = hashMap[page_frames[i]] #getting address from hashMap
            Head = RemoveNode(Head, address) #pop from that place in O(1) and return Head if changed
            New_address = AddNode(Head,page_frames[i])# put it in front
            hashMap[page_frames[i]] = New_address #updating hashMap position of queue             
        else: #if not found
            # print(f"Page Fault Here - {page_frames[i]}---")
            if(LenDLL(Head) < 3 ): #if cache is not full
                New_address = AddNode(Head,page_frames[i]) #adding Node in DLL     
                hashMap[page_frames[i]] = New_address #updating hashMap position of queue
            else:
                del hashMap[Head.data] #deleting from hashmap
                Head = PopFirst(Head) #pop least used One from DLL queue memory            
                New_address = AddNode(Head,page_frames[i]) #adding Node in DLL     
                hashMap[page_frames[i]] = New_address #updating hashMap position of queue
        
        PrintLL(Head)
        print(hashMap)
            

if __name__ == '__main__':
    page_frames = [1,2,3,4,5,3,4,1,1,2]
    LRUCache(page_frames)
