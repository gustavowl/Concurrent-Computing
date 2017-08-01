# ASSIGNMENT INFO

The purpose of the assignment was to show the students a simple example of how concurrent computing can run faster than sequential. Also, to show that by using more threads, the program will not necessarily run faster.

The activity was to simply implement two versions of a matrix multiplication algorithm: a single threaded and a multithreaded. A benchmark was also requisited.

Initially, the assignment should be implemented using either Java or C++. However, the professor let me develop it in Python. Although, I ended developing the same algorithm in C++ since the Python version was too slow to benchmarking for some cases.

All the matrices found at [matrices/](matrices/) were given by Professor [Everton](http://www.dimap.ufrn.br/~everton/?lang=en) so we could benchmark the algorithms.

## Beyond the scope
To quench a curiosity I have, I decided to keep working on this assignment. The idea is to benchmark the matrix multiplication (initially) for 3 languages: C++, Python (compiled and not compiled), and GO. I'm doing this so I can have a better knowledge regarding each language's speed and the best scenario in which I should use them.

## Executing
Matrices format. The following is an example of the expected matrix format.
```
4 4
13 8 62 64 
78 31 25 61 
81 14 79 26 
28 31 30 26 
```
The first value represents the number of rows and the second, the number of columns. The remaining values are the matrice's elements.

All the algorithms follow the same logic. They receive two input matrices, stored in files. Then, they create another file, containing the result matrix. For example, multiplying the previous matrix by the following:

```
4 4
86 26 37 97 
25 53 85 86 
93 98 64 46 
62 20 21 53
```
will result in a file with content
```
4 4
11052 8118 6473 8193
13590 7341 8402 14615
16275 11110 9789 14073
```

### C++

#### COMPILING
C++ code needs to be compiled in order to be executed. Both codes (sequential and threaded) use the C++11 standard. The threaded version uses the lpthread library and it may be necessary to install it.
##### Sequential
In order to compile the sequential code, and supposing the user is at the [cpp directory](cpp/), run the following command.
```
g++ matrix_mult.cpp --std=c++11 -o mm
```
This will generate an executable with name `mm`.
##### Threaded
TODO

#### RUNNING

##### Sequential
Supposing you are still located at the [cpp directory](cpp/) and the code was compiled exactly as described at the [Compiling section](#compiling), run the following command:
```
./mm <matrix_a> <matrix_b> <output_file>

<matrix_a> the file path of the first matrix.
<matrix_b> the file path of the second matrix.
<outuput_file> the file path of the result matrix. If the file does not exist it is created automatically.
```
The input matrices format must be as described at [Executing section](#executing). The output matrix will also follow the same pattern.

The following example will procude the same result as the one described at the [Executing section](#executing). Supposing the user is still located at the [cpp directory](cpp/), run the following command:
```
./mm ../matrices/a4x4.txt ../matrices/b4x4.txt output.txt 
```
The output.txt file was created at the current directory, check its content to see the result matrix \(`cat output.txt`\)
##### Threaded
TODO

### Python
Since Python code is interpreted, it is possible to run the provided code as long as [the interpreter](https://www.python.org/downloads/) is installed.

#### Sequential
If the user is in the [python directory](python/), the following command can be executed in order to run the program:
```
python matrix_mult.py <matrix_a> <matrix_b> <output_file>

<matrix_a> the file path of the first matrix.
<matrix_b> the file path of the second matrix.
<outuput_file> the file path of the result matrix. If the file does not exist it is created automatically.
```

#### Threaded
TODO

### GO
GO is compiled, but the command used to compile the code is used alongside the on to run it. Please visit the official website for [GO installing instructions](https://golang.org/doc/install).
#### Sequential
Run the following command if located in the [go directory](go/)
```
go run matrix_mult.go <matrix_a> <matrix_b> <output_file>

<matrix_a> the file path of the first matrix.
<matrix_b> the file path of the second matrix.
<outuput_file> the file path of the result matrix. If the file does not exist it is created automatically.
```
#### Threaded
TODO


### sequential\_benchmark.sh

In order to run this script, it is necessary to install [bc](https://www.gnu.org/software/bc/manual/html_mono/bc.html) and compile the C++ code **exactly** as described at the [Compiling section](#compiling). Also, it is necessary to have [python](https://www.python.org/downloads/) installed.

It may be necessary to add execution permission to the file \(`chmod +x sequential_benchmark.sh`\). To run it, just execute the `./sequential_benchmark` command. 
