import threading
import time
import sys

#this algorithm will compute, at least, one row of the result matrix.
#matrix_a * matrix_b = matrix
#row_start <= row_end
#row_start is the index of the first row the result matrix to be computed
#row_end is the last row to be computed
def multiply_matrix(matrix_a, matrix_b, row_start, row_end, matrix):
	#print(str(row_start) + ' ' + str(row_end))
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

if (len(sys.argv) == 5):
	time_start = time.time()
	matrix_a = read_file(sys.argv[1])
	matrix_b = read_file(sys.argv[2])
	time_end = time.time()
	print("Time to read files: " + str(time_end - time_start) + " seconds")

	result = [[0] * len(matrix_b[0])] * len(matrix_a)

	thread_list = []
	qtt_threads = int(sys.argv[4])
	proportion = len(result) // qtt_threads
	mod = len(result) % qtt_threads
	first_row = last_row = 0
	for i in range(qtt_threads):
		last_row = first_row + proportion - 1
		if mod > 0:
			last_row += 1
			mod -= 1
		thread_list.append(threading.Thread(target=multiply_matrix, args=(
			matrix_a, matrix_b, first_row, last_row, result)))
		first_row = last_row + 1

#	t1 = threading.Thread(target=multiply_matrix, args=(
#		matrix_a, matrix_b, 0, len(matrix_b)//2, result))
#	t2 = threading.Thread(target=multiply_matrix, args=(
#		matrix_a, matrix_b, len(matrix_b)//2+1, len(matrix_b), result))

	time_start = time.time()
	for i in range(qtt_threads):
		thread_list[i].start()
	for i in range(qtt_threads):
		thread_list[i].join()
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
		"\n3 - Output file\n4 - Number of threads")