def LeftMax(arr,e):
    i = e-1
    max = arr[e]
    while(i != -1):
        if(arr[i] > max):
            max = arr[i]
        i = i-1
    return max

def RightMax(arr,e):
    i = e+1
    max = arr[e]
    while(i != len(arr)):
        if(arr[i] > max):
            max = arr[i]
        i = i+1
    return max

arr = [int(x) for x in input().split()]

# {7 0 4 2 5 0 6 4 0 5}

sum = 0
for i in range(1,len(arr)):
    # print()
    print("array elemnt is :",arr[i])
    sum = sum + min(LeftMax(arr,i),RightMax(arr,i)) - arr[i] 
print(sum)