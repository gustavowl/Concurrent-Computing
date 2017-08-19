#!/bin/bash

if [ $# = 2 ]; then
	echo right number of args
	#Implement loop for reading
else
	echo 'Wrong number of arguments. Expecting 2 arguments:'
	echo -e '1 - Benchmark file\n2 - Output file'
fi