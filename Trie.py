class Trie:
    def __init__(self,letter):
        self.letter = letter
        self.count = 0
        self.EndsHere = 0
        self.arr = [None]*26

def CreateTrie():
    Root = Trie('/')
    return Root

def AddLetter(Root,letter):
    pass            

def AddWord(Root,word):
    Temp = Root
    for letter in word:
        num = ord(letter)%97
        if(Temp.arr[num] == None):
            Temp.arr[num] = Trie(letter)
            Temp = Temp.arr[num]
            Temp.count = 1
        else:
            Temp = Temp.arr[num]
    Temp.EndsHere = 1
    # print(Temp.letter)

def PrintTrie(Temp):
    for Node in Temp.arr:
        if(Node != None):
            print(Node.letter,end="")
            if(Node.EndsHere == 0):
                PrintTrie(Node)
            print()            

def CheckWordExists(Root,word):
    Temp = Root
    for letter in word:
        num = ord(letter)%97
        if(Temp.arr[num] != None):
            Temp = Temp.arr[num]
        else:
            print("Word breaks here",end=" ")
            print(letter)
            Temp = None
            break
    if(Temp != None and Temp.EndsHere == 1):
        print(f"Yes {word} exists:")
    else:
        print(f"No {word} do not exists:")

if __name__ == '__main__':
    Root = CreateTrie()
    AddWord(Root,'virag')
    AddWord(Root,'vagar')
    PrintTrie(Root)
    CheckWordExists(Root,'virag')
    CheckWordExists(Root,'viragq')
    CheckWordExists(Root,'vagar')