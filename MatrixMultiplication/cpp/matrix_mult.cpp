#include <iostream>
#include <fstream>
#include <chrono>

using namespace std;

int** read_file(string path, int* number_of_rows, int* number_of_columns) {
	ifstream input_matrix;
	input_matrix.open(path);

	string str_from_file;
	int** matrix = 0;
	
	if (input_matrix.is_open()) {
		string temp;
		//read twice
		//first value: number of rows
		if(!input_matrix.eof()) {
			input_matrix >> str_from_file;
			*number_of_rows = stoi(str_from_file);
			//cout << *number_of_rows << " ";
		}

		//second value: number of columns
		if(!input_matrix.eof()) {
			input_matrix >> str_from_file;
			*number_of_columns = stoi(str_from_file);
			//cout << *number_of_columns;
		}
		
		matrix = new int*[*number_of_rows];

		for (int i = 0; i < *number_of_rows; i++) {
			matrix[i] = new int[*number_of_columns];
		}

		int i = 0;
		
		//for reasons of I don`t know why, it reads the last element twice
		while(!input_matrix.eof() && i < *number_of_rows * *number_of_columns) {
			input_matrix >> str_from_file;

			matrix[i / *number_of_columns][i % *number_of_columns] = 
				stoi(str_from_file);
			/*cout << "[" << i / *number_of_columns << "][" <<
				i % *number_of_columns << "]\t";
			cout << matrix[i / *number_of_columns][i % *number_of_columns] << endl;*/
			i++;
		}
	}
	else {
		cout << "Could not open file" << endl;
	}
	input_matrix.close();

	return matrix;
}

int** multiply_matrix(int** matrix_a, int rows_a, int cols_a,
	int** matrix_b, int rows_b, int cols_b, int* rows_c, int* cols_c) {

	*rows_c = rows_a;
	*cols_c = cols_b;
	int val;
	int** matrix_c = new int*[rows_a];

	for (int i = 0; i < rows_a; i++)
		matrix_c[i] = new int[cols_b];

	for (int i = 0; i < rows_a; i++) {
		for (int j = 0; j < cols_b; j++) {
			val = 0;
			for (int k = 0; k < rows_b; k++)
				val += matrix_a[i][k] * matrix_b[k][j];
			matrix_c[i][j] = val;
		}
	}

	return matrix_c;
}

void print_matrix(int** matrix, int rows, int cols) {
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			cout << matrix[i][j] << ' ';
		}
		cout << endl;
	}
}

void save_matrix_to_file(int** matrix_c, int m, int n, char* file_name) {
	ofstream output_file;
	output_file.open(file_name);
	output_file << m << ' ' << n;
	string str;
	for (int i = 0; i < m; i++) {
		str = '\n' + to_string(matrix_c[i][0]);
		for (int j = 1; j < n; j++)
			str += ' ' + to_string(matrix_c[i][j]);
		output_file << str;
	}
	output_file.close();
}

int main(int argc, char* argv[]) {
	if (argc == 4) {
		int i, j, k, l, m, n = 0;
		chrono::high_resolution_clock::time_point start_time, end_time;
		chrono::duration<double> time_span;

		start_time = chrono::high_resolution_clock::now();
		int** matrix_a = read_file(argv[1], &i, &j);
		int** matrix_b = read_file(argv[2], &k, &l);
		end_time = chrono::high_resolution_clock::now();
		time_span = chrono::duration_cast<chrono::duration<double>>(
			end_time - start_time);
		cout << "Time to read files: " << time_span.count() << 
			" seconds" << endl;

		start_time = chrono::high_resolution_clock::now();
		int** matrix_c = multiply_matrix(matrix_a, i, j, matrix_b, k, l, &m, &n);
		end_time = chrono::high_resolution_clock::now();
		time_span = chrono::duration_cast<chrono::duration<double>>(
			end_time - start_time);
		cout << "Time to multiply matrices: " << time_span.count() << 
			" seconds" << endl;
		
		start_time = chrono::high_resolution_clock::now();
		save_matrix_to_file(matrix_c, m, n, argv[3]);
		end_time = chrono::high_resolution_clock::now();
		time_span = chrono::duration_cast<chrono::duration<double>>(
			end_time - start_time);
		cout << "Time to save result matrix to file: " << time_span.count() <<
			" seconds" << endl;

		for (int m = 0; m < i; m++) {
			delete matrix_a[m];
		}
		delete matrix_a;

		for (int m = 0; m < k; m++) {
			delete matrix_b[m];
		}
		delete matrix_b;

		for (int i = 0; i < m; i++) {
			delete matrix_c[i];
		}
		delete matrix_c;
	}
	else
		cout << "INVALID NUMBER OF ARGUMENTS! \n1 - Matrix A's file\n" <<
			"2 - Matrix B's file\n3 - Output file" << endl;
	return 0;
}