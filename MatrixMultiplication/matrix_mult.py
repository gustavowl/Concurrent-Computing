import time

def read_file(path):
	#generates matrix from file
	with open(path) as file:
		content = file.readlines() #saves each line to content.
		#content is a vector of lines, i.e. each line is an element
	#print(content)
	content = [x.strip() for x in content] #removes '\n' char from the end of line
	ret_matrix = [] #declares variable
	#generates matrix from content, i.e. list of list

	for i in range(1, len(content)):
		ret_matrix.append([eval(n) for n in content[i].split()]) #also converts to float list
	#ends matrix generation
	return ret_matrix


matrix_a = read_file("matrixA.txt")
matrix_b = read_file("matrixB.txt")

#multiplies matrices. matrixA x matrixB
result = [[0] * len(matrix_a)] * len(matrix_b[0]) #declares result matrix
#number of columns and rows is not verified

rows_matrix_a = len(matrix_a)
cols_matrix_b = len(matrix_b[0])
rows_matrix_b = len(matrix_b)

time_start = time.time()
print("START")
for i in range(rows_matrix_a): #supposes that matrix has at least 1 row
	row = []
	for j in range(cols_matrix_b):
		val = 0
		for k in range(rows_matrix_b):
			val += matrix_a[i][k] * matrix_b[k][j]
		row.append(val)
	result[i] = row

time_end = time.time()
print("END")
print(result)
print("Time: " + str(time_end - time_start))