# longest subarray with sum =0 o(n)
arr = [int(x) for x in input().split()]

hashMap = [None]*10

max_length = 0

sum=0
hashMap[0] = 0
for i in range(len(arr)):
	sum = sum + arr[i]
	if(hashMap[sum] == None):
		hashMap[sum] = i
	else: 	
		if(max_length < i - hashMap[sum]):
			max_length =  i - hashMap[sum]
			# print(max_length)

print(max_length)	
# print(hashMap)	


