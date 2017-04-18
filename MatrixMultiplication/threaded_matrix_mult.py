import threading

#this algorithm will compute, at least, one row of the result matrix.
#matrix_a * matrix_b = matrix
#row_start <= row_end
#row_start is the index of the first row the result matrix to be computed
#row_end is the last row to be computed
def multiply_matrix(matrix_a, matrix_b, row_start, row_end, matrix):
	for i in range(row_start, row_end + 1): #supposes that matrix has at least 1 row
		result2 = []
		for j in range(len(matrixB[0])):
			val = 0
			for k in range(len(matrixB)):
				val += matrixA[i][k] * matrixB[k][j]
			result2.append(val)
		matrix[i] = result2


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

result = [[0] * len(matrixA)] * len(matrixB[0])


t1 = threading.Thread(target=multiply_matrix, args=(
	matrixA, matrixB, 0, 1, result))
t2 = threading.Thread(target=multiply_matrix, args=(
	matrixA, matrixB, 2, 3, result))
t1.start()
t2.start()
t1.join()
t2.join()
print(result)