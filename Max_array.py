arr = [int(x) for x in input().split()]

max = arr[0]
for i in range(len(arr)):
    if(arr[i]>max):
        max = arr[i]
print(max)

