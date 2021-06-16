# Longest substring without repeat  linear o(n) solution 
str = input("Enter the string\n")

start = 0
hashmap = [None]*26
max_length = 0

for i in range(0,len(str)):
    
	index = ord(str[i])%97
	# print(index,end=" ")

	if(hashmap[index] == None):
		hashmap[index] = i
		max_length = max_length + 1
	else:
		start = i #reseting start
		if(i - start > max_length):
			max_length = i - start

# print(hashmap)
print(max_length)
