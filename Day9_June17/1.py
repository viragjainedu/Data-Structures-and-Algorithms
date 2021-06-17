#board printing 
def print_r (board):
	for i in range(len(board)):
		sub = board[i]
		for j in range(len(sub)):
			print(board[i][j],end=" ")
		print()

#not attacked code 
def not_attacked(board,row,col):
	for i in range(0,len(board)):
		if(board[row][i] == 0):
			pass
		else:
			# print("Row: ", row , "Col: " ,i)
			return False

	for i in range(0,len(board)):
		if(board[i][col] == 0):
			pass
		else:
			# print("Row: ", i , "Col: " ,col)
			return False

	i=row
	j=col
	while(i+1 < len(board) and j+1 < len(board)):
		i = i+1
		j = j+1
		if(board[i][j] == 0):
			pass
		else:
			# print("Row: ", i , "Col: " ,j)
			return False
	i=row
	j=col
	while(i+1 < len(board) and j-1 < len(board) and j-1 >= 0  ):
		i = i+1
		j = j-1
		if(board[i][j] == 0):
			pass
		else:
			# print("Row: ", i , "Col: " ,j)
			return False
	i=row
	j=col
	while(i-1 >= 0 and j-1 >= 0):
		i = i-1
		j = j-1
		if(board[i][j] == 0):
			pass
		else:
			# print("Row: ", i , "Col: " ,j)
			return False
	i=row
	j=col
	while(i-1 >= 0 and j+1 < len(board)):
		i = i-1
		j = j+1
		if(board[i][j] == 0):
			pass
		else:
			# print("Row: ", i , "Col: " ,j)
			return False

	return True

# for i in range(len(board)):
# 	sub = board[i]
# 	for j in range(len(sub)):
# 		if(not_attacked(board,i,j)):
# 			board[i][j] = 1

# backtracking code
def backtrack(board,n_queen):

	for i in range(len(board)):
		for j in  range(len(board)):
			# print(not_attacked(board,i,j),end=" ")
			if(	not_attacked(board,i,j)	):
				board[i][j] = 1
				# print(board)
				if(backtrack(board,n_queen-1) == False):
					board[i][j] = 0
				else:
					return True
			else:
				continue
	
	if(n_queen != 0):
		# print(n_queen)
		return False
	
	print_r(board)

	return True


if __name__ == "__main__":
	n = int(input("Enter Grid N of board\n"))
	board = [[0 for i in range(n)] for j in range(n)]
	# board = [[1,0,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]	
	# print("Hello")
	# print(not_attacked(board,2,3)) #True means not attacked
	backtrack(board,len(board))
	# board[0][0] =1
	# print(board)
	# print(board)