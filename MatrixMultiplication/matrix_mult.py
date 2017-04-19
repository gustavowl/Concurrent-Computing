import time

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
result = [[0] * len(matrixA)] * len(matrixB[0]) #declares result matrix
#number of columns and rows is not verified

rows_matrix_a = len(matrixA)
cols_matrix_b = len(matrixB[0])
rows_matrix_b = len(matrixB)

time_start = time.time()
print("START")
for i in range(rows_matrix_a): #supposes that matrix has at least 1 row
	row = []
	for j in range(cols_matrix_b):
		val = 0
		for k in range(rows_matrix_b):
			val += matrixA[i][k] * matrixB[k][j]
		row.append(val)
	result[i] = row

time_end = time.time()
print("END")
print(result)
print("Time: " + str(time_end - time_start))