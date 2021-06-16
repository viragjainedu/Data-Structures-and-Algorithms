
# o(n2) solution twice hashing 

n = int(input("Array length\n"))
arr = [int(i) for i in input().split()][:n]

target = int(input("Target\n"))

paired_sum = []
for i in range(n):
	for j in range(i+1,n):
		paired_sum.append(arr[i]+arr[j])
print(paired_sum)

hash_arr = [None]*100
for i in range(0,len(paired_sum)):
	hash_arr[paired_sum[i]] = i

for i in range(0,len(paired_sum)):
	rem = target - paired_sum[i]
	if(hash_arr[rem]):
		print(i,hash_arr[rem])

