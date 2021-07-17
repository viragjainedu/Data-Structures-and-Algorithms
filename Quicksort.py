
def Partition(arr,start,end):
    pivot_index = start
    pivot = arr[pivot_index]

    while(start < end):

        while(start < len(arr) and arr[start] < arr[pivot_index]):
            start += 1

        while(end < len(arr) and arr[end] > arr[pivot_index]):
            end -= 1

        if(start < end):
            arr[start],arr[end] = arr[end],arr[start]
    
    arr[end],arr[pivot_index] = arr[pivot_index],arr[end]
    return end

def QuickSort(arr,start,end):
    if(start <end):
        p = Partition(arr,start,end)
        QuickSort(arr,start,p-1)
        QuickSort(arr,p+1,end)

if __name__ == '__main__':
    # arr = [int(x) for x in input().split()]
    arr = [9,-3,5,2,6,8,-6,1,3]
    QuickSort(arr,0,len(arr)-1)
    print(arr)
