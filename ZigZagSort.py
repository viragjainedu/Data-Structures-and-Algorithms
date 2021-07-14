
# n = int(input())
arr = [int(x) for x in input().split()]

# a < b > c < d > e < f. 
# 5
# . [1,2,3,4,5]
# 0 [1,2,3,4,5]
# 1 [1,3,2,5,3]
# 2 [1,4,2,5,3]

for i in range(len(arr)-1):
    if(i%2 == 0):
        if(arr[i] < arr[i+1]):
            pass
        else:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    else:
        if(arr[i] > arr[i+1]):
            pass
        else:
            arr[i],arr[i+1] = arr[i+1],arr[i]
print(arr)