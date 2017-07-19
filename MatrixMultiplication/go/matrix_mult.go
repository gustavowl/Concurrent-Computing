package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"strconv"
)

func read_file(path string) [][]int {
	data, _ := ioutil.ReadFile(path)
	splt := strings.Split(string(data), "\n")
	temp := strings.Split(splt[0], " ")

	rows, _ := strconv.Atoi(temp[0])
	cols, _ := strconv.Atoi(temp[1])
	
	var matrix [][]int
	for i := 0; i < rows; i++ {
		str_row := strings.Split(splt[i + 1], " ")
		var int_row []int
		for j:= 0; j < cols; j++ {
			temp, _ := strconv.Atoi(str_row[j])
			int_row = append(int_row, temp)
		}
		matrix = append(matrix, int_row)
	}

	return matrix
}

func main() {
	matrix_a := read_file("../matrices/a4x4.txt")
	matrix_b := read_file("../matrices/b4x4.txt")
	fmt.Println(matrix_a)
	fmt.Println(matrix_b)

	var result [][]int = make([][]int, len(matrix_a), len(matrix_a))
	for i, row_a := range matrix_a {
		var row_res []int = make([]int, len(matrix_b[0]), len(matrix_b[0]))
		result[i] = row_res
		for j := range matrix_b[i] {
			for k, row_b := range matrix_b {
				result[i][j] += row_a[k] * row_b[j]
			}
		}
	}
	fmt.Println(result)
}