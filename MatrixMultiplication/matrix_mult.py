import threading

#generates matrix from file
with open("matrixA.txt") as file:
	content = file.readlines() #saves each line to content.
	#content is a vector of lines, i.e. each line is an element
#print(content)
content = [x.strip() for x in content] #removes '\n' char from the end of line
matrixA = [] #declares variable
#generates matrix from content, i.e. list of list
for i in range(len(content)):
	matrixA.append([eval(n) for n in content[i].split()]) #also converts to float list
#ends matrix generation

#generates matrix from file
with open("matrixB.txt") as file:
	content = file.readlines() #saves each line to content.
	#content is a vector of lines, i.e. each line is an element
#print(content)
content = [x.strip() for x in content] #removes '\n' char from the end of line
matrixB = [] #declares variable
#generates matrix from content, i.e. list of list
for i in range(len(content)):
	matrixB.append([eval(n) for n in content[i].split()]) #also converts to float list
#ends matrix generation

#multiplies matrices. matrixA x matrixB
result = [] #declares result matrix
#number of columns and rows is not verified
for i in range(len(matrixA)): #supposes that matrix has at least 1 row
	result2 = []
	for j in range(len(matrixB[0])):
		val = 0
		for k in range(len(matrixB)):
			val += matrixA[i][k] * matrixB[k][j]
		result2.append(val)
	result.append(result2)

print(result)