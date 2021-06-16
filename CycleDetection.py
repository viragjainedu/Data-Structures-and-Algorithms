# directed graph
from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	
	def DaddEdge(self,u,v):
		if(v==-1):
			self.graph[u] =[]
			return
		self.graph[u].append(v)
	
	def UDaddEdge(self,u,v):
		if(v==-1):
			self.graph[u] = []
		self.graph[u].append(v)
		self.graph[v].append(u)
	
	def cycledetection(self,s):
		# print(max(self.graph))
		
		visited = [False]*(max(self.graph) + 1)
		stack = []

		stack.append(s)
		# visited[s] = False
		visited[s] = True

		print(self.iscycle(stack,visited))

		# iterative approach
		# while(stack):
				# for i in self.graph[s]:


	def iscycle(self,stack,visited):
		# print(stack)
		if(not stack):
			return False

		s = stack.pop()
		
		visited[s] = True
		for i in self.graph[s]:
			# print(visited)
			if( visited[i] == False):
				stack.append(i)
			else:
				# print(i)
				return True
		return self.iscycle(stack,visited)

g = Graph()
g.DaddEdge(0, 1)
g.DaddEdge(1, 2)
g.DaddEdge(2, 4)
g.DaddEdge(4, 6)
g.DaddEdge(6, 5)
g.DaddEdge(5, 3)
g.DaddEdge(3, 1)

g.cycledetection(0)
# print(g.graph)
