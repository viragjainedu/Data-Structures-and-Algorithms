
def SlidingWindowMaximumDequeue(n,k,arr):

    ans_deqeue = []
    ans_deqeue.append((arr[0],0))
    for i in range(1,n):
        
        if(ans_deqeue[0] and ans_deqeue[0][1] == i-k ): #popping if deque front has left the window
            ans_deqeue.pop(0)
        
        if(ans_deqeue[0] and arr[i] > ans_deqeue[0][0]): #if arr element is greater than deque max
            ans_deqeue = []
            ans_deqeue.append((arr[i],i)) #then reset ans_deque and add new 
        elif(ans_deqeue[0] and  arr[i] < ans_deqeue[0][0]): #if arr element is less than deque max
            if(len(ans_deqeue) > 1):
                ans_deqeue.pop(1) #then append it 
            ans_deqeue.append((arr[i],i)) #then append it 
        else:
            pass

        if(i >= 2): #popping if deque front has left the window
            print(ans_deqeue[0][0])

if __name__ == '__main__':
    n = int(input("Enter N: "))
    k = int(input("Enter K: "))
    arr =  [int(x) for x in input("Enter Array: ").split()]   
    SlidingWindowMaximumDequeue(n,k,arr)

"""
k=3
arr = [1 2 3 1 4 5 2 3 6] 
"""
