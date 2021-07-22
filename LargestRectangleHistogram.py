
def LargestRectangle(arr):

    s = [0]
    
    left_limit = [-1]*len(arr)
    left_limit[0] = 0

    right_limit = [-1]*len(arr)
    right_limit[-1] = len(arr)-1
    
    for i in range(1,len(arr)):
        if(arr[i] > arr[s[-1]]): 
            s.append(i)
            left_limit[i] = i
        else:#if on left is greater than current
            while(len(s) != 0 and arr[i] < arr[s[-1]]):
                popped_value = s[-1]
                s.pop(-1)
            left_limit[i] = popped_value
            s.append(i)
    print(left_limit)

    s=[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        # print(i)
        print(s,right_limit)
        if(arr[i] > arr[s[-1]]): 
            s.append(i)
            right_limit[i] = i
        else:#if on left is greater than current
            while(len(s) != 0 and arr[i] < arr[s[-1]]):
                popped_value = s[-1]
                s.pop(-1)
            right_limit[i] = popped_value
            s.append(i)
    print(right_limit)

if __name__ == '__main__':
    # n = int(input("Enter N: "))
    # k = int(input("Enter K: "))
    arr =  [int(x) for x in input("Enter Array: ").split()]   
    LargestRectangle(arr)

"""
k=3
arr = [1 2 3 1 4 5 2 3 6] 
"""
