import time
import sys

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

if (len(sys.argv) == 4):
	time_start = time.time()
	matrix_a = read_file(sys.argv[1])
	matrix_b = read_file(sys.argv[2])
	time_end = time.time()
	print("Time to read files: " + str(time_end - time_start) + " seconds")

	#multiplies matrices. matrixA x matrixB
	result = [[0] * len(matrix_a)] * len(matrix_b[0]) #declares result matrix
	#number of columns and rows is not verified

	rows_matrix_a = len(matrix_a)
	cols_matrix_b = len(matrix_b[0])
	rows_matrix_b = len(matrix_b)

	time_start = time.time()
	for i in range(rows_matrix_a): #supposes that matrix has at least 1 row
		row = []
		for j in range(cols_matrix_b):
			val = 0
			for k in range(rows_matrix_b):
				val += matrix_a[i][k] * matrix_b[k][j]
			row.append(val)
		result[i] = row

	time_end = time.time()
	print("Time to multiply matrices: " + str(time_end - time_start) + " seconds")

	time_start = time.time()
	output_file = open(sys.argv[3], 'w')
	output_file.write(str(len(result)) + ' ' + str(len(result[0])))
	for i in range(len(result)):
		buff = str(result[i])
		buff = buff.replace(",", "")	
		output_file.write('\n' + buff[1:len(buff) - 1])
	time_end = time.time()
	print("Time to save to output file: " + str(time_end - time_start) + " seconds")
else:
	print("Invalid number of arguments.\n1 - Matrix A's file\n2 - Matrix B's file" +
		"\n3 - Output file")