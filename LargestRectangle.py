def PrintMat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end=" ")
        print()
        
def MaxSizeRec(mat):
    print()

if __name__ == '__main__':
    mat = [[0 for x in range(4)] for y in range(4)]
    MaxSizeRec(mat)
    PrintMat(mat)