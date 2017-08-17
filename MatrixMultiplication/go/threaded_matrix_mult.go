package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"strconv"
	"time"
	"os"
	"sync"
	"runtime"
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

func multiply_matrix(matrix_a [][]int, matrix_b [][]int, row_start int, 
	row_end int, matrix [][]int, wg *sync.WaitGroup) {
	
	for i := row_start; i <= row_end; i++ {
		var row_res []int = make([]int, len(matrix_b[0]), len(matrix_b[0]))
		matrix[i] = row_res
		for j := range matrix_b[i] {
			for k, row_b := range matrix_b {
				matrix[i][j] += matrix_a[i][k] * row_b[j]
			}
		}
	}
	wg.Done()
}

func main() {
	if len(os.Args) == 5 {
		runtime.GOMAXPROCS(4) //needed on raspberry pi to use all 4 cores
		time_start := time.Now()
		matrix_a := read_file(os.Args[1])
		matrix_b := read_file(os.Args[2])
		fmt.Println("Time to read files: " + time.Since(time_start).String())

		qtt_threads, _ := strconv.Atoi(os.Args[4])
		var result [][]int = make([][]int, len(matrix_a), len(matrix_a))
		proportion := len(result) / qtt_threads
		mod := len(result) % qtt_threads
		next_row := 0
		time_start = time.Now()
		proportion += 1
		var wg sync.WaitGroup
		wg.Add(qtt_threads)

		for i := 0; i < qtt_threads; i++ {
			if mod == 0 {
				proportion -= 1
			}
			mod -= 1
			go multiply_matrix(matrix_a, matrix_b, next_row, next_row + proportion - 1, result, &wg)
			next_row += proportion
		}
		wg.Wait()
		fmt.Println("Time to multiply matrices: " + time.Since(time_start).String())

		time_start = time.Now()
		f, _ := os.OpenFile(os.Args[3], os.O_WRONLY | os.O_CREATE, 0644)
		content := strconv.Itoa(len(result)) + " " + strconv.Itoa(len(result[0])) + "\n"
		f.WriteString(content)
		for _, row := range result {
			content = ""
			for _, elem := range row {
				content += strconv.Itoa(elem) + " "
			}
			content += "\n"
			f.WriteString(content)
		}
		f.Close()
		fmt.Println("Time to write result matrix to file: " + time.Since(time_start).String())

	} else {
		fmt.Println("Invalid number of arguments.\n1 - Matrix A's file\n2 - Matrix B's file" +
			"\n3 - Output file\n4 - Number of threads")
	}
}
