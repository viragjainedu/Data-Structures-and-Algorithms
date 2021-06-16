class Node:
	def __init__(self,data):
		self.left = None
		self.right = None
		self.data = data
	
	def traversal(self):
		if(self.data == None):
			return 
		self.left.traversal()
		print(self.data)
		self.right.traversal()

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
	
	def Height(self,m):
		return max(self.left.Height(m+1) if self.left else m+1 , self.right.Height(m+1) if self.right else m+1)
    
	def Diameter(self):    

		if self is None:
			return 0	
     
		if(self.left):
			lheight = self.left.Height(0)
			ldiameter = self.left.Diameter()
		else:
			lheight = 0
			ldiameter =0

		if(self.right):
			rheight = self.right.Height(0)
			rdiameter = self.right.Diameter()
		else:
			rheight = 0
			rdiameter = 0


		k =  max(lheight + rheight +1 , max(ldiameter , rdiameter))
		print(k , self.data, lheight , rheight)
		return k

root = Node(10)
root.insert(11)
root.insert(9)
root.insert(12)
root.insert(8)
root.insert(7)
root.insert(15)
root.insert(16)
root.insert(17)

# root = Node(20)
# root.insert(15)
# root.insert(25)
# root.insert(5)
# root.insert(18)
# root.insert(22)
# root.PrintTree()


# m = dict()
# root.bottomview(m,0)
# root.topview(m,0)
# print(m)

maxheight = 0
# print(root.Height(maxheight))
print(root.Diameter())

