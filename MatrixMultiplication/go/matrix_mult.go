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
	s := read_file("../matrices/a4x4.txt")
	fmt.Println(s)
}