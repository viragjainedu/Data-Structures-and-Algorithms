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

	def bottomview(self,m,current):
		if(self != None):
			if(bool(m) == False):
				m[current] = self.data
			if(self.left):
				# if(m[current - 1]):
				m[current - 1] = self.left.data  
				# else:
					# m[current -1] = self.left.data
				self.left.bottomview( m , current-1)
			if(self.right):
				m[current + 1] = self.right.data  
				self.right.bottomview( m , current+1)
		else:
			return None
	def topview(self,m,current):
		if(self != None):
			if(bool(m) == False):
				m[current] = self.data
			if(self.left):
				# if(m[current - 1]):
				if current-1 in m.keys():
					pass
				else:
					m[current - 1 ] = self.left.data  
				self.left.topview( m , current-1)
			if(self.right):
				if current+1 in m.keys():
					pass
				else:
					m[current + 1 ] = self.right.data  
				self.right.topview( m , current+1)
		else:
			return None


# root = Node(10)
# root.insert(11)
# root.insert(9)
# root.insert(12)
# root.insert(8)
# root.insert(7)
# root.insert(15)

root = Node(20)
root.insert(15)
root.insert(25)
root.insert(5)
root.insert(18)
root.insert(22)


m = dict()
# root.bottomview(m,0)
root.topview(m,0)
print(m)
# root.PrintTree()


