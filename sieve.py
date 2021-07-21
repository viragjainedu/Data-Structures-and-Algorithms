import math
def sieve(n):
    arr = [1]*(n+1)
    arr[0] = 0
    arr[1] = 0
    for i in range(2,math.ceil(math.sqrt(n))):
        if (arr[i] == 0):
            continue
        for j in range(2*i,n+1,i):
            arr[j] = 0
    for i in range(len(arr)):
        if(arr[i] == 1):
           print(i,end=" ")

if __name__ == '__main__':
    n = int(input())
    sieve(n)