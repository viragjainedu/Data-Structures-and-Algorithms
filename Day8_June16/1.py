#greedy problem - n meeting in one room 

start = [int(x) for x in input().split()]
finish = [int(x) for x in input().split()]

max =  0
for i in range(len(finish)):	
	max = 0
	for j in range(len(finish)):
		if(	finish[j] < finish[max] ):
			finish[j] , finish[max] = finish[max] , finish[j]
			start[j] , start[max] = start[max] , start[j]
		max = j
	# print(finish)


print(start)
print(finish)

meet = 0
last=0
for i in range(len(finish)-1):
	# print(start[i+1], finish[i] , end=" ")
	if(start[i+1] >= finish[last]):
		meet = meet + 1
		last = i
	# print()

print(meet)