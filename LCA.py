class Node:
	def __init__(self,data):
		self.left = None
		self.right = None
		self.data = data
	
		
	# Iterative function for inorder tree traversal
	def inOrder(root):
		
		# Set current to root of binary tree
		current = root 
		stack = [] # initialize stack
		done = 0
		
		while True:
			
			# Reach the left most Node of the current Node
			if current is not None:
				
				# Place pointer to a tree node on the stack 
				# before traversing the node's left subtree
				stack.append(current)
			
				current = current.left 

			
			# BackTrack from the empty subtree and visit the Node
			# at the top of the stack; however, if the stack is 
			# empty you are done
			elif(stack):
				current = stack.pop()
				print(current.data, end=" ") # Python 3 printing
			
				# We have visited the node and its left 
				# subtree. Now, it's right subtree's turn
				current = current.right 

			else:
				break
		
		print()

	def PrintTree(self):
		if(self.left):
			self.left.PrintTree()
		print(self.data)
		# if(self.right):
		# 	self.right.PrintTree()

	def insert(self,data):
		if(self.data):
			if(data < self.data):
				if(self.left == None):
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif(data > self.data):
				if(self.right == None):
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data=data

	def FindPath(self,goal,path):
		# if(self.data != goal):
		path.append(self.data)
		print(path)
		if(self.data == goal):
			return True

		if(self.left and self.left.FindPath(goal  , path)):
			return True
		if(self.right and self.right.FindPath(goal , path)):
			return True
		path.pop()
		return False
def LCA(path1,path2):
	i=0
	while(True):
		i = i+1			
		if(i<len(path1) and i<len(path2) and path1[i] == path2[i]):
			continue
		else:
			break
	return path1[i-1]

root = Node(10)
root.insert(11)
root.insert(9)
root.insert(12)
root.insert(8)
root.insert(7)
root.insert(15)

path1=[]
path2=[]
# print(root.FindPath(10,path1))
# print(root.FindPath(15,path2))
print(path1)
print(path2)
print(LCA(path1,path2))
# root.PrintTree()



# Driver program to test above function



# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# root.inOrder()
