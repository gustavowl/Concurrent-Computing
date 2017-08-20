#!/bin/bash

if [ $# = 2 ]; then
	first=true
	echo -ne '(' > $2
	while read -r line; do
		if [ `expr match "$line" 'Time to multiply matrices: '` -gt 0 ]; then
			temp=${line:27}
			temp=${temp:0:`expr index "$temp" ' '`}
			if [ $first = false ]; then
				echo -ne ', '$temp >> $2
			else
				first=false
				echo -ne $temp >> $2
			fi
		fi

	done < $1
	echo ')' >> $2
else
	echo 'Wrong number of arguments. Expecting 2 arguments:'
	echo -e '1 - Benchmark file\n2 - Output file'
fi