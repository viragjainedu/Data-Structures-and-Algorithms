def printPascal(num):
	for line in range(1,num+1):
		C = 1
		for i in range(1,line+1):
			print(C, end = " ")
			C = int(C * (line - i) / i)			
		print()


if __name__ == '__main__':
	printPascal(5)