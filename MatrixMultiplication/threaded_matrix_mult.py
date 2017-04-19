import threading
import time

#this algorithm will compute, at least, one row of the result matrix.
#matrix_a * matrix_b = matrix
#row_start <= row_end
#row_start is the index of the first row the result matrix to be computed
#row_end is the last row to be computed
def multiply_matrix(matrix_a, matrix_b, row_start, row_end, matrix):
	for i in range(row_start, row_end + 1): #supposes that matrix has at least 1 row
		row = []
		for j in range(len(matrix_b[0])):
			val = 0
			for k in range(len(matrix_b)):
				val += matrix_a[i][k] * matrix_b[k][j]
			row.append(val)
		matrix[i] = row

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

result = [[0] * len(matrix_b[0])] * len(matrix_a)


t1 = threading.Thread(target=multiply_matrix, args=(
	matrix_a, matrix_b, 0, len(matrix_b)//2, result))
t2 = threading.Thread(target=multiply_matrix, args=(
	matrix_a, matrix_b, len(matrix_b)//2+1, len(matrix_b), result))

time_start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
time_end = time.time()
print(result)
print("Time: " + str(time_end - time_start))