def kadanesAlgo(arr):
	max_so_far = 0
	max_ending_here = 0

	for i in range(len(arr)):
		max_ending_here = max_ending_here + arr[i]
		if(max_ending_here > max_so_far):
			max_so_far = max_ending_here
		if(max_ending_here < 0):
			max_ending_here = 0
	return max_so_far

if __name__ == '__main__':
	arr = [-2, -3, 4, -1, -2, 1, 5, -3]
	print(kadanesAlgo(arr))