# longest consecutive sequence hashing O(n)
arr = [ int(i) for i in input().split() ]

hash_arr = [None]*100

for i in range(len(arr)):
	hash_arr[arr[i]] = i
# print(hash_arr)

max = 0
temp_max = 0
for i in range(len(hash_arr)):
	if(hash_arr[i]):
		if(hash_arr[i-1] != None):
			temp_max = temp_max + 1
			# print(temp_max)
		else:
			temp_max = 0
		if(temp_max > max):
			max = temp_max
		
print(max+1)
