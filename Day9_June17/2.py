#Sudoko
def valid(grid,row,col,number):

	# checking vertical
	for i in range(9):
		if(grid[row][i] == number):
			return False
	# checking horizontal
	for i in range(9):
		if(grid[i][col] == number):
			return False

	# checking in small grids
	if(row < 3 and col < 3):
		for i in range(0,3):
			for j in range(0,3):
				if(grid[i][j] == number):
					return False
	if(row < 3 and col < 6 and col >= 3):
		for i in range(0,3):
			for j in range(3,6):
				if(grid[i][j] == number):
					return False
	if(row < 3 and col < 9 and col>=6):
		for i in range(0,3):
			for j in range(6,9):
				if(grid[i][j] == number):
					return False

	if(row >= 3 and row <= 6  and col < 3):
		for i in range(0,3):
			for j in range(0,3):
				if(grid[i][j] == number):
					return False
	if(row >= 3 and row <= 6 and col < 6 and col >= 3):
		for i in range(0,3):
			for j in range(3,6):
				if(grid[i][j] == number):
					return False
	if(row >= 3 and row <= 6 and col < 9 and col>=6):
		for i in range(0,3):
			for j in range(6,9):
				if(grid[i][j] == number):
					return False


	if(row >= 6 and row <= 9  and col < 3):
		for i in range(0,3):
			for j in range(0,3):
				if(grid[i][j] == number):
					return False
	if(row >= 6 and row <= 9 and col < 6 and col >= 3):
		for i in range(0,3):
			for j in range(3,6):
				if(grid[i][j] == number):
					return False
	if(row >= 6 and row <= 9 and col < 9 and col>=6):
		for i in range(0,3):
			for j in range(6,9):
				if(grid[i][j] == number):
					return False

	return True


def solveSudoku(grid):
	for i in range(9):
		for j in range(9):
			for num in range(9):
				if( valid(grid,i,j,num) == True):
					grid[i][j] = num
					if(solveSudoku(grid) == False): 
						grid[i][j] = 0
					else:
						print("grid")
						return True
				else:
					continue
	return False

# if(__name__ == '__main'):
grid =[[0 for x in range(9)]for y in range(9)]

# assigning values to the grid
grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],[5, 2, 0, 0, 0, 0, 0, 0, 0],[0, 8, 7, 0, 0, 0, 0, 3, 1],[0, 0, 3, 0, 1, 0, 0, 8, 0],[9, 0, 0, 8, 6, 3, 0, 0, 5],[0, 5, 0, 0, 9, 0, 6, 0, 0],[1, 3, 0, 0, 0, 0, 2, 5, 0],[0, 0, 0, 0, 0, 0, 0, 7, 4],[0, 0, 5, 2, 0, 6, 3, 0, 0]]

# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())


# print( valid(grid,0,1,2) )
solveSudoku(grid)