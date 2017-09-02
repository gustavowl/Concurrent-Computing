#!/bin/bash

if [ $# = 2 ]; then
	first=true
	index=0
	echo -ne "" > $2
	data_array[$index]=0
	while read -r line; do
		if [ `expr match "$line" 'Time to multiply matrices: '` -gt 0 ]; then
			temp=${line:27}
			temp=${temp:0:`expr index "$temp" ' '`}
			data_array[$index]=$temp
			#insertion sort
			for i in `seq $index -1 1`; do
				if [ $(echo "${data_array[$[$i - 1]]} > ${data_array[$i]}" | bc -l) = 1 ]; then
					#change
					temp=${data_array[$[$i - 1]]}
					data_array[$[$i - 1]]=${data_array[$i]}
					data_array[$i]=$temp
				fi
			done
			index=$[$index + 1]
		elif [ `expr match "$line" "-*.* Thread(s)"` -gt 0 ]; then
			if [ $first = false ]; then
				for i in `seq 0 $[$index - 1]`; do
					if [ $i -gt 0 ]; then
						echo -ne ', '${data_array[$i]} >> $2
					else
						echo -ne '('${data_array[$i]} >> $2
					fi
				done
				echo -ne ')\n\nmean: ' >> $2

				#calculates median
				if [ $[$index % 2] = 0 ]; then #even number of elements
					mean1=${data_array[$[$index / 2 - 1]]}
					mean2=${data_array[$[$index / 2]]}
					echo -ne $(echo "($mean1 + $mean2) / 2" | bc -l) >> $2
				else #odd number of elements
					mean=${data_array[$[$index / 2]]}
					echo $mean >> $2
				fi

				echo -ne '\n\n\n\n'$line'\n' >> $2

				index=0
			else
				echo -ne $line'\n' >> $2
				first=false
			fi
		fi

	done < $1
	
	#should have created a routine
	for i in `seq 0 $[$index - 1]`; do
		if [ $i -gt 0 ]; then
			echo -ne ', '${data_array[$i]} >> $2
		else
			echo -ne '('${data_array[$i]} >> $2
		fi
	done
	echo -ne ')\n\nmean: ' >> $2

	#calculates median
	if [ $[$index % 2] = 0 ]; then #even number of elements
		mean1=${data_array[$[$index / 2 - 1]]}
		mean2=${data_array[$[$index / 2]]}
		echo -ne $(echo "($mean1 + $mean2) / 2" | bc -l) >> $2
	else #odd number of elements
		mean=${data_array[$[$index / 2]]}
		echo $mean >> $2
	fi
else
	echo 'Wrong number of arguments. Expecting 2 arguments:'
	echo -e '1 - Benchmark file\n2 - Output file'
fi