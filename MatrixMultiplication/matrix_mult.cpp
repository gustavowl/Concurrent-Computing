#include <iostream>
#include <fstream>
#include <string>

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
		cout << i << ' ';
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

int main() {
	cout << "Hello warudo" << endl;
	int i, j, k, l, m, n = 0;
	int** matrix_a = read_file("Matrizes/A4x4.txt", &i, &j);
	int** matrix_b = read_file("Matrizes/B4x4.txt", &k, &l);

	int** matrix_c = multiply_matrix(matrix_a, i, j, matrix_b, k, l, &m, &n);
	print_matrix(matrix_c, m, n);

	for (int m = 0; m < i; m++) {
		delete matrix_a[m];
	}
	delete matrix_a;

	for (int m = 0; m < k; m++) {
		delete matrix_b[m];
	}
	delete matrix_b;
	return 0;
}